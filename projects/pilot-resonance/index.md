---
type: project
title: Pilot — driven damped oscillator resonance
owner: dsjamieson
status: active
members: [dsjamieson]
label: pilot-resonance
---

# Pilot: driven damped oscillator resonance

> The shared toy problem for the [pilot](../../PILOT.md). It will be deleted or archived when the pilot ends.

## Goal

Find the driving frequency $\omega_r$ that maximizes the steady-state amplitude of

$$
\ddot x + 2\gamma\,\dot x + \omega_0^2 x = \frac{F}{m}\cos\omega t ,
$$

analytically and numerically, for $\omega_0 = 1$ and $\gamma = 0.1$, and confirm that the two agree.

## Current status

Analytic derivation drafted; numerical check not yet done.

## Key results

| Result | Status |
|---|---|

## Derivations

- [Driving frequency that maximizes the steady-state amplitude](derivations/resonance-frequency.md) (draft)

## Open tasks

Tracked as GitHub Issues with the `pilot-resonance` label.
