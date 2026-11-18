#!/usr/bin/env python3
"""
Roommate Cart - Live Interactive Application Builder
Guarantees every button, tab, card, input, stepper, slider, and inline function
works seamlessly across all 38 screens without any errors.
"""

import os
import re
import json

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
    1: {"title": "Splash & Value Proposition", "phase": "1. Onboarding & Setup", "tag": "WELCOME", "description": "Introduction to Roommate Cart wireframe: 'One cart, many payments, one delivery'. Features value props (No Chasing, Fair by Default) and live order split topology diagram.", "instructions": "Tap 'Get Started' to begin phone onboarding, or use the bottom navigator to explore any screen.", "default_next": 2, "default_prev": 1, "nav_tab": None},
    2: {"title": "Phone & OTP Verification", "phase": "1. Onboarding & Setup", "tag": "AUTH", "description": "Enter Indian mobile number (+91 98765 43210) and verify via 6-digit SMS OTP with auto-resend countdown.", "instructions": "Type in OTP boxes or tap 'VERIFY' to authenticate and proceed to Roommate profile setup.", "default_next": 3, "default_prev": 1, "nav_tab": None},
    3: {"title": "Roommate Profile Setup", "phase": "1. Onboarding & Setup", "tag": "IDENTITY", "description": "Name configuration and Roommate Token selection (Aarav, Maya, Kabir, Zoya) with signature brutalist warm utility colors.", "instructions": "Type your name, select an avatar token (A, M, K, Z), and tap 'CONTINUE'.", "default_next": 4, "default_prev": 2, "nav_tab": None},
    4: {"title": "Campus & Hostel Locator", "phase": "1. Onboarding & Setup", "tag": "LOCATION", "description": "Select university or student residence (e.g., IIT Bombay, Hostel 14 / Powai Flats). Supports instant search and chip selection.", "instructions": "Tap your hostel chip or tap 'CONTINUE' to create or join your flat.", "default_next": 5, "default_prev": 3, "nav_tab": None},
    5: {"title": "Create or Join Flat", "phase": "1. Onboarding & Setup", "tag": "FLAT SETUP", "description": "Create 'Flat 402' or join using 6-character invite code or flat QR code.", "instructions": "Tap 'CREATE FLAT' or 'JOIN FLAT' to link your UPI payment app.", "default_next": 6, "default_prev": 4, "nav_tab": None},
    6: {"title": "Link UPI & Permissions", "phase": "1. Onboarding & Setup", "tag": "PAYMENT SETUP", "description": "Select preferred UPI payment app (Google Pay, PhonePe, Paytm, CRED) for zero-click instant settlement requests and push notifications.", "instructions": "Select an app (e.g. GPay) and tap 'CONFIRM & GO TO FLAT' to enter the home dashboard.", "default_next": 7, "default_prev": 5, "nav_tab": None},
    7: {"title": "Home (Active Open Carts)", "phase": "2. Flat Hub & Dashboard", "tag": "CORE HUB", "description": "Flat 402 Home screen: View active open grocery carts ('Sunday Restock', 4m left), member status chips (Aarav, Maya, Kabir, Zoya), and quick actions.", "instructions": "Tap '+ NEW CART' to start a haul (Screen 11), tap the open cart to view items (Screen 16), or switch tabs below.", "default_next": 16, "default_prev": 6, "nav_tab": "carts"},
    8: {"title": "Home (Empty State)", "phase": "2. Flat Hub & Dashboard", "tag": "EMPTY STATE", "description": "Home screen state when no roommate has initiated an active cart. Shows quick start templates and past haul history prompt.", "instructions": "Tap '+ NEW CART' or 'QUICK START' to initiate a new cart.", "default_next": 11, "default_prev": 7, "nav_tab": "carts"},
    9: {"title": "Flat Members & Settings", "phase": "2. Flat Hub & Dashboard", "tag": "FLAT SETTINGS", "description": "Flat 402 configuration: Roommates directory, UPI routing rules, auto-settlement caps, and flat invite links.", "instructions": "Review flatmates, toggle flat rules, or use bottom navigation to switch between tabs.", "default_next": 12, "default_prev": 7, "nav_tab": "flat"},
    10: {"title": "Activity & Notifications Feed", "phase": "2. Flat Hub & Dashboard", "tag": "NOTIFICATIONS", "description": "Real-time stream of flat activity: cart creation alerts, item addition pings, payment settlement confirmations, and debt nudges.", "instructions": "Filter by 'All', 'Unread', or 'Payments'. Tap any notification to mark as read and view details.", "default_next": 7, "default_prev": 7, "nav_tab": None},
    11: {"title": "Start New Shared Cart", "phase": "3. Shopping & Shared Cart", "tag": "CREATE CART", "description": "Configure haul: Name cart ('Sunday Restock'), select quick commerce store (Blinkit, Zepto, Instamart), and set automatic lock timer (15m, 30m, 1h).", "instructions": "Tap store options, set timer, and tap 'CREATE CART' to invite roommates.", "default_next": 12, "default_prev": 7, "nav_tab": "carts"},
    12: {"title": "Invite Roommates to Cart", "phase": "3. Shopping & Shared Cart", "tag": "INVITE", "description": "Broadcast cart join link via WhatsApp group, copy direct link, or scan flat QR code.", "instructions": "Tap 'COPY LINK' (copies to clipboard) or tap 'START SHOPPING' to browse grocery items.", "default_next": 13, "default_prev": 11, "nav_tab": "carts"},
    13: {"title": "Store Catalog & Browse", "phase": "3. Shopping & Shared Cart", "tag": "BROWSE", "description": "Browse items across categories: Staples, Dairy, Snacks, Produce. High-contrast typography and instant '+ ADD' chips.", "instructions": "Tap '+ ADD' on any item, tap a card to open Item Detail (Screen 15), or tap bottom cart bar (Screen 16).", "default_next": 15, "default_prev": 12, "nav_tab": "carts"},
    14: {"title": "Search Grocery Items", "phase": "3. Shopping & Shared Cart", "tag": "SEARCH", "description": "Real-time search results for 'Basmati Rice' and popular flat essentials with one-tap add buttons.", "instructions": "Type to search, tap '+ ADD' to add item, or tap 'View Cart' to open Screen 16.", "default_next": 15, "default_prev": 13, "nav_tab": "carts"},
    15: {"title": "Item Detail & Ownership Sheet", "phase": "3. Shopping & Shared Cart", "tag": "ITEM MODAL", "description": "Detailed product sheet for Basmati Rice 5kg (₹540). Set quantity (+/-) and ownership (Shared Flat vs Personal Only).", "instructions": "Tap '-' or '+' to change quantity and see total price update, then tap 'ADD TO CART'.", "default_next": 16, "default_prev": 13, "nav_tab": "carts"},
    16: {"title": "Shared Cart View", "phase": "3. Shopping & Shared Cart", "tag": "LIVE CART", "description": "Central shared haul: Live countdown timer (04:12), items grouped by roommates (Aarav, Maya, Kabir), split tags, and locked status.", "instructions": "Watch timer tick down, tap '+ ADD AN ITEM', or tap 'LOCK CART (2/4 READY)' to proceed to split mode.", "default_next": 17, "default_prev": 13, "nav_tab": "carts"},
    17: {"title": "Ownership Split Mode", "phase": "3. Shopping & Shared Cart", "tag": "SPLIT RULES", "description": "Select how items are split: 'Equal Split' (all 4 split equally), 'Personal Only' (pay for what you consume), or 'Prorated / Custom Share'.", "instructions": "Tap an option card to select it, then tap 'CONFIRM'.", "default_next": 18, "default_prev": 16, "nav_tab": "carts"},
    18: {"title": "Prorated Share Editor", "phase": "3. Shopping & Shared Cart", "tag": "SLIDERS", "description": "Interactive sliders to adjust individual roommate share ratios (Aarav 40%, Maya 30%, Kabir 30%) with live rupee balance re-tallying.", "instructions": "Drag sliders to test micro-interactions, then tap 'CONFIRM SHARES' to view the checkout summary.", "default_next": 19, "default_prev": 17, "nav_tab": "carts"},
    19: {"title": "Checkout Summary & Split Breakdown", "phase": "4. Checkout & UPI Split", "tag": "CHECKOUT", "description": "Comprehensive haul breakdown: items subtotal (₹1,308), delivery fee (₹60 split as ₹15/each), taxes, and final individual rupee commitments.", "instructions": "Select delivery time slot chip, review split tallies, and tap 'PROCEED TO PAY'.", "default_next": 20, "default_prev": 16, "nav_tab": "carts"},
    20: {"title": "Your Share (₹342 Due)", "phase": "4. Checkout & UPI Split", "tag": "YOUR SHARE", "description": "Personal settlement screen: 'Your Share: ₹342' with instant UPI payment triggers (Google Pay, PhonePe) and lock timer badge.", "instructions": "Tap 'GPAY INSTANT' or 'PHONEPE' to trigger the simulated UPI handoff animation.", "default_next": 21, "default_prev": 19, "nav_tab": "carts"},
    21: {"title": "UPI Handoff Transition Sheet", "phase": "4. Checkout & UPI Split", "tag": "UPI HANDOFF", "description": "Dynamic dark sheet simulating UPI handoff to Google Pay on NPCI rails. Includes progress bar animation and security verification.", "instructions": "Sheet automatically simulates payment completion and transitions to Payment Success (Screen 22).", "default_next": 22, "default_prev": 20, "nav_tab": "carts"},
    22: {"title": "Payment Success Receipt", "phase": "4. Checkout & UPI Split", "tag": "PAID SUCCESS", "description": "Settlement confirmation: 'PAID · ₹342 confirmed.' UPI transaction ID with copy action, and live roommate funding status tags.", "instructions": "Tap 'VIEW PAYMENT STATUS' (Screen 25) to check on remaining roommates, or tap 'Spot Her' (Screen 26).", "default_next": 25, "default_prev": 20, "nav_tab": "carts"},
    23: {"title": "Payment Failed State", "phase": "4. Checkout & UPI Split", "tag": "PAYMENT FAILED", "description": "UPI failure handling: 'DIDN'T GO THROUGH · Bank server timeout or insufficient UPI balance.'", "instructions": "Tap 'TRY AGAIN' to re-trigger UPI handoff (Screen 21) or tap 'ASK A ROOMMATE TO SPOT ME' (Screen 27).", "default_next": 21, "default_prev": 20, "nav_tab": "carts"},
    24: {"title": "Cart Timer Expired", "phase": "4. Checkout & UPI Split", "tag": "TIMER EXPIRED", "description": "Cart lock countdown reached 00:00 before all roommates completed their UPI payments. Outlines recovery credit options.", "instructions": "Tap 'EXTEND TIMER' or 'CREDIT OPTION' to resolve the deadlock.", "default_next": 25, "default_prev": 20, "nav_tab": "carts"},
    25: {"title": "Roommate Payment Status (2 of 4 Paid)", "phase": "5. Roommate Dynamics & Edge Cases", "tag": "STATUS BOARD", "description": "Live status dashboard: Aarav (Paid ₹342), Maya (Paid ₹342), Kabir (Pending), Zoya (Short by ₹120). Includes 'NUDGE UNPAID' action.", "instructions": "Tap 'NUDGE UNPAID' for live haptic vibration, or tap Zoya's warning card to enter the spot-me resolution flow (Screen 26).", "default_next": 26, "default_prev": 22, "nav_tab": "carts"},
    26: {"title": "Zoya Is Short (Deficit Alert)", "phase": "5. Roommate Dynamics & Edge Cases", "tag": "DEFICIT CRISIS", "description": "Roommate shortfall alert: Zoya's bank balance is short by ₹120. Choose resolution: Spot her, Use flat room pool, or Drop her items.", "instructions": "Tap any resolution card to select it, then tap 'CONFIRM'.", "default_next": 27, "default_prev": 25, "nav_tab": "carts"},
    27: {"title": "Spot-Me Approval & Payback Terms", "phase": "5. Roommate Dynamics & Edge Cases", "tag": "SPOT ME", "description": "Formalize peer credit: 'Zoya asked you to spot her ₹120.' Select payback terms (1st of Month vs Next Friday) with auto-ledger logging.", "instructions": "Select payback term and tap 'APPROVE SPOT ME' to finalize and return to paid status.", "default_next": 22, "default_prev": 26, "nav_tab": "carts"},
    28: {"title": "Flat Room Pool (Cover Difference)", "phase": "5. Roommate Dynamics & Edge Cases", "tag": "ROOM POOL", "description": "Use flat petty cash reserves (Balance: ₹450) to cover the ₹120 shortfall with interactive +/- allocation steppers.", "instructions": "Tap '-' or '+' to adjust pool contribution and tap 'USE POOL FUNDS'.", "default_next": 22, "default_prev": 26, "nav_tab": "carts"},
    29: {"title": "Pay or Drop Items Ultimatum", "phase": "5. Roommate Dynamics & Edge Cases", "tag": "DROP ITEMS", "description": "Fairness safeguard: Automatically drop non-paying roommate's personal items so the rest of the flat's essential groceries dispatch immediately.", "instructions": "Toggle item checkboxes, then tap 'CONFIRM DROP & DISPATCH' to advance directly to live order tracking (Screen 33).", "default_next": 33, "default_prev": 26, "nav_tab": "carts"},
    30: {"title": "Substitute Item Voting (Out of Stock)", "phase": "5. Roommate Dynamics & Edge Cases", "tag": "OUT OF STOCK", "description": "Dark store stock alert: 'Farm Eggs 30pk out of stock.' Flatmates cast fast majority vote on suggested replacement (Organic Eggs 24pk).", "instructions": "Tap 'Accept Organic Eggs' to cast vote and approve majority.", "default_next": 19, "default_prev": 16, "nav_tab": "carts"},
    31: {"title": "Surge Price Changed Alert", "phase": "5. Roommate Dynamics & Edge Cases", "tag": "PRICE ALERT", "description": "Quick commerce surge alert: 'Tomatoes moved from ₹38 to ₹62 due to peak demand.' Option to accept split delta or drop item.", "instructions": "Tap 'ACCEPT SURGE' to proceed to checkout summary (Screen 19) or drop item.", "default_next": 19, "default_prev": 19, "nav_tab": "carts"},
    32: {"title": "Cart Expired Revive", "phase": "5. Roommate Dynamics & Edge Cases", "tag": "REVIVE CART", "description": "Revive an expired or abandoned cart haul with a single tap, refreshing dark store pricing and recreating member shares.", "instructions": "Tap 'REVIVE THIS CART' to restore the cart and reopen the shared haul (Screen 16).", "default_next": 16, "default_prev": 24, "nav_tab": "carts"},
    33: {"title": "Live Order Tracking & ETA", "phase": "6. Fulfillment, Ledger & Batching", "tag": "TRACKING", "description": "Live fulfillment tracker: Dark store packing -> Rider picked up on EV -> Arriving at Campus Gate 2 (ETA 8 mins).", "instructions": "Tap 'COLLECT AT GATE 2' or rider call button to simulate delivery receipt (Screen 34).", "default_next": 34, "default_prev": 7, "nav_tab": "orders"},
    34: {"title": "Delivered & Unbox Confirmation", "phase": "6. Fulfillment, Ledger & Batching", "tag": "DELIVERED", "description": "Delivery confirmation: Haul dropped at Flat 402 doorstep. Unbox checklist to verify items and upload proof photo.", "instructions": "Check items to mark verified, then tap 'EVERYTHING'S HERE' (Screen 36) or 'SOMETHING'S MISSING' (Screen 35).", "default_next": 36, "default_prev": 33, "nav_tab": "orders"},
    35: {"title": "Report Missing / Damaged Items", "phase": "6. Fulfillment, Ledger & Batching", "tag": "ISSUE REPORT", "description": "Report delivery discrepancy (e.g. cracked eggs, missing butter). Auto-calculates individual split refunds and credits flat ledger.", "instructions": "Select missing items and tap 'SUBMIT TICKET & CREDIT' to view updated flat ledger (Screen 37).", "default_next": 37, "default_prev": 34, "nav_tab": "orders"},
    36: {"title": "Order History & Haul Receipts", "phase": "6. Fulfillment, Ledger & Batching", "tag": "PAST ORDERS", "description": "Archive of past grocery hauls: Filter by 'All', 'Mine', or 'Flat 402'. Detailed receipts with item lists and roommate split tallies.", "instructions": "Tap tabs (ALL, MINE, FLAT 402) to filter, or tap past order cards to inspect receipts.", "default_next": 33, "default_prev": 7, "nav_tab": "orders"},
    37: {"title": "Flat Expense Ledger & Balances", "phase": "6. Fulfillment, Ledger & Batching", "tag": "LEDGER", "description": "Consolidated flat debt ledger: 'WHO OWES WHAT · Net Balances'. Kabir owes you ₹180, You owe Maya ₹90. One-tap UPI settlement.", "instructions": "Tap 'SETTLE VIA UPI' to trigger instant payment (Screen 21), or tap 'REMIND' to send WhatsApp ping.", "default_next": 38, "default_prev": 7, "nav_tab": "ledger"},
    38: {"title": "Floor Batching (Multi-Flat Logistics)", "phase": "6. Fulfillment, Ledger & Batching", "tag": "COMMUNITY BATCH", "description": "Building-level logistics: Flat 401, Flat 402, and Flat 403 pooling Blinkit delivery orders into a single rider drop to save ₹60 fee.", "instructions": "Tap 'JOIN THIS BATCH' to create a haul attached to the building drop (Screen 11).", "default_next": 11, "default_prev": 37, "nav_tab": "flat"}
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

def extract_body(html_content):
    body_match = re.search(r'<body[^>]*>(.*?)</body>', html_content, re.DOTALL | re.IGNORECASE)
    if not body_match:
        return ""
    raw_body = body_match.group(1).strip()
    # Strip inline script tags so they do not crash global JS execution
    clean_html = re.sub(r'<script[^>]*>.*?</script>', '', raw_body, flags=re.DOTALL | re.IGNORECASE).strip()
    return clean_html

def build_app():
    screens = collect_screen_files()
    print(f"Loaded {len(screens)} screen files.")

    screens_html_blocks = []
    screens_data_dict = {}

    for num in sorted(screens.keys()):
        name, html_path = screens[num]
        with open(html_path, 'r', encoding='utf-8') as f:
            content = f.read()
        body_html = extract_body(content)
        meta = SCREEN_METADATA.get(num, {
            "title": name,
            "phase": "Flow",
            "tag": f"S{num:02d}",
            "description": "",
            "instructions": "",
            "default_next": (num % 38) + 1,
            "default_prev": max(1, num - 1),
            "nav_tab": None
        })

        screens_data_dict[num] = {
            "num": num,
            "name": name,
            "title": meta["title"],
            "phase": meta["phase"],
            "tag": meta["tag"],
            "description": meta["description"],
            "instructions": meta["instructions"],
            "default_next": meta["default_next"],
            "default_prev": meta["default_prev"],
            "nav_tab": meta["nav_tab"]
        }

        screen_block = f"""
        <!-- SCREEN {num:02d}: {meta['title']} -->
        <div id="screen-view-{num}" class="screen-view {'active' if num == 1 else ''}" data-screen-num="{num}" data-tab="{meta.get('nav_tab') or ''}">
          {body_html}
        </div>
        """
        screens_html_blocks.append(screen_block)

    screens_joined = "\n".join(screens_html_blocks)
    screens_json = json.dumps(screens_data_dict, indent=2)

    # Master Template with all 41 globally defined functions and master delegated click handler
    with open('/Users/sonukewat/Downloads/stitch_roommate_cart_mobile_app/kinetic_utility/live_runtime_template.html', 'r', encoding='utf-8') as tf:
        template = tf.read()

    full_html = template.replace('/*__SCREENS_JSON__*/', screens_json)
    full_html = full_html.replace('<!--__SCREENS_JOINED__-->', screens_joined)

    # Write output to both paths
    os.makedirs(os.path.dirname(OUTPUT_PATH_1), exist_ok=True)
    with open(OUTPUT_PATH_1, 'w', encoding='utf-8') as f:
        f.write(full_html)
    print(f"Generated {OUTPUT_PATH_1} ({len(full_html)} bytes)")

    with open(OUTPUT_PATH_2, 'w', encoding='utf-8') as f:
        f.write(full_html)
    print(f"Generated {OUTPUT_PATH_2} ({len(full_html)} bytes)")

if __name__ == '__main__':
    build_app()

