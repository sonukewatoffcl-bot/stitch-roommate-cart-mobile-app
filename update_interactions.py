#!/usr/bin/env python3
"""
Adds comprehensive live interactions to generate_app.py
Every single button, input, tab, card, toggle, slider, and stepper in all 38 screens
becomes completely interactive, tactile, and connected.
"""

import os
import re

GENERATE_SCRIPT = '/Users/sonukewat/Downloads/stitch_roommate_cart_mobile_app/kinetic_utility/generate_app.py'

# Read existing generate_app.py
with open(GENERATE_SCRIPT, 'r', encoding='utf-8') as f:
    content = f.read()

# Let's inspect the replacement target in generate_master_html
# We want to replace the wireInteractiveNavigation function and add sound effects, state management, and all 38 screen live interactions.

INTERACTION_CODE = r'''
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
        const offlineStrip = s7.querySelector('.bg-\\[\\#121212\\]');
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
    }
'''

# Find the wireInteractiveNavigation function in generate_app.py and replace it with INTERACTION_CODE
pattern = r'    // Wire all interactive buttons and bottom nav items across all 38 screens.*?function wireInteractiveNavigation\(\) \{.*?(?=    // Auto-detect mobile screen size on load)'
new_content = re.sub(pattern, INTERACTION_CODE.strip(), content, flags=re.DOTALL)

# Also add the Sound toggle button into the top header toolbar:
sound_btn_html = r'''
      <!-- Sound & Haptics Toggle -->
      <button id="sound-toggle-btn" onclick="toggleSound()" title="Toggle Sound & Haptic Clicks" class="w-8 h-8 rounded-full bg-[#242624] hover:bg-[#323632] text-[#faf9f5] flex items-center justify-center transition-all">
        <span class="material-symbols-outlined text-[16px]">volume_up</span>
      </button>
'''
if 'id="sound-toggle-btn"' not in new_content:
    new_content = new_content.replace(
        '<!-- Device View Toggle -->',
        sound_btn_html + '\n      <!-- Device View Toggle -->'
    )

with open(GENERATE_SCRIPT, 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f"Updated {GENERATE_SCRIPT} successfully!")

