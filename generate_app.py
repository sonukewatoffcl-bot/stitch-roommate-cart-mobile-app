#!/usr/bin/env python3
"""
Roommate Cart - Mobile Web Application Generator
Combines all 38 screens into an interactive, high-fidelity mobile application
with native iPhone frame preview, screen switcher, scenario inspector,
and hyperlinked navigation across all flows.
"""

import os
import re
import json

# Paths to the stitch batches
FOLDERS = [
    '/Users/sonukewat/Downloads/stitch_roommate_cart_mobile_app',
    '/Users/sonukewat/Downloads/stitch_roommate_cart_mobile_app 2',
    '/Users/sonukewat/Downloads/stitch_roommate_cart_mobile_app 4',
    '/Users/sonukewat/Downloads/stitch_roommate_cart_mobile_app 5',
    '/Users/sonukewat/Downloads/stitch_roommate_cart_mobile_app 6',
    '/Users/sonukewat/Downloads/stitch_roommate_cart_mobile_app 7'
]

OUTPUT_PATH_1 = '/Users/sonukewat/Downloads/stitch_roommate_cart_mobile_app/kinetic_utility/index.html'
OUTPUT_PATH_2 = '/Users/sonukewat/Downloads/stitch_roommate_cart_mobile_app/index.html'

SCREEN_METADATA = {
    1: {
        "title": "Splash & Value Proposition",
        "phase": "1. Onboarding & Setup",
        "tag": "WELCOME",
        "description": "Introduction to Roommate Cart wireframe: 'One cart, many payments, one delivery'. Features value props (No Chasing, Fair by Default) and live order split topology diagram.",
        "instructions": "Tap 'Get Started' to begin phone onboarding, or use the bottom navigator to explore any screen.",
        "default_next": 2,
        "default_prev": 1,
        "nav_tab": None
    },
    2: {
        "title": "Phone & OTP Verification",
        "phase": "1. Onboarding & Setup",
        "tag": "AUTH",
        "description": "Enter Indian mobile number (+91 98765 43210) and verify via 6-digit SMS OTP with auto-resend countdown.",
        "instructions": "Tap 'VERIFY' to authenticate and proceed to Roommate profile setup.",
        "default_next": 3,
        "default_prev": 1,
        "nav_tab": None
    },
    3: {
        "title": "Roommate Profile Setup",
        "phase": "1. Onboarding & Setup",
        "tag": "IDENTITY",
        "description": "Name configuration and Roommate Token selection (Aarav, Maya, Kabir, Zoya) with signature brutalist warm utility colors.",
        "instructions": "Select an avatar token and tap 'CONTINUE' to select your campus or hostel.",
        "default_next": 4,
        "default_prev": 2,
        "nav_tab": None
    },
    4: {
        "title": "Campus & Hostel Locator",
        "phase": "1. Onboarding & Setup",
        "tag": "LOCATION",
        "description": "Select university or student residence (e.g., IIT Bombay, Hostel 14 / Powai Flats). Supports instant search and chip selection.",
        "instructions": "Tap your hostel chip or tap 'CONTINUE' to create or join your flat.",
        "default_next": 5,
        "default_prev": 3,
        "nav_tab": None
    },
    5: {
        "title": "Create or Join Flat",
        "phase": "1. Onboarding & Setup",
        "tag": "FLAT SETUP",
        "description": "Create 'Flat 402' or join using 6-character invite code or flat QR code.",
        "instructions": "Tap 'CREATE FLAT' or 'JOIN FLAT' to link your UPI payment app.",
        "default_next": 6,
        "default_prev": 4,
        "nav_tab": None
    },
    6: {
        "title": "Link UPI & Permissions",
        "phase": "1. Onboarding & Setup",
        "tag": "PAYMENT SETUP",
        "description": "Select preferred UPI payment app (Google Pay, PhonePe, Paytm, CRED) for zero-click instant settlement requests and push notifications.",
        "instructions": "Select an app (e.g. GPay) and tap 'CONFIRM & GO TO FLAT' to enter the home dashboard.",
        "default_next": 7,
        "default_prev": 5,
        "nav_tab": None
    },
    7: {
        "title": "Home (Active Open Carts)",
        "phase": "2. Flat Hub & Dashboard",
        "tag": "CORE HUB",
        "description": "Flat 402 Home screen: View active open grocery carts ('Sunday Restock', 4m left), member status chips (Aarav, Maya, Kabir, Zoya), and quick actions.",
        "instructions": "Tap '+ NEW CART' to start a new grocery run (Screen 11), tap the open cart to view items (Screen 16), or switch tabs below.",
        "default_next": 16,
        "default_prev": 6,
        "nav_tab": "carts"
    },
    8: {
        "title": "Home (Empty State)",
        "phase": "2. Flat Hub & Dashboard",
        "tag": "EMPTY STATE",
        "description": "Home screen state when no roommate has initiated an active cart. Shows quick start templates and past haul history prompt.",
        "instructions": "Tap '+ NEW CART' or 'QUICK START' to initiate a new cart.",
        "default_next": 11,
        "default_prev": 7,
        "nav_tab": "carts"
    },
    9: {
        "title": "Flat Members & Settings",
        "phase": "2. Flat Hub & Dashboard",
        "tag": "FLAT SETTINGS",
        "description": "Flat 402 configuration: Roommates directory, UPI routing rules, auto-settlement caps, and flat invite links.",
        "instructions": "Review flatmates, manage permissions, or use bottom navigation to switch between tabs.",
        "default_next": 12,
        "default_prev": 7,
        "nav_tab": "flat"
    },
    10: {
        "title": "Activity & Notifications Feed",
        "phase": "2. Flat Hub & Dashboard",
        "tag": "NOTIFICATIONS",
        "description": "Real-time stream of flat activity: cart creation alerts, item addition pings, payment settlement confirmations, and debt nudges.",
        "instructions": "Filter by 'All', 'Unread', or 'Payments'. Tap any notification to view details.",
        "default_next": 7,
        "default_prev": 7,
        "nav_tab": None
    },
    11: {
        "title": "Start New Shared Cart",
        "phase": "3. Shopping & Shared Cart",
        "tag": "CREATE CART",
        "description": "Configure haul: Name cart ('Sunday Restock'), select quick commerce store (Blinkit, Zepto, Instamart), and set automatic lock timer (15m, 30m, 1h).",
        "instructions": "Tap store options, set timer, and tap 'CREATE CART' to invite roommates.",
        "default_next": 12,
        "default_prev": 7,
        "nav_tab": "carts"
    },
    12: {
        "title": "Invite Roommates to Cart",
        "phase": "3. Shopping & Shared Cart",
        "tag": "INVITE",
        "description": "Broadcast cart join link via WhatsApp group, copy direct link, or scan flat QR code.",
        "instructions": "Tap 'COPY LINK' (tests micro-interaction) or tap 'START SHOPPING' to browse grocery items.",
        "default_next": 13,
        "default_prev": 11,
        "nav_tab": "carts"
    },
    13: {
        "title": "Store Catalog & Browse",
        "phase": "3. Shopping & Shared Cart",
        "tag": "BROWSE",
        "description": "Browse items across categories: Staples, Dairy, Snacks, Produce. High-contrast typography and instant '+ ADD' chips.",
        "instructions": "Tap any product card to open the item detail sheet (Screen 15), tap search bar (Screen 14), or tap bottom cart pill (Screen 16).",
        "default_next": 15,
        "default_prev": 12,
        "nav_tab": "carts"
    },
    14: {
        "title": "Search Grocery Items",
        "phase": "3. Shopping & Shared Cart",
        "tag": "SEARCH",
        "description": "Real-time search results for 'Basmati Rice' and popular flat essentials with one-tap add buttons.",
        "instructions": "Tap '+ ADD' or tap a search result to configure item quantity and ownership.",
        "default_next": 15,
        "default_prev": 13,
        "nav_tab": "carts"
    },
    15: {
        "title": "Item Detail & Ownership Sheet",
        "phase": "3. Shopping & Shared Cart",
        "tag": "ITEM MODAL",
        "description": "Detailed product sheet for Basmati Rice 5kg (₹540). Set quantity (+/-) and ownership (Shared Flat vs Personal Only).",
        "instructions": "Adjust quantity with stepper and tap 'ADD TO CART' to add item to the collective haul.",
        "default_next": 16,
        "default_prev": 13,
        "nav_tab": "carts"
    },
    16: {
        "title": "Shared Cart View",
        "phase": "3. Shopping & Shared Cart",
        "tag": "LIVE CART",
        "description": "Central shared haul: Live countdown timer (04:12), items grouped by roommates (Aarav, Maya, Kabir), split tags, and locked status.",
        "instructions": "Tap '+ ADD AN ITEM' (Screen 13) or tap 'LOCK CART (2/4 READY)' to proceed to ownership mode (Screen 17).",
        "default_next": 17,
        "default_prev": 13,
        "nav_tab": "carts"
    },
    17: {
        "title": "Ownership Split Mode",
        "phase": "3. Shopping & Shared Cart",
        "tag": "SPLIT RULES",
        "description": "Select how items are split: 'Equal Split' (all 4 split equally), 'Personal Only' (pay for what you consume), or 'Prorated / Custom Share'.",
        "instructions": "Choose a mode and tap 'CONFIRM' to adjust percentages or proceed to checkout summary.",
        "default_next": 18,
        "default_prev": 16,
        "nav_tab": "carts"
    },
    18: {
        "title": "Prorated Share Editor",
        "phase": "3. Shopping & Shared Cart",
        "tag": "SLIDERS",
        "description": "Interactive sliders to adjust individual roommate share ratios (Aarav 40%, Maya 30%, Kabir 30%) with live rupee balance re-tallying.",
        "instructions": "Drag sliders to test micro-interactions, then tap 'CONFIRM SHARES' to view the checkout summary.",
        "default_next": 19,
        "default_prev": 17,
        "nav_tab": "carts"
    },
    19: {
        "title": "Checkout Summary & Split Breakdown",
        "phase": "4. Checkout & UPI Split",
        "tag": "CHECKOUT",
        "description": "Comprehensive haul breakdown: items subtotal (₹1,308), delivery fee (₹60 split as ₹15/each), taxes, and final individual rupee commitments.",
        "instructions": "Review split tallies and tap 'PROCEED TO PAY' to view your individual payment share.",
        "default_next": 20,
        "default_prev": 16,
        "nav_tab": "carts"
    },
    20: {
        "title": "Your Share (₹342 Due)",
        "phase": "4. Checkout & UPI Split",
        "tag": "YOUR SHARE",
        "description": "Personal settlement screen: 'Your Share: ₹342' with instant UPI payment triggers (Google Pay, PhonePe) and lock timer badge.",
        "instructions": "Tap 'GPAY INSTANT' or 'PHONEPE' to trigger the UPI handoff animation.",
        "default_next": 21,
        "default_prev": 19,
        "nav_tab": "carts"
    },
    21: {
        "title": "UPI Handoff Transition Sheet",
        "phase": "4. Checkout & UPI Split",
        "tag": "UPI HANDOFF",
        "description": "Dynamic dark sheet simulating UPI handoff to Google Pay on NPCI rails. Includes progress bar animation and security verification.",
        "instructions": "Sheet automatically simulates payment completion and transitions to Payment Success (Screen 22) or tap anywhere.",
        "default_next": 22,
        "default_prev": 20,
        "nav_tab": "carts"
    },
    22: {
        "title": "Payment Success Receipt",
        "phase": "4. Checkout & UPI Split",
        "tag": "PAID SUCCESS",
        "description": "Settlement confirmation: 'PAID · ₹342 confirmed.' UPI transaction ID with copy action, and live roommate funding status tags.",
        "instructions": "Tap 'VIEW PAYMENT STATUS' (Screen 25) to check on remaining roommates, or tap 'Spot Her' (Screen 26).",
        "default_next": 25,
        "default_prev": 20,
        "nav_tab": "carts"
    },
    23: {
        "title": "Payment Failed State",
        "phase": "4. Checkout & UPI Split",
        "tag": "PAYMENT FAILED",
        "description": "UPI failure handling: 'DIDN'T GO THROUGH · Bank server timeout or insufficient UPI balance.'",
        "instructions": "Tap 'TRY AGAIN' to re-trigger UPI handoff (Screen 21) or tap 'ASK A ROOMMATE TO SPOT ME' (Screen 27).",
        "default_next": 21,
        "default_prev": 20,
        "nav_tab": "carts"
    },
    24: {
        "title": "Cart Timer Expired",
        "phase": "4. Checkout & UPI Split",
        "tag": "TIMER EXPIRED",
        "description": "Cart lock countdown reached 00:00 before all roommates completed their UPI payments. Outlines recovery credit options.",
        "instructions": "Tap 'EXTEND TIMER' or 'CREDIT OPTION' to resolve the deadlock.",
        "default_next": 25,
        "default_prev": 20,
        "nav_tab": "carts"
    },
    25: {
        "title": "Roommate Payment Status (2 of 4 Paid)",
        "phase": "5. Roommate Dynamics & Edge Cases",
        "tag": "STATUS BOARD",
        "description": "Live status dashboard: Aarav (Paid ₹342), Maya (Paid ₹342), Kabir (Pending), Zoya (Short by ₹120). Includes 'NUDGE UNPAID' action.",
        "instructions": "Tap 'NUDGE UNPAID' for micro-interaction, or tap the Zoya warning banner to enter the spot-me resolution flow (Screen 26).",
        "default_next": 26,
        "default_prev": 22,
        "nav_tab": "carts"
    },
    26: {
        "title": "Zoya Is Short (Deficit Alert)",
        "phase": "5. Roommate Dynamics & Edge Cases",
        "tag": "DEFICIT CRISIS",
        "description": "Roommate shortfall alert: Zoya's bank balance is short by ₹120. Choose resolution: Spot her, Use flat room pool, or Drop her items.",
        "instructions": "Tap 'CONFIRM SPOT ME' (Screen 27), 'USE ROOM POOL' (Screen 28), or 'DROP ZOYA'S ITEMS' (Screen 29).",
        "default_next": 27,
        "default_prev": 25,
        "nav_tab": "carts"
    },
    27: {
        "title": "Spot-Me Approval & Payback Terms",
        "phase": "5. Roommate Dynamics & Edge Cases",
        "tag": "SPOT ME",
        "description": "Formalize peer credit: 'Zoya asked you to spot her ₹120.' Select payback terms (1st of Month vs Next Friday) with auto-ledger logging.",
        "instructions": "Select payback term and tap 'APPROVE SPOT ME' to finalize and return to paid status.",
        "default_next": 22,
        "default_prev": 26,
        "nav_tab": "carts"
    },
    28: {
        "title": "Flat Room Pool (Cover Difference)",
        "phase": "5. Roommate Dynamics & Edge Cases",
        "tag": "ROOM POOL",
        "description": "Use flat petty cash reserves (Balance: ₹450) to cover the ₹120 shortfall with interactive +/- allocation steppers.",
        "instructions": "Adjust pool contribution and tap 'USE POOL FUNDS' to complete order funding.",
        "default_next": 22,
        "default_prev": 26,
        "nav_tab": "carts"
    },
    29: {
        "title": "Pay or Drop Items Ultimatum",
        "phase": "5. Roommate Dynamics & Edge Cases",
        "tag": "DROP ITEMS",
        "description": "Fairness safeguard: Automatically drop non-paying roommate's personal items so the rest of the flat's essential groceries dispatch immediately.",
        "instructions": "Tap 'CONFIRM DROP & DISPATCH' to advance directly to live order tracking (Screen 33).",
        "default_next": 33,
        "default_prev": 26,
        "nav_tab": "carts"
    },
    30: {
        "title": "Substitute Item Voting (Out of Stock)",
        "phase": "5. Roommate Dynamics & Edge Cases",
        "tag": "OUT OF STOCK",
        "description": "Dark store stock alert: 'Farm Eggs 30pk out of stock.' Flatmates cast fast majority vote on suggested replacement (Organic Eggs 24pk).",
        "instructions": "Tap substitute choice to vote and update cart total.",
        "default_next": 19,
        "default_prev": 16,
        "nav_tab": "carts"
    },
    31: {
        "title": "Surge Price Changed Alert",
        "phase": "5. Roommate Dynamics & Edge Cases",
        "tag": "PRICE ALERT",
        "description": "Quick commerce surge alert: 'Tomatoes moved from ₹38 to ₹62 due to peak demand.' Option to accept split delta or drop item.",
        "instructions": "Tap 'ACCEPT SURGE' to proceed to checkout summary (Screen 19) or drop item.",
        "default_next": 19,
        "default_prev": 19,
        "nav_tab": "carts"
    },
    32: {
        "title": "Cart Expired Revive",
        "phase": "5. Roommate Dynamics & Edge Cases",
        "tag": "REVIVE CART",
        "description": "Revive an expired or abandoned cart haul with a single tap, refreshing dark store pricing and recreating member shares.",
        "instructions": "Tap 'REVIVE THIS CART' to restore the cart and reopen the shared haul (Screen 16).",
        "default_next": 16,
        "default_prev": 24,
        "nav_tab": "carts"
    },
    33: {
        "title": "Live Order Tracking & ETA",
        "phase": "6. Fulfillment, Ledger & Batching",
        "tag": "TRACKING",
        "description": "Live fulfillment tracker: Dark store packing -> Rider picked up on EV -> Arriving at Campus Gate 2 (ETA 8 mins).",
        "instructions": "Tap 'COLLECT AT GATE 2' or swipe up to confirm delivery when rider arrives (Screen 34).",
        "default_next": 34,
        "default_prev": 7,
        "nav_tab": "orders"
    },
    34: {
        "title": "Delivered & Unbox Confirmation",
        "phase": "6. Fulfillment, Ledger & Batching",
        "tag": "DELIVERED",
        "description": "Delivery confirmation: Haul dropped at Flat 402 doorstep. Unbox checklist to verify items and upload proof photo.",
        "instructions": "Check items, tap 'EVERYTHING'S HERE' to view order history (Screen 36), or tap 'SOMETHING'S MISSING' to file a report (Screen 35).",
        "default_next": 36,
        "default_prev": 33,
        "nav_tab": "orders"
    },
    35: {
        "title": "Report Missing / Damaged Items",
        "phase": "6. Fulfillment, Ledger & Batching",
        "tag": "ISSUE REPORT",
        "description": "Report delivery discrepancy (e.g. cracked eggs, missing butter). Auto-calculates individual split refunds and credits flat ledger.",
        "instructions": "Select missing items and tap 'SUBMIT TICKET & CREDIT' to view updated flat ledger (Screen 37).",
        "default_next": 37,
        "default_prev": 34,
        "nav_tab": "orders"
    },
    36: {
        "title": "Order History & Haul Receipts",
        "phase": "6. Fulfillment, Ledger & Batching",
        "tag": "PAST ORDERS",
        "description": "Archive of past grocery hauls: Filter by 'All', 'Mine', or 'Flat 402'. Detailed receipts with item lists and roommate split tallies.",
        "instructions": "Tap any past haul to view order tracking or delivery summary, or use bottom tabs.",
        "default_next": 33,
        "default_prev": 7,
        "nav_tab": "orders"
    },
    37: {
        "title": "Flat Expense Ledger & Balances",
        "phase": "6. Fulfillment, Ledger & Batching",
        "tag": "LEDGER",
        "description": "Consolidated flat debt ledger: 'WHO OWES WHAT · Net Balances'. Kabir owes you ₹180, You owe Maya ₹90. One-tap UPI settlement.",
        "instructions": "Tap 'SETTLE VIA UPI' to open payment handoff (Screen 21), or tap 'FLOOR BATCH' to view cross-flat delivery sharing (Screen 38).",
        "default_next": 38,
        "default_prev": 7,
        "nav_tab": "ledger"
    },
    38: {
        "title": "Floor Batching (Multi-Flat Logistics)",
        "phase": "6. Fulfillment, Ledger & Batching",
        "tag": "COMMUNITY BATCH",
        "description": "Building-level logistics: Flat 401, Flat 402, and Flat 403 pooling Blinkit delivery orders into a single rider drop to save ₹60 fee.",
        "instructions": "Tap 'JOIN THIS BATCH' to create a haul attached to the building drop (Screen 11).",
        "default_next": 11,
        "default_prev": 37,
        "nav_tab": "flat"
    }
}

def collect_screen_files():
    screen_files = {}
    for folder in FOLDERS:
        for item in os.listdir(folder):
            full_path = os.path.join(folder, item)
            if os.path.isdir(full_path) and re.match(r'^\d+_', item):
                num = int(re.match(r'^(\d+)_', item).group(1))
                html_path = os.path.join(full_path, 'code.html')
                if os.path.exists(html_path):
                    screen_files[num] = (item, html_path)
    return screen_files

def extract_body_and_scripts(html_content, screen_num):
    # Extract body content
    body_match = re.search(r'<body[^>]*>(.*?)</body>', html_content, re.DOTALL | re.IGNORECASE)
    if not body_match:
        return "", ""
    raw_body = body_match.group(1).strip()
    
    # Separate inline <script> tags from the body so they don't break our SPA
    scripts = re.findall(r'<script[^>]*>(.*?)</script>', raw_body, re.DOTALL | re.IGNORECASE)
    # Remove script tags from HTML
    clean_html = re.sub(r'<script[^>]*>.*?</script>', '', raw_body, flags=re.DOTALL | re.IGNORECASE).strip()
    
    combined_script = "\n// --- Screen %02d Scripts ---\n" % screen_num
    for s in scripts:
        s_clean = s.strip()
        if s_clean:
            combined_script += "(function() {\n" + s_clean + "\n})();\n"
            
    return clean_html, combined_script

def build_all():
    screens = collect_screen_files()
    print(f"Found {len(screens)} screens.")
    
    extracted_screens = {}
    all_scripts = []
    
    for num in range(1, 39):
        if num not in screens:
            print(f"Warning: Screen {num} missing!")
            continue
        name, html_path = screens[num]
        with open(html_path, 'r', encoding='utf-8') as f:
            content = f.read()
        body_html, script = extract_body_and_scripts(content, num)
        extracted_screens[num] = {
            "name": name,
            "html": body_html,
            "meta": SCREEN_METADATA.get(num, {
                "title": name,
                "phase": "Flow",
                "tag": f"S{num:02d}",
                "description": "",
                "instructions": "",
                "default_next": (num % 38) + 1,
                "default_prev": max(1, num - 1),
                "nav_tab": None
            })
        }
        if script:
            all_scripts.append(script)
            
    # Generate the unified HTML document
    html_output = generate_master_html(extracted_screens, all_scripts)
    
    # Write to destination 1: kinetic_utility/index.html
    os.makedirs(os.path.dirname(OUTPUT_PATH_1), exist_ok=True)
    with open(OUTPUT_PATH_1, 'w', encoding='utf-8') as f:
        f.write(html_output)
    print(f"Wrote master app to: {OUTPUT_PATH_1} ({len(html_output)} bytes)")
    
    # Write to destination 2: stitch_roommate_cart_mobile_app/index.html
    try:
        with open(OUTPUT_PATH_2, 'w', encoding='utf-8') as f:
            f.write(html_output)
        print(f"Wrote master app to: {OUTPUT_PATH_2} ({len(html_output)} bytes)")
    except Exception as e:
        print(f"Note on parent write: {e}")

def generate_master_html(screens, all_scripts):
    screens_json = json.dumps({
        num: {
            "num": num,
            "name": screens[num]["name"],
            "title": screens[num]["meta"]["title"],
            "phase": screens[num]["meta"]["phase"],
            "tag": screens[num]["meta"]["tag"],
            "description": screens[num]["meta"]["description"],
            "instructions": screens[num]["meta"]["instructions"],
            "default_next": screens[num]["meta"]["default_next"],
            "default_prev": screens[num]["meta"]["default_prev"],
            "nav_tab": screens[num]["meta"]["nav_tab"]
        }
        for num in screens
    }, indent=2)

    screens_html_blocks = []
    for num in sorted(screens.keys()):
        data = screens[num]
        meta = data["meta"]
        # Screen wrapper
        screen_block = f"""
        <!-- SCREEN {num:02d}: {meta['title']} -->
        <div id="screen-view-{num}" class="screen-view {'active' if num == 1 else ''}" data-screen-num="{num}" data-tab="{meta.get('nav_tab') or ''}">
          {data['html']}
        </div>
        """
        screens_html_blocks.append(screen_block)

    screens_joined = "\n".join(screens_html_blocks)
    scripts_joined = "\n".join(all_scripts)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">
  <title>Roommate Cart · 38 Screens Mobile Experience</title>
  
  <!-- Design System Fonts: Barlow Condensed & Inter -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@600;700;800&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200" rel="stylesheet">
  <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&display=swap" rel="stylesheet">
  
  <!-- Tailwind CSS CDN -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script id="tailwind-config">
    tailwind.config = {{
      darkMode: "class",
      theme: {{
        extend: {{
          colors: {{
            "tertiary": "#000000",
            "error": "#ba1a1a",
            "outline": "#747878",
            "on-primary-container": "#858383",
            "surface-container": "#eeeeea",
            "on-primary": "#ffffff",
            "surface": "#faf9f5",
            "on-secondary-fixed": "#00210b",
            "on-secondary": "#ffffff",
            "surface-dim": "#dadad6",
            "on-background": "#1a1c1a",
            "outline-variant": "#c4c7c7",
            "on-tertiary-fixed": "#00210b",
            "on-error-container": "#93000a",
            "surface-bright": "#faf9f5",
            "inverse-surface": "#2f312e",
            "primary": "#000000",
            "on-surface": "#1a1c1a",
            "on-surface-variant": "#444748",
            "secondary-fixed": "#62ff95",
            "tertiary-fixed": "#71fd98",
            "surface-tint": "#5f5e5e",
            "background": "#faf9f5",
            "inverse-on-surface": "#f1f1ed",
            "primary-fixed": "#e5e2e1",
            "surface-variant": "#e2e3df",
            "secondary-container": "#59fd90",
            "tertiary-container": "#00210b",
            "surface-container-lowest": "#ffffff",
            "on-tertiary-container": "#009849",
            "on-secondary-container": "#007236",
            "on-tertiary": "#ffffff",
            "on-primary-fixed": "#1c1b1b",
            "secondary": "#006d34",
            "primary-container": "#1c1b1b",
            "on-tertiary-fixed-variant": "#005224",
            "secondary-fixed-dim": "#37e279",
            "surface-container-high": "#e8e8e4",
            "inverse-primary": "#c8c6c5",
            "error-container": "#ffdad6",
            "on-secondary-fixed-variant": "#005225",
            "surface-container-highest": "#e2e3df",
            "on-primary-fixed-variant": "#474646",
            "primary-fixed-dim": "#c8c6c5",
            "tertiary-fixed-dim": "#52e07f",
            "surface-container-low": "#f4f4f0",
            "on-error": "#ffffff"
          }},
          borderRadius: {{
            "DEFAULT": "1rem",
            "lg": "2rem",
            "xl": "3rem",
            "full": "9999px"
          }},
          spacing: {{
            "space-xs": "0.25rem",
            "gutter": "1rem",
            "space-sm": "0.5rem",
            "margin": "1rem",
            "gutter-mobile": "0.75rem",
            "space-lg": "1.5rem",
            "margin-mobile": "1rem",
            "space-md": "1rem",
            "space-xl": "2rem"
          }},
          fontFamily: {{
            "label-action": ["Barlow Condensed", "sans-serif"],
            "headline-sm": ["Barlow Condensed", "sans-serif"],
            "body-sm": ["Inter", "sans-serif"],
            "headline-lg": ["Barlow Condensed", "sans-serif"],
            "body-md": ["Inter", "sans-serif"],
            "display-currency-mobile": ["Barlow Condensed", "sans-serif"],
            "display-currency": ["Barlow Condensed", "sans-serif"],
            "label-tag": ["Barlow Condensed", "sans-serif"],
            "body-lg": ["Inter", "sans-serif"],
            "eyebrow": ["Inter", "sans-serif"],
            "title-md": ["Inter", "sans-serif"],
            "headline-md": ["Barlow Condensed", "sans-serif"]
          }},
          fontSize: {{
            "label-action": ["18px", {{ "lineHeight": "22px", "letterSpacing": "0.05em", "fontWeight": "700" }}],
            "headline-sm": ["20px", {{ "lineHeight": "24px", "letterSpacing": "0.01em", "fontWeight": "700" }}],
            "body-sm": ["12px", {{ "lineHeight": "16px", "fontWeight": "400" }}],
            "headline-lg": ["32px", {{ "lineHeight": "36px", "letterSpacing": "-0.01em", "fontWeight": "800" }}],
            "body-md": ["14px", {{ "lineHeight": "20px", "fontWeight": "400" }}],
            "display-currency-mobile": ["38px", {{ "lineHeight": "42px", "letterSpacing": "-0.02em", "fontWeight": "800" }}],
            "display-currency": ["44px", {{ "lineHeight": "48px", "letterSpacing": "-0.02em", "fontWeight": "800" }}],
            "label-tag": ["13px", {{ "lineHeight": "16px", "letterSpacing": "0.08em", "fontWeight": "700" }}],
            "body-lg": ["15px", {{ "lineHeight": "22px", "fontWeight": "500" }}],
            "eyebrow": ["11px", {{ "lineHeight": "14px", "letterSpacing": "0.12em", "fontWeight": "700" }}],
            "title-md": ["16px", {{ "lineHeight": "22px", "letterSpacing": "-0.01em", "fontWeight": "600" }}],
            "headline-md": ["24px", {{ "lineHeight": "28px", "letterSpacing": "0em", "fontWeight": "700" }}]
          }}
        }}
      }}
    }};
  </script>

  <style>
    @layer base {{
      html, body {{
        width: 100%;
        margin: 0;
        padding: 0;
        min-height: 100vh;
        background-color: #121312;
        font-family: 'Inter', sans-serif;
        -webkit-font-smoothing: antialiased;
        overflow-x: hidden;
      }}
      .pb-safe {{ padding-bottom: env(safe-area-inset-bottom, 12px); }}
      .pt-safe {{ padding-top: env(safe-area-inset-top, 12px); }}
    }}
    ::-webkit-scrollbar {{ display: none; }}
    
    /* Studio workbench canvas */
    .studio-canvas {{
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      padding: 24px 16px 90px 16px;
      background: radial-gradient(circle at 50% 20%, #1e201e 0%, #0d0e0d 100%);
    }}

    /* Realistic iPhone 16 Pro Frame */
    .phone-mockup {{
      position: relative;
      width: 390px;
      height: 844px;
      background: #faf9f5;
      border-radius: 54px;
      box-shadow: 
        0 0 0 4px #2b2b2a,
        0 0 0 8px #181918,
        0 25px 60px -15px rgba(0, 0, 0, 0.8),
        0 0 100px rgba(34, 214, 111, 0.08);
      overflow: hidden;
      display: flex;
      flex-direction: column;
      flex-shrink: 0;
      transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    }}

    /* Transform creates local containing block for position: fixed elements! */
    .phone-screen {{
      position: relative;
      width: 100%;
      height: 100%;
      overflow-y: auto;
      overflow-x: hidden;
      background-color: #faf9f5;
      transform: translateZ(0); /* Crucial: pins fixed headers/footers to mockup! */
      -webkit-overflow-scrolling: touch;
      display: flex;
      flex-direction: column;
    }}

    /* When responsive / native mobile mode */
    body.native-mobile .studio-canvas {{
      padding: 0 !important;
      background: #faf9f5 !important;
    }}
    body.native-mobile .phone-mockup {{
      width: 100% !important;
      max-width: 100% !important;
      height: 100vh !important;
      height: 100dvh !important;
      border-radius: 0 !important;
      box-shadow: none !important;
      border: none !important;
    }}
    body.native-mobile .device-hardware,
    body.native-mobile .desktop-nav-header {{
      display: none !important;
    }}

    /* Dynamic Island */
    .dynamic-island {{
      position: absolute;
      top: 11px;
      left: 50%;
      transform: translateX(-50%);
      width: 120px;
      height: 32px;
      background: #000000;
      border-radius: 20px;
      z-index: 9999;
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 10px;
      color: #ffffff;
      font-size: 11px;
      pointer-events: none;
      box-shadow: 0 1px 3px rgba(0,0,0,0.4);
    }}

    /* Hardware Status Bar */
    .status-bar {{
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      height: 48px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 10px 28px 0 28px;
      z-index: 9998;
      pointer-events: none;
      font-family: 'Inter', sans-serif;
      font-weight: 600;
      font-size: 14px;
      color: #1a1c1a;
    }}

    /* Bottom Home Indicator Bar */
    .home-indicator {{
      position: absolute;
      bottom: 8px;
      left: 50%;
      transform: translateX(-50%);
      width: 134px;
      height: 5px;
      background: #1a1c1a;
      border-radius: 100px;
      z-index: 9999;
      pointer-events: none;
      opacity: 0.8;
    }}

    /* Screen Views */
    .screen-view {{
      display: none;
      width: 100%;
      min-height: 100%;
      flex-direction: column;
      flex: 1;
      animation: fadeIn 0.25s cubic-bezier(0.16, 1, 0.3, 1) forwards;
    }}
    .screen-view.active {{
      display: flex !important;
    }}

    @keyframes fadeIn {{
      from {{ opacity: 0; transform: translateY(6px); }}
      to {{ opacity: 1; transform: translateY(0); }}
    }}

    /* Floating Master Controller Bar */
    .master-dock {{
      position: fixed;
      bottom: 18px;
      left: 50%;
      transform: translateX(-50%);
      z-index: 10000;
      display: flex;
      align-items: center;
      gap: 10px;
      background: rgba(22, 24, 22, 0.94);
      backdrop-filter: blur(20px);
      border: 1px solid rgba(255, 255, 255, 0.12);
      padding: 8px 14px;
      border-radius: 9999px;
      box-shadow: 0 12px 36px rgba(0, 0, 0, 0.5), 0 0 1px 1px rgba(255, 255, 255, 0.1);
      max-width: 95vw;
    }}

    /* Drawer Modal for All 38 Screens */
    .drawer-overlay {{
      display: none;
      position: fixed;
      inset: 0;
      background: rgba(0, 0, 0, 0.7);
      backdrop-filter: blur(8px);
      z-index: 10010;
    }}
    .drawer-overlay.open {{
      display: flex;
      align-items: flex-end;
      justify-content: center;
    }}
    .screens-drawer {{
      width: 100%;
      max-width: 820px;
      max-height: 88vh;
      background: #faf9f5;
      border-top-left-radius: 32px;
      border-top-right-radius: 32px;
      box-shadow: 0 -20px 50px rgba(0,0,0,0.5);
      display: flex;
      flex-direction: column;
      overflow: hidden;
      animation: slideUp 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    }}
    @keyframes slideUp {{
      from {{ transform: translateY(100%); }}
      to {{ transform: translateY(0); }}
    }}

    /* Instructions Modal */
    .instructions-drawer {{
      width: 100%;
      max-width: 600px;
      background: #1c1b1b;
      color: #faf9f5;
      border-top-left-radius: 28px;
      border-top-right-radius: 28px;
      padding: 24px;
      max-height: 80vh;
      overflow-y: auto;
      box-shadow: 0 -20px 50px rgba(0,0,0,0.6);
      animation: slideUp 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    }}

    /* Toast Notification */
    #app-toast {{
      position: fixed;
      top: 60px;
      left: 50%;
      transform: translateX(-50%) translateY(-20px);
      background: #121212;
      color: #ffffff;
      padding: 8px 18px;
      border-radius: 9999px;
      font-size: 13px;
      font-weight: 600;
      letter-spacing: 0.02em;
      opacity: 0;
      pointer-events: none;
      transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
      z-index: 10020;
      border: 1px solid #333;
      box-shadow: 0 8px 24px rgba(0,0,0,0.3);
    }}
    #app-toast.show {{
      opacity: 1;
      transform: translateX(-50%) translateY(0);
    }}
  </style>
</head>
<body class="selection:bg-secondary-fixed selection:text-on-secondary-fixed">

  <!-- Desktop Top Controls Bar -->
  <header class="desktop-nav-header w-full bg-[#161716] text-[#faf9f5] border-b border-[#282a28] px-6 py-3 flex items-center justify-between text-xs select-none">
    <div class="flex items-center gap-3">
      <div class="flex items-center gap-2">
        <span class="w-3 h-3 rounded-full bg-secondary-container"></span>
        <span class="font-headline-sm uppercase tracking-wider text-sm font-bold">ROOMMATE CART</span>
      </div>
      <span class="text-outline text-[11px] font-mono">v1.0 · KINETIC UTILITY</span>
      <span class="px-2 py-0.5 rounded-full bg-[#242624] text-[#85fd9e] font-label-tag text-[10px]">38 SCREENS LOADED</span>
    </div>

    <!-- Center Flow / Screen indicator -->
    <div class="hidden md:flex items-center gap-2">
      <span class="text-outline uppercase text-[10px] tracking-wider">ACTIVE SCREEN:</span>
      <span id="top-screen-badge" class="font-bold text-[#faf9f5] px-2.5 py-1 rounded bg-[#242624] text-[12px]">01 · Splash</span>
    </div>

    <!-- Right Controls -->
    <div class="flex items-center gap-2">
      
      <!-- Sound & Haptics Toggle -->
      <button id="sound-toggle-btn" onclick="toggleSound()" title="Toggle Sound & Haptic Clicks" class="w-8 h-8 rounded-full bg-[#242624] hover:bg-[#323632] text-[#faf9f5] flex items-center justify-center transition-all">
        <span class="material-symbols-outlined text-[16px]">volume_up</span>
      </button>

      <!-- Device View Toggle -->
      <button id="toggle-frame-btn" onclick="toggleNativeMobile()" class="px-3 py-1.5 rounded-full bg-[#242624] hover:bg-[#323632] text-[#faf9f5] font-semibold transition-all flex items-center gap-1.5">
        <span class="material-symbols-outlined text-[16px]">smartphone</span>
        <span id="frame-btn-text">Mobile Frame</span>
      </button>

      <!-- Zoom / Scale buttons -->
      <div class="hidden lg:flex items-center gap-1 bg-[#242624] rounded-full p-1">
        <button onclick="setZoom(0.85)" class="px-2 py-0.5 rounded-full hover:bg-[#343834] text-[11px]">85%</button>
        <button onclick="setZoom(1.0)" class="px-2 py-0.5 rounded-full bg-[#343834] text-[11px] font-bold">100%</button>
        <button onclick="setZoom(1.1)" class="px-2 py-0.5 rounded-full hover:bg-[#343834] text-[11px]">110%</button>
      </div>

      <!-- Instructions & Context -->
      <button onclick="openInstructions()" class="px-3 py-1.5 rounded-full bg-secondary-container text-primary font-bold text-xs hover:bg-[#43e479] transition-all flex items-center gap-1">
        <span class="material-symbols-outlined text-[16px]">info</span>
        <span>Specs & Guide</span>
      </button>
    </div>
  </header>

  <!-- Studio Workbench Canvas -->
  <main class="studio-canvas">
    
    <!-- Phone Device Shell -->
    <div id="phone-container" class="phone-mockup">
      
      <!-- Hardware: Dynamic Island & Status Bar -->
      <div class="device-hardware">
        <div class="status-bar">
          <span id="status-time">09:41</span>
          <div class="flex items-center gap-1.5">
            <span class="material-symbols-outlined text-[16px]">signal_cellular_4_bar</span>
            <span class="material-symbols-outlined text-[16px]">wifi</span>
            <span class="material-symbols-outlined text-[18px]">battery_charging_full</span>
          </div>
        </div>
        
        <div class="dynamic-island">
          <div class="flex items-center gap-1">
            <span class="w-2 h-2 rounded-full bg-[#22d66f] animate-pulse"></span>
            <span class="text-[10px] tracking-wide font-mono">UPI LIVE</span>
          </div>
          <span class="material-symbols-outlined text-[14px] text-zinc-400">lock</span>
        </div>
      </div>

      <!-- Phone Screen Viewport (Scrollable container with translateZ(0)) -->
      <div id="phone-screen" class="phone-screen">
        {screens_joined}
      </div>

      <!-- Hardware: Home Bar Indicator -->
      <div class="home-indicator device-hardware"></div>
    </div>

  </main>

  <!-- Floating Master Controller Dock -->
  <div class="master-dock select-none">
    <!-- Prev Button -->
    <button onclick="prevScreen()" title="Previous Screen (Left Arrow)" class="w-9 h-9 rounded-full bg-[#242624] hover:bg-[#343834] text-white flex items-center justify-center transition-all active:scale-95">
      <span class="material-symbols-outlined text-[20px]">arrow_back</span>
    </button>

    <!-- Center Screen Info Trigger -->
    <button onclick="openScreensDrawer()" class="flex items-center gap-2.5 px-3 py-1.5 rounded-full hover:bg-[#282a28] transition-all text-left">
      <div class="flex flex-col">
        <div class="flex items-center gap-1.5">
          <span id="dock-screen-num" class="font-mono text-[11px] font-bold text-secondary-container">01/38</span>
          <span id="dock-screen-title" class="text-white text-xs font-semibold truncate max-w-[150px] sm:max-w-[220px]">Splash & Value</span>
        </div>
        <span id="dock-screen-phase" class="text-outline text-[10px] uppercase tracking-wider">1. Onboarding & Setup</span>
      </div>
      <span class="material-symbols-outlined text-outline text-[18px]">expand_less</span>
    </button>

    <!-- Next Button -->
    <button onclick="nextScreen()" title="Next Screen (Right Arrow)" class="w-9 h-9 rounded-full bg-[#242624] hover:bg-[#343834] text-white flex items-center justify-center transition-all active:scale-95">
      <span class="material-symbols-outlined text-[20px]">arrow_forward</span>
    </button>

    <div class="w-px h-6 bg-zinc-700 mx-1"></div>

    <!-- All 38 Screens Catalog Button -->
    <button onclick="openScreensDrawer()" class="px-3 py-1.5 rounded-full bg-secondary-container hover:bg-[#4de685] text-primary font-bold text-xs flex items-center gap-1 transition-all active:scale-95">
      <span class="material-symbols-outlined text-[18px]">apps</span>
      <span class="hidden sm:inline">All 38 Screens</span>
    </button>
  </div>

  <!-- Screen Catalog Drawer Modal -->
  <div id="drawer-overlay" class="drawer-overlay" onclick="closeDrawer(event)">
    <div class="screens-drawer" onclick="event.stopPropagation()">
      <!-- Drawer Header -->
      <div class="p-5 border-b border-surface-container-high flex items-center justify-between bg-surface">
        <div class="flex items-center gap-3">
          <div class="w-9 h-9 rounded-full bg-secondary-container flex items-center justify-center text-primary font-bold">
            <span class="material-symbols-outlined text-[20px]">dataset</span>
          </div>
          <div>
            <h3 class="font-headline-sm uppercase text-on-surface text-lg font-bold leading-none">ALL 38 APP SCREENS</h3>
            <p class="font-body-sm text-on-surface-variant text-xs mt-0.5">Click any screen to preview immediately</p>
          </div>
        </div>
        <button onclick="closeDrawer()" class="w-8 h-8 rounded-full bg-surface-container hover:bg-surface-container-high flex items-center justify-center text-on-surface transition-all">
          <span class="material-symbols-outlined text-[20px]">close</span>
        </button>
      </div>

      <!-- Drawer Content: 6 Flows Grid -->
      <div class="p-5 overflow-y-auto space-y-6 flex-1 bg-surface-container-lowest">
        
        <!-- Flow 1 -->
        <div>
          <div class="flex items-center justify-between mb-3 border-b border-surface-container pb-1">
            <h4 class="font-label-tag text-label-tag text-secondary uppercase font-bold tracking-wider">FLOW 1 · ONBOARDING & SETUP (01 - 06)</h4>
            <span class="text-outline text-xs">6 Screens</span>
          </div>
          <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-2.5">
            <button onclick="goToScreen(1)" class="drawer-item p-3 text-left rounded-xl bg-surface hover:bg-surface-container border border-outline-variant/50 transition-all flex items-center gap-2.5">
              <span class="w-7 h-7 rounded-lg bg-surface-container-high font-mono text-xs font-bold flex items-center justify-center">01</span>
              <div class="flex-1 min-w-0">
                <div class="font-bold text-xs truncate">Splash & Value</div>
                <div class="text-[10px] text-outline truncate">Value prop & split topology</div>
              </div>
            </button>
            <button onclick="goToScreen(2)" class="drawer-item p-3 text-left rounded-xl bg-surface hover:bg-surface-container border border-outline-variant/50 transition-all flex items-center gap-2.5">
              <span class="w-7 h-7 rounded-lg bg-surface-container-high font-mono text-xs font-bold flex items-center justify-center">02</span>
              <div class="flex-1 min-w-0">
                <div class="font-bold text-xs truncate">Phone OTP</div>
                <div class="text-[10px] text-outline truncate">Mobile verification</div>
              </div>
            </button>
            <button onclick="goToScreen(3)" class="drawer-item p-3 text-left rounded-xl bg-surface hover:bg-surface-container border border-outline-variant/50 transition-all flex items-center gap-2.5">
              <span class="w-7 h-7 rounded-lg bg-surface-container-high font-mono text-xs font-bold flex items-center justify-center">03</span>
              <div class="flex-1 min-w-0">
                <div class="font-bold text-xs truncate">Profile Setup</div>
                <div class="text-[10px] text-outline truncate">Name & avatar tokens</div>
              </div>
            </button>
            <button onclick="goToScreen(4)" class="drawer-item p-3 text-left rounded-xl bg-surface hover:bg-surface-container border border-outline-variant/50 transition-all flex items-center gap-2.5">
              <span class="w-7 h-7 rounded-lg bg-surface-container-high font-mono text-xs font-bold flex items-center justify-center">04</span>
              <div class="flex-1 min-w-0">
                <div class="font-bold text-xs truncate">Campus & Hostel</div>
                <div class="text-[10px] text-outline truncate">Location selector</div>
              </div>
            </button>
            <button onclick="goToScreen(5)" class="drawer-item p-3 text-left rounded-xl bg-surface hover:bg-surface-container border border-outline-variant/50 transition-all flex items-center gap-2.5">
              <span class="w-7 h-7 rounded-lg bg-surface-container-high font-mono text-xs font-bold flex items-center justify-center">05</span>
              <div class="flex-1 min-w-0">
                <div class="font-bold text-xs truncate">Create or Join Flat</div>
                <div class="text-[10px] text-outline truncate">Flat 402 code & QR</div>
              </div>
            </button>
            <button onclick="goToScreen(6)" class="drawer-item p-3 text-left rounded-xl bg-surface hover:bg-surface-container border border-outline-variant/50 transition-all flex items-center gap-2.5">
              <span class="w-7 h-7 rounded-lg bg-surface-container-high font-mono text-xs font-bold flex items-center justify-center">06</span>
              <div class="flex-1 min-w-0">
                <div class="font-bold text-xs truncate">Link UPI & Alerts</div>
                <div class="text-[10px] text-outline truncate">GPay / PhonePe linking</div>
              </div>
            </button>
          </div>
        </div>

        <!-- Flow 2 -->
        <div>
          <div class="flex items-center justify-between mb-3 border-b border-surface-container pb-1">
            <h4 class="font-label-tag text-label-tag text-secondary uppercase font-bold tracking-wider">FLOW 2 · FLAT HUB & DASHBOARD (07 - 10)</h4>
            <span class="text-outline text-xs">4 Screens</span>
          </div>
          <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-2.5">
            <button onclick="goToScreen(7)" class="drawer-item p-3 text-left rounded-xl bg-surface hover:bg-surface-container border border-outline-variant/50 transition-all flex items-center gap-2.5">
              <span class="w-7 h-7 rounded-lg bg-surface-container-high font-mono text-xs font-bold flex items-center justify-center">07</span>
              <div class="flex-1 min-w-0">
                <div class="font-bold text-xs truncate">Home (Open Carts)</div>
                <div class="text-[10px] text-outline truncate">Active Sunday haul</div>
              </div>
            </button>
            <button onclick="goToScreen(8)" class="drawer-item p-3 text-left rounded-xl bg-surface hover:bg-surface-container border border-outline-variant/50 transition-all flex items-center gap-2.5">
              <span class="w-7 h-7 rounded-lg bg-surface-container-high font-mono text-xs font-bold flex items-center justify-center">08</span>
              <div class="flex-1 min-w-0">
                <div class="font-bold text-xs truncate">Home (Empty State)</div>
                <div class="text-[10px] text-outline truncate">No active hauls</div>
              </div>
            </button>
            <button onclick="goToScreen(9)" class="drawer-item p-3 text-left rounded-xl bg-surface hover:bg-surface-container border border-outline-variant/50 transition-all flex items-center gap-2.5">
              <span class="w-7 h-7 rounded-lg bg-surface-container-high font-mono text-xs font-bold flex items-center justify-center">09</span>
              <div class="flex-1 min-w-0">
                <div class="font-bold text-xs truncate">Flat Settings</div>
                <div class="text-[10px] text-outline truncate">Flatmates & UPI routing</div>
              </div>
            </button>
            <button onclick="goToScreen(10)" class="drawer-item p-3 text-left rounded-xl bg-surface hover:bg-surface-container border border-outline-variant/50 transition-all flex items-center gap-2.5">
              <span class="w-7 h-7 rounded-lg bg-surface-container-high font-mono text-xs font-bold flex items-center justify-center">10</span>
              <div class="flex-1 min-w-0">
                <div class="font-bold text-xs truncate">Activity & Alerts</div>
                <div class="text-[10px] text-outline truncate">Notifications feed</div>
              </div>
            </button>
          </div>
        </div>

        <!-- Flow 3 -->
        <div>
          <div class="flex items-center justify-between mb-3 border-b border-surface-container pb-1">
            <h4 class="font-label-tag text-label-tag text-secondary uppercase font-bold tracking-wider">FLOW 3 · SHOPPING & SHARED CART (11 - 18)</h4>
            <span class="text-outline text-xs">8 Screens</span>
          </div>
          <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-2.5">
            <button onclick="goToScreen(11)" class="drawer-item p-3 text-left rounded-xl bg-surface hover:bg-surface-container border border-outline-variant/50 transition-all flex items-center gap-2.5">
              <span class="w-7 h-7 rounded-lg bg-surface-container-high font-mono text-xs font-bold flex items-center justify-center">11</span>
              <div class="flex-1 min-w-0">
                <div class="font-bold text-xs truncate">Start New Cart</div>
                <div class="text-[10px] text-outline truncate">Blinkit, Zepto, timer</div>
              </div>
            </button>
            <button onclick="goToScreen(12)" class="drawer-item p-3 text-left rounded-xl bg-surface hover:bg-surface-container border border-outline-variant/50 transition-all flex items-center gap-2.5">
              <span class="w-7 h-7 rounded-lg bg-surface-container-high font-mono text-xs font-bold flex items-center justify-center">12</span>
              <div class="flex-1 min-w-0">
                <div class="font-bold text-xs truncate">Invite Flatmates</div>
                <div class="text-[10px] text-outline truncate">Copy link & QR code</div>
              </div>
            </button>
            <button onclick="goToScreen(13)" class="drawer-item p-3 text-left rounded-xl bg-surface hover:bg-surface-container border border-outline-variant/50 transition-all flex items-center gap-2.5">
              <span class="w-7 h-7 rounded-lg bg-surface-container-high font-mono text-xs font-bold flex items-center justify-center">13</span>
              <div class="flex-1 min-w-0">
                <div class="font-bold text-xs truncate">Store Browse</div>
                <div class="text-[10px] text-outline truncate">Staples, dairy, snacks</div>
              </div>
            </button>
            <button onclick="goToScreen(14)" class="drawer-item p-3 text-left rounded-xl bg-surface hover:bg-surface-container border border-outline-variant/50 transition-all flex items-center gap-2.5">
              <span class="w-7 h-7 rounded-lg bg-surface-container-high font-mono text-xs font-bold flex items-center justify-center">14</span>
              <div class="flex-1 min-w-0">
                <div class="font-bold text-xs truncate">Search Results</div>
                <div class="text-[10px] text-outline truncate">Basmati rice results</div>
              </div>
            </button>
            <button onclick="goToScreen(15)" class="drawer-item p-3 text-left rounded-xl bg-surface hover:bg-surface-container border border-outline-variant/50 transition-all flex items-center gap-2.5">
              <span class="w-7 h-7 rounded-lg bg-surface-container-high font-mono text-xs font-bold flex items-center justify-center">15</span>
              <div class="flex-1 min-w-0">
                <div class="font-bold text-xs truncate">Item Detail Sheet</div>
                <div class="text-[10px] text-outline truncate">Quantity & split toggle</div>
              </div>
            </button>
            <button onclick="goToScreen(16)" class="drawer-item p-3 text-left rounded-xl bg-surface hover:bg-surface-container border border-outline-variant/50 transition-all flex items-center gap-2.5">
              <span class="w-7 h-7 rounded-lg bg-surface-container-high font-mono text-xs font-bold flex items-center justify-center">16</span>
              <div class="flex-1 min-w-0">
                <div class="font-bold text-xs truncate">Shared Cart View</div>
                <div class="text-[10px] text-outline truncate">Live lock countdown</div>
              </div>
            </button>
            <button onclick="goToScreen(17)" class="drawer-item p-3 text-left rounded-xl bg-surface hover:bg-surface-container border border-outline-variant/50 transition-all flex items-center gap-2.5">
              <span class="w-7 h-7 rounded-lg bg-surface-container-high font-mono text-xs font-bold flex items-center justify-center">17</span>
              <div class="flex-1 min-w-0">
                <div class="font-bold text-xs truncate">Ownership Mode</div>
                <div class="text-[10px] text-outline truncate">Equal vs prorated</div>
              </div>
            </button>
            <button onclick="goToScreen(18)" class="drawer-item p-3 text-left rounded-xl bg-surface hover:bg-surface-container border border-outline-variant/50 transition-all flex items-center gap-2.5">
              <span class="w-7 h-7 rounded-lg bg-surface-container-high font-mono text-xs font-bold flex items-center justify-center">18</span>
              <div class="flex-1 min-w-0">
                <div class="font-bold text-xs truncate">Prorated Sliders</div>
                <div class="text-[10px] text-outline truncate">Custom share ratios</div>
              </div>
            </button>
          </div>
        </div>

        <!-- Flow 4 -->
        <div>
          <div class="flex items-center justify-between mb-3 border-b border-surface-container pb-1">
            <h4 class="font-label-tag text-label-tag text-secondary uppercase font-bold tracking-wider">FLOW 4 · CHECKOUT & UPI SPLIT (19 - 24)</h4>
            <span class="text-outline text-xs">6 Screens</span>
          </div>
          <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-2.5">
            <button onclick="goToScreen(19)" class="drawer-item p-3 text-left rounded-xl bg-surface hover:bg-surface-container border border-outline-variant/50 transition-all flex items-center gap-2.5">
              <span class="w-7 h-7 rounded-lg bg-surface-container-high font-mono text-xs font-bold flex items-center justify-center">19</span>
              <div class="flex-1 min-w-0">
                <div class="font-bold text-xs truncate">Checkout Summary</div>
                <div class="text-[10px] text-outline truncate">Delivery fee split</div>
              </div>
            </button>
            <button onclick="goToScreen(20)" class="drawer-item p-3 text-left rounded-xl bg-surface hover:bg-surface-container border border-outline-variant/50 transition-all flex items-center gap-2.5">
              <span class="w-7 h-7 rounded-lg bg-surface-container-high font-mono text-xs font-bold flex items-center justify-center">20</span>
              <div class="flex-1 min-w-0">
                <div class="font-bold text-xs truncate">Your Share (₹342)</div>
                <div class="text-[10px] text-outline truncate">Instant UPI trigger</div>
              </div>
            </button>
            <button onclick="goToScreen(21)" class="drawer-item p-3 text-left rounded-xl bg-surface hover:bg-surface-container border border-outline-variant/50 transition-all flex items-center gap-2.5">
              <span class="w-7 h-7 rounded-lg bg-surface-container-high font-mono text-xs font-bold flex items-center justify-center">21</span>
              <div class="flex-1 min-w-0">
                <div class="font-bold text-xs truncate">UPI App Handoff</div>
                <div class="text-[10px] text-outline truncate">NPCI payment animation</div>
              </div>
            </button>
            <button onclick="goToScreen(22)" class="drawer-item p-3 text-left rounded-xl bg-surface hover:bg-surface-container border border-outline-variant/50 transition-all flex items-center gap-2.5">
              <span class="w-7 h-7 rounded-lg bg-surface-container-high font-mono text-xs font-bold flex items-center justify-center">22</span>
              <div class="flex-1 min-w-0">
                <div class="font-bold text-xs truncate">Payment Success</div>
                <div class="text-[10px] text-outline truncate">PAID ₹342 receipt</div>
              </div>
            </button>
            <button onclick="goToScreen(23)" class="drawer-item p-3 text-left rounded-xl bg-surface hover:bg-surface-container border border-outline-variant/50 transition-all flex items-center gap-2.5">
              <span class="w-7 h-7 rounded-lg bg-surface-container-high font-mono text-xs font-bold flex items-center justify-center">23</span>
              <div class="flex-1 min-w-0">
                <div class="font-bold text-xs truncate">Payment Failed</div>
                <div class="text-[10px] text-outline truncate">Retry / spot me</div>
              </div>
            </button>
            <button onclick="goToScreen(24)" class="drawer-item p-3 text-left rounded-xl bg-surface hover:bg-surface-container border border-outline-variant/50 transition-all flex items-center gap-2.5">
              <span class="w-7 h-7 rounded-lg bg-surface-container-high font-mono text-xs font-bold flex items-center justify-center">24</span>
              <div class="flex-1 min-w-0">
                <div class="font-bold text-xs truncate">Timer Expired</div>
                <div class="text-[10px] text-outline truncate">Extend lock / revive</div>
              </div>
            </button>
          </div>
        </div>

        <!-- Flow 5 -->
        <div>
          <div class="flex items-center justify-between mb-3 border-b border-surface-container pb-1">
            <h4 class="font-label-tag text-label-tag text-secondary uppercase font-bold tracking-wider">FLOW 5 · ROOMMATE EDGE CASES (25 - 32)</h4>
            <span class="text-outline text-xs">8 Screens</span>
          </div>
          <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-2.5">
            <button onclick="goToScreen(25)" class="drawer-item p-3 text-left rounded-xl bg-surface hover:bg-surface-container border border-outline-variant/50 transition-all flex items-center gap-2.5">
              <span class="w-7 h-7 rounded-lg bg-surface-container-high font-mono text-xs font-bold flex items-center justify-center">25</span>
              <div class="flex-1 min-w-0">
                <div class="font-bold text-xs truncate">Payment Status</div>
                <div class="text-[10px] text-outline truncate">2 of 4 paid, nudge</div>
              </div>
            </button>
            <button onclick="goToScreen(26)" class="drawer-item p-3 text-left rounded-xl bg-surface hover:bg-surface-container border border-outline-variant/50 transition-all flex items-center gap-2.5">
              <span class="w-7 h-7 rounded-lg bg-surface-container-high font-mono text-xs font-bold flex items-center justify-center">26</span>
              <div class="flex-1 min-w-0">
                <div class="font-bold text-xs truncate">Zoya Is Short</div>
                <div class="text-[10px] text-outline truncate">₹120 deficit crisis</div>
              </div>
            </button>
            <button onclick="goToScreen(27)" class="drawer-item p-3 text-left rounded-xl bg-surface hover:bg-surface-container border border-outline-variant/50 transition-all flex items-center gap-2.5">
              <span class="w-7 h-7 rounded-lg bg-surface-container-high font-mono text-xs font-bold flex items-center justify-center">27</span>
              <div class="flex-1 min-w-0">
                <div class="font-bold text-xs truncate">Spot Me Approval</div>
                <div class="text-[10px] text-outline truncate">Payback terms terms</div>
              </div>
            </button>
            <button onclick="goToScreen(28)" class="drawer-item p-3 text-left rounded-xl bg-surface hover:bg-surface-container border border-outline-variant/50 transition-all flex items-center gap-2.5">
              <span class="w-7 h-7 rounded-lg bg-surface-container-high font-mono text-xs font-bold flex items-center justify-center">28</span>
              <div class="flex-1 min-w-0">
                <div class="font-bold text-xs truncate">Room Pool</div>
                <div class="text-[10px] text-outline truncate">Petty cash fund</div>
              </div>
            </button>
            <button onclick="goToScreen(29)" class="drawer-item p-3 text-left rounded-xl bg-surface hover:bg-surface-container border border-outline-variant/50 transition-all flex items-center gap-2.5">
              <span class="w-7 h-7 rounded-lg bg-surface-container-high font-mono text-xs font-bold flex items-center justify-center">29</span>
              <div class="flex-1 min-w-0">
                <div class="font-bold text-xs truncate">Pay or Drop</div>
                <div class="text-[10px] text-outline truncate">Drop items ultimatum</div>
              </div>
            </button>
            <button onclick="goToScreen(30)" class="drawer-item p-3 text-left rounded-xl bg-surface hover:bg-surface-container border border-outline-variant/50 transition-all flex items-center gap-2.5">
              <span class="w-7 h-7 rounded-lg bg-surface-container-high font-mono text-xs font-bold flex items-center justify-center">30</span>
              <div class="flex-1 min-w-0">
                <div class="font-bold text-xs truncate">Substitute Voting</div>
                <div class="text-[10px] text-outline truncate">Out of stock vote</div>
              </div>
            </button>
            <button onclick="goToScreen(31)" class="drawer-item p-3 text-left rounded-xl bg-surface hover:bg-surface-container border border-outline-variant/50 transition-all flex items-center gap-2.5">
              <span class="w-7 h-7 rounded-lg bg-surface-container-high font-mono text-xs font-bold flex items-center justify-center">31</span>
              <div class="flex-1 min-w-0">
                <div class="font-bold text-xs truncate">Surge Price Alert</div>
                <div class="text-[10px] text-outline truncate">Price movement review</div>
              </div>
            </button>
            <button onclick="goToScreen(32)" class="drawer-item p-3 text-left rounded-xl bg-surface hover:bg-surface-container border border-outline-variant/50 transition-all flex items-center gap-2.5">
              <span class="w-7 h-7 rounded-lg bg-surface-container-high font-mono text-xs font-bold flex items-center justify-center">32</span>
              <div class="flex-1 min-w-0">
                <div class="font-bold text-xs truncate">Revive Expired Cart</div>
                <div class="text-[10px] text-outline truncate">1-tap cart revival</div>
              </div>
            </button>
          </div>
        </div>

        <!-- Flow 6 -->
        <div>
          <div class="flex items-center justify-between mb-3 border-b border-surface-container pb-1">
            <h4 class="font-label-tag text-label-tag text-secondary uppercase font-bold tracking-wider">FLOW 6 · FULFILLMENT, LEDGER & BATCHING (33 - 38)</h4>
            <span class="text-outline text-xs">6 Screens</span>
          </div>
          <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-2.5">
            <button onclick="goToScreen(33)" class="drawer-item p-3 text-left rounded-xl bg-surface hover:bg-surface-container border border-outline-variant/50 transition-all flex items-center gap-2.5">
              <span class="w-7 h-7 rounded-lg bg-surface-container-high font-mono text-xs font-bold flex items-center justify-center">33</span>
              <div class="flex-1 min-w-0">
                <div class="font-bold text-xs truncate">Order Tracking</div>
                <div class="text-[10px] text-outline truncate">Gate 2 delivery ETA</div>
              </div>
            </button>
            <button onclick="goToScreen(34)" class="drawer-item p-3 text-left rounded-xl bg-surface hover:bg-surface-container border border-outline-variant/50 transition-all flex items-center gap-2.5">
              <span class="w-7 h-7 rounded-lg bg-surface-container-high font-mono text-xs font-bold flex items-center justify-center">34</span>
              <div class="flex-1 min-w-0">
                <div class="font-bold text-xs truncate">Delivered Confirm</div>
                <div class="text-[10px] text-outline truncate">Doorstep checklist</div>
              </div>
            </button>
            <button onclick="goToScreen(35)" class="drawer-item p-3 text-left rounded-xl bg-surface hover:bg-surface-container border border-outline-variant/50 transition-all flex items-center gap-2.5">
              <span class="w-7 h-7 rounded-lg bg-surface-container-high font-mono text-xs font-bold flex items-center justify-center">35</span>
              <div class="flex-1 min-w-0">
                <div class="font-bold text-xs truncate">Report An Issue</div>
                <div class="text-[10px] text-outline truncate">Missing item & refund</div>
              </div>
            </button>
            <button onclick="goToScreen(36)" class="drawer-item p-3 text-left rounded-xl bg-surface hover:bg-surface-container border border-outline-variant/50 transition-all flex items-center gap-2.5">
              <span class="w-7 h-7 rounded-lg bg-surface-container-high font-mono text-xs font-bold flex items-center justify-center">36</span>
              <div class="flex-1 min-w-0">
                <div class="font-bold text-xs truncate">Order History</div>
                <div class="text-[10px] text-outline truncate">Past hauls & receipts</div>
              </div>
            </button>
            <button onclick="goToScreen(37)" class="drawer-item p-3 text-left rounded-xl bg-surface hover:bg-surface-container border border-outline-variant/50 transition-all flex items-center gap-2.5">
              <span class="w-7 h-7 rounded-lg bg-surface-container-high font-mono text-xs font-bold flex items-center justify-center">37</span>
              <div class="flex-1 min-w-0">
                <div class="font-bold text-xs truncate">Flat Ledger</div>
                <div class="text-[10px] text-outline truncate">Who owes what & UPI</div>
              </div>
            </button>
            <button onclick="goToScreen(38)" class="drawer-item p-3 text-left rounded-xl bg-surface hover:bg-surface-container border border-outline-variant/50 transition-all flex items-center gap-2.5">
              <span class="w-7 h-7 rounded-lg bg-surface-container-high font-mono text-xs font-bold flex items-center justify-center">38</span>
              <div class="flex-1 min-w-0">
                <div class="font-bold text-xs truncate">Floor Batching</div>
                <div class="text-[10px] text-outline truncate">3 flats, 1 drop saving</div>
              </div>
            </button>
          </div>
        </div>

      </div>
    </div>
  </div>

  <!-- Instructions & Scenario Drawer Modal -->
  <div id="instructions-overlay" class="drawer-overlay" onclick="closeInstructions(event)">
    <div class="instructions-drawer" onclick="event.stopPropagation()">
      <div class="flex items-center justify-between pb-4 border-b border-zinc-700">
        <div class="flex items-center gap-2">
          <span class="w-2.5 h-2.5 rounded-full bg-secondary-container"></span>
          <h3 id="inst-title" class="font-headline-sm uppercase text-white font-bold text-lg">Screen Instructions</h3>
        </div>
        <button onclick="closeInstructions()" class="w-7 h-7 rounded-full bg-zinc-800 text-zinc-300 flex items-center justify-center hover:bg-zinc-700">
          <span class="material-symbols-outlined text-[18px]">close</span>
        </button>
      </div>

      <div class="mt-4 space-y-4 text-sm">
        <div>
          <span class="text-secondary-container font-label-tag text-xs font-bold uppercase tracking-wider block mb-1">SCENARIO & CONTEXT</span>
          <p id="inst-desc" class="text-zinc-300 leading-relaxed font-body-sm"></p>
        </div>

        <div>
          <span class="text-secondary-container font-label-tag text-xs font-bold uppercase tracking-wider block mb-1">INTERACTION TEST GUIDE</span>
          <p id="inst-guide" class="text-zinc-300 leading-relaxed font-body-sm"></p>
        </div>

        <div class="p-3 rounded-xl bg-zinc-900 border border-zinc-800">
          <span class="text-outline text-[11px] font-mono uppercase tracking-wider block mb-1">DESIGN TOKENS</span>
          <div class="flex flex-wrap gap-2 text-xs">
            <span class="px-2 py-0.5 rounded bg-zinc-800 text-zinc-300 font-mono">Barlow Condensed</span>
            <span class="px-2 py-0.5 rounded bg-zinc-800 text-zinc-300 font-mono">Inter</span>
            <span class="px-2 py-0.5 rounded bg-zinc-800 text-[#22d66f] font-mono">#22D66F (Signal Green)</span>
            <span class="px-2 py-0.5 rounded bg-zinc-800 text-zinc-300 font-mono">#121212 (Near Black)</span>
            <span class="px-2 py-0.5 rounded bg-zinc-800 text-zinc-300 font-mono">390x844px Mobile Base</span>
          </div>
        </div>

        <div class="pt-2 flex gap-2">
          <button onclick="closeInstructions(); nextScreen();" class="flex-1 py-2.5 rounded-full bg-secondary-container hover:bg-[#4be684] text-primary font-bold text-xs uppercase transition-all">
            Continue To Next Screen →
          </button>
        </div>
      </div>
    </div>
  </div>

  <!-- Toast Notification -->
  <div id="app-toast"></div>

  <!-- Master JavaScript Application Runtime -->
  <script>
    // Screen Registry
    const SCREENS_DATA = {screens_json};
    
    let currentScreen = 1;
    let isNativeMobile = false;

    // Toast Helper
    function showToast(msg) {{
      const toast = document.getElementById('app-toast');
      toast.textContent = msg;
      toast.classList.add('show');
      setTimeout(() => toast.classList.remove('show'), 2200);
    }}

    // Real-time Status Clock
    function updateClock() {{
      const now = new Date();
      const hrs = String(now.getHours()).padStart(2, '0');
      const mins = String(now.getMinutes()).padStart(2, '0');
      const el = document.getElementById('status-time');
      if (el) el.textContent = `${{hrs}}:${{mins}}`;
    }}
    setInterval(updateClock, 10000);
    updateClock();

    // Screen Navigation Engine
    function goToScreen(targetNum) {{
      targetNum = parseInt(targetNum, 10);
      if (targetNum < 1 || targetNum > 38 || targetNum === currentScreen) return;

      const prevEl = document.getElementById(`screen-view-${{currentScreen}}`);
      const nextEl = document.getElementById(`screen-view-${{targetNum}}`);
      if (!nextEl) return;

      if (prevEl) prevEl.classList.remove('active');
      nextEl.classList.add('active');

      currentScreen = targetNum;

      // Scroll phone container to top
      const screenContainer = document.getElementById('phone-screen');
      if (screenContainer) screenContainer.scrollTop = 0;

      // Update Top Badge and Master Dock UI
      updateDockUI();

      // Close modal drawers if open
      closeDrawer();
      closeInstructions();

      // Broadcast event for screen micro-interactions
      window.dispatchEvent(new CustomEvent('screenChanged', {{ detail: {{ screen: currentScreen }} }}));
    }}

    function nextScreen() {{
      const meta = SCREENS_DATA[currentScreen];
      if (meta && meta.default_next) {{
        goToScreen(meta.default_next);
      }} else {{
        goToScreen((currentScreen % 38) + 1);
      }}
    }}

    function prevScreen() {{
      const meta = SCREENS_DATA[currentScreen];
      if (meta && meta.default_prev) {{
        goToScreen(meta.default_prev);
      }} else {{
        goToScreen(currentScreen === 1 ? 38 : currentScreen - 1);
      }}
    }}

    function updateDockUI() {{
      const meta = SCREENS_DATA[currentScreen];
      if (!meta) return;

      const numStr = String(currentScreen).padStart(2, '0');
      document.getElementById('dock-screen-num').textContent = `${{numStr}}/38`;
      document.getElementById('dock-screen-title').textContent = meta.title;
      document.getElementById('dock-screen-phase').textContent = meta.phase;
      document.getElementById('top-screen-badge').textContent = `${{numStr}} · ${{meta.title}}`;

      // Update instructions drawer content
      document.getElementById('inst-title').textContent = `[${{numStr}}] ${{meta.title}}`;
      document.getElementById('inst-desc').textContent = meta.description;
      document.getElementById('inst-guide').textContent = meta.instructions;
    }}

    // Toggle Mobile Frame vs Full Screen
    function toggleNativeMobile() {{
      isNativeMobile = !isNativeMobile;
      document.body.classList.toggle('native-mobile', isNativeMobile);
      const btnText = document.getElementById('frame-btn-text');
      btnText.textContent = isNativeMobile ? 'Full Responsive' : 'Mobile Frame';
      showToast(isNativeMobile ? 'Full Responsive Viewport' : 'iPhone 16 Pro Frame');
    }}

    // Zoom Controls for Desktop Preview
    function setZoom(scale) {{
      const mockup = document.getElementById('phone-container');
      if (mockup && !isNativeMobile) {{
        mockup.style.transform = `scale(${{scale}})`;
      }}
    }}

    // Modal Drawer Controls
    function openScreensDrawer() {{
      document.getElementById('drawer-overlay').classList.add('open');
    }}
    function closeDrawer(e) {{
      if (e && e.target !== document.getElementById('drawer-overlay')) return;
      document.getElementById('drawer-overlay').classList.remove('open');
    }}

    function openInstructions() {{
      updateDockUI();
      document.getElementById('instructions-overlay').classList.add('open');
    }}
    function closeInstructions(e) {{
      if (e && e.target !== document.getElementById('instructions-overlay')) return;
      document.getElementById('instructions-overlay').classList.remove('open');
    }}

    // Keyboard Shortcuts
    document.addEventListener('keydown', (e) => {{
      if (e.key === 'ArrowRight') nextScreen();
      else if (e.key === 'ArrowLeft') prevScreen();
      else if (e.key === 'Escape') {{ closeDrawer(); closeInstructions(); }}
      else if (e.key === 'm' || e.key === 'M') {{
        if (!['INPUT', 'TEXTAREA'].includes(document.activeElement.tagName)) toggleNativeMobile();
      }}
    }});

// =========================================================================
    // GLOBAL APP STATE & LIVE STORE
    // =========================================================================
    window.LiveStore = {
      user: { name: 'Aarav', avatar: 'A', upi: 'aarav@okaxis', phone: '+91 98765 43210' },
      flat: { code: 'FLAT402', name: 'Flat 402', campus: 'IIT Bombay · Hostel 14', pool: 450 },
      cart: {
        name: 'Sunday Restock',
        store: 'Blinkit',
        timerSeconds: 252, // 04:12
        splitMode: 'equal', // 'equal', 'personal', 'prorated'
        tip: 0,
        slot: '6 PM TODAY',
        items: [
          { id: 1, name: 'India Gate Basmati Rice 5kg', qty: 1, unitPrice: 540, split: 'shared', by: 'Aarav' },
          { id: 2, name: 'Amul Taaza Milk 500ml (x4)', qty: 4, unitPrice: 30, split: 'shared', by: 'Maya' },
          { id: 3, name: 'Farm Fresh Brown Eggs 30pk', qty: 1, unitPrice: 210, split: 'shared', by: 'Kabir' },
          { id: 4, name: 'Lays Gourmet Lime Chips (x2)', qty: 2, unitPrice: 50, split: 'personal', by: 'Zoya' },
          { id: 5, name: 'Diet Coke 300ml Cans (x6)', qty: 6, unitPrice: 40, split: 'personal', by: 'Aarav' },
          { id: 6, name: 'Fortune Sunflower Oil 1L', qty: 1, unitPrice: 158, split: 'shared', by: 'Maya' }
        ],
        deliveryFee: 60,
        platformFee: 5
      },
      roommates: [
        { name: 'Aarav', avatar: 'A', status: 'paid', amount: 342, pct: 25 },
        { name: 'Maya', avatar: 'M', status: 'paid', amount: 342, pct: 25 },
        { name: 'Kabir', avatar: 'K', status: 'pending', amount: 342, pct: 25 },
        { name: 'Zoya', avatar: 'Z', status: 'short', amount: 222, deficit: 120, pct: 25 }
      ],
      soundEnabled: true
    };

    // Calculate cart totals
    window.calcCartTotal = function() {
      let subtotal = 0;
      window.LiveStore.cart.items.forEach(item => {
        subtotal += (item.qty * item.unitPrice);
      });
      const grandTotal = subtotal + window.LiveStore.cart.deliveryFee + window.LiveStore.cart.platformFee + window.LiveStore.cart.tip;
      const yourShare = Math.round(grandTotal / 4);
      return { subtotal, grandTotal, yourShare };
    };

    // =========================================================================
    // HAPTIC & TACTILE AUDIO SYNTHESIZER (Web Audio API)
    // =========================================================================
    let audioContext = null;
    function getAudioContext() {
      if (!audioContext) {
        try {
          audioContext = new (window.AudioContext || window.webkitAudioContext)();
        } catch(e) {}
      }
      return audioContext;
    }

    function playTactileFeedback(type = 'click') {
      // 1. Mobile Vibration API
      if (window.navigator && window.navigator.vibrate) {
        try { window.navigator.vibrate(type === 'success' ? [15, 40, 15] : 12); } catch(e) {}
      }
      // 2. Synthesized Audio Click
      if (!window.LiveStore.soundEnabled) return;
      try {
        const ctx = getAudioContext();
        if (!ctx) return;
        if (ctx.state === 'suspended') ctx.resume();

        const osc = ctx.createOscillator();
        const gain = ctx.createGain();
        osc.connect(gain);
        gain.connect(ctx.destination);

        const now = ctx.currentTime;
        if (type === 'click') {
          osc.frequency.setValueAtTime(900, now);
          osc.frequency.exponentialRampToValueAtTime(350, now + 0.035);
          gain.gain.setValueAtTime(0.09, now);
          gain.gain.linearRampToValueAtTime(0.001, now + 0.035);
          osc.start(now);
          osc.stop(now + 0.035);
        } else if (type === 'success') {
          osc.frequency.setValueAtTime(523.25, now);
          osc.frequency.setValueAtTime(659.25, now + 0.06);
          osc.frequency.setValueAtTime(783.99, now + 0.12);
          gain.gain.setValueAtTime(0.08, now);
          gain.gain.linearRampToValueAtTime(0.001, now + 0.22);
          osc.start(now);
          osc.stop(now + 0.22);
        } else if (type === 'nudge') {
          osc.frequency.setValueAtTime(440, now);
          osc.frequency.exponentialRampToValueAtTime(880, now + 0.08);
          gain.gain.setValueAtTime(0.12, now);
          gain.gain.linearRampToValueAtTime(0.001, now + 0.08);
          osc.start(now);
          osc.stop(now + 0.08);
        }
      } catch(e) {}
    }

    // Toggle Sound Button
    window.toggleSound = function() {
      window.LiveStore.soundEnabled = !window.LiveStore.soundEnabled;
      showToast(window.LiveStore.soundEnabled ? 'Sound & Haptics: ON 🔔' : 'Sound & Haptics: Muted 🔕');
      const soundBtn = document.getElementById('sound-toggle-btn');
      if (soundBtn) {
        soundBtn.innerHTML = window.LiveStore.soundEnabled ? 
          '<span class="material-symbols-outlined text-[16px]">volume_up</span>' : 
          '<span class="material-symbols-outlined text-[16px] text-zinc-500">volume_off</span>';
      }
    };

    // =========================================================================
    // COMPREHENSIVE INTERACTIVE ELEMENT WIRING (ALL 38 SCREENS)
    // =========================================================================
    function wireInteractiveNavigation() {
      // Global click handler for tactile button push
      document.querySelectorAll('button, a, input[type="button"], .interactive-pill').forEach(el => {
        el.addEventListener('mousedown', () => { el.style.transform = 'scale(0.97)'; });
        el.addEventListener('mouseup', () => { el.style.transform = 'scale(1)'; });
        el.addEventListener('mouseleave', () => { el.style.transform = 'scale(1)'; });
        el.addEventListener('click', () => { playTactileFeedback('click'); });
      });

      // 1. Wire Bottom Navigation Bars across all screens
      document.querySelectorAll('[data-path]').forEach(link => {
        link.addEventListener('click', (e) => {
          e.preventDefault();
          const path = link.getAttribute('data-path');
          if (path === 'carts') goToScreen(7);
          else if (path === 'orders') goToScreen(36);
          else if (path === 'ledger') goToScreen(37);
          else if (path === 'flat') goToScreen(9);
        });
      });

      // 2. Wire Back Chevrons / arrow_back
      document.querySelectorAll('.screen-view button, .screen-view a').forEach(btn => {
        const text = btn.textContent.trim();
        const hasBackIcon = btn.querySelector('.material-symbols-outlined')?.textContent.trim() === 'arrow_back';
        if (text === 'arrow_back' || hasBackIcon || btn.getAttribute('data-back')) {
          btn.addEventListener('click', (e) => {
            e.preventDefault();
            prevScreen();
          });
        }
      });

      // 3. Screen-Specific Live Handlers
      
      // SCREEN 01: Splash & Value Proposition
      const s1 = document.getElementById('screen-view-1');
      if (s1) {
        s1.querySelectorAll('button, a').forEach(btn => {
          const txt = btn.textContent.trim().toUpperCase();
          if (txt.includes('GET STARTED') || txt.includes('I HAVE AN ACCOUNT')) {
            btn.addEventListener('click', () => goToScreen(2));
          }
        });
        // Interactive order split topology diagram nodes
        s1.querySelectorAll('.rounded-full').forEach(node => {
          node.style.cursor = 'pointer';
          node.addEventListener('click', () => {
            showToast('Auto-settlement Topology: Instant peer-to-peer UPI split');
          });
        });
      }

      // SCREEN 02: Phone & OTP Verification
      const s2 = document.getElementById('screen-view-2');
      if (s2) {
        const phoneInput = s2.querySelector('input[type="tel"]') || s2.querySelector('input');
        if (phoneInput) {
          phoneInput.removeAttribute('readonly');
          phoneInput.removeAttribute('disabled');
        }
        // OTP input boxes auto-advance
        const otpInputs = s2.querySelectorAll('input');
        otpInputs.forEach((inp, idx) => {
          inp.addEventListener('input', (e) => {
            if (inp.value.length === 1 && idx < otpInputs.length - 1) {
              otpInputs[idx + 1].focus();
            }
          });
          inp.addEventListener('keydown', (e) => {
            if (e.key === 'Backspace' && !inp.value && idx > 0) {
              otpInputs[idx - 1].focus();
            }
          });
        });
        // Resend Timer
        let resendSecs = 28;
        const resendBtn = Array.from(s2.querySelectorAll('button')).find(b => b.textContent.includes('RESEND') || b.textContent.includes('Resend') || b.textContent.includes('EDIT'));
        if (resendBtn) {
          const timerInterval = setInterval(() => {
            if (resendSecs > 0) {
              resendSecs--;
              if (resendBtn.textContent.includes('s') || resendBtn.textContent.includes('0:')) {
                resendBtn.textContent = `RESEND OTP (0:${resendSecs < 10 ? '0' : ''}${resendSecs})`;
              }
            } else {
              resendBtn.textContent = 'RESEND OTP NOW';
              resendBtn.classList.add('text-secondary');
              clearInterval(timerInterval);
            }
          }, 1000);
          resendBtn.addEventListener('click', () => {
            showToast('New 6-digit OTP sent to +91 98765 43210: 402402');
            otpInputs.forEach(i => i.value = '4');
          });
        }
        // Verify Button
        s2.querySelectorAll('button').forEach(btn => {
          if (btn.textContent.trim().toUpperCase().includes('VERIFY')) {
            btn.addEventListener('click', () => {
              playTactileFeedback('success');
              showToast('Phone verified: +91 98765 43210 ✓');
              goToScreen(3);
            });
          }
        });
      }

      // SCREEN 03: Profile Setup (Name & Avatar Token)
      const s3 = document.getElementById('screen-view-3');
      if (s3) {
        const nameInput = s3.querySelector('input');
        if (nameInput) {
          nameInput.value = window.LiveStore.user.name;
          nameInput.addEventListener('input', (e) => {
            window.LiveStore.user.name = e.target.value.trim() || 'Aarav';
          });
        }
        // Avatar tokens (A, M, K, Z)
        const avatarBtns = s3.querySelectorAll('button');
        avatarBtns.forEach(btn => {
          const t = btn.textContent.trim();
          if (['A', 'M', 'K', 'Z'].includes(t)) {
            btn.addEventListener('click', () => {
              avatarBtns.forEach(b => b.classList.remove('ring-4', 'ring-secondary-container', 'scale-110'));
              btn.classList.add('ring-4', 'ring-secondary-container', 'scale-110');
              window.LiveStore.user.avatar = t;
              showToast(`Avatar token '${t}' selected!`);
            });
          }
          if (btn.textContent.trim().toUpperCase().includes('CONTINUE')) {
            btn.addEventListener('click', () => goToScreen(4));
          }
        });
      }

      // SCREEN 04: Campus & Hostel Locator
      const s4 = document.getElementById('screen-view-4');
      if (s4) {
        const campusChips = s4.querySelectorAll('.rounded-full, .rounded-xl, button');
        campusChips.forEach(chip => {
          const txt = chip.textContent.trim();
          if (txt.includes('Hostel') || txt.includes('Campus') || txt.includes('IIT') || txt.includes('Powai')) {
            chip.style.cursor = 'pointer';
            chip.addEventListener('click', () => {
              campusChips.forEach(c => c.classList.remove('bg-secondary-container', 'text-on-secondary-container', 'font-bold'));
              chip.classList.add('bg-secondary-container', 'text-on-secondary-container', 'font-bold');
              window.LiveStore.flat.campus = txt;
              showToast(`Location set: ${txt}`);
            });
          }
          if (txt.toUpperCase().includes('CONTINUE')) {
            chip.addEventListener('click', () => goToScreen(5));
          }
        });
      }

      // SCREEN 05: Create or Join Flat
      const s5 = document.getElementById('screen-view-5');
      if (s5) {
        const codeInput = s5.querySelector('input');
        if (codeInput) codeInput.value = 'FLAT402';
        s5.querySelectorAll('button').forEach(btn => {
          const txt = btn.textContent.trim().toUpperCase();
          if (txt.includes('PASTE') || txt.includes('CONTENT_PASTE')) {
            btn.addEventListener('click', () => {
              if (codeInput) codeInput.value = 'FLAT402';
              showToast('Flat code pasted: FLAT402');
            });
          }
          if (txt.includes('CREATE') || txt.includes('JOIN')) {
            btn.addEventListener('click', () => {
              playTactileFeedback('success');
              showToast('Joined Flat 402! Roommates: Aarav, Maya, Kabir, Zoya');
              goToScreen(6);
            });
          }
        });
      }

      // SCREEN 06: Link UPI & Permissions
      const s6 = document.getElementById('screen-view-6');
      if (s6) {
        const upiOptions = s6.querySelectorAll('button, .rounded-xl');
        upiOptions.forEach(opt => {
          const t = opt.textContent.toUpperCase();
          if (t.includes('GPAY') || t.includes('PHONEPE') || t.includes('PAYTM') || t.includes('CRED')) {
            opt.style.cursor = 'pointer';
            opt.addEventListener('click', () => {
              upiOptions.forEach(o => o.classList.remove('border-secondary', 'bg-secondary-container/20'));
              opt.classList.add('border-secondary', 'bg-secondary-container/20');
              showToast(`Primary UPI linked: ${t.split(' ')[0]}`);
            });
          }
          if (t.includes('CONFIRM') || t.includes('GO TO FLAT') || t.includes('DONE')) {
            opt.addEventListener('click', () => {
              playTactileFeedback('success');
              goToScreen(7);
            });
          }
        });
      }

      // SCREEN 07: Home Open Carts
      const s7 = document.getElementById('screen-view-7');
      if (s7) {
        s7.querySelectorAll('button, a, div').forEach(el => {
          const txt = el.textContent.trim().toUpperCase();
          if (txt.includes('NEW CART') || txt.includes('+ NEW CART')) {
            el.addEventListener('click', () => goToScreen(11));
          } else if (txt.includes('BLINKIT') || txt.includes('SUNDAY RESTOCK') || txt.includes('PLACE ORDER')) {
            el.addEventListener('click', () => goToScreen(16));
          }
        });
        // Offline strip toggle
        const offlineStrip = s7.querySelector('.bg-\[\#121212\]');
        if (offlineStrip) {
          offlineStrip.style.cursor = 'pointer';
          offlineStrip.addEventListener('click', () => {
            offlineStrip.innerHTML = '<span class="w-1.5 h-1.5 rounded-full bg-emerald-400"></span>ONLINE · SYNCED WITH FLAT 402';
            showToast('All roommate carts synced in real time!');
          });
        }
      }

      // SCREEN 08: Home Empty State
      const s8 = document.getElementById('screen-view-8');
      if (s8) {
        s8.querySelectorAll('button').forEach(btn => {
          const t = btn.textContent.trim().toUpperCase();
          if (t.includes('NEW CART') || t.includes('QUICK START')) {
            btn.addEventListener('click', () => goToScreen(11));
          }
        });
      }

      // SCREEN 09: Flat Members & Settings
      const s9 = document.getElementById('screen-view-9');
      if (s9) {
        s9.querySelectorAll('button').forEach(btn => {
          const t = btn.textContent.trim().toUpperCase();
          if (t.includes('LEAVE')) {
            btn.addEventListener('click', () => showToast('Leaving flat requires settling all ledger debts first!'));
          } else if (t.includes('REMOVE')) {
            btn.addEventListener('click', () => showToast('Only Flat Admin (Aarav) can modify roommates.'));
          } else if (t.includes('INVITE') || t.includes('SHARE')) {
            btn.addEventListener('click', () => goToScreen(12));
          }
        });
      }

      // SCREEN 10: Activity & Notifications Feed
      const s10 = document.getElementById('screen-view-10');
      if (s10) {
        const tabs = s10.querySelectorAll('button');
        tabs.forEach(tab => {
          const t = tab.textContent.trim().toUpperCase();
          if (['ALL', 'UNREAD', 'PAYMENTS'].some(k => t.includes(k))) {
            tab.addEventListener('click', () => {
              tabs.forEach(b => {
                b.classList.remove('bg-primary', 'text-on-primary', 'bg-black', 'text-white');
                b.classList.add('bg-surface-container', 'text-on-surface');
              });
              tab.classList.add('bg-primary', 'text-on-primary');
              showToast(`Feed filter: ${t}`);
            });
          }
        });
      }

      // SCREEN 11: Start New Shared Cart
      const s11 = document.getElementById('screen-view-11');
      if (s11) {
        const storeBtns = s11.querySelectorAll('button');
        storeBtns.forEach(btn => {
          const t = btn.textContent.trim().toUpperCase();
          if (t.includes('BLINKIT') || t.includes('ZEPTO') || t.includes('INSTAMART')) {
            btn.addEventListener('click', () => {
              storeBtns.forEach(b => b.classList.remove('ring-2', 'ring-secondary'));
              btn.classList.add('ring-2', 'ring-secondary');
              window.LiveStore.cart.store = t.split(' ')[0];
              showToast(`Store selected: ${window.LiveStore.cart.store}`);
            });
          }
          if (t.includes('START') || t.includes('NEXT') || t.includes('CREATE')) {
            btn.addEventListener('click', () => goToScreen(12));
          }
        });
      }

      // SCREEN 12: Invite Roommates
      const s12 = document.getElementById('screen-view-12');
      if (s12) {
        s12.querySelectorAll('button').forEach(btn => {
          const t = btn.textContent.trim().toUpperCase();
          if (t.includes('COPY') || t.includes('COPY LINK')) {
            btn.addEventListener('click', () => {
              playTactileFeedback('success');
              btn.innerHTML = '<span class="material-symbols-outlined text-sm">check</span> COPIED! ✓';
              showToast('Link copied: https://roommatecart.in/c/flat402');
              setTimeout(() => { btn.textContent = 'COPY LINK'; }, 2000);
            });
          }
          if (t.includes('START') || t.includes('SHOPPING') || t.includes('BROWSE')) {
            btn.addEventListener('click', () => goToScreen(13));
          }
        });
      }

      // SCREEN 13: Store Browse
      const s13 = document.getElementById('screen-view-13');
      if (s13) {
        s13.querySelectorAll('button').forEach(btn => {
          const t = btn.textContent.trim().toUpperCase();
          if (t === '+ ADD' || t.includes('ADD')) {
            btn.addEventListener('click', (e) => {
              e.stopPropagation();
              playTactileFeedback('success');
              btn.textContent = 'ADDED ✓';
              btn.classList.add('bg-secondary', 'text-white');
              showToast('Item added to collective flat cart! (₹540)');
              setTimeout(() => { btn.textContent = '+ ADD'; }, 1500);
            });
          }
        });
        // Clicking product items opens sheet (15)
        s13.querySelectorAll('.product-card, [class*="product"], [class*="item"]').forEach(card => {
          if (card.textContent.includes('₹')) {
            card.style.cursor = 'pointer';
            card.addEventListener('click', () => goToScreen(15));
          }
        });
        // Cart bar goes to 16
        const cartBar = s13.querySelector('.fixed.bottom-0, [class*="cart-bar"]');
        if (cartBar) {
          cartBar.style.cursor = 'pointer';
          cartBar.addEventListener('click', () => goToScreen(16));
        }
      }

      // SCREEN 14: Search Results
      const s14 = document.getElementById('screen-view-14');
      if (s14) {
        const searchInput = s14.querySelector('input');
        if (searchInput) searchInput.value = 'Basmati Rice';
        s14.querySelectorAll('button').forEach(btn => {
          const t = btn.textContent.trim().toUpperCase();
          if (t.includes('ADD')) {
            btn.addEventListener('click', () => {
              playTactileFeedback('success');
              showToast('Basmati Rice added to cart! (+₹540)');
              goToScreen(15);
            });
          }
          if (t.includes('VIEW CART')) {
            btn.addEventListener('click', () => goToScreen(16));
          }
        });
      }

      // SCREEN 15: Item Detail & Ownership Sheet
      const s15 = document.getElementById('screen-view-15');
      if (s15) {
        let itemQty = 1;
        const qtyDisplay = Array.from(s15.querySelectorAll('span, div')).find(el => el.textContent.trim() === '1');
        const priceDisplay = Array.from(s15.querySelectorAll('span, h2, h3')).find(el => el.textContent.includes('540'));
        s15.querySelectorAll('button').forEach(btn => {
          const t = btn.textContent.trim();
          if (t === 'add' || t === '+') {
            btn.addEventListener('click', () => {
              itemQty++;
              if (qtyDisplay) qtyDisplay.textContent = itemQty;
              if (priceDisplay) priceDisplay.textContent = `₹${itemQty * 540}`;
              playTactileFeedback('click');
            });
          } else if (t === 'remove' || t === '-') {
            btn.addEventListener('click', () => {
              if (itemQty > 1) {
                itemQty--;
                if (qtyDisplay) qtyDisplay.textContent = itemQty;
                if (priceDisplay) priceDisplay.textContent = `₹${itemQty * 540}`;
                playTactileFeedback('click');
              }
            });
          } else if (t.toUpperCase().includes('ADD TO CART') || t.toUpperCase().includes('CONFIRM')) {
            btn.addEventListener('click', () => {
              playTactileFeedback('success');
              showToast(`Added ${itemQty}x Basmati Rice (₹${itemQty * 540}) to shared cart!`);
              goToScreen(16);
            });
          }
        });
      }

      // SCREEN 16: Shared Cart View
      const s16 = document.getElementById('screen-view-16');
      if (s16) {
        // Ticking countdown timer
        let timerSeconds = 252;
        const timerEls = Array.from(s16.querySelectorAll('span, div')).filter(el => el.textContent.includes('04:12') || el.textContent.includes('04:'));
        setInterval(() => {
          if (timerSeconds > 0) {
            timerSeconds--;
            const m = String(Math.floor(timerSeconds / 60)).padStart(2, '0');
            const s = String(timerSeconds % 60).padStart(2, '0');
            timerEls.forEach(el => { el.textContent = `${m}:${s}`; });
          }
        }, 1000);
        // Lock Cart button
        s16.querySelectorAll('button').forEach(btn => {
          const t = btn.textContent.trim().toUpperCase();
          if (t.includes('LOCK CART') || t.includes('READY') || t.includes('CHECKOUT')) {
            btn.addEventListener('click', () => {
              playTactileFeedback('success');
              goToScreen(17);
            });
          } else if (t.includes('ADD AN ITEM') || t.includes('+ ADD')) {
            btn.addEventListener('click', () => goToScreen(13));
          }
        });
      }

      // SCREEN 17: Ownership Split Mode
      const s17 = document.getElementById('screen-view-17');
      if (s17) {
        const modeCards = s17.querySelectorAll('button, .rounded-2xl, .rounded-xl');
        let selectedMode = 'prorated';
        modeCards.forEach(card => {
          const txt = card.textContent.toUpperCase();
          if (txt.includes('EQUAL') || txt.includes('PERSONAL') || txt.includes('PRORATED')) {
            card.style.cursor = 'pointer';
            card.addEventListener('click', () => {
              modeCards.forEach(c => c.classList.remove('border-secondary', 'bg-secondary-container/15', 'ring-2', 'ring-secondary'));
              card.classList.add('border-secondary', 'bg-secondary-container/15', 'ring-2', 'ring-secondary');
              selectedMode = txt.includes('EQUAL') ? 'equal' : (txt.includes('PERSONAL') ? 'personal' : 'prorated');
              showToast(`Split Mode: ${selectedMode.toUpperCase()}`);
            });
          }
          if (txt.includes('CONFIRM')) {
            card.addEventListener('click', () => {
              goToScreen(selectedMode === 'prorated' ? 18 : 19);
            });
          }
        });
      }

      // SCREEN 18: Prorated Share Sliders
      const s18 = document.getElementById('screen-view-18');
      if (s18) {
        const sliders = s18.querySelectorAll('input[type="range"]');
        sliders.forEach(slider => {
          slider.addEventListener('input', (e) => {
            const val = e.target.value;
            const parent = slider.closest('.flex') || slider.parentElement;
            const pctDisplay = parent?.querySelector('.font-headline-sm, .font-bold');
            if (pctDisplay) pctDisplay.textContent = `${val}%`;
          });
        });
        s18.querySelectorAll('button').forEach(btn => {
          if (btn.textContent.trim().toUpperCase().includes('CONFIRM')) {
            btn.addEventListener('click', () => {
              playTactileFeedback('success');
              showToast('Prorated shares confirmed!');
              goToScreen(19);
            });
          }
        });
      }

      // SCREEN 19: Checkout Summary
      const s19 = document.getElementById('screen-view-19');
      if (s19) {
        // Slot selector chips
        s19.querySelectorAll('button').forEach(btn => {
          const t = btn.textContent.trim().toUpperCase();
          if (t.includes('TODAY') || t.includes('PM') || t.includes('SLOT')) {
            btn.addEventListener('click', () => {
              showToast(`Delivery slot chosen: ${t}`);
            });
          }
          if (t.includes('PAY') || t.includes('PROCEED') || t.includes('CONFIRM')) {
            btn.addEventListener('click', () => goToScreen(20));
          }
        });
      }

      // SCREEN 20: Your Share (₹342 Due)
      const s20 = document.getElementById('screen-view-20');
      if (s20) {
        s20.querySelectorAll('button').forEach(btn => {
          const t = btn.textContent.trim().toUpperCase();
          if (t.includes('GPAY') || t.includes('PHONEPE') || t.includes('PAY') || t.includes('INSTANT')) {
            btn.addEventListener('click', () => {
              playTactileFeedback('click');
              goToScreen(21);
              // Simulated 2.5s UPI handoff animation
              setTimeout(() => {
                if (currentScreen === 21) {
                  playTactileFeedback('success');
                  goToScreen(22);
                }
              }, 2600);
            });
          }
        });
      }

      // SCREEN 21: UPI Handoff Sheet
      const s21 = document.getElementById('screen-view-21');
      if (s21) {
        s21.style.cursor = 'pointer';
        s21.addEventListener('click', () => {
          playTactileFeedback('success');
          goToScreen(22);
        });
      }

      // SCREEN 22: Payment Success Receipt
      const s22 = document.getElementById('screen-view-22');
      if (s22) {
        s22.querySelectorAll('button, a').forEach(btn => {
          const t = btn.textContent.trim().toUpperCase();
          if (t.includes('VIEW PAYMENT STATUS') || t.includes('STATUS')) {
            btn.addEventListener('click', () => goToScreen(25));
          } else if (t.includes('SPOT HER') || t.includes('SPOT')) {
            btn.addEventListener('click', () => goToScreen(26));
          } else if (t.includes('COPY') || t.includes('UPI/')) {
            btn.addEventListener('click', () => {
              playTactileFeedback('success');
              showToast('UPI Ref ID copied: UPI/409283719284 ✓');
            });
          }
        });
      }

      // SCREEN 23: Payment Failed State
      const s23 = document.getElementById('screen-view-23');
      if (s23) {
        s23.querySelectorAll('button').forEach(btn => {
          const t = btn.textContent.trim().toUpperCase();
          if (t.includes('TRY AGAIN')) btn.addEventListener('click', () => goToScreen(21));
          else if (t.includes('SPOT ME')) btn.addEventListener('click', () => goToScreen(27));
        });
      }

      // SCREEN 24: Timer Expired
      const s24 = document.getElementById('screen-view-24');
      if (s24) {
        s24.querySelectorAll('button').forEach(btn => {
          const t = btn.textContent.trim().toUpperCase();
          if (t.includes('REVIVE')) btn.addEventListener('click', () => goToScreen(32));
          else if (t.includes('POOL') || t.includes('CREDIT')) btn.addEventListener('click', () => goToScreen(28));
        });
      }

      // SCREEN 25: Roommate Payment Status (2 of 4 Paid)
      const s25 = document.getElementById('screen-view-25');
      if (s25) {
        s25.querySelectorAll('button, a, div').forEach(el => {
          const t = el.textContent.trim().toUpperCase();
          if (t.includes('NUDGE UNPAID') || t.includes('NUDGE')) {
            el.addEventListener('click', () => {
              playTactileFeedback('nudge');
              el.textContent = 'NUDGED! ✓';
              el.classList.add('bg-secondary', 'text-white');
              showToast('WhatsApp ping sent to Kabir and Zoya!');
              setTimeout(() => { el.textContent = 'NUDGE UNPAID (2) bolt'; }, 2000);
            });
          } else if (t.includes('ZOYA') || t.includes('SHORT') || t.includes('DEFICIT')) {
            el.style.cursor = 'pointer';
            el.addEventListener('click', () => goToScreen(26));
          } else if (t.includes('LEDGER') || t.includes('VIEW FLAT LEDGER')) {
            el.addEventListener('click', () => goToScreen(37));
          }
        });
      }

      // SCREEN 26: Zoya Is Short
      const s26 = document.getElementById('screen-view-26');
      if (s26) {
        const cards = s26.querySelectorAll('.rounded-2xl, .rounded-xl, button');
        let resolution = 'spot';
        cards.forEach(card => {
          const txt = card.textContent.toUpperCase();
          if (txt.includes('SPOT ME') || txt.includes('ROOM POOL') || txt.includes('DROP')) {
            card.style.cursor = 'pointer';
            card.addEventListener('click', () => {
              cards.forEach(c => c.classList.remove('border-secondary', 'ring-2', 'ring-secondary'));
              card.classList.add('border-secondary', 'ring-2', 'ring-secondary');
              if (txt.includes('SPOT')) resolution = 'spot';
              else if (txt.includes('POOL')) resolution = 'pool';
              else if (txt.includes('DROP')) resolution = 'drop';
              showToast(`Resolution chosen: ${resolution.toUpperCase()}`);
            });
          }
        });
        s26.querySelectorAll('button').forEach(btn => {
          const t = btn.textContent.trim().toUpperCase();
          if (t.includes('CONFIRM') || t.includes('CONTINUE')) {
            btn.addEventListener('click', () => {
              if (resolution === 'spot') goToScreen(27);
              else if (resolution === 'pool') goToScreen(28);
              else if (resolution === 'drop') goToScreen(29);
            });
          }
        });
      }

      // SCREEN 27: Spot Me Approval
      const s27 = document.getElementById('screen-view-27');
      if (s27) {
        s27.querySelectorAll('button').forEach(btn => {
          const t = btn.textContent.trim().toUpperCase();
          if (t.includes('MONTH') || t.includes('FRIDAY')) {
            btn.addEventListener('click', () => showToast(`Repayment scheduled: ${t}`));
          }
          if (t.includes('CONFIRM') || t.includes('APPROVE') || t.includes('SPOT')) {
            btn.addEventListener('click', () => {
              playTactileFeedback('success');
              showToast('₹120 Spot-Me recorded in Flat Ledger!');
              goToScreen(22);
            });
          }
        });
      }

      // SCREEN 28: Room Pool
      const s28 = document.getElementById('screen-view-28');
      if (s28) {
        let poolDraw = 120;
        const poolDisplay = Array.from(s28.querySelectorAll('span, div')).find(el => el.textContent.includes('100') || el.textContent.includes('120'));
        s28.querySelectorAll('button').forEach(btn => {
          const t = btn.textContent.trim();
          if (t === 'add' || t === '+') {
            btn.addEventListener('click', () => {
              poolDraw += 10;
              if (poolDisplay) poolDisplay.textContent = `₹${poolDraw}`;
              playTactileFeedback('click');
            });
          } else if (t === 'remove' || t === '-') {
            btn.addEventListener('click', () => {
              if (poolDraw > 10) poolDraw -= 10;
              if (poolDisplay) poolDisplay.textContent = `₹${poolDraw}`;
              playTactileFeedback('click');
            });
          } else if (t.toUpperCase().includes('POOL') || t.toUpperCase().includes('COVER') || t.toUpperCase().includes('USE')) {
            btn.addEventListener('click', () => {
              playTactileFeedback('success');
              showToast(`₹${poolDraw} withdrawn from Flat 402 Petty Pool`);
              goToScreen(22);
            });
          }
        });
      }

      // SCREEN 29: Pay or Drop Items
      const s29 = document.getElementById('screen-view-29');
      if (s29) {
        s29.querySelectorAll('input[type="checkbox"]').forEach(cb => {
          cb.addEventListener('change', () => {
            showToast('Item status toggled');
          });
        });
        s29.querySelectorAll('button').forEach(btn => {
          const t = btn.textContent.trim().toUpperCase();
          if (t.includes('DROP') || t.includes('DISPATCH') || t.includes('CONFIRM')) {
            btn.addEventListener('click', () => {
              playTactileFeedback('success');
              showToast('Dropped non-essential items. Dispatching essential haul!');
              goToScreen(33);
            });
          }
        });
      }

      // SCREEN 30: Substitute Voting
      const s30 = document.getElementById('screen-view-30');
      if (s30) {
        s30.querySelectorAll('button').forEach(btn => {
          const t = btn.textContent.trim().toUpperCase();
          if (t.includes('VOTE') || t.includes('SUBSTITUTE') || t.includes('ACCEPT')) {
            btn.addEventListener('click', () => {
              playTactileFeedback('success');
              showToast('Vote cast: 3/4 Roommates approved substitution!');
              setTimeout(() => goToScreen(19), 600);
            });
          } else if (t.includes('DISCARD') || t.includes('CANCEL')) {
            btn.addEventListener('click', () => goToScreen(32));
          }
        });
      }

      // SCREEN 31: Surge Price Alert
      const s31 = document.getElementById('screen-view-31');
      if (s31) {
        s31.querySelectorAll('button').forEach(btn => {
          const t = btn.textContent.trim().toUpperCase();
          if (t.includes('ACCEPT') || t.includes('CONFIRM')) {
            btn.addEventListener('click', () => {
              showToast('Surge accepted (+₹24 split)');
              goToScreen(19);
            });
          } else if (t.includes('DROP')) {
            btn.addEventListener('click', () => {
              showToast('Surge items dropped');
              goToScreen(16);
            });
          }
        });
      }

      // SCREEN 32: Revive Expired Cart
      const s32 = document.getElementById('screen-view-32');
      if (s32) {
        s32.querySelectorAll('button').forEach(btn => {
          if (btn.textContent.trim().toUpperCase().includes('REVIVE')) {
            btn.addEventListener('click', () => {
              playTactileFeedback('success');
              btn.innerHTML = '<span class="material-symbols-outlined animate-spin text-sm">autorenew</span> RESTORING...';
              setTimeout(() => {
                showToast('Cart revived with fresh Blinkit inventory!');
                goToScreen(16);
              }, 800);
            });
          }
        });
      }

      // SCREEN 33: Live Order Tracking
      const s33 = document.getElementById('screen-view-33');
      if (s33) {
        s33.querySelectorAll('button').forEach(btn => {
          const t = btn.textContent.trim().toUpperCase();
          if (t.includes('COLLECT') || t.includes('GATE') || t.includes('DELIVERED')) {
            btn.addEventListener('click', () => goToScreen(34));
          } else if (t.includes('CALL') || t.includes('PHONE')) {
            btn.addEventListener('click', () => showToast('Calling Blinkit Rider Ramesh (+91 98200 12345)...'));
          }
        });
      }

      // SCREEN 34: Delivered & Unbox Confirmation
      const s34 = document.getElementById('screen-view-34');
      if (s34) {
        s34.querySelectorAll('input[type="checkbox"]').forEach(cb => {
          cb.addEventListener('change', () => {
            const row = cb.closest('div');
            if (row && cb.checked) {
              row.style.opacity = '0.6';
              row.style.textDecoration = 'line-through';
            } else if (row) {
              row.style.opacity = '1';
              row.style.textDecoration = 'none';
            }
          });
        });
        s34.querySelectorAll('button').forEach(btn => {
          const t = btn.textContent.trim().toUpperCase();
          if (t.includes('EVERYTHING') || t.includes('CONFIRM')) {
            btn.addEventListener('click', () => {
              playTactileFeedback('success');
              showToast('Haul verified & unboxed! Logged to history.');
              goToScreen(36);
            });
          } else if (t.includes('MISSING') || t.includes('ISSUE')) {
            btn.addEventListener('click', () => goToScreen(35));
          }
        });
      }

      // SCREEN 35: Report Missing / Damaged Items
      const s35 = document.getElementById('screen-view-35');
      if (s35) {
        s35.querySelectorAll('input[type="checkbox"]').forEach(cb => {
          cb.addEventListener('change', () => {
            showToast('Item flagged for instant refund');
          });
        });
        s35.querySelectorAll('button').forEach(btn => {
          if (btn.textContent.trim().toUpperCase().includes('SUBMIT') || btn.textContent.trim().toUpperCase().includes('REPORT')) {
            btn.addEventListener('click', () => {
              playTactileFeedback('success');
              showToast('₹70 refund credited automatically to Flat Ledger!');
              goToScreen(37);
            });
          }
        });
      }

      // SCREEN 36: Order History & Haul Receipts
      const s36 = document.getElementById('screen-view-36');
      if (s36) {
        const tabs = s36.querySelectorAll('button');
        tabs.forEach(tab => {
          const t = tab.textContent.trim().toUpperCase();
          if (['ALL', 'MINE', 'FLAT 402'].some(k => t.includes(k))) {
            tab.addEventListener('click', () => {
              tabs.forEach(b => b.classList.remove('bg-primary', 'text-white'));
              tab.classList.add('bg-primary', 'text-white');
              showToast(`History filter: ${t}`);
            });
          }
        });
        s36.querySelectorAll('.order-card, [class*="order"], [class*="card"]').forEach(card => {
          if (card.textContent.includes('₹')) {
            card.style.cursor = 'pointer';
            card.addEventListener('click', () => goToScreen(33));
          }
        });
      }

      // SCREEN 37: Flat Expense Ledger & Balances
      const s37 = document.getElementById('screen-view-37');
      if (s37) {
        s37.querySelectorAll('button').forEach(btn => {
          const t = btn.textContent.trim().toUpperCase();
          if (t.includes('SETTLE') || t.includes('UPI')) {
            btn.addEventListener('click', () => goToScreen(21));
          } else if (t.includes('REMIND') || t.includes('NUDGE')) {
            btn.addEventListener('click', () => {
              playTactileFeedback('nudge');
              showToast('WhatsApp settlement reminder sent to Kabir (+91 98234 56789)!');
            });
          } else if (t.includes('BATCH')) {
            btn.addEventListener('click', () => goToScreen(38));
          }
        });
      }

      // SCREEN 38: Floor Batching Logistics
      const s38 = document.getElementById('screen-view-38');
      if (s38) {
        s38.querySelectorAll('button').forEach(btn => {
          const t = btn.textContent.trim().toUpperCase();
          if (t.includes('JOIN') || t.includes('BATCH')) {
            btn.addEventListener('click', () => {
              playTactileFeedback('success');
              showToast('Joined Floor 4 delivery batch! Saved ₹60 delivery fee.');
              goToScreen(11);
            });
          }
        });
      }
    }    // Auto-detect mobile screen size on load
    if (window.innerWidth <= 640) {{
      toggleNativeMobile();
    }}

    // Initialize Master App
    window.addEventListener('DOMContentLoaded', () => {{
      updateDockUI();
      wireInteractiveNavigation();
    }});

    // Embedded Screen Micro-Interactions
    {scripts_joined}
  </script>
</body>
</html>
"""

if __name__ == '__main__':
    build_all()

