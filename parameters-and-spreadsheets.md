# Parameters and Spreadsheets

Chapter 5 put the design's numbers at
the top of a script. This chapter puts
them *inside the document*, in a
spreadsheet any user can open and edit —
the difference between a part its author
can reprogram and a part its *owner*
can configure. The lab's second script,
`freecad-lab/build_params.py`, builds
the identical bracket this way, and this
chapter is its story.

## First, proof the parameter idea itself

Before the spreadsheet, the plain claim
deserves its evidence: is the part from
chapter 5 really *parametric* — does a
changed number rebuild it correctly?
The script reads the hole diameter from
the environment, so one shell line runs
the experiment (transcript
`t03-parametric-hole16.txt`):

```
$ HOLE_DIA=16 freecadcmd build_part.py
volume measured : 26346.053 mm^3
volume expected : 26346.053 mm^3
volume error    : 0.0000 %
```

The difference from the 10 mm part is
1470.266 mm³ — exactly π × (8² − 5²) × 12,
the extra cylinder removed, neither a
microlitre more nor less. The bounding
box did not move; the face count did not
change; the fillets are untouched. That
is parametric behaviour *proven*, not
asserted: the model is a function, and
the lab evaluated it at two points and
checked both against closed-form sums.

## The spreadsheet as the part's dashboard

The Spreadsheet workbench gives a
document a grid of cells. Cells can hold
numbers, and — the essential move — can
be given **aliases**, names by which the
rest of the document refers to them:

```python
sheet = doc.addObject("Spreadsheet::Sheet", "Params")
rows = [("Length", 60.0), ("Width", 40.0), ("Height", 12.0),
        ("HoleDia", 10.0), ("FilletR", 2.0)]
for i, (name, value) in enumerate(rows, start=1):
    sheet.set("A%d" % i, name)
    sheet.set("B%d" % i, repr(value))
    sheet.setAlias("B%d" % i, name)
```

Then the model stops containing numbers
and starts containing **expressions** —
pointers at the sheet. This is where
chapter 6's named constraints collect
their reward:

```python
sk.setExpression("Constraints.Length", "Params.Length")
sk.setExpression("Constraints.Width", "Params.Width")
pad.setExpression("Length", "Params.Height")
sk2.setExpression("Constraints.HoleDia", "Params.HoleDia")
fillet.setExpression("Radius", "Params.FilletR")
doc.recompute()
```

Bound this way, the part reports the
same 27816.319 mm³ as before — the
spreadsheet changed where the numbers
live, not what they are. Then the lab
changed exactly one cell (transcript
`t04-spreadsheet.txt`):

```
bound to sheet:      volume 27816.319  expected 27816.319
HoleDia cell now 16: volume 26346.053  expected 26346.053
hole diameter as the sketch reports it: 16.000 mm
```

One cell, one recompute, and the sketch
*itself* now believes the hole is 16 mm —
the same destination as the scripted
run, reached by editing a table. In the
graphical program this is the everyday
workflow the feature exists for: open
the Params sheet, type a new value, and
watch the part follow.

## When to use which

Script parameters (chapter 5) suit parts
*generated* by other programs or built
in batches — chapter 14 uses them that
way. Spreadsheet parameters suit parts
*handed to a person*: the sheet is
visible, printable, and safe to edit
without reading code, and it travels
inside the same FCStd file as the part
(chapter 12). Either way, the discipline
is identical and it is the guide's whole
thesis: every size exists exactly once,
under a name, and the shape is merely
what the names currently say.
