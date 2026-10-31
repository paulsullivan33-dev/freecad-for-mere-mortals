# Glossary

The terms used in this guide, collected
in one place.

**3MF** — a modern mesh exchange format:
a zip holding an XML description of a
triangle mesh, with units. STL's
successor (chapter 10).

**Assembly** — a document-level
arrangement of several bodies placed by
joints, so a mechanism can be checked
as a whole (chapter 13).

**Body** — one solid part under
construction in Part Design, built as a
tree of features (chapter 2).

**Boolean operation** — combining solids
by set logic: fuse (union), cut
(difference), common (intersection).
The Part workbench's native tongue
(chapter 4).

**BRep** — boundary representation: a
solid described by its faces, edges and
vertices and the surfaces they lie on.
The `.brp` files inside an FCStd are
BReps (chapter 12).

**Constraint** — a promise a sketch
keeps about its geometry: coincident,
horizontal, a length of 60. The set of
them is the sketch's real content
(chapter 6).

**Degree of freedom (DoF)** — the
movement a sketch still permits itself.
Zero means fully constrained.

**Document** — one FreeCAD file: every
object, sketch, parameter and setting
of a project (chapter 2).

**Expression** — a formula in place of
a number in a property, typically
pointing at a spreadsheet cell:
`Params.HoleDia` (chapter 9).

**Face / edge / vertex** — the boundary
pieces of a solid: its surfaces, their
rims, their corners — the things the
kernel counts and chapter 8 audits.

**FCStd** — FreeCAD's native document
format: a zip of XML and BRep geometry
(chapter 12).

**Feature** — one step in a body's
history: a pad, a pocket, a fillet.
Features are instructions; the shape is
their replayed result (chapter 2).

**Fillet** — a rounded replacement for
a sharp edge, of a stated radius.
Its flat-sided cousin is a **chamfer**,
a straight bevel (chapter 7).

**Fully constrained** — a sketch with
no degrees of freedom left: it cannot
change shape except by a number being
edited (chapter 6).

**Kernel** — the library that computes
exact solids — volumes, cuts, surface
intersections. FreeCAD's is Open
CASCADE (chapter 2).

**Mesh** — a solid approximated by flat
triangles; what STL and 3MF carry, and
what printers consume (chapter 10).

**Pad** — a Part Design feature that
stretches a sketch into a slab of a
given thickness (chapter 5).

**Parametric** — defined by named
numbers, so changing a number rebuilds
the thing. The guide's thesis
(chapters 1 and 9).

**Pocket** — a pad in reverse: a sketch
stretched through a body, removing
material (chapter 7).

**Recompute** — the act of replaying a
document's dependency chain so every
object reflects its inputs.

**Sketch** — a constrained 2D drawing
on a plane, feeding features
(chapter 6).

**STEP** — ISO 10303, the CAD exchange
format carrying exact solids between
programs (chapter 10).

**STL** — the oldest mesh format: a
header and a list of triangles, no
units, no curves (chapter 10).

**Tip** — the last feature in a body;
its shape is the body's shape
(chapter 2).

**Topological naming problem** — the
instability of face and edge names
across rebuilds, and the breakage it
causes (chapter 16).

**Workbench** — a themed toolbox over
the same document: Sketcher, Part
Design, Spreadsheet, and the rest
(chapter 4).
