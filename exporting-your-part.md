# Exporting Your Part

A part that only exists inside FreeCAD
is a part nobody can make. This chapter
exports the bracket three ways — for a
printer, for another CAD program, and
in FreeCAD's own format — and then, in
keeping with chapter 8's habit, measures
what actually arrived in each file.

## Which format for which journey

- **STL** — the 3D printer's lingua
  franca: a skin of triangles, nothing
  else. No units stored in the file, no
  curves, no history. Every slicer eats
  it.
- **3MF** — STL's modern successor: a
  zip holding an XML description of the
  mesh, with units and room for colour
  and more. Newer slicers prefer it.
- **STEP** (ISO 10303) — the CAD world's
  exchange format: the *exact* solid,
  curves and all, readable by essentially
  every professional CAD program. This is
  what you send a machine shop or a
  colleague on different software.
- **FCStd** — FreeCAD's native document
  (chapter 12): the only format that
  keeps the feature tree, the sketches
  and the spreadsheet — the design
  itself, editable. Archive this one even
  when you ship the others.

## What the lab exported — and checked

All four were produced from the finished
part (the 3MF export runs through the
Mesh workbench; the rest are one call
each in the scripts). Verification,
transcript `t05-exports.txt`:

**STEP.** 13,597 bytes, and its header
says what it is in the standard's own
ceremony:

```
FILE_DESCRIPTION(('FreeCAD Model'),'2;1');
FILE_SCHEMA(('AUTOMOTIVE_DESIGN { 1 0 10303 214 1 1 1 1 }'));
```

— an AP214 solid, written by "Open
CASCADE STEP processor 7.8": chapter 2's
kernel, signing its work.

**STL.** 51,684 bytes holding 1,032
triangles — a claim the lab checked
forensically rather than trusted: a
binary STL is an 84-byte header and
50 bytes per triangle, and 84 + 50 ×
1032 = 51,684 exactly. Then the triangles
themselves were summed, edge by edge,
into a volume by a small independent
script that knows nothing of FreeCAD:
**27,816.6 mm³** against the true solid's
27,816.319. That gap — a few parts in
ten thousand — is the honest price of
approximating cylinders with flat
facets, and it is why STL is a
*manufacturing* format, not an archival
one: fine for a printer laying down
0.2 mm layers, wrong for a part whose
curved surfaces must stay exact. (Mesh
density is a setting; finer triangles
shrink the gap and grow the file.)

**3MF.** Exported successfully, 9,650
bytes — smaller than the STL for the
same mesh, one of its design goals.

**FCStd.** Saved, closed, and reopened:
the shape that came back reports volume
27816.319 mm³ and valid — the native
round trip is lossless, as it must be,
since this is the format the design
actually lives in.

## The print path, honestly

From STL or 3MF, a **slicer** (a separate
program — this series' OrcaSlicer and
3D Printing guides cover that world)
turns the mesh into printer instructions.
FreeCAD's part in that story ends at a
mesh that is *watertight* — one solid,
no holes in the skin — which is why
chapter 8's "solids: 1, valid: True"
line matters beyond tidiness: a mesh
built from a valid solid tessellates
cleanly, and the 1,032 triangles above
are that cleanliness, counted. What this
lab did not do is print anything; no
printer was attached to it, and the
guide claims the files, not the object.
