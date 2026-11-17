---
type: project
title: Example — large-amplitude pendulum
owner: dsjamieson
status: active
members: [dsjamieson]
label: example-pendulum
---

# Example: large-amplitude pendulum

> A worked example of the vault conventions. Delete this project once real ones exist.

## Goal

Find the amplitude dependence of a simple pendulum's period beyond the small-angle limit, and check it numerically.

## Current status

Series derived to fourth order; numerical check agrees to $4\times10^{-6}$ at $\theta_0 = 0.5$.

## Key results

| Result | Status |
|---|---|
| [Period correction to $O(\theta_0^4)$](results/2026-11-17-period-fourth-order.md) | preliminary |
| [Period correction to $O(\theta_0^2)$](results/2026-11-10-period-second-order.md) | superseded |

## Derivations

- [Period as a series in amplitude](derivations/period-series.md)

## Open tasks

Tracked as GitHub Issues with the `example-pendulum` label.
