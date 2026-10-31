# Workbenches — Part, Part Design and Sketcher

By the end of this chapter you can answer
the beginner's real question — "there are
three ways to make a box; which one do I
use?" — because the workbenches are not
three programs but three *opinions* about
modelling, and the opinion decides what
editing feels like later.

## What a workbench is

A **workbench** is a toolbox arranged
around one way of working. The lab's
FreeCAD 1.1.4 shipped with these, read
from its own program tree: Part, Part
Design, Sketcher, Draft, Assembly, BIM,
CAM, FEM, Material, Mesh, OpenSCAD,
Spreadsheet, Surface, TechDraw and
others. You will use four of them in this
guide — Sketcher, Part Design, Part and
Spreadsheet — and meet the rest by name.

## Sketcher: where shapes begin

**Sketcher** makes the flat drawings
that features consume. Its whole craft
is geometry plus **constraints**
(chapter 6): lines, arcs and circles,
told exactly where they live. Every
serious FreeCAD workflow spends half its
life here, whichever workbench owns the
features afterwards.

## Part Design: one body, built in order

**Part Design** is the opinionated route,
and the one this guide teaches. A
**body** is one solid. Features arrive
in order — **pad** a sketch into a slab,
**pocket** a cut into it, **fillet** an
edge — and each feature's output is the
next feature's input (chapter 2's tree).
Nothing exists outside the order: you
cannot union two bodies inside Part
Design, because the body's rule is
*always exactly one solid, always the
result of its history*. That discipline
is what makes parametric editing
predictable: change any earlier number
and the whole history replays.

Reach for Part Design when the thing is
a *part*: one connected lump of material
with a shape you can describe as a
sequence of adds and cuts. Most printed
and machined pieces are exactly that.

## Part: solids as building blocks

The **Part** workbench is the kernel's
own toolbox, undisguised. It offers
primitive solids (box, cylinder, sphere)
and **boolean** operations — fuse
(union), cut (difference), common
(intersection) — applied to any shapes,
in any order, with no single-solid rule
and no enforced history. It is looser
and more direct: three primitives and
two cuts can outrun a feature tree for
quick, lumpy shapes, and Part is also
where shapes imported from other
programs are repaired and combined.

The cost is bookkeeping. A boolean tree
remembers less about your *intent* than
a Part Design body does, and editing it
deep in the tree is where chapter 16's
naming problem bites hardest. The common
advice, which this guide follows, is:
Part Design for parts you design, Part
for shapes you wrangle.

## The supporting benches

- **Spreadsheet** — a sheet of named
  numbers inside the document. Chapter 9
  drives the whole part from one.
- **TechDraw** — turns a 3D part into a
  2D workshop drawing with dimensions;
  the way a design leaves the building
  on paper. (Documented, not run, here.)
- **Mesh** — handles STL-style triangle
  meshes: inspecting, repairing and
  converting what printers and scanners
  trade in (chapter 10 exports through
  it).
- **Assembly** — joins finished bodies
  with joints so they move as a mechanism
  should. New as a built-in in the 1.x
  series; chapter 13 gives its honest
  state.

Switching benches mid-task is normal and
safe: the document doesn't care which
toolbox made an object. What you cannot
switch mid-part is the *opinion* — a
body is a Part Design citizen from birth.
