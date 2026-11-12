---
title: Tide Table
slug: tide-table
revision: r2
format: Eurorack 10HP
license: MIT
summary: A slow quad LFO with tide-like phase drift, four linked outputs and a freeze input.
tags: [modulation, lfo, slow]
fabrication_package_url: https://github.com/frenchbyjen-cmd/tide-table
---

# Tide Table

Tide Table produces four slowly drifting control voltages from a single
master clock.  The outputs are phase-locked at a wide ratio but each one
drifts a little, so patches breathe instead of sweeping in lockstep.

The r2 revision adds a freeze gate and reduces the maximum cycle from twenty
minutes to twelve.  The analog integrator core is unchanged from r1; only the
front panel and the output scaling network differ.

All calibration points are marked on the silkscreen and repeated in
`docs/assembly.md` in the fabrication package.
