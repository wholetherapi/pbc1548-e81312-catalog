# Ferrous Bloom assembly notes

## Order of operations

1. Fit the resonator bank and the driver buffer before the front panel.
2. Calibrate the damping network at the four test points with a 1 kHz sine.
3. Only connect the front panel after the driver rails are verified.

## Calibration

- TP1: driver A idle offset, 2.5 V ± 0.1 V.
- TP2: driver B idle offset, 2.5 V ± 0.1 V.
- TP3: damping control reference, 1.0 V.
- TP4: output bias, 0.0 V.

## QA checklist

- Six resonators sweep cleanly with no rattle at maximum excitation.
- Damping control covers the full range without zipper noise.
- Panel fits the 12HP frame without binding on the rails.

Reference build photos live in the workshop binder; ask a coordinator before
ordering a run.
