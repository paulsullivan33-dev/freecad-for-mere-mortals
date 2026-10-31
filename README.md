# FreeCAD for Mere Mortals

A drawing of a part is a picture. A
**model** of a part is something better:
a solid that exists in the computer as
measurements, which you can weigh without
touching it, section without cutting it,
and change by changing a number.
**FreeCAD** is a free program that builds
such models. You sketch flat shapes, give
them thickness, cut holes through them,
round their corners — and at every step
the part is defined by **parameters**,
numbers with names, so the design is the
numbers and the shape is just what the
numbers currently produce.

This guide explains how FreeCAD thinks,
how to install it, and how to design a
first real part: a plain block, sixty
millimetres long, with a hole through the
middle and rounded corners — the kind of
bracket blank a workshop actually uses.
Then it does something most CAD guides
skip: it **proves** the part. The lab
that wrote this guide worked entirely
through FreeCAD's scripting console, with
no screen it could model on, so every
claim here is checked against arithmetic
done by hand: the block's volume, minus
the hole's cylinder, minus the corners
the fillets removed. The program's
answers matched the hand sums to the last
printed digit — and when the first build
came out wrong, it was the same arithmetic
that caught it, because the error was
exactly half a hole.

The lab behind this guide ran the real
thing: **FreeCAD 1.1.4**, the official
release, downloaded from the project's
own site with its checksum verified, on
a small Linux machine. Against it the
lab built the part twice (once wrongly,
once right), rebuilt it with a bigger
hole to show it is truly parametric,
rebuilt it a third time driven by a
spreadsheet whose single changed cell
moved the hole on its own, and exported
the result as a native file, a **STEP**
file for other CAD programs, an **STL**
mesh for printing, and a **3MF** file.
Each export was then checked by opening
it again and measuring what came back.

What the lab could not do, it did not
fake. It never modelled by hand on a
screen — the sandbox's display could not
run the graphical program — so clicking
your way through a design is taught from
the documentation and labelled as such,
while everything the scripting console
could do for real is shown with its
transcripts. `criteria.md` keeps the full
ledger of what was run and what was only
read.

One honest line before any procedure:
FreeCAD will model exactly the part you
describe, including a part that would
snap in half the moment it is loaded.
The numbers being exact is not the part
being strong. Chapter 16 returns to this;
keep it in mind from chapter 1.

## What this guide covers

- [**What FreeCAD is**](what-freecad-is.md) —
  drawing versus modelling, what
  "parametric" buys you, and who this
  program is for
- [**The moving parts**](the-moving-parts.md) —
  the geometry kernel that does the maths,
  documents, bodies, features and sketches,
  and which layer holds what
- [**Installing FreeCAD**](installing-freecad.md) —
  the official downloads, the checksum
  check, and the AppImage taken apart so
  it runs without FUSE
- [**Workbenches**](workbenches.md) —
  Part, Part Design and Sketcher — three
  different answers to "how do I make a
  shape", and how to choose
- [**Your first part**](your-first-part.md) —
  a sketch, a pad, and a solid block whose
  size is three named numbers
- [**Sketches and constraints**](sketches-and-constraints.md) —
  how a sketch knows where it is: geometry,
  constraints, and degrees of freedom
- [**Holes, pockets and fillets**](holes-pockets-and-fillets.md) —
  cutting through the block and rounding
  its corners, one feature at a time
- [**Proving the geometry**](proving-the-geometry.md) —
  volume, area and bounding box checked
  against hand arithmetic — and the first
  build that failed the check by exactly
  half a hole
- [**Parameters and spreadsheets**](parameters-and-spreadsheets.md) —
  the same part driven by a spreadsheet,
  where changing one cell rebuilds it
- [**Exporting your part**](exporting-your-part.md) —
  STEP for other CAD programs, STL and 3MF
  for the printer, and measuring what
  comes back out
- [**The Python console**](the-python-console.md) —
  FreeCAD's built-in scripting — the tool
  this whole lab was built with, treated
  as a feature, not a back door
- [**Files and formats**](files-and-formats.md) —
  the native FCStd file opened up: it is
  a zip, and its contents explain a lot
- [**Assemblies**](assemblies.md) —
  more than one part: what FreeCAD 1.x
  ships, and what it honestly does not
- [**Recipes**](recipes.md) — a parametric
  family of brackets from one script, a
  pre-print checklist, and batch exports
- [**The neighbours**](the-neighbours.md) —
  OpenSCAD's code, Blender's meshes, the
  commercial CAD giants, and when each is
  the better tool
- [**Limits**](limits.md) — the topological
  naming problem, kernel quirks, and the
  gap between an exact model and a safe
  part
- [**Troubleshooting**](troubleshooting.md) —
  the renamed property that broke the
  first script, the constraint that did
  not centre, and the checks that catch
  both
- [**Glossary**](glossary.md) — the
  terms, collected in one place

## What it doesn't cover

Modelling by hand in the graphical
program — the mouse-and-menus craft of
sketching, dragging and picking faces —
is described from FreeCAD's documentation,
not demonstrated, because this guide's
lab had no working display (chapter 3
says exactly why). Engineering judgement
is likewise out: this guide can teach you
to make a bracket of an exact size, not
whether that bracket will hold your
shelf. Simulation, machining toolpaths
and rendering exist in FreeCAD and are
pointed at, not taught.

## How to use this guide

Read chapter 1 for the model and chapter
2 before installing anything — knowing
which layer holds what turns later
confusion into a named problem. Chapters
3 to 7 build the part; chapter 8 is the
one to read slowly even if your own build
looks right, because its checks are how
you catch a part that is quietly wrong.
The lab's scripts are
`freecad-lab/build_part.py` and
`freecad-lab/build_params.py`; its
transcripts live in
`freecad-lab/transcripts/`, and the part
itself — native, STEP and STL — sits
beside them in `freecad-lab/`.

---

## Part of the series

This guide is one of the [For Mere Mortals](https://paulsullivan33-dev.github.io/mere-mortals/) guides: plain-language guides to the tools programmers and makers use.

Related guides:

- [CAD for Mere Mortals](https://paulsullivan33-dev.github.io/cad-for-mere-mortals/)
- [OpenSCAD for Mere Mortals](https://paulsullivan33-dev.github.io/openscad-for-mere-mortals/)
- [3D Printing for Mere Mortals](https://paulsullivan33-dev.github.io/3d-printing-for-mere-mortals/)

## License

The writing in this guide is licensed under [CC BY 4.0](https://github.com/paulsullivan33-dev/freecad-for-mere-mortals/blob/main/LICENSE). Code examples and lab scripts are licensed under the [MIT License](https://github.com/paulsullivan33-dev/freecad-for-mere-mortals/blob/main/LICENSE-CODE).
