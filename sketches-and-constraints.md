# Sketches and Constraints

A sketch is a set of promises. The
geometry — lines, arcs, circles — is
what you see; the **constraints** are
what the sketch *guarantees*: this side
is horizontal, this corner touches that
one, this length is 60 and may not drift.
This chapter works through the constraint
set of the guide's block sketch, because
reading one real set teaches the whole
vocabulary.

## Degrees of freedom

Every unconstrained point in a sketch can
wander in two directions; the solver
counts the wandering left as **degrees
of freedom** (DoF). A sketch with DoF
remaining can still change shape when
something upstream moves — sometimes
that is freedom you want, more often it
is a surprise scheduled for later.
**Fully constrained** means DoF = 0:
the geometry can only be what the
constraints say. Good sketches aim for
it; the graphical program reports the
count as you work, and a sketch answers
the question directly — its
`FullyConstrained` property is what the
lab checked in the transcript above.

## The block sketch, constraint by constraint

The rectangle from chapter 5 has four
lines and, in the end, twelve
constraints — and the finished sketch
reports itself **fully constrained**,
as does the hole sketch of the next
chapter (transcript
`t02b-fully-constrained.txt`):

- **Coincident** (×4): each line's end
  *is* the next line's start — one point,
  not two that merely overlap. Without
  this, the "rectangle" is four sticks;
  a pad would refuse it or, worse, accept
  a hairline crack.
- **Horizontal / Vertical** (×4): the
  sides' directions, fixed. Two numbers
  (the side lengths) now fully determine
  the shape's proportions.
- **Position from the origin** (×2): the
  first corner is pinned at (−30, −20) by
  two signed distance constraints from
  the origin point. The rectangle is
  thereby *centred* — its middle is the
  world's origin, which is why the hole
  of chapter 7 can be specified as
  "a circle at (0, 0)".
- **Length and Width** (×2): dimensional
  constraints, and the script *names*
  them — `sk.renameConstraint(c_len,
  "Length")`. A named constraint is an
  addressable number: chapter 9 will
  point a spreadsheet at `Constraints.
  Length` and drive the rectangle from a
  table cell.

That is the whole method: shape from
geometry, position from the origin,
sizes from named dimensions. A sketch
constrained this way cannot surprise
you later; one constrained by eye can,
and eventually will.

## A constraint that didn't — the honest bit

The lab's first version of this sketch
used a **Symmetric** constraint to centre
the rectangle — two opposite corners
declared symmetric about the origin. It
looked right, the solver accepted it,
the build succeeded. It was wrong: the
solved rectangle ran from x = 0 to 60
instead of −30 to 30, centred on nothing.
Chapter 8 tells how the measurements
caught it (the bounding box gave it away
in one line). The lesson stands on its
own here: a constraint in the list is
not a constraint *understood*. The
solver enforces what you actually said,
which is not always what you meant —
the sketching version of a truth this
series meets in every tool it covers.
The fix was not cleverer constraints,
just more explicit ones: two plain
distances from the origin, which say
exactly where the corner is.

## Working habits that pay

- **Constrain to the origin and the
  axes**, not to other geometry, whenever
  you can — they never move.
- **Name your driving dimensions** at
  the moment you create them; future you
  (and chapter 9's spreadsheet) will
  refer to them by name.
- **Spend all the freedom.** If DoF
  remains, decide whether it is deliberate.
- **Read the solver's complaints.** A
  redundant or conflicting constraint is
  the sketch telling you two of your
  promises disagree; believe it early,
  while the fix is small.
