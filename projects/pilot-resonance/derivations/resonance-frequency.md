---
type: derivation
title: Driving frequency that maximizes the steady-state amplitude
owner: dsjamieson
date: 2026-11-17
status: draft
checked_by:
---

# Driving frequency that maximizes the steady-state amplitude

## Setup and assumptions

Driven, damped harmonic oscillator

$$
\ddot x + 2\gamma\,\dot x + \omega_0^2 x = \frac{F}{m}\cos\omega t ,
$$

with $\omega_0, \gamma, F/m > 0$. We look at the steady state, after the transient (which decays as $e^{-\gamma t}$) has died out, and ask which $\omega$ maximizes its amplitude at fixed $F$, $\gamma$, $\omega_0$.

## Derivation

Write the drive as the real part of $(F/m)e^{i\omega t}$ and look for $x(t) = \mathrm{Re}\,[\,\tilde A e^{i\omega t}]$. Substituting,

$$
\left(\omega_0^2 - \omega^2 + 2i\gamma\omega\right)\tilde A = \frac{F}{m}
\quad\Rightarrow\quad
\tilde A = \frac{F/m}{\omega_0^2-\omega^2+2i\gamma\omega}.
$$

The steady-state amplitude is $A(\omega)=|\tilde A|$:

$$
A(\omega) = \frac{F/m}{\sqrt{D(\omega)}}, \qquad
D(\omega) = (\omega_0^2-\omega^2)^2 + 4\gamma^2\omega^2 .
$$

Maximizing $A$ means minimizing $D$. With $u=\omega^2 \ge 0$,

$$
D(u) = (\omega_0^2-u)^2 + 4\gamma^2 u, \qquad
\frac{dD}{du} = -2(\omega_0^2-u) + 4\gamma^2 = 0
\;\Rightarrow\; u^* = \omega_0^2 - 2\gamma^2 .
$$

Since $d^2D/du^2 = 2 > 0$, this is a minimum of $D$. It lies in the allowed range $u\ge 0$ only if $\gamma < \omega_0/\sqrt2$. Otherwise $D$ is increasing for all $u\ge0$ and the amplitude is largest at $\omega = 0$ (no resonance peak).

The peak amplitude follows from $D(u^*) = 4\gamma^2(\omega_0^2-\gamma^2)$.

## Result

$$
\boxed{\omega_r = \sqrt{\omega_0^2 - 2\gamma^2}\quad(\gamma<\omega_0/\sqrt2),\qquad
A_{\max} = \frac{F/m}{2\gamma\sqrt{\omega_0^2-\gamma^2}}}
$$

For the pilot values $\omega_0 = 1$, $\gamma = 0.1$:
$\omega_r = \sqrt{0.98} \approx 0.98995$ and $A_{\max} \approx 5.0252\,F/m$.

## Checks

- **Dimensions:** $\gamma$ and $\omega_0$ both have units of 1/time, so $\omega_r$ does; $A_{\max}$ has units of $(F/m)\,\text{time}^2$, i.e. length. ✓
- **Weak damping** ($\gamma\ll\omega_0$): $\omega_r \approx \omega_0 - \gamma^2/\omega_0$, which tends to $\omega_0$. ✓ Note that $\omega_r$ is lower than the natural frequency $\omega_0$ and also lower than the damped free-oscillation frequency $\sqrt{\omega_0^2-\gamma^2}$.
- **Peak height at $\omega_0$:** $A(\omega_0) = (F/m)/(2\gamma\omega_0)$, slightly below $A_{\max}$, as it must be. ✓
- **Numerical confirmation** against a direct amplitude scan for $\omega_0=1$, $\gamma=0.1$ is still to do; this note stays `draft` until then.
