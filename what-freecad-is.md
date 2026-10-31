# What FreeCAD Is

**FreeCAD** is a **parametric 3D CAD**
program. Each of those words earns its
place. **CAD** — computer-aided design —
means software for designing physical
things: brackets, enclosures, gears,
furniture, machine parts. **3D** means
the design is a solid with volume, not a
flat drawing. **Parametric** is the word
that changes how you work, and it gets
its own section below.

FreeCAD is **free software**: free to
download, free to run, and licensed so
you may read and change its code (the
project is licensed under the LGPL; the
program announces this itself every time
it starts — transcript `t00-version.txt`
shows the banner). It runs on Windows,
macOS and Linux. It is built by a
community project, and it shows in both
directions: it is remarkably capable for
something with no price, and it is
rougher around the edges than the
commercial programs in chapter 15.

## Drawing versus modelling

A drawing program holds lines. If you
draw a rectangle that is "60 mm wide",
the 60 lives in your head and in a label;
the lines themselves would be just as
happy at 61. Move a corner and nothing
else adjusts, because nothing knows what
the rectangle *means*.

A CAD model holds a solid, and the solid
is built from **features** — a padded
sketch, a cut hole, a rounded corner —
each defined by numbers. Ask the program
for the part's volume and it answers from
the geometry itself, to as many digits as
you want. Change a number and every
feature that depends on it rebuilds. The
shape is a *consequence* of the numbers,
never the other way round.

That difference decides what the program
is good for. A drawing can describe a
part. A model can be *interrogated*: its
weight estimated from its volume and a
material, its fit against a mating part
checked before anything is cut, its
weakest dimension found by changing
numbers and watching the result.

## What "parametric" buys you

Because the numbers are the design,
families of parts become cheap. The part
this guide builds — a block, 60 × 40 × 12
mm, with a centred hole and rounded
corners — accepts its hole diameter as a
number at the top of a script. Chapter 8
proves the point with arithmetic: the
same script, told `HOLE_DIA=16` instead
of 10, produced a part lighter by
exactly the volume of the extra material
removed, π × (8² − 5²) × 12 = 1470.266
mm³, measured to the third decimal. And
chapter 9 puts those numbers in a
**spreadsheet** inside the document, so
the design becomes a table you edit
rather than a shape you redraw.

Parametric modelling has a price, and
this guide will not hide it: the model
remembers *how* it was built, step by
step, and later steps refer to earlier
geometry by names that can shift when
the shape changes — the **topological
naming problem** of chapter 16, the
single most famous frustration in
FreeCAD. It is manageable, and chapters
6 and 16 teach the working habits that
manage it, but you should know it exists
before you fall in love with the rest.

## Who it is for

FreeCAD suits people who make things:
the home workshop printing a replacement
knob, the hobbyist cutting an enclosure
on a small CNC mill, the engineer who
wants a capable CAD at home without a
four-figure subscription. Its parts can
go to a 3D printer (chapter 10), to
another CAD program (the same chapter),
or to a workshop drawing (the TechDraw
workbench, chapter 4). It is not a
sculpting tool — organic shapes belong
to Blender's world, chapter 15 — and it
is not a guarantee: as the README said,
the program will happily model a part
that would fail in service. Exact is not
the same as safe, and no chapter of this
guide can make that judgement for you.
