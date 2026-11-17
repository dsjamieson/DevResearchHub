---
type: derivation
title: Pendulum period as a series in amplitude
owner: dsjamieson
date: 2026-11-17
status: draft
checked_by:
---

# Pendulum period as a series in amplitude

## Setup and assumptions

Point mass, massless rod of length $L$, no friction, release from rest at angle $\theta_0$. Let $\omega_0 = \sqrt{g/L}$ and $k = \sin(\theta_0/2)$.

## Derivation

Energy conservation gives $\dot\theta^2 = 2\omega_0^2(\cos\theta - \cos\theta_0)$, so

$$
T = \frac{4}{\omega_0}\int_0^{\pi/2}\frac{d\phi}{\sqrt{1-k^2\sin^2\phi}} = \frac{4}{\omega_0}K(k),
$$

using the substitution $\sin(\theta/2) = k\sin\phi$. Expanding the complete elliptic integral,

$$
K(k) = \frac{\pi}{2}\left[1 + \frac{k^2}{4} + \frac{9k^4}{64} + O(k^6)\right],
$$

and $k^2 = \theta_0^2/4 - \theta_0^4/48 + O(\theta_0^6)$.

## Result

$$
\boxed{T = T_0\left[1 + \frac{\theta_0^2}{16} + \frac{11\,\theta_0^4}{3072} + O(\theta_0^6)\right]}, \qquad T_0 = \frac{2\pi}{\omega_0}
$$

## Checks

- $\theta_0 \to 0$ recovers $T_0$.
- Matches the standard result (e.g. Landau & Lifshitz, *Mechanics*, §11 problem).
