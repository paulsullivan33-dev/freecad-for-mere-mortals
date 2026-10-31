# The Moving Parts

This chapter names the layers inside
FreeCAD, so that when something behaves
strangely later you know which layer to
blame. Five ideas carry the whole
program: a **kernel**, a **document**, a
**body**, a **feature tree**, and a
**sketch**.

## The kernel does the maths

Underneath everything sits a geometry
**kernel** — a library whose job is
exact solids: what is the volume of this
shape, does this cut leave one solid or
two, where exactly do these two curved
surfaces meet. FreeCAD's kernel is
**Open CASCADE** (you will see its name
in the STEP files of chapter 10, which
it writes). When this guide's lab asked
for a volume and got 27816.319 mm³, that
number came from the kernel measuring
the true curved solid — not from a mesh
approximation. The kernel is also where
the quirks live: it decides how a
cylinder's surface is split into faces,
and its naming of faces and edges is the
root of chapter 16's problem.

## The document is the file

A **document** is one FreeCAD file —
your whole project: every part, sketch,
spreadsheet and setting in it. Chapter
12 opens one up and finds a zip archive
holding an XML description plus the
geometry of every object. When you save,
you save the document; when the program
**recomputes**, it walks the document's
objects in dependency order and rebuilds
each from its inputs.

## The body and the feature tree

Inside a document, a **body** (in the
Part Design way of working, chapter 4)
is one solid part under construction.
The body is built as a **tree of
features**: a pad, then a fillet on the
pad, then a pocket through both. Each
feature takes the previous feature's
solid and modifies it, and the body's
visible shape is the *last* feature's
result — its **tip**.

This is why FreeCAD can change its mind
so well: edit the first feature's sketch
and the fillet and the pocket rebuild on
top of the new shape, because they were
never shapes themselves, only
instructions. It is also why order
matters and why a broken feature poisons
everything after it. Our part's tree has
four entries — BlockSketch, Pad,
CornerFillet, Hole (on HoleSketch) — and
the saved file keeps the intermediate
shape of every one (chapter 12 shows
them, named, inside the zip).

## The sketch is the drawing that isn't

A **sketch** is a flat, 2D drawing that
lives on a plane and feeds a feature:
pad it and it becomes a slab; the slab's
outline *is* the sketch, stretched
through a thickness. What makes a sketch
different from a drawing in a paint
program is **constraints** — chapter 6's
subject: statements like "this side is
60 mm", "these corners coincide", "this
circle sits on the origin". The sketch
solver keeps every statement true at
once, and counts the freedom remaining
as **degrees of freedom**. A sketch whose
freedom is all spent is **fully
constrained** — it cannot wobble — and
that, not the picture, is what makes it
engineering rather than art.

## Workbenches are toolboxes, not rooms

FreeCAD organises its tools into
**workbenches** — themed toolboxes
(Sketcher, Part Design, Spreadsheet,
TechDraw for drawings, CAM for toolpaths,
and more; chapter 4 lists the ones the
lab's copy shipped). Switching workbench
changes the tools on offer, not the
document: all of them read and write the
same objects. Think of one workshop with
many benches, one project on the table.

## The console underneath

Finally, everything the graphical program
can do is also reachable from **Python**,
FreeCAD's built-in scripting language —
every object, property and command this
guide uses was driven from the console
program `freecadcmd`, which is how a lab
with no screen could build real parts.
Chapter 11 treats scripting as what it
is: not a back door for programmers, but
the same front door, typed instead of
clicked.
