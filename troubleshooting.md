# Troubleshooting

The failures this guide's lab actually
met, plus the checks that caught them.
In keeping with the series, each entry
starts from the symptom as it appeared.

## "Object has no attribute 'Support'"

`'Sketcher.SketchObject' object has no
attribute 'Support'` — the lab's second
run died in its first second. FreeCAD
**1.1 renamed the sketch attachment
property**: what scripts and tutorials
for 1.0 call `Support` is
`AttachmentSupport` now. The fix is one
word; the lesson is bigger. Scripts are
written against a version. State yours
(chapter 3 pins 1.1.4), and when a script
from the internet fails on an attribute
that plainly *should* exist, check the
version it was written for before you
check your own typing.

## freecadcmd eats your arguments

`File format not supported: out10` — the
console program treats extra words on
its command line as *more files to open*,
so passing a script parameters the usual
way mangles both. The lab's scripts take
their parameters from the **environment**
instead (`HOLE_DIA=16 freecadcmd
build_part.py`), which chapter 9's
recipes rely on. If a value must reach
a script, the environment is the
reliable door.

## The part built, and it is wrong

Symptom: no error anywhere; volume off
by a suspiciously round amount. This is
chapter 8's whole story — the lab's
block was uncentred by a misunderstood
constraint and its hole became a notch,
the giveaway being an error of *exactly
half a cylinder* and a bounding box
starting at 0 where −30 was expected.
The general form: **when a measurement
is wrong by a clean fraction, believe
it literally** and go looking for the
half, the double, or the factor of ten
that the geometry is confessing to.
Checks, in the order the lab learned to
run them: bounding box against
intention; volume against the hand sum;
face census against the design (a hole
adds a face; a notch changes two).

## The pocket cut nothing, or the wrong way

A pocket whose sketch lies on a body's
*base plane* cuts in the sketch's
default direction — which may be *out
of* the part. The recompute then errors
or, quieter, the volume simply does not
change. Chapter 7's build needed
`Reversed = True` for exactly this
reason. Diagnosis is chapter 8's again:
compare volume before and after the
feature; a cut that removed nothing is
a cut that went somewhere else.

## A feature errors after an edit upstream

The tree marks the failing feature and
everything below it stops. First suspect
is chapter 16: an edit changed the
shape's topology and a stored face or
edge name now points somewhere else —
or nowhere. Open the failing feature,
re-select its references (in the GUI, by
clicking the geometry it should use; in
a script, by selecting on meaning, as
chapter 7's edge-finder does), and
recompute. If a *fillet* is the failure,
try a smaller radius before anything
else; it is the kernel's most common
refusal (chapter 16).

## The graphical program will not start

On a normal desktop this is rare. In
servers, sandboxes and virtual displays
it is not: the lab's AppImage stopped
with a Qt platform error, traced to a
missing `libxcb-cursor0` library on the
*host* (chapter 3). The console program
is unaffected by all of it — one more
reason chapter 11's door is worth
knowing: a machine that cannot open the
window can still build, measure and
export the part.

## "It worked in the tutorial"

Tutorials age across versions in the
small ways this chapter is made of: a
renamed property, a moved menu, a
default that flipped. When steps and
your screen disagree, trust the
*objects* over the instructions —
inspect the thing in front of you (its
properties are listed in the GUI's
property editor and in the console
alike), and let chapter 2's map tell
you which layer you are actually
looking at.
