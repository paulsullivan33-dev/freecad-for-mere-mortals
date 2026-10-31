# build_params.py — the same bracket block, but every size lives in a
# spreadsheet named Params, and the model only holds expressions that
# point at it. Edit the sheet, recompute, and the part follows.
# Run: freecadcmd build_params.py   (measurements printed to stdout)

import math

import FreeCAD as App
import Part
import Sketcher

doc = App.newDocument("BracketParams")
body = doc.addObject("PartDesign::Body", "Body")
XY = [f for f in body.Origin.OriginFeatures if f.Name == "XY_Plane"][0]

# ---- the spreadsheet: one row per parameter -------------------------------
sheet = doc.addObject("Spreadsheet::Sheet", "Params")
rows = [("Length", 60.0), ("Width", 40.0), ("Height", 12.0),
        ("HoleDia", 10.0), ("FilletR", 2.0)]
for i, (name, value) in enumerate(rows, start=1):
    sheet.set("A%d" % i, name)
    sheet.set("B%d" % i, repr(value))
    sheet.setAlias("B%d" % i, name)
doc.recompute()

L, W, H, D, R = 60.0, 40.0, 12.0, 10.0, 2.0  # starting values, as in the sheet

# ---- block sketch + pad (same construction as build_part.py) --------------
sk = body.newObject("Sketcher::SketchObject", "BlockSketch")
sk.AttachmentSupport = [(XY, "")]
sk.MapMode = "FlatFace"
L2, W2 = L / 2.0, W / 2.0
pts = [(-L2, -W2), (L2, -W2), (L2, W2), (-L2, W2)]
for i in range(4):
    x1, y1 = pts[i]
    x2, y2 = pts[(i + 1) % 4]
    sk.addGeometry(Part.LineSegment(App.Vector(x1, y1, 0),
                                    App.Vector(x2, y2, 0)), False)
for i in range(4):
    sk.addConstraint(Sketcher.Constraint("Coincident", i, 2, (i + 1) % 4, 1))
    sk.addConstraint(Sketcher.Constraint("Horizontal" if i % 2 == 0 else "Vertical", i))
sk.addConstraint(Sketcher.Constraint("DistanceX", -1, 1, 0, 1, -L2))
sk.addConstraint(Sketcher.Constraint("DistanceY", -1, 1, 0, 1, -W2))
c_len = sk.addConstraint(Sketcher.Constraint("DistanceX", 0, 1, 0, 2, L))
c_wid = sk.addConstraint(Sketcher.Constraint("DistanceY", 1, 1, 1, 2, W))
sk.renameConstraint(c_len, "Length")
sk.renameConstraint(c_wid, "Width")

pad = body.newObject("PartDesign::Pad", "Pad")
pad.Profile = sk
pad.Length = H

vertical = []
doc.recompute()
for i, e in enumerate(pad.Shape.Edges):
    c = e.Curve
    if hasattr(c, "Direction") and abs(c.Direction.z) > 0.999:
        vertical.append("Edge%d" % (i + 1))
fillet = body.newObject("PartDesign::Fillet", "CornerFillet")
fillet.Base = (pad, vertical)
fillet.Radius = R

sk2 = body.newObject("Sketcher::SketchObject", "HoleSketch")
sk2.AttachmentSupport = [(XY, "")]
sk2.MapMode = "FlatFace"
sk2.addGeometry(Part.Circle(App.Vector(0, 0, 0), App.Vector(0, 0, 1), D / 2.0), False)
sk2.addConstraint(Sketcher.Constraint("Coincident", 0, 3, -1, 1))
c_dia = sk2.addConstraint(Sketcher.Constraint("Diameter", 0, D))
sk2.renameConstraint(c_dia, "HoleDia")

pocket = body.newObject("PartDesign::Pocket", "Hole")
pocket.Profile = sk2
pocket.Type = "ThroughAll"
pocket.Reversed = True
doc.recompute()

# ---- now bind the model to the sheet --------------------------------------
sk.setExpression("Constraints.Length", "Params.Length")
sk.setExpression("Constraints.Width", "Params.Width")
pad.setExpression("Length", "Params.Height")
sk2.setExpression("Constraints.HoleDia", "Params.HoleDia")
fillet.setExpression("Radius", "Params.FilletR")
doc.recompute()

expected = L * W * H - math.pi * (D / 2.0) ** 2 * H - 4 * (R ** 2 - math.pi * R ** 2 / 4.0) * H
print("bound to sheet: volume %.3f  expected %.3f" % (body.Shape.Volume, expected))

# ---- change ONE cell: the hole diameter, 10 -> 16 --------------------------
sheet.set("B4", "16")
doc.recompute()
D = 16.0
expected = L * W * H - math.pi * (D / 2.0) ** 2 * H - 4 * (R ** 2 - math.pi * R ** 2 / 4.0) * H
print("HoleDia cell now 16: volume %.3f  expected %.3f" % (body.Shape.Volume, expected))
print("hole diameter as the sketch reports it: %.3f mm"
      % sk2.getDatum("HoleDia"))
doc.saveAs("out_sheet/bracket_params.FCStd")
