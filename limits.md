# Limits

What FreeCAD cannot do, or cannot do
reliably, stated plainly. Some of these
the lab met; the rest are the project's
own well-documented behaviour, labelled
as such.

**The topological naming problem.**
Features refer to earlier geometry by
name — `Face6`, `Edge3` — and those
names are assigned by position when a
shape is built. Change an early feature
so the shape's topology shifts, and a
name can come to point at *different*
geometry: the fillet lands on the wrong
edge, a dimension measures the wrong
face, or the recompute fails outright.
This is the most famous frustration in
FreeCAD, and no honest guide may skip
it. The current state, fairly: FreeCAD
1.x's element maps — the `.Map.txt`
files visible inside every FCStd
(chapter 12) — were a major project to
make names track their geometry across
rebuilds, and they have greatly reduced
the problem. Reduced is not abolished.
The working defences are habits, all
taught earlier in this guide: attach
sketches to base planes and datum
geometry rather than to faces (chapter
5), constrain sketches to origins and
axes (chapter 6), put fillets late in
the tree (chapter 7), and in scripts,
select geometry by what it *is*, not by
its name (chapter 7 again).

**Fillets are the kernel's mood.**
Rounding is mathematically the hardest
common operation — surfaces must blend
through corners where several edges
meet — and Open CASCADE declines some
that other kernels accept: a radius
larger than the smallest face it must
cross, junctions of three filleted
edges, fillets running into holes. The
failures are usually honest (the
feature errors, the tree marks it), and
the remedies are craft: smaller radius,
fillet fewer edges per feature, fillet
earlier or later in the order. Expect a
negotiation, not a guarantee.

**Booleans can return invalid solids.**
A cut or fuse occasionally produces a
shape that fails its own validity
check, especially with faces that
merely *touch* (coplanar surfaces are
the classic trigger). This is why the
lab's scripts ask `isValid()` after
every build (chapter 8): an invalid
solid exports into invalid files and
fails downstream, in the slicer or the
machine shop, where the diagnosis costs
more.

**Exact is not safe.** The README said
it and it belongs in the limits in so
many words: FreeCAD computes the part
you describe. It does not know the
load on your bracket, the creep of your
plastic, or the code your building
inspector applies. Its FEM workbench
can simulate stresses, but a simulation
run by someone who cannot yet judge
its assumptions is a number, not a
verdict. Safety-critical parts need an
engineer, not a chapter.

**The graphical craft is a craft.**
This guide taught the model, not the
mouse: sketching fluently, picking the
right face in a crowded view, *seeing*
a design — these are skills of the hand
and eye that the lab could not practise
(chapter 3) and a book transmits only
partly. Budget your first GUI hours as
tuition.

**Scale and patience.** A document
recomputes its whole dependency chain;
a part with hundreds of features, or an
assembly of many bodies (chapter 13),
can take real time to update on modest
hardware, and FCStd files grow with
every cached intermediate shape. None
of this is a defect — it is the price
of a model that remembers everything —
but a warehouse-sized project will feel
it, and the commercial tools of chapter
15 have spent more money than FreeCAD
has smoothing exactly this.
