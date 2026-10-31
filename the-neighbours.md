# The Neighbours

FreeCAD is one answer to "how do I
design a thing". This chapter places it
among the others a maker will meet,
fairly: each of these is the right tool
for somebody, and two of them have
guides of their own in this series.

## OpenSCAD — the part as a program

[OpenSCAD for Mere Mortals](https://paulsullivan33-dev.github.io/openscad-for-mere-mortals/)
builds parts from code alone: no
sketches, no mouse, the shape is the
output of a script in a language made
for geometry. Its solids are built by
combining and subtracting primitives,
and its parameters are variables in the
text — chapter 9's idea taken to its
limit. Choose it when the part is
inherently *programmatic* (patterns,
generated shapes, text-driven variants)
or when you think in code more fluently
than in sketches. Choose FreeCAD when
the part wants shaping by reference to
its own faces and edges, when sketches
with constraints feel like the design
itself, or when you need exact curved
solids exchanged by STEP — OpenSCAD's
exports are meshes, with chapter 10's
caveat built in. This series' general
[CAD for Mere Mortals](https://paulsullivan33-dev.github.io/cad-for-mere-mortals/)
compares the two on the same bracket.

## Blender — meshes, not measurements

Blender models in triangles and
sculpts beautifully; its shapes are
surfaces first and solids when they are
careful. For characters, scenes and
organic forms it is unmatched and free.
For a bracket it is the wrong physics:
dimensions are something you impose on
a mesh, not something the mesh *is*, and
there is no feature tree to re-drive.
Different craft, different guide —
[Blender for Mere Mortals](https://paulsullivan33-dev.github.io/blender-for-mere-mortals/).

## The commercial giants

**Fusion 360**, **Onshape** and
**SolidWorks** are what professional
part design mostly runs on. They are
more polished than FreeCAD in the ways
money buys: fillets that succeed more
often, assemblies with a decade of
hardening, drawing tools, support. Their
costs are also real: subscriptions,
cloud-held files (Onshape entirely,
Fusion largely), licences that can
change terms, and — the quiet one —
your back catalogue living in a format
only their program opens. FreeCAD's
counter-offer is chapter 12's: your
design is a zip of XML and open geometry
on your own disk, in a program whose
source you may read. Many workshops run
both: commercial CAD at work, FreeCAD
at home, STEP files walking between
them (chapter 10).

## The shallow end, honourably

**Tinkercad** and its kin — browser
editors where parts are dragged,
grouped and holed — are genuinely good
first tools, and for a one-off spacer
or a child's name-tag they finish the
job before FreeCAD has finished
installing. What they do not teach is
parameters and constraints, so their
ceiling arrives quickly; this guide
exists for the day it does.

## And after the model

A designed part still has to be *made*:
sliced for a printer (the series'
[3D Printing for Mere Mortals](https://paulsullivan33-dev.github.io/3d-printing-for-mere-mortals/)),
drawn for a workshop (TechDraw, chapter
4), or cut by a machine (FreeCAD's own
CAM workbench). FreeCAD's place in that
chain is the middle: it is where the
thing's *dimensions* are decided and
proved. That is a narrower claim than
"it does everything", and it is the one
this guide has tried to earn.
