# Holes, Pockets and Fillets

The block from chapter 5 is a slab. This
chapter turns it into the finished part —
rounded corners and a hole through the
middle — with the two feature types that
cover most of real modelling: **fillet**,
which reshapes existing material, and
**pocket**, the cutting twin of the pad.

## The fillet: rounding the vertical corners

A **fillet** replaces a sharp edge with
a rounded surface of a given radius.
The script's problem is *which edges*:
the pad's shape has twelve, and the four
wanted are the vertical ones. Rather
than hard-coding edge names — which are
exactly the fragile references chapter
16 warns about — the script *finds*
them, by asking each edge's curve which
way it points:

```python
for i, e in enumerate(pad.Shape.Edges):
    if abs(e.Curve.Direction.z) > 0.999:   # runs along Z: vertical
        vertical.append("Edge%d" % (i + 1))
fillet = body.newObject("PartDesign::Fillet", "CornerFillet")
fillet.Base = (pad, vertical)
fillet.Radius = FILLET_R
```

On the lab's pad it found `Edge1, Edge2,
Edge5, Edge8` (transcript
`t02-build-fixed.txt`), and the recompute
replaced four sharp corners with quarter
cylinders of radius 2 mm. Each corner
loses a little material — the square the
rounding cuts away, 2² − π·2²/4 mm² of
it, times the height — a number chapter
8 needs exactly: 10.301 mm³ per corner.

Two habits hide in this small code.
First, *select by meaning, not by name*,
whenever a script can. Second, notice the
order: the fillet is applied to the pad
*before* the hole is cut, because feature
order is the design's story — chapter 2's
tree — and a fillet attempted over an
edge the hole later removes is a classic
way to break a model.

## The pocket: a pad that removes

A **pocket** is a pad run in reverse: a
sketch's outline, stretched through the
body, *subtracting* material instead of
adding it. The hole sketch is the
simplest sketch in the guide — one
circle, two constraints (its centre
coincident with the origin, one named
**Diameter** constraint, `HoleDia`):

```python
sk2.addGeometry(Part.Circle(App.Vector(0, 0, 0),
                            App.Vector(0, 0, 1), HOLE_DIA / 2.0), False)
sk2.addConstraint(Sketcher.Constraint("Coincident", 0, 3, -1, 1))
c_dia = sk2.addConstraint(Sketcher.Constraint("Diameter", 0, HOLE_DIA))
```

"Coincident with the origin" works
because chapter 6 centred the block on
that same origin: one fixed point serves
both sketches, and the hole is centred
*by construction*, not by measurement.

```python
pocket = body.newObject("PartDesign::Pocket", "Hole")
pocket.Profile = sk2
pocket.Type = "ThroughAll"
pocket.Reversed = True
```

Two details deserve a reader's attention.
**ThroughAll** is a pocket *type*: cut
through everything, however thick the
body becomes later — a promise that
survives chapter 9's parameter changes,
where a fixed depth of "12 mm" would
silently stop being true if the height
ever changed. And **Reversed**: the hole
sketch sits on the XY plane, at the
block's *floor*, so the cut must run
upwards, against the sketch's default
direction. Get it wrong and the pocket
either cuts air below the part or the
recompute complains there is nothing to
cut — an error worth meeting once, in a
lab, rather than in a design you care
about.

## The finished part

After the recompute, the body's tip is
the pocket, and the part is complete:
one valid solid (the script asks, and
`shape.isValid()` answers True), eleven
faces — top, bottom, four sides, four
fillet cylinders, one hole wall. Whether
it is the part you *intended* is a
different question from whether it is a
valid solid, and it is exactly the
question chapter 8 exists to answer —
with sums.
