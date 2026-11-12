# Patchbay Collective — module catalogue source

Static content for the collective's public module catalogue.  The site
generator reads every Markdown file under `modules/` and renders it to the
public showcase.

Layout:

- `modules/` — one Markdown file per catalogue module.  Front matter carries
  the title, revision, format, summary and an optional
  `fabrication_package_url` pointing at the module's fabrication package.
- `packages/` — one directory per module slug holding that module's
  fabrication package (hardware sources, firmware and assembly docs).  A
  directory only appears once the package has actually shipped; directories
  that merely announce a future package contain a status README and empty
  stubs only.
- `data/fabrication_ledger.json` — the canonical production ledger kept by the
  workshop coordinators.  Each run is recorded with the modules that were
  physically built; a run is either `finalized` (it shipped) or `planned`
  (it is still being scheduled).  The per-module `batches` arrays are the
  authoritative record of which runs included a module.
- `scripts/render_ledger.py` — renders a human-readable copy of the ledger to
  `site/archive/fabrication_report.html` for the archive page.
- `site/` — generated archive output, checked in for the static host.

Fabrication packages are kept in a sibling repository, one directory per
module slug; that directory contains the hardware sources, firmware and
assembly docs for the module.

Front matter is parsed with a plain YAML loader; unknown keys are ignored by
the renderer but must still be valid YAML.
