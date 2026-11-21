# ADR 0001: Reuse the vectorized CF Gauss mark in the banner

## Context

The personal GitHub profile has a banner containing a CF Gauss logo mark. The paths in `assets/banner.svg` match the vectorized mark in `assets/logo-vetor.svg`; the banner applies its own placement and gradient.

## Decision

Keep the banner mark derived from the vectorized source, preserving the original logo silhouette. Record the source relationship here instead of in an SVG comment.

## Consequence

A future brand change must review both the source mark and the banner embedding. The PNG banner used by `README.md` may need to be regenerated separately; changing the SVG alone does not update the visible PNG.
