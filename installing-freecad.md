# Installing FreeCAD

This chapter gets you a FreeCAD whose
version you can state and whose download
you have verified. The check takes two
minutes and is the same habit this series
teaches everywhere: a program that will
hold your designs should prove it is the
program the project shipped.

## Where it comes from

FreeCAD is distributed from the project's
own site, **freecad.org**, which points
to its release page on GitHub
(`github.com/FreeCAD/FreeCAD/releases`).
There is also a package in most Linux
distributions' repositories — usually
older than the official release, which
matters more than usual here, because
FreeCAD 1.1 renamed things that scripts
and tutorials written for 1.0 rely on
(chapter 17 meets one). For this guide,
use the official build: on Windows an
installer, on macOS a disk image, on
Linux an **AppImage** — one file that
carries the whole program and its
libraries. The lab's copy was
`FreeCAD_1.1.4-Linux-x86_64-py311.AppImage`,
820,812,280 bytes, from the **1.1.4**
release of 28 September 2026.

## Verify the download

Each release asset travels with a small
companion file, the same name plus
`-SHA256.txt`, holding its published
**SHA-256 checksum**. Download both,
then compare against what your machine
computes:

```
$ cat FreeCAD_1.1.4-Linux-x86_64-py311.AppImage-SHA256.txt
f6dc6ba676e5ac96a565ebc8d657232f94c6158e85b4352141bd1a46f6b43434  ...
$ sha256sum FreeCAD.AppImage
f6dc6ba676e5ac96a565ebc8d657232f94c6158e85b4352141bd1a46f6b43434  ...
```

The lab's two lines matched exactly
(transcript `t00a-download-and-verify.txt`).
If yours ever differ, stop: delete the
file and download it again from the
project's page. A checksum that fails is
either a damaged download or the wrong
file entirely, and neither belongs near
your work.

## Running it — and the lab's detour

On Windows and macOS, install or mount
and launch as usual. On Linux, mark the
AppImage executable and run it:

```
chmod +x FreeCAD_1.1.4-Linux-x86_64-py311.AppImage
./FreeCAD_1.1.4-Linux-x86_64-py311.AppImage
```

An AppImage normally mounts itself
through a mechanism called **FUSE**. The
lab's sandbox has no FUSE, so it used the
documented escape hatch every AppImage
carries — `--appimage-extract` unpacks
the whole tree, and the programs then run
in place:

```
./FreeCAD.AppImage --appimage-extract
./squashfs-root/usr/bin/freecadcmd --version
FreeCAD 1.1.4 Revision: 20260928 (Git shallow)
```

The unpacked tree is 3.1 GB — the bundle
carries its own Python, its own libraries,
even other tools (the lab found `gmsh`
and a finite-element solver sharing the
folder). You will likely never need the
detour; the lab records it because a
sandbox is exactly where FUSE tends to be
missing, and because the extraction
doubles as a look inside the box:
chapter 4's list of workbenches was read
from that tree's `Mod` folder, not from
a brochure.

Two programs matter from here on:
**`freecad`**, the graphical program, and
**`freecadcmd`**, the same engine with a
console instead of windows — the lab's
workhorse, and chapter 11's subject.

## A confession about the graphical program

The lab could not use `freecad` itself.
Under the sandbox's virtual display the
graphical program stopped at startup:
its Qt toolkit needs a small library
(`libxcb-cursor0`) that this machine does
not have, and no screenshot exists
because no window ever opened. On your
machine — any ordinary desktop — this
does not apply; the same AppImage opens
normally. But it is why this guide's
hands-on chapters drive the console and
teach the graphical craft from the
project's documentation, labelled as
such. What is demonstrated here was
demonstrated for real; the ledger in
`criteria.md` draws the line precisely.
