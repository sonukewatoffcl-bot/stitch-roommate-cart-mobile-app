---
name: Kinetic Utility
colors:
  surface: '#faf9f5'
  surface-dim: '#dadad6'
  surface-bright: '#faf9f5'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f4f4f0'
  surface-container: '#eeeeea'
  surface-container-high: '#e8e8e4'
  surface-container-highest: '#e2e3df'
  on-surface: '#1a1c1a'
  on-surface-variant: '#444748'
  inverse-surface: '#2f312e'
  inverse-on-surface: '#f1f1ed'
  outline: '#747878'
  outline-variant: '#c4c7c7'
  surface-tint: '#5f5e5e'
  primary: '#000000'
  on-primary: '#ffffff'
  primary-container: '#1c1b1b'
  on-primary-container: '#858383'
  inverse-primary: '#c8c6c5'
  secondary: '#006d34'
  on-secondary: '#ffffff'
  secondary-container: '#59fd90'
  on-secondary-container: '#007236'
  tertiary: '#000000'
  on-tertiary: '#ffffff'
  tertiary-container: '#00210b'
  on-tertiary-container: '#009849'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#e5e2e1'
  primary-fixed-dim: '#c8c6c5'
  on-primary-fixed: '#1c1b1b'
  on-primary-fixed-variant: '#474646'
  secondary-fixed: '#62ff95'
  secondary-fixed-dim: '#37e279'
  on-secondary-fixed: '#00210b'
  on-secondary-fixed-variant: '#005225'
  tertiary-fixed: '#71fd98'
  tertiary-fixed-dim: '#52e07f'
  on-tertiary-fixed: '#00210b'
  on-tertiary-fixed-variant: '#005224'
  background: '#faf9f5'
  on-background: '#1a1c1a'
  surface-variant: '#e2e3df'
typography:
  display-currency:
    fontFamily: Barlow Condensed
    fontSize: 44px
    fontWeight: '800'
    lineHeight: 48px
    letterSpacing: -0.02em
  display-currency-mobile:
    fontFamily: Barlow Condensed
    fontSize: 38px
    fontWeight: '800'
    lineHeight: 42px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Barlow Condensed
    fontSize: 32px
    fontWeight: '800'
    lineHeight: 36px
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Barlow Condensed
    fontSize: 24px
    fontWeight: '700'
    lineHeight: 28px
    letterSpacing: 0em
  headline-sm:
    fontFamily: Barlow Condensed
    fontSize: 20px
    fontWeight: '700'
    lineHeight: 24px
    letterSpacing: 0.01em
  title-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '600'
    lineHeight: 22px
    letterSpacing: -0.01em
  body-lg:
    fontFamily: Inter
    fontSize: 15px
    fontWeight: '500'
    lineHeight: 22px
  body-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 20px
  body-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '400'
    lineHeight: 16px
  eyebrow:
    fontFamily: Inter
    fontSize: 11px
    fontWeight: '700'
    lineHeight: 14px
    letterSpacing: 0.12em
  label-action:
    fontFamily: Barlow Condensed
    fontSize: 18px
    fontWeight: '700'
    lineHeight: 22px
    letterSpacing: 0.05em
  label-tag:
    fontFamily: Barlow Condensed
    fontSize: 13px
    fontWeight: '700'
    lineHeight: 16px
    letterSpacing: 0.08em
rounded:
  sm: 0.5rem
  DEFAULT: 1rem
  md: 1.5rem
  lg: 2rem
  xl: 3rem
  full: 9999px
spacing:
  gutter: 1rem
  gutter-mobile: 0.75rem
  margin: 1rem
  margin-mobile: 1rem
  space-xs: 0.25rem
  space-sm: 0.5rem
  space-md: 1rem
  space-lg: 1.5rem
  space-xl: 2rem
---

## Brand & Style

This design system is engineered for the high-velocity, shared-living dynamics of student flats across metropolitan India. It channels a **brutalist warm utility wireframe** aesthetic: raw, high-contrast, structural, and strictly functional, softened through warm organic paper tones. The experience eliminates the friction and social awkwardness of tracking shared grocery hauls and chasing peer debts by projecting financial clarity, rapid settlement, and indisputable legibility.

### Emotional Signature
- **Direct & Uncompromising:** Dense, ultra-readable numeric hierarchies prioritizing rupee balances, splitting splits without ambiguity.
- **Warm Industrial:** Physical inventory ledger cues paired with the speed of Indian fintech rails (UPI).
- **Tactile Decisiveness:** Stark contrasts between stark near-black structural anchors and punchy signal greens instill confidence during settlement flows.

## Colors

The palette leverages a high-contrast balance between an organic off-white substrate and dense near-black foundational structures, energized by a hyper-visible signal green.

### Palette Architecture
- **Primary Canvas (`#F8F8F4`):** Warm off-white recalling newsprint and receipt slips, setting an unpretentious utility ground.
- **Structural Black (`#121212`):** Grounded near-black applied to high-impact primary buttons, dominant typography, and crisp edge anchors.
- **Signal Green (`#22D66F`):** Functional accent indicating instant UPI settlements, positive balances, complete actions, and full funding checkpoints.
- **Deep Signal Green (`#18B85C`):** High-contrast interactive press states and critical inline text links requiring WCAG AAA adherence.
- **Muted Warm Fill (`#D9D8D2`):** Structural neutral for unfilled meters, placeholder states, disabled controls, and secondary avatar markers.
- **Hairline Dividers (`#E6E4DC` on light, `#2A2A2A` on dark):** Crisp structural boundaries isolating split tallies without visual bulk.
- **Surface Elevation Cards (`#FFFFFF` in light mode, `#1E1E1E` in dark mode):** Elevated containers floating cleanly atop the foundational canvas.

## Typography

The typographic balance pairs an authoritative, tight-tracking industrial display face (**Barlow Condensed**) with a rational, highly legible sans-serif (**Inter**). 

### Hierarchy Guidelines
- **Financial Metric Dominance:** All Indian Rupee (₹) amounts, totals, ledger splits, and roommate balance delta values render strictly via `Barlow Condensed` in weights `700` through `800`.
- **Eyebrow Meta-Tracking:** System path indicators, apartment codes, and sequence counters (e.g., `STEP 02 · FLAT 402`) must be set in uppercase `eyebrow` styling using `Inter` with expanded tracking (`0.12em`).
- **Body & Labels:** Functional UI parameters, line-item descriptions, and system notifications rely on `Inter` (`400` and `500`) to guarantee legibility at small viewing scales.

## Layout & Spacing

This layout is strictly calibrated around a fixed **390x844px** mobile viewport with dynamic safe-area insets. 

### Spacing Principles
- **Grid Structure:** Fluid 4-column layout bounded by a consistent `16px` (`1rem`) canvas gutter and edge margin.
- **Vertical Rhythm:** Strict incremental steps of `4px` (`space-xs`), `8px` (`space-sm`), `16px` (`space-md`), `24px` (`space-lg`), and `32px` (`space-xl`).
- **Tactile Padding:** Interactive targets maintain an absolute minimum touch zone of `48x48px`. Full-width actions occupy the base sticky dock zone with an internal vertical pad of `14px` (`py-3.5`) to `16px` (`py-4`).

## Elevation & Depth

This system avoids decorative atmospheric blurs, soft skeuomorphic gradients, and deep drop shadows in favor of a **flat, tactile wireframe architecture**.

### Visual Separation Rules
- **Physical Surfaces:** Contrast is created entirely through solid color fills and structural hairline outlines (`1px solid #E6E4DC`).
- **Zero-Shadow Philosophy:** No drop shadows or ambient blurs are permitted on default cards, sheets, or buttons. All surfaces sit flush on the canvas like physical index cards.
- **Modal Depth:** Bottom settlement sheets and UPI payment drawer layers utilize a flat, solid `1px` top perimeter rule accompanied by a semi-opaque `#121212` backdrop mask (40% opacity) without ambient diffusion.

## Shapes

The design incorporates a geometric duality: radical full-pill silhouettes applied to interactive controls contrasted against hyper-curved, planar structural cards.

### Shape Scale Rules
- **Interactive Elements (`rounded-full` / 9999px):** Primary triggers, action chips, avatar circles, and settlement tags always feature pill geometries.
- **Card Enclosures (`rounded-2xl` / 1.5rem to `rounded-3xl` / 2rem):** Substantial corner radiuses that frame collective lists, item tallies, and bill cards.
- **Input Fields (`rounded-xl` / 1rem):** Slightly more restrained corners for numeric and text data fields to maximize interior hit area.

## Components

### Buttons
- **Primary UPI Action:** Full-width pill (`rounded-full`), padded `py-4`, filled with `#121212` with text rendered in `label-action` using `#FFFFFF`. In terminal confirmation steps, switch background to `#22D66F` with `#121212` text.
- **Secondary Split Action:** Full-width pill, `1px solid #121212`, transparent fill, with `#121212` uppercase display typography.

### Pill Status Tags
- **Paid / Joined:** Background `#22D66F`, text `#121212`, zero border, `py-1`, `px-3`, uppercase `label-tag`.
- **Pending / Waiting:** Transparent background, `1px solid #121212`, text `#121212`, `py-1`, `px-3`, uppercase `label-tag`.
- **Short / Deficit:** Background `#121212`, text `#FFFFFF`, zero border, `py-1`, `px-3`, uppercase `label-tag`.

### Roommate Circle Avatars
Circular tokens (`36x36px` or `44x44px`), display initials centered in `headline-sm`:
- **Identity A:** `#121212` background, `#FFFFFF` text.
- **Identity M:** `#22D66F` background, `#121212` text.
- **Identity K:** `#D9D8D2` background, `#121212` text.
- **Identity Z:** `#FFFFFF` background, `#121212` text, bounded by a `1px solid #121212` perimeter.

### Cards & Cart Line Items
- **Cart Containers:** Surfaces use `#FFFFFF` (light mode) wrapped in a `1px solid #E6E4DC` hairline, corner radius set to `rounded-2xl` (`1.5rem`).
- **Line Items:** Grocery rows feature horizontal divider rules, item quantities formatted in `Inter` (`body-md`), with rupee prices right-aligned in `Barlow Condensed` (`headline-sm`).
- **Progress Split Trackers:** Solid `#D9D8D2` tracking troughs filled proportionally with `#22D66F` segments representing settled room shares.

### Inputs & Financial Keypads
- **Rupee Entry:** Clean surface container with `#F8F8F4` or `#FFFFFF`, a prominent `₹` prefix anchored in `headline-lg`, accompanied by a minimal underline or a hairline boundary.
- **Top Bar:** Top-left 24px navigation chevron, aligned with tracked eyebrow text specifying group status (e.g., `FLAT 402 CART`).