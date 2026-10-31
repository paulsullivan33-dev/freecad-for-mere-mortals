# The Python Console

Everything in this guide was built by
typing. This chapter makes that a
feature instead of a confession:
FreeCAD's scripting is not an add-on but
the program's own machinery exposed, and
learning its outline pays even if you
model with the mouse forever.

## Two doors, one room

`freecadcmd` — the console program the
lab used — and the graphical `freecad`
run the same engine: same document
format, same objects, same kernel. Start
the console and its banner names the
build (transcript `t00-version.txt`):

```
FreeCAD 1.1.4, Libs: 1.1.4R20260928 (Git shallow)
```

Inside the graphical program there is a
Python console panel with the same
interpreter, watching the same document
you are clicking on. Nothing in the
lab's scripts is console-only magic;
each line names an object and a property
that the GUI also has — the Pad's
`Length`, the sketch's `Constraints`,
the body's `Shape`. Reading a script is
therefore a way of *learning the GUI's
vocabulary*: the property editor's rows
are these same names.

## What scripting is for

- **Repetition.** Chapter 14's recipe
  builds a family of brackets by looping
  over a table of sizes — forty parts in
  the time one takes by hand, each
  exported and measured.
- **Proof.** Chapter 8's checks — volume,
  bounding box, face census — are three
  lines of console. GUI measurement tools
  answer the same questions one at a time;
  a script answers them *every* time, on
  every rebuild, without forgetting.
- **Excavation.** When a model misbehaves,
  asking the shape directly — which face
  is the cylinder, where is its centre of
  mass — is how chapter 8 found a hole
  sitting on an edge. The GUI can show
  you the part; the console can
  *interrogate* it.
- **Generation.** Geometry too tedious
  or too regular to draw — gear teeth,
  thread profiles, a hundred holes in a
  pattern — is a loop, not an afternoon.

## The shape of a script

The lab's scripts follow a pattern worth
copying: parameters at the top, build in
the middle, **measurements printed at
the end** — so a script's output is not
"it ran" but "it ran *and the part is
provably this*". Scripts run with
`freecadcmd build_part.py`; parameters
arrive through the environment (chapter
9) because argument passing under
`freecadcmd` has its own opinions
(chapter 17's first entry).

## Honest limits of the typed door

Two, both met by the lab. First, the API
moves between versions: chapter 3's
`AttachmentSupport` rename broke a
script written for 1.0 semantics, and
FreeCAD does not promise scripts eternal
life — pin your FreeCAD version in any
script that matters, as this guide pins
1.1.4. Second, some things are
genuinely GUI-shaped: picking "that
face, there" with a mouse is one click
and, in code, a small investigation
(chapter 7's edge-finder is the lab's
answer, and it is more code than the
click). The console is a first-class
door, not the only one; the craft is
knowing which door a given job wants.
