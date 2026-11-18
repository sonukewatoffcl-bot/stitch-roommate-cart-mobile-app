#!/usr/bin/env python3
"""
Roommate Cart - Comprehensive Interactive Mobile App Generator
Generates a fully functional, live, tapable mobile web application across all 38 screens
with deep interactivity, realistic state machines, live timers, zero clipping,
and authentic Blinkit / UPI fintech flows.
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

OUTPUT_1 = '/Users/sonukewat/Downloads/stitch_roommate_cart_mobile_app/kinetic_utility/index.html'
OUTPUT_2 = '/Users/sonukewat/Downloads/stitch_roommate_cart_mobile_app/index.html'

SCREEN_METADATA = {
    1: {"title": "Splash & Value Proposition", "phase": "1. Onboarding & Setup", "tag": "WELCOME", "description": "Introduction to Roommate Cart: One cart, many payments, one delivery. No chasing, fair by default.", "instructions": "Tap 'Get Started' to enter the phone onboarding flow.", "default_next": 2, "default_prev": 1, "nav_tab": None},
    2: {"title": "Phone & OTP Verification", "phase": "1. Onboarding & Setup", "tag": "AUTH", "description": "Indian mobile number verification with 6-digit OTP and resend countdown timer.", "instructions": "Type or tap OTP boxes, then tap 'VERIFY' to test authentication.", "default_next": 3, "default_prev": 1, "nav_tab": None},
    3: {"title": "Roommate Profile Setup", "phase": "1. Onboarding & Setup", "tag": "IDENTITY", "description": "Configure your name and select your signature roommate avatar token (A, M, K, Z).", "instructions": "Type name, tap an avatar token, and tap 'CONTINUE'.", "default_next": 4, "default_prev": 2, "nav_tab": None},
    4: {"title": "Campus & Hostel Locator", "phase": "1. Onboarding & Setup", "tag": "LOCATION", "description": "Select university campus or hostel residence (IIT Bombay, Hostel 14).", "instructions": "Tap a hostel chip to select it, then tap 'CONTINUE'.", "default_next": 5, "default_prev": 3, "nav_tab": None},
    5: {"title": "Create or Join Flat", "phase": "1. Onboarding & Setup", "tag": "FLAT SETUP", "description": "Join Flat 402 via 6-character code (FLAT402) or create a new flat.", "instructions": "Tap 'JOIN FLAT' or 'CREATE FLAT' to advance.", "default_next": 6, "default_prev": 4, "nav_tab": None},
    6: {"title": "Link UPI & Permissions", "phase": "1. Onboarding & Setup", "tag": "PAYMENT SETUP", "description": "Select UPI provider (Google Pay, PhonePe, Paytm) and configure autopay.", "instructions": "Select an app and tap 'CONFIRM & GO TO FLAT'.", "default_next": 7, "default_prev": 5, "nav_tab": None},
    7: {"title": "Home (Active Open Carts)", "phase": "2. Flat Hub & Dashboard", "tag": "CORE HUB", "description": "Flat 402 Home dashboard: Active Sunday haul, timer, roommates status, and quick actions.", "instructions": "Tap the open haul card to view cart (Screen 16), or tap '+ NEW CART' (Screen 11).", "default_next": 16, "default_prev": 6, "nav_tab": "carts"},
    8: {"title": "Home (Empty State)", "phase": "2. Flat Hub & Dashboard", "tag": "EMPTY STATE", "description": "Home screen state when no cart is open. Quick start haul buttons.", "instructions": "Tap '+ NEW CART' or 'QUICK START' to start a haul.", "default_next": 11, "default_prev": 7, "nav_tab": "carts"},
    9: {"title": "Flat Members & Settings", "phase": "2. Flat Hub & Dashboard", "tag": "FLAT SETTINGS", "description": "Flat 402 directory: Aarav, Maya, Kabir, Zoya. Manage rules and invite links.", "instructions": "Review roommates, toggle flat rules, or use bottom tabs.", "default_next": 12, "default_prev": 7, "nav_tab": "flat"},
    10: {"title": "Activity & Notifications Feed", "phase": "2. Flat Hub & Dashboard", "tag": "NOTIFICATIONS", "description": "Real-time activity stream: settlement alerts, item addition pings, debt nudges.", "instructions": "Filter tabs (All, Unread, Payments) or tap notifications to view.", "default_next": 7, "default_prev": 7, "nav_tab": None},
    11: {"title": "Start New Shared Cart", "phase": "3. Shopping & Shared Cart", "tag": "CREATE CART", "description": "Select store (Blinkit, Zepto, Instamart) and set lock timer (15m, 30m, 1h).", "instructions": "Tap store options, set timer, and tap 'CREATE CART'.", "default_next": 12, "default_prev": 7, "nav_tab": "carts"},
    12: {"title": "Invite Roommates to Cart", "phase": "3. Shopping & Shared Cart", "tag": "INVITE", "description": "Broadcast cart join link via WhatsApp group, copy link, or scan QR.", "instructions": "Tap 'COPY LINK' or tap 'START SHOPPING' to browse store.", "default_next": 13, "default_prev": 11, "nav_tab": "carts"},
    13: {"title": "Store Catalog & Browse", "phase": "3. Shopping & Shared Cart", "tag": "BROWSE", "description": "Browse grocery items across categories with instant '+ ADD' chips.", "instructions": "Tap '+ ADD' on any item, tap card to open Detail Sheet (Screen 15), or tap bottom cart bar.", "default_next": 15, "default_prev": 12, "nav_tab": "carts"},
    14: {"title": "Search Grocery Items", "phase": "3. Shopping & Shared Cart", "tag": "SEARCH", "description": "Instant search for groceries with real-time add buttons.", "instructions": "Type in search box, tap '+ ADD', or tap 'View Cart'.", "default_next": 15, "default_prev": 13, "nav_tab": "carts"},
    15: {"title": "Item Detail & Ownership Sheet", "phase": "3. Shopping & Shared Cart", "tag": "ITEM MODAL", "description": "Product sheet for Basmati Rice 5kg (₹540) with quantity steppers and split selector.", "instructions": "Tap '-' or '+' to change quantity, then tap 'ADD TO CART'.", "default_next": 16, "default_prev": 13, "nav_tab": "carts"},
    16: {"title": "Shared Cart View", "phase": "3. Shopping & Shared Cart", "tag": "LIVE CART", "description": "Shared haul with live price-lock timer, roommate badges, and total.", "instructions": "Tap '+ ADD AN ITEM' or tap 'LOCK CART (2/4 READY)' to checkout.", "default_next": 17, "default_prev": 13, "nav_tab": "carts"},
    17: {"title": "Ownership Split Mode", "phase": "3. Shopping & Shared Cart", "tag": "SPLIT RULES", "description": "Choose split mode: Equal split, Personal only, or Prorated custom shares.", "instructions": "Tap an option card to select it, then tap 'CONFIRM'.", "default_next": 18, "default_prev": 16, "nav_tab": "carts"},
    18: {"title": "Prorated Share Editor", "phase": "3. Shopping & Shared Cart", "tag": "SLIDERS", "description": "Interactive sliders to adjust roommate split ratios with live rupee balances.", "instructions": "Drag sliders to test split calculation, then tap 'CONFIRM SHARES'.", "default_next": 19, "default_prev": 17, "nav_tab": "carts"},
    19: {"title": "Checkout Summary & Split Breakdown", "phase": "4. Checkout & UPI Split", "tag": "CHECKOUT", "description": "Haul overview: subtotal, delivery fee split (₹15 each), taxes, and final share.", "instructions": "Select delivery slot and tap 'CONTINUE TO PAY'.", "default_next": 20, "default_prev": 16, "nav_tab": "carts"},
    20: {"title": "Your Share (₹342 Due)", "phase": "4. Checkout & UPI Split", "tag": "YOUR SHARE", "description": "Personal settlement screen with instant Google Pay / PhonePe triggers.", "instructions": "Tap 'GPAY INSTANT' or 'PHONEPE' to trigger UPI handoff.", "default_next": 21, "default_prev": 19, "nav_tab": "carts"},
    21: {"title": "UPI Handoff Transition Sheet", "phase": "4. Checkout & UPI Split", "tag": "UPI HANDOFF", "description": "Dynamic dark sheet simulating NPCI UPI payment handoff.", "instructions": "Animated loader auto-advances to Payment Success (Screen 22).", "default_next": 22, "default_prev": 20, "nav_tab": "carts"},
    22: {"title": "Payment Success Receipt", "phase": "4. Checkout & UPI Split", "tag": "PAID SUCCESS", "description": "PAID confirmation with UPI transaction ID and roommate status tags.", "instructions": "Tap 'VIEW PAYMENT STATUS' (Screen 25) or 'Spot Her' (Screen 26).", "default_next": 25, "default_prev": 20, "nav_tab": "carts"},
    23: {"title": "Payment Failed State", "phase": "4. Checkout & UPI Split", "tag": "PAYMENT FAILED", "description": "UPI bank server timeout / failure recovery flow.", "instructions": "Tap 'TRY AGAIN' or 'ASK A ROOMMATE TO SPOT ME'.", "default_next": 21, "default_prev": 20, "nav_tab": "carts"},
    24: {"title": "Cart Timer Expired", "phase": "4. Checkout & UPI Split", "tag": "TIMER EXPIRED", "description": "Lock timer expired before all 4 roommates paid.", "instructions": "Tap 'EXTEND TIMER' or 'REVIVE THIS CART'.", "default_next": 25, "default_prev": 20, "nav_tab": "carts"},
    25: {"title": "Roommate Payment Status (2 of 4 Paid)", "phase": "5. Roommate Dynamics & Edge Cases", "tag": "STATUS BOARD", "description": "Live status dashboard: Aarav (Paid), Maya (Paid), Kabir (Pending), Zoya (Short).", "instructions": "Tap 'NUDGE UNPAID' or tap Zoya's warning card to enter resolution.", "default_next": 26, "default_prev": 22, "nav_tab": "carts"},
    26: {"title": "Zoya Is Short (Deficit Alert)", "phase": "5. Roommate Dynamics & Edge Cases", "tag": "DEFICIT CRISIS", "description": "Zoya's account is short by ₹120. Choose: Spot Her, Room Pool, or Drop Items.", "instructions": "Select any resolution card, then tap 'CONFIRM'.", "default_next": 27, "default_prev": 25, "nav_tab": "carts"},
    27: {"title": "Spot-Me Approval & Payback Terms", "phase": "5. Roommate Dynamics & Edge Cases", "tag": "SPOT ME", "description": "Formalize peer credit: Select payback terms (1st of month vs next Friday).", "instructions": "Select payback term and tap 'APPROVE SPOT ME'.", "default_next": 22, "default_prev": 26, "nav_tab": "carts"},
    28: {"title": "Flat Room Pool (Cover Difference)", "phase": "5. Roommate Dynamics & Edge Cases", "tag": "ROOM POOL", "description": "Use flat petty cash reserve (Balance: ₹450) to cover the ₹120 deficit.", "instructions": "Tap '-' or '+' to change pool draw, then tap 'USE POOL FUNDS'.", "default_next": 22, "default_prev": 26, "nav_tab": "carts"},
    29: {"title": "Pay or Drop Items Ultimatum", "phase": "5. Roommate Dynamics & Edge Cases", "tag": "DROP ITEMS", "description": "Drop non-paying roommate's snacks so essentials dispatch immediately.", "instructions": "Toggle checkboxes, then tap 'CONFIRM DROP & DISPATCH'.", "default_next": 33, "default_prev": 26, "nav_tab": "carts"},
    30: {"title": "Substitute Item Voting (Out of Stock)", "phase": "5. Roommate Dynamics & Edge Cases", "tag": "OUT OF STOCK", "description": "Farm Eggs out of stock: Majority vote on Organic Eggs substitute.", "instructions": "Tap 'Accept Organic Eggs' to cast vote and approve majority.", "default_next": 19, "default_prev": 16, "nav_tab": "carts"},
    31: {"title": "Surge Price Changed Alert", "phase": "5. Roommate Dynamics & Edge Cases", "tag": "PRICE ALERT", "description": "Tomatoes surge pricing alert: Option to accept delta or drop item.", "instructions": "Tap 'ACCEPT SURGE' to proceed to checkout.", "default_next": 19, "default_prev": 19, "nav_tab": "carts"},
    32: {"title": "Cart Expired Revive", "phase": "5. Roommate Dynamics & Edge Cases", "tag": "REVIVE CART", "description": "Revive an abandoned haul with 1 tap, refreshing dark store pricing.", "instructions": "Tap 'REVIVE THIS CART' to reopen the shared cart.", "default_next": 16, "default_prev": 24, "nav_tab": "carts"},
    33: {"title": "Live Order Tracking & ETA", "phase": "6. Fulfillment, Ledger & Batching", "tag": "TRACKING", "description": "Live fulfillment stepper: Packing -> Rider Ramesh EV -> Campus Gate 2.", "instructions": "Tap 'COLLECT AT GATE 2' to confirm delivery.", "default_next": 34, "default_prev": 7, "nav_tab": "orders"},
    34: {"title": "Delivered & Unbox Confirmation", "phase": "6. Fulfillment, Ledger & Batching", "tag": "DELIVERED", "description": "Haul dropped at Flat 402 doorstep. Unbox checklist & verification.", "instructions": "Check off items, then tap 'EVERYTHING'S HERE' or 'SOMETHING'S MISSING'.", "default_next": 36, "default_prev": 33, "nav_tab": "orders"},
    35: {"title": "Report Missing / Damaged Items", "phase": "6. Fulfillment, Ledger & Batching", "tag": "ISSUE REPORT", "description": "Report delivery discrepancy for auto-refund to Flat Ledger.", "instructions": "Select damaged item and tap 'SUBMIT TICKET & CREDIT'.", "default_next": 37, "default_prev": 34, "nav_tab": "orders"},
    36: {"title": "Order History & Haul Receipts", "phase": "6. Fulfillment, Ledger & Batching", "tag": "PAST ORDERS", "description": "Archive of past grocery hauls: Filter by All, Mine, or Flat 402.", "instructions": "Tap filter tabs (ALL, MINE, FLAT 402) or tap an order card.", "default_next": 33, "default_prev": 7, "nav_tab": "orders"},
    37: {"title": "Flat Expense Ledger & Balances", "phase": "6. Fulfillment, Ledger & Batching", "tag": "LEDGER", "description": "Consolidated net debt ledger: Kabir owes you ₹180, You owe Maya ₹90.", "instructions": "Tap 'SETTLE VIA UPI' or tap 'REMIND' to ping Kabir.", "default_next": 38, "default_prev": 7, "nav_tab": "ledger"},
    38: {"title": "Floor Batching (Multi-Flat Logistics)", "phase": "6. Fulfillment, Ledger & Batching", "tag": "COMMUNITY BATCH", "description": "Flat 401, 402, 403 pooling Blinkit orders to save ₹60 delivery fee.", "instructions": "Tap 'JOIN THIS BATCH' to create a pooled haul.", "default_next": 11, "default_prev": 37, "nav_tab": "flat"}
}

def collect_screens():
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

def sanitize_and_enhance_screen_html(html_content, num):
    # Extract body content
    body_m = re.search(r'<body[^>]*>(.*?)</body>', html_content, re.DOTALL | re.IGNORECASE)
    raw = body_m.group(1).strip() if body_m else html_content
    # Strip existing script tags to avoid global clashes
    clean = re.sub(r'<script[^>]*>.*?</script>', '', raw, flags=re.DOTALL | re.IGNORECASE).strip()
    
    # In Screen 02: Replace static OTP boxes with interactive inputs
    if num == 2:
        # Check if static grid is present
        otp_replacement = """
        <!-- Interactive 6-Digit OTP Box Grid -->
        <div class="grid grid-cols-6 gap-2 w-full mb-space-sm" id="otp-inputs-container">
          <input type="text" inputmode="numeric" maxlength="1" value="4" class="otp-digit-box flex items-center justify-center h-13 py-3 bg-surface-container-lowest border-2 border-primary rounded-DEFAULT text-on-surface font-headline-sm text-headline-sm text-center shadow-sm focus:outline-none focus:border-secondary transition-colors" data-idx="0">
          <input type="text" inputmode="numeric" maxlength="1" value="8" class="otp-digit-box flex items-center justify-center h-13 py-3 bg-surface-container-lowest border border-outline-variant rounded-DEFAULT text-on-surface font-headline-sm text-headline-sm text-center shadow-sm focus:outline-none focus:border-secondary transition-colors" data-idx="1">
          <input type="text" inputmode="numeric" maxlength="1" value="2" class="otp-digit-box flex items-center justify-center h-13 py-3 bg-surface-container-lowest border border-outline-variant rounded-DEFAULT text-on-surface font-headline-sm text-headline-sm text-center shadow-sm focus:outline-none focus:border-secondary transition-colors" data-idx="2">
          <input type="text" inputmode="numeric" maxlength="1" value="9" class="otp-digit-box flex items-center justify-center h-13 py-3 bg-surface-container-lowest border border-outline-variant rounded-DEFAULT text-on-surface font-headline-sm text-headline-sm text-center shadow-sm focus:outline-none focus:border-secondary transition-colors" data-idx="3">
          <input type="text" inputmode="numeric" maxlength="1" value="1" class="otp-digit-box flex items-center justify-center h-13 py-3 bg-surface-container-lowest border border-outline-variant rounded-DEFAULT text-on-surface font-headline-sm text-headline-sm text-center shadow-sm focus:outline-none focus:border-secondary transition-colors" data-idx="4">
          <input type="text" inputmode="numeric" maxlength="1" value="4" class="otp-digit-box flex items-center justify-center h-13 py-3 bg-surface-container-lowest border border-outline-variant rounded-DEFAULT text-on-surface font-headline-sm text-headline-sm text-center shadow-sm focus:outline-none focus:border-secondary transition-colors" data-idx="5">
        </div>
        """
        clean = re.sub(r'<div class=\"grid grid-cols-6 gap-2 w-full mb-space-sm\">.*?</div>\s*</div>\s*</div>\s*<!-- Timer & Resend Row -->', otp_replacement + '\n</div>\n</div>\n<!-- Timer & Resend Row -->', clean, flags=re.DOTALL)
        
    return clean

def build_app():
    screens = collect_screens()
    print(f"Loaded {len(screens)} screen files.")

    screens_html_list = []
    screens_data_dict = {}

    for num in sorted(screens.keys()):
        name, path = screens[num]
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        sanitized = sanitize_and_enhance_screen_html(content, num)
        meta = SCREEN_METADATA.get(num)
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
          {sanitized}
        </div>
        """
        screens_html_list.append(screen_block)

    screens_joined = "\n".join(screens_html_list)
    screens_json = json.dumps(screens_data_dict, indent=2)

    with open('/Users/sonukewat/Downloads/stitch_roommate_cart_mobile_app/kinetic_utility/live_runtime_template.html', 'r', encoding='utf-8') as tf:
        template = tf.read()

    full_html = template.replace('/*__SCREENS_JSON__*/', screens_json)
    full_html = full_html.replace('<!--__SCREENS_JOINED__-->', screens_joined)

    # Add sticky header & footer container rules to CSS in template
    sticky_css_rules = """
    /* Pinned mobile headers and action bars contained to 390px phone container */
    .screen-view {
      position: absolute !important;
      inset: 0 !important;
      width: 100% !important;
      height: 100% !important;
      display: flex !important;
      flex-direction: column !important;
      overflow-y: auto !important;
      overflow-x: hidden !important;
      background-color: #faf9f5 !important;
      -webkit-overflow-scrolling: touch !important;
      opacity: 0 !important;
      pointer-events: none !important;
      transform: translateX(40px) !important;
      transition: opacity 0.24s ease-out, transform 0.24s cubic-bezier(0.16, 1, 0.3, 1) !important;
    }
    .screen-view.active {
      opacity: 1 !important;
      pointer-events: auto !important;
      transform: translateX(0) !important;
      z-index: 10 !important;
    }
    .screen-view.slide-back {
      transform: translateX(-40px) !important;
      opacity: 0 !important;
    }
    .screen-view header.fixed,
    .screen-view .fixed.top-0 {
      position: sticky !important;
      top: 0 !important;
      left: 0 !important;
      width: 100% !important;
      max-width: 100% !important;
      z-index: 40 !important;
    }
    .screen-view nav.fixed,
    .screen-view .fixed.bottom-0 {
      position: sticky !important;
      bottom: 0 !important;
      left: 0 !important;
      width: 100% !important;
      max-width: 100% !important;
      z-index: 40 !important;
    }
    """
    full_html = full_html.replace('</style>', sticky_css_rules + '\n  </style>')

    # Write output to active workspace and root folder
    os.makedirs(os.path.dirname(OUTPUT_1), exist_ok=True)
    with open(OUTPUT_1, 'w', encoding='utf-8') as f:
        f.write(full_html)
    print(f"Generated {OUTPUT_1} ({len(full_html)} bytes)")

    with open(OUTPUT_2, 'w', encoding='utf-8') as f:
        f.write(full_html)
    print(f"Generated {OUTPUT_2} ({len(full_html)} bytes)")

if __name__ == '__main__':
    build_app()
