# Writing criteria for this guide

Every "for Mere Mortals" guide is written to the same nine-point
standard, so a reader who trusts one can trust the rest. Here it
is, with the verification notes for this particular guide below.

1. **Fix it first.** Reader outcomes lead, not action items: each
   chapter opens by naming the outcome it delivers, shows a check
   the reader can run to confirm they got it, and a reasonable
   reader finishes able to state what was done, what it means,
   and what to try next.
2. **Plain language.** Short sentences, everyday vocabulary,
   technical terms defined on first use. No slang, and no
   idioms that only make sense in one country — the reader may
   be translating as they go.
3. **No dead ends.** A guide never tells the reader to do
   something it cannot show them how to verify. Every claim a
   reader relies on — an install, a command, an output — is
   something this guide demonstrates or clearly labels
   documented-only below.
4. **Live-verified where it matters.** Procedures are run for
   real in the guide's lab wherever the build machine allows it,
   and the transcripts kept in the repository are the evidence.
   What could not be run is listed honestly below, never
   presented as if it had been.
5. **General audiences.** Nothing in this guide — examples,
   fixtures, names, addresses — is modelled on any particular
   reader or author's real life, network, or organisations.
   The lab's part is an invented bracket blank.
6. **Standalone.** A reader needs this guide, its lab, and
   nothing else. Where another guide would genuinely help, it
   is pointed to once, by name, and the chapter still completes
   without it.
7. **Honest about limits.** Chapter 16 names what the tool
   cannot do: the topological naming problem (reduced in 1.x,
   not abolished), fillets the kernel refuses, booleans that
   return invalid solids, recompute cost at scale, and the gap
   between an exact model and a safe part.
8. **The safety line is in the text, early.** FreeCAD raises no
   interception question of the kind other guides in this
   series carry, but the README and chapter 1 draw its line
   plainly — the program models exactly the part you describe,
   including one that would fail under load, and exact is not
   the same as safe — and chapter 16 repeats it as a limit.
9. **Builds clean.** The site builds with MkDocs in strict mode
   with no warnings, and a fresh reader following the chapters
   in order reaches the stated outcome of each.

## Verification notes for this guide

The build machine is a 2-CPU, ~7.7 GB Ubuntu 24.04 sandbox,
shared with other work while the lab ran. FreeCAD **1.1.4**
(revision 20260928) was obtained as the official release
AppImage `FreeCAD_1.1.4-Linux-x86_64-py311.AppImage`
(820,812,280 bytes) from the project's GitHub release page.
Its SHA-256 matched the release's published checksum file
exactly (`f6dc6ba6…43434`, transcript
`t00a-download-and-verify.txt`). The sandbox has no FUSE, so
the AppImage was unpacked with `--appimage-extract` and run
unmodified from the extracted tree (3.1 GB); the version was
confirmed from the program itself (`t00-version.txt`). All
modelling was done with `freecadcmd`, the console build of
the same engine.

Run for real, with transcripts as evidence:

- The fixture part — a Part Design body: centred rectangle
  sketch (12 constraints), pad, r2 fillet on the four vertical
  edges (found by direction, not by name), Ø10 hole pocketed
  ThroughAll — measuring volume **27816.319 mm³**, area
  7371.841 mm², bounding box 60 × 40 × 12, 11 faces / 27
  edges, one valid solid — matching hand arithmetic to every
  printed digit (t02). Both sketches report
  `FullyConstrained` True (t02b).
- The first, wrong build of the same script (a Symmetric
  constraint that did not centre the sketch): volume
  28287.558 mm³, +1.6941 %, an error of exactly half the hole
  cylinder; probing the saved shape showed bounding box
  x ∈ [0, 60] and the hole wall's centre of mass at x = 2r/π —
  kept as chapter 8's worked example (t01).
- Parametric rebuild with HOLE_DIA=16: volume **26346.053
  mm³**, again exact; the delta against the Ø10 part is
  1470.266 mm³ = π(8² − 5²) × 12 (t03).
- The spreadsheet build: identical part driven by a `Params`
  sheet through expressions on named constraints; changing
  one cell (HoleDia 10 → 16) and recomputing reproduced
  26346.053 mm³, with the sketch reporting the new diameter
  itself (t04).
- Exports from the finished part, each verified after the
  fact (t05): FCStd saved and reopened (volume identical,
  valid); STEP written (AP214 header, Open CASCADE STEP
  processor 7.8, 13,597 bytes); binary STL parsed
  independently — 1,032 triangles, file size consistent with
  its header, mesh volume from raw triangles 27816.6 mm³
  against the solid's 27816.319; 3MF exported (9,650 bytes).
  The FCStd was listed as a zip: Document.xml plus per-feature
  `.brp` shapes and `.Map.txt` element maps.
- Two genuine version/behaviour findings, both taught in the
  guide: FreeCAD 1.1 renamed the sketch attachment property
  `Support` → `AttachmentSupport` (the lab's second run died
  on it verbatim), and `freecadcmd` treats extra command-line
  words as files to open, so the lab's scripts take parameters
  from the environment (chapter 17).

Documented only — described from the project's documentation,
not run, and the text does not claim otherwise:

- All graphical modelling: clicking through sketches, pads
  and fillets, the measurement tools, and the property
  editor. The graphical program could not start in this
  sandbox (its Qt toolkit needs `libxcb-cursor0`, absent on
  this host; chapter 3). Every object the GUI steps name was
  created and inspected for real through the console, whose
  objects and properties are the same ones.
- Assemblies in use (chapter 13): the Assembly workbench's
  presence in the shipped tree was verified from the
  extracted files; joints, grounding and solving are
  described from the project documentation.
- TechDraw drawings, the FEM and CAM workbenches, and the
  Addon Manager: named and placed, not exercised.
- Actually printing or machining the part: the lab produced
  and verified the files; no printer or machine was attached
  to it.
- Neighbour characterisations in chapter 15 (OpenSCAD and
  Blender behaviour is covered by their own guides in this
  series; the commercial programs are described from their
  public material).

Fixtures are this guide's own and deliberately generic: a
60 × 40 × 12 mm block with a centred hole and rounded
corners — a bracket blank with no owner, no organisation and
no load to carry. The lab scripts are
`freecad-lab/build_part.py` and `freecad-lab/build_params.py`;
the exported part (`bracket.FCStd`, `bracket.step`,
`bracket.stl`) sits beside them.
