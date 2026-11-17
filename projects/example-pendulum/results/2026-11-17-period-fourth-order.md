---
type: result
title: Period correction to O(θ0⁴), checked numerically
owner: dsjamieson
date: 2026-11-17
status: preliminary
code: n/a
data: n/a
supersedes: 2026-11-10-period-second-order.md
superseded_by:
---

# Period correction to $O(\theta_0^4)$, checked numerically

## Result

$$
T/T_0 = 1 + \frac{\theta_0^2}{16} + \frac{11\,\theta_0^4}{3072}
$$

At $\theta_0 = 0.5$: series gives $1.015\,849$; exact $\tfrac{2}{\pi}K(\sin 0.25) = 1.015\,853$. Relative error $3.7\times10^{-6}$, consistent with the omitted $O(\theta_0^6)$ term.

## How it was obtained

- **Code / data:** n/a. This example uses a one-line check: $\tfrac{2}{\pi}K(k) = 1/\mathrm{AGM}(1, \sqrt{1-k^2})$ with $k = \sin 0.25$. In a real result, cite `repo@commit` and the data path here.

## Checks

Replaces the [second-order result](2026-11-10-period-second-order.md); the error at $\theta_0 = 0.5$ drops from $2.2\times10^{-4}$ to $3.7\times10^{-6}$.

## Related

- Derivation: [Period as a series in amplitude](../derivations/period-series.md)
