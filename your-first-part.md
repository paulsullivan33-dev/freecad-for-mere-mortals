# Your First Part

By the end of this chapter you have a
solid block of exact size — 60 × 40 × 12
mm — built the Part Design way, and you
understand every step because the lab
performs it in a script you can read:
`freecad-lab/build_part.py`. In the
graphical program the same steps are a
sketch drawn with the mouse and a Pad
button; the objects created are identical
either way, which is why a typed lab can
teach a clicked craft's foundations.
(Documentation covers the clicking; this
chapter covers the *model*, which is the
part that transfers.)

## The parameters come first

The script opens with the design stated
as named numbers — the habit this whole
guide exists to teach:

```python
LENGTH = 60.0   # X size of the block
WIDTH = 40.0    # Y size of the block
HEIGHT = 12.0   # Z size of the block (the pad length)
HOLE_DIA = 10.0  # centred through-hole diameter
FILLET_R = 2.0  # radius on the four vertical corners
```

Millimetres, always, in FreeCAD's world,
unless a document says otherwise. Nothing
in the part will be typed twice: every
later line refers to these names.

## A body, and a sketch on a plane

```python
doc = App.newDocument("BracketBlock")
body = doc.addObject("PartDesign::Body", "Body")
XY = [f for f in body.Origin.OriginFeatures if f.Name == "XY_Plane"][0]

sk = body.newObject("Sketcher::SketchObject", "BlockSketch")
sk.AttachmentSupport = [(XY, "")]
sk.MapMode = "FlatFace"
```

A new body brings an **origin**: three
axes and three planes, the document's
fixed frame of reference. The sketch is
**attached** to the XY plane — flat on
the floor of the world, so to speak — and
attachment matters: a sketch glued to a
base plane cannot drift when the model
changes, a small decision that chapter 16
will show is worth real money. (In
FreeCAD 1.0 and earlier the property was
called `Support`; 1.1 renamed it
`AttachmentSupport`, and older scripts
stop dead on the difference — chapter 17.)

## Drawing the rectangle

Four line segments, corner to corner:

```python
pts = [(-L2, -W2), (L2, -W2), (L2, W2), (-L2, W2)]
for i in range(4):
    sk.addGeometry(Part.LineSegment(...), False)
```

On their own these are just four lines
that happen to touch — a drawing, in
chapter 1's sense. What turns them into
a rectangle that *means* 60 × 40, centred
on the origin, is the constraint work of
chapter 6: corners made coincident,
sides made horizontal and vertical, the
corner's position fixed from the origin,
and two named dimensions, `Length` and
`Width`, holding the sizes. In the GUI
you would click the same constraints
from the toolbar; the solver cannot tell
the difference.

## The pad: a sketch with thickness

```python
pad = body.newObject("PartDesign::Pad", "Pad")
pad.Profile = sk
pad.Length = HEIGHT
doc.recompute()
```

A **pad** stretches a sketch's filled
outline along its normal — here, up from
the XY plane — by the given length. The
recompute is where the kernel does its
work: after it, `pad.Shape` is a true
solid, 28,800 mm³ of it (60 × 40 × 12 —
a sum chapter 8 will hold the whole part
to). The body's **tip** is now the pad.
Save the document and you have a part:
plain, holeless, sharp-cornered, and
already more useful than a picture of
one, because every number in it can
still be changed.

In the graphical program, expect this
same shape of work: New Body, New Sketch
(pick the XY plane), draw, constrain,
close the sketch, Pad, type 12. The
clicks differ; the tree does not.
Chapter 6 now slows down on the
constraints, because they — not the
lines — are where a sketch's quality is
decided.
