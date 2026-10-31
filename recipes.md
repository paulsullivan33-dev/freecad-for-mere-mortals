# Recipes

Short, complete jobs assembled from steps
the earlier chapters proved. Nothing
here introduces a new mechanism; each
recipe names the transcripts its steps
were verified in.

## A variant in one line

*You have the bracket; you need it with
a 16 mm hole for a bigger bolt.*

Chapter 9's run, verbatim in spirit:

```
HOLE_DIA=16 freecadcmd build_part.py
```

Read the measurements before you keep
the file: volume 26346.053 mm³, bounding
box unchanged, faces still 11. If a
variant's numbers surprise you, the
variant is wrong, whatever the shape
looks like (`t03-parametric-hole16.txt`).

## A family, not a part

*You need the bracket in five hole
sizes for a workshop drawer.*

The same script is the loop body; a
shell loop over sizes produces five
folders of FCStd + STEP + STL, each with
its measurements printed as it builds:

```
for d in 6 8 10 12 16; do
  HOLE_DIA=$d OUTDIR=out_$d freecadcmd build_part.py
done
```

Because every run re-proves itself
(chapter 8's block is at the end of the
script), the batch is self-checking:
grep the five outputs for `volume error`
and anything that is not `0.0000 %` is a
part to discard, not to debug by eye.
Names live in the parameters, so the
family stays consistent in every
dimension but the one you varied.

## The pre-print checklist

*Before any STL leaves for a slicer:*

1. Recompute, and confirm the tip
   feature reports no error.
2. Ask the shape its three questions —
   solids: 1; valid: True; volume equal
   to the hand sum or the last trusted
   value (chapter 8).
3. Export the STL, then *measure the
   file*: byte size against its triangle
   count (84 + 50 × n), as chapter 10
   did, if the export matters.
4. Keep the FCStd with the STL, same
   folder, same name. The mesh is a
   photograph; the FCStd is the recipe
   (chapter 12).

## Hand the part to someone else

*The recipient does not "do CAD"; they
need the hole at 14 mm and the length
at 80.*

Ship the spreadsheet build
(`build_params.py`, chapter 9): the
FCStd carries its Params sheet inside
it. The recipient opens one file, edits
two labelled cells, recomputes — the
part follows, and every other dimension
is guaranteed untouched, because it was
never re-typed. Send chapter 9 with it;
it is three pages and it is the manual
for exactly this.
