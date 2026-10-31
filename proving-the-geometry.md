# Proving the Geometry

A CAD program that builds the wrong part
does not usually tell you. It shows a
plausible shape, valid and solid, and the
wrongness waits inside the numbers. This
chapter is the guide's centre for the
same reason the audio chapter was in the
Piper guide: it shows how to *prove* a
part is the part you meant, using checks
the program cannot pass by accident —
and then tells the story of this guide's
own first build, which failed them.

## The hand sum

Our part is three facts of school
geometry standing on each other:

- the block: 60 × 40 × 12 = **28,800 mm³**
- minus the hole, a cylinder:
  π × 5² × 12 = **942.478 mm³**
- minus four filleted corners, each the
  square the rounding removes:
  (2² − π·2²/4) × 12 = 10.301 mm³,
  so **41.204 mm³** for the four

Expected volume: 28,800 − 942.478 −
41.204 = **27,816.319 mm³**. Expected
bounding box: exactly 60 × 40 × 12 (the
fillets round *inside* the outline; the
hole breaks no surface but the top and
bottom). Expected face count: 11 (see
chapter 7). Any program output that
disagrees with these numbers is wrong,
however good it looks — that is what
makes them a proof and not a vibe.

## The program's answer

The script reads the finished shape's own
measurements (`t02-build-fixed.txt`):

```
valid solid: True | solids: 1
volume measured : 27816.319 mm^3
volume expected : 27816.319 mm^3
volume error    : -0.0000 %
bounding box    : 60.000 x 40.000 x 12.000 mm
faces: 11  edges: 27  vertices: 18
```

Agreement to every printed digit. The
surface area gets the same treatment in
the lab notes — top and bottom with the
hole and corners accounted, four sides
shortened by the fillets, four fillet
walls and the hole wall — 7,371.84 mm²
by hand against 7,371.841 measured. A
kernel measuring the *true* curved solid
lands exactly on the closed-form sums;
that is what "exact geometry" means in
practice, and it is why CAD volumes can
be trusted in a way mesh volumes
(chapter 10) only approach.

## The first build, which was wrong

The first run of the same script printed
this instead (transcript
`t01-first-build-wrong.txt`):

```
volume measured : 28287.558 mm^3
volume error    : 1.6941 %
faces: 12  edges: 32  vertices: 22
```

Valid solid. Plausible shape. And
**471.239 mm³ too heavy** — a difference
that is, to the digit, *half the hole's
cylinder*. Numbers that clean are an
accusation: somewhere, half a hole
exists. Probing the saved shape found
both halves of the story:

```
bbox min (-0.00, -20.00, 0.00)  max (60.00, 20.00, 12.00)
hole face centre of mass (3.183, 0, 6)
```

The bounding box runs from x = 0 to 60 —
the block was never centred (chapter 6's
Symmetric constraint had not said what
its author meant). The hole, dutifully
placed at the origin, therefore sat on
the block's *edge*, cutting a half-disc
notch instead of a hole; and 3.183 is
2r/π, exactly where the centre of mass
of a *half*-cylinder wall must sit (a
whole one would sit at 0) — the shape
confessing its own geometry to anyone
who asks in numbers.

Read the moral carefully, because it is
the chapter: **the error was not in the
modelling but in the assumption**, and
no amount of looking at the part would
have found it as fast as one subtraction
did. The fix took two lines (explicit
distances from the origin, chapter 6)
and the re-run matched the hand sum
exactly. Every check in this chapter is
one you can run on your own parts, in
the GUI's measurement tools or in three
lines of console — chapter 11 shows the
console form. Run them especially when
the part "looks right". Looks are how
the first build passed.
