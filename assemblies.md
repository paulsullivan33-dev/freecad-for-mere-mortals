# More Than One Part — Assemblies

A part is not a product. The bracket of
the previous chapters bolts to something,
and the question "do the holes line up,
does the lid clear the board, does the
arm swing without hitting the frame" is
asked of an **assembly**: several bodies
placed in relation to each other. This
chapter is labelled plainly: the lab
built single parts only, so what follows
is documented from the project's own
material, not demonstrated — read it as
a map of what awaits, with the honest
state of things as of FreeCAD 1.1.4.

## What ships in the box

FreeCAD 1.x carries a built-in
**Assembly** workbench — it is in the
program tree the lab unpacked in chapter
3, alongside the other workbenches. Its
model, from the project's documentation:
bodies are brought into an assembly as
**components**, one component is
**grounded** (fixed in space), and the
rest are connected by **joints** —
relationships that permit exactly the
motion the real connection permits. A
hinge joint lets a lid rotate and
nothing else; a slider lets a drawer
translate; a fixed joint makes two
parts one. An assembly **solver** then
keeps every joint true at once, and you
can drag a part and watch the mechanism
obey its own rules — the assembly-level
cousin of the sketch solver of chapter 6.

Before the built-in workbench existed,
assemblies were done with add-on
workbenches (A2plus and Assembly4 are
the names a search will meet), installed
through the Addon Manager. They still
exist and hold older projects; new work
in 1.x starts with the built-in.

## The honest state of it

Three cautions, stated as the
documentation and the project's own
issue history support them. First,
assembly modelling is younger in FreeCAD
than part modelling: the joints and the
solver work, but the polish — and the
decade of tutorials — that Part Design
has, it does not, yet. Second, an
assembly multiplies chapter 16's naming
problem by the number of parts: every
joint refers to geometry on two bodies,
and a careless edit upstream can move a
joint's anchor. The habits of chapter 6
(constrain to origins and planes) pay
double here. Third, large assemblies
stress the recompute: each part rebuilds
in dependency order, and a mechanism of
hundreds of bodies is a patience test on
modest hardware. None of this makes
assemblies a bad idea — a bracket whose
holes were checked against its mating
part in an assembly is worth ten checked
alone — but it makes them the *second*
skill, learned after single parts are
boring. Which is this guide's order too.
