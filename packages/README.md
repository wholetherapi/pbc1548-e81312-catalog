# Patchbay Collective — fabrication packages

One directory per module slug, kept alongside the catalogue content.  A
directory only appears here once the module's fabrication package has actually
shipped; directories that only announce a future package contain nothing but a
status README and empty stubs.

Layout per module:

- `README.md` — package status and an overview of the shipped revision.
- `hardware/` — KiCad sources, panel artwork and fabrication outputs.
- `firmware/` — the shipped firmware for the revision.
- `docs/` — assembly notes, calibration points and the QA checklist.

Directories whose names do not match a catalogue module (archives, legacy
revisions, workshop notes) are kept for repair documentation only.
