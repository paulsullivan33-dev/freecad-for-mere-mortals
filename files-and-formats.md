# Files and Formats

This chapter takes the native file
apart. It is a short chapter with a long
shadow, because what is inside
`bracket.FCStd` explains both how
FreeCAD remembers a design and where
chapter 16's famous problem lives.

## The FCStd file is a zip

Rename it if you like; any zip tool
opens it. The lab listed the contents
of the guide's own part (transcript
`t05-exports.txt`):

```
Document.xml                    64,029 bytes
Body.Shape.brp                  19,140 bytes
BlockSketch.Shape.brp            1,671 bytes
Pad.Shape.brp                    5,217 bytes
CornerFillet.Shape.brp          17,604 bytes
Hole.Shape.brp                  21,271 bytes
...and a .Map.txt beside most shapes
```

Three kinds of content:

- **`Document.xml`** — the design as
  data: every object, its type, its
  properties, the expressions of chapter
  9, the constraint values. This is the
  *recipe*.
- **`.brp` files** — the geometry itself,
  one per object, in Open CASCADE's
  native shape format: the pad's solid,
  the fillet's solid, the final shape.
  This is the *result*, cached per
  feature — which is why a document can
  reopen and show its part instantly,
  before any recompute.
- **`.Map.txt` files** — the element
  maps: for each shape, the names of its
  faces and edges and where they came
  from. Unassuming text files, and the
  front line of the topological naming
  problem — FreeCAD 1.x keeps these maps
  precisely so that "the face the fillet
  was applied to" can be tracked across
  rebuilds. Chapter 16 picks this up.

Notice what the file therefore *is*: not
a picture of a part, and not just a
solid, but the full construction —
sketches, parameters, intermediate
shapes — in an open container you can
inspect with tools you already have.
Version-control systems can store it;
diff tools can read the XML half of it;
and a corrupted download shows up as a
zip that will not open, long before it
shows up as a wrong part.

## The other formats, placed

Chapter 10 exported STEP (the exact
solid, for other CAD), STL and 3MF (the
triangle skin, for printers). Against
the anatomy above their poverty is the
point: an STL holds *only* the skin of
the final shape — no recipe, no
parameters, no names. That is why the
rule of this guide is: **archive the
FCStd, ship the STEP, print the STL.**
Losing the FCStd and keeping the STL is
keeping a photograph of a cake in place
of the recipe — recognisable, and no
way back to the ingredients.

One more resident of the file worth
knowing: the spreadsheet of chapter 9
lives in `Document.xml` too, cells,
aliases and all. Send someone the FCStd
and you have sent them the part *and*
its dashboard.
