# build_part.py — the FreeCAD guide lab fixture.
# A parametric block with a centred through-hole and filleted corners,
# built with Part Design from two sketches. Every size is a named
# parameter at the top; change a number, re-run, get a new part.
#
# Usage: freecadcmd build_part.py
# Optional environment: HOLE_DIA=16 OUTDIR=somewhere
# Writes measurements to stdout and bracket.FCStd / .step / .stl
# into OUTDIR (default: current directory).

import math
import os

import FreeCAD as App
import Part
import Sketcher

# ---- parameters (millimetres) -------------------------------------------
LENGTH = 60.0   # X size of the block
WIDTH = 40.0    # Y size of the block
HEIGHT = 12.0   # Z size of the block (the pad length)
HOLE_DIA = 10.0  # centred through-hole diameter
FILLET_R = 2.0  # radius on the four vertical corners

if os.environ.get("HOLE_DIA"):
    HOLE_DIA = float(os.environ["HOLE_DIA"])
OUTDIR = os.environ.get("OUTDIR", ".")
os.makedirs(OUTDIR, exist_ok=True)

doc = App.newDocument("BracketBlock")
body = doc.addObject("PartDesign::Body", "Body")
XY = [f for f in body.Origin.OriginFeatures if f.Name == "XY_Plane"][0]

# ---- sketch 1: the rectangle, on the XY plane ----------------------------
sk = body.newObject("Sketcher::SketchObject", "BlockSketch")
sk.AttachmentSupport = [(XY, "")]  # the XY plane (was "Support" before 1.1)
sk.MapMode = "FlatFace"

L2, W2 = LENGTH / 2.0, WIDTH / 2.0
pts = [(-L2, -W2), (L2, -W2), (L2, W2), (-L2, W2)]
for i in range(4):
    x1, y1 = pts[i]
    x2, y2 = pts[(i + 1) % 4]
    sk.addGeometry(Part.LineSegment(App.Vector(x1, y1, 0),
                                    App.Vector(x2, y2, 0)), False)
for i in range(4):  # corners coincident, sides horizontal/vertical
    sk.addConstraint(Sketcher.Constraint("Coincident", i, 2, (i + 1) % 4, 1))
    sk.addConstraint(Sketcher.Constraint("Horizontal" if i % 2 == 0 else "Vertical", i))
sk.addConstraint(Sketcher.Constraint("DistanceX", -1, 1, 0, 1, -L2))  # corner from origin
sk.addConstraint(Sketcher.Constraint("DistanceY", -1, 1, 0, 1, -W2))
c_len = sk.addConstraint(Sketcher.Constraint("DistanceX", 0, 1, 0, 2, LENGTH))
c_wid = sk.addConstraint(Sketcher.Constraint("DistanceY", 1, 1, 1, 2, WIDTH))
sk.renameConstraint(c_len, "Length")
sk.renameConstraint(c_wid, "Width")
doc.recompute()
print("block sketch fully constrained:", sk.FullyConstrained)

# ---- pad ------------------------------------------------------------------
pad = body.newObject("PartDesign::Pad", "Pad")
pad.Profile = sk
pad.Length = HEIGHT
doc.recompute()

# ---- fillet: the four vertical edges of the pad ---------------------------
vertical = []
for i, e in enumerate(pad.Shape.Edges):
    curve = e.Curve
    if hasattr(curve, "Direction") and abs(curve.Direction.z) > 0.999:
        vertical.append("Edge%d" % (i + 1))
print("vertical edges found:", vertical)
fillet = body.newObject("PartDesign::Fillet", "CornerFillet")
fillet.Base = (pad, vertical)
fillet.Radius = FILLET_R
doc.recompute()

# ---- sketch 2: the hole, a circle at the centre, on the XY plane ----------
sk2 = body.newObject("Sketcher::SketchObject", "HoleSketch")
sk2.AttachmentSupport = [(XY, "")]
sk2.MapMode = "FlatFace"
sk2.addGeometry(Part.Circle(App.Vector(0, 0, 0), App.Vector(0, 0, 1),
                            HOLE_DIA / 2.0), False)
sk2.addConstraint(Sketcher.Constraint("Coincident", 0, 3, -1, 1))  # centre on origin
c_dia = sk2.addConstraint(Sketcher.Constraint("Diameter", 0, HOLE_DIA))
sk2.renameConstraint(c_dia, "HoleDia")
doc.recompute()

# ---- pocket: cut the hole through everything ------------------------------
pocket = body.newObject("PartDesign::Pocket", "Hole")
pocket.Profile = sk2
pocket.Type = "ThroughAll"
pocket.Reversed = True   # sketch sits on the bottom plane; cut upwards
doc.recompute()
print("hole sketch fully constrained:", sk2.FullyConstrained)

shape = body.Shape
shape.check(True)

# ---- expected values, computed by hand ------------------------------------
block = LENGTH * WIDTH * HEIGHT
hole = math.pi * (HOLE_DIA / 2.0) ** 2 * HEIGHT
corner = (FILLET_R ** 2 - math.pi * FILLET_R ** 2 / 4.0) * HEIGHT
expected = block - hole - 4 * corner

print("=== MEASUREMENTS ===")
print("parameters: L=%g W=%g H=%g hole_dia=%g fillet_r=%g"
      % (LENGTH, WIDTH, HEIGHT, HOLE_DIA, FILLET_R))
print("valid solid:", shape.isValid(), "| solids:", len(shape.Solids))
print("volume measured : %.3f mm^3" % shape.Volume)
print("volume expected : %.3f mm^3 (block %.1f - hole %.3f - 4 corners %.3f)"
      % (expected, block, hole, 4 * corner))
print("volume error    : %.4f %%" % (100.0 * (shape.Volume - expected) / expected))
print("surface area    : %.3f mm^2" % shape.Area)
bb = shape.BoundBox
print("bounding box    : %.3f x %.3f x %.3f mm" % (bb.XLength, bb.YLength, bb.ZLength))
print("faces: %d  edges: %d  vertices: %d"
      % (len(shape.Faces), len(shape.Edges), len(shape.Vertexes)))

# ---- exports ---------------------------------------------------------------
doc.saveAs(os.path.join(OUTDIR, "bracket.FCStd"))
import Import
Import.export([body], os.path.join(OUTDIR, "bracket.step"))
import Mesh
Mesh.export([body], os.path.join(OUTDIR, "bracket.stl"))
print("exports written to", OUTDIR)
