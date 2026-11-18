# 🛒 Roommate Cart (Kinetic Utility)
> **One cart, many payments, one delivery. No chasing, fair by default.**

A complete, 38-screen interactive mobile web application designed for Indian college hostel roommates and flatmates pooling quick-commerce grocery hauls (Blinkit, Zepto, Instamart) with automated UPI split settlements.

Built strictly according to the **Kinetic Utility** brutalist design system (`#FAF9F5` warm paper, `#121212` ink, `#22D66F` electric mint accent, Barlow Condensed + Inter typography).

---

## 📱 Live Demo & Setup

### Run Locally:
```bash
# Clone the repository
git clone https://github.com/sonukewatoffcl-bot/stitch-roommate-cart-mobile-app.git
cd stitch-roommate-cart-mobile-app

# Start local server (no dependencies needed!)
python3 -m http.server 8080
```
Open **[http://localhost:8080](http://localhost:8080)** in Safari, Chrome, or any mobile browser.

---

## ⚡ Core Features & Interactivity

- **iPhone 16 Pro Frame & Responsive Mode:** Toggle seamlessly between an authentic phone mockup and full responsive viewport (press `M`).
- **Tactile Audio & Haptic Feedback Engine:** Web Audio API sound synthesis simulating physical button clicks, payment chimes, and WhatsApp nudges (press `S` to toggle sound).
- **Interactive 6-Digit OTP Verification:** Dynamic input boxes with auto-advance, backspace navigation, resend countdown timer (`0:28`), and loading validation.
- **Store Catalog & Cart Steppers:** Instant category filtering (`Dairy`, `Snacks`, `Beverages`), `+ ADD` buttons morphing into live quantity steppers `[-] 1 [+]`, and floating bottom cart tally updating in real time.
- **Live Price-Lock Countdown:** Real-time ticking cart lock timer (`14:59`...) ensuring synchronized dark store orders.
- **Prorated Share Editor:** 4 real interactive range sliders dynamically calculating percentage and exact Rupee shares live for all flatmates out of ₹1,240.
- **Simulated NPCI / UPI Handoff:** Authentic GPay / PhonePe animated transit screen auto-completing payment after 2.5s to generate receipt with copyable UPI Reference ID.
- **Deficit Resolution Engine:** Dedicated workflows when a roommate is short on balance:
  1. **Spot Me:** Formal peer loan with payback dates logged to Flat Ledger.
  2. **Room Pool:** Flat petty cash reserve steppers updating an interactive circular SVG progress ring.
  3. **Pay or Drop:** Drop non-paying items and recalculate the basket.
- **Delivery Verification Checklist:** Tap delivery items to toggle strike-throughs and update the live counter (`5/5 VERIFIED ✓`).
- **Flat Expense Ledger:** Consolidated debt ledger with instant WhatsApp reminder pings, UPI settlement handoff, and downloadable expense reports.

---

## 🗺️ Complete 38-Screen Architecture

### Phase 1: Onboarding & Flat Setup (Screens 01–06)
- **01_splash_value:** Hero value proposition with tapable roommate avatars (Aarav, Maya, Kabir, Zoya) displaying live roles.
- **02_phone_otp:** Indian mobile number auth with 6 interactive OTP input boxes, timer, and demo paste.
- **03_profile_setup:** Real-time name input updating avatar initials (`A`) and 4 color theme pickers.
- **04_campus_hostel:** IIT Bombay campus and hostel selector cards with radio checks.
- **05_create_or_join_flat:** Toggle cards between "Join Flat 402" and "Create New Flat".
- **06_link_upi_notifications:** UPI app selector (GPay, PhonePe, Paytm, CRED) and auto-detect permissions switch.

### Phase 2: Flat Hub & Dashboard (Screens 07–10)
- **07_home_open_carts:** Active Sunday haul dashboard; tapping card opens live cart; bottom navigation dock.
- **08_home_empty_state:** Empty state haul launcher with quick re-order buttons.
- **09_flat_members_settings:** Roommate directory, toggleable slide-up QR drawer, and invite link copy.
- **10_activity_notifications:** Tab-filtered notification feed (`ALL`, `UNREAD`, `PAYMENTS`) with WhatsApp nudge shortcuts.

### Phase 3: Shopping & Shared Cart (Screens 11–18)
- **11_new_cart:** Store selector (Blinkit, Zepto, Instamart), timer chips (15m, 30m, 1h), and cart name clear button.
- **12_invite_roommates:** WhatsApp broadcast button, QR code modal, and copy cart link with checkmark feedback.
- **13_store_browse:** Category pills, live `+ ADD` quantity steppers, and floating bottom cart bar.
- **14_search_results:** Real-time search filter and cart tally synchronization.
- **15_item_detail_sheet:** Product modal with steppers multiplying base unit price (`₹520`), and per-person split calculator.
- **16_cart:** Live price-lock timer, steppers, item deletion recalculating subtotal and taxes, and checkout trigger.
- **17_ownership_mode:** Split mode selector (Equal Split, Itemized, Custom Prorated).
- **18_prorated_share_editor:** 4 interactive sliders calculating roommate percentages and rupee balances live.

### Phase 4: Checkout & UPI Split (Screens 19–24)
- **19_checkout_summary:** Delivery slot selection (`Instant`, `Evening`, `Tomorrow`) and transparent cost breakdown.
- **20_your_share:** Personal payment screen (`₹342 Due`), timer countdown, and UPI app trigger.
- **21_upi_handoff:** Dark transition sheet simulating NPCI payment gateway with 2.5s auto-completion.
- **22_payment_success:** Payment confirmation receipt with copyable UPI Reference ID and roommate statuses.
- **23_payment_failed:** Bank timeout recovery flow with retry and "Spot Me" shortcuts.
- **24_timer_expired:** Expired lock state with timer extension and haul revival options.

### Phase 5: Roommate Dynamics & Edge Cases (Screens 25–32)
- **25_payment_status:** Live status dashboard (`2 of 4 Paid`), "Nudge Kabir" pulse, and Zoya deficit alert card.
- **26_zoya_is_short:** Crisis resolution selector (`Spot`, `Pool`, `Drop`) updating the dynamic CTA button.
- **27_spot_me_approval:** Formal peer loan setup with payback term chips and auto-deduction toggle.
- **28_room_pool:** Contribution steppers adjusting flat petty cash draw and SVG circular progress ring.
- **29_pay_or_drop:** Drop items confirmation with strikethrough basket recalculation.
- **30_substitute_voting:** Urgent out-of-stock substitution voting cards with live roommate vote counts.
- **31_price_changed_alert:** Dark store surge pricing approval with item drop option.
- **32_cart_expired_revive:** One-tap cart revival refreshing inventory without losing items.

### Phase 6: Fulfillment, Ledger & Logistics (Screens 33–38)
- **33_order_tracking:** Live delivery partner tracker (Hero Splendor EV), progress stepper, and gate delivery call.
- **34_delivered_confirm:** Unboxing verification checklist with strikethroughs and counter updates (`5/5 VERIFIED ✓`).
- **35_report_an_issue:** Damaged/missing item report selector, reason pills, photo upload simulation, and ledger credit.
- **36_order_history:** Past orders archive with filter pills (`ALL`, `THIS MONTH`, `MY ITEMS`).
- **37_flat_ledger:** Consolidated debt balances, WhatsApp nudge button, instant UPI settlement, and statement export.
- **38_floor_batch:** Neighbor flat haul batching (Flat 401 & 403) to pool and save the ₹60 delivery fee.

---

## 🎨 Design System Tokens

| Token | Hex / Value | Usage |
|---|---|---|
| **Background / Canvas** | `#FAF9F5` | Warm off-white paper finish |
| **Ink / Surface** | `#121212` | High-contrast brutalist text & headers |
| **Accent / Action** | `#22D66F` | Electric mint green for buttons & highlights |
| **Subtle Card** | `#F2EFE9` | Surface container elements |
| **Eyebrow Font** | `Barlow Condensed` | Uppercase, bold, tracking-wide labels |
| **Body Font** | `Inter` | Clean, readable UI numbers and descriptions |

---

## 🛠️ Project Structure

```
├── index.html                   # Master single-page app (all 38 screens in one reactive engine)
├── DESIGN.md                    # Kinetic Utility design tokens and wireframe rules
├── README.md                    # Project documentation
├── generate_master_suite.py     # Python builder script
├── live_runtime_template.html   # Master HTML shell & reactive state engine
├── update_template_and_build.py # Automated compilation pipeline
└── screens/                     # Source assets and code for all 38 original screens
    ├── 01_splash_value/
    ├── 02_phone_otp/
    ├── ...
    └── 38_floor_batch/
```

---

## 📄 License
MIT © 2026 Sonu Kewat
