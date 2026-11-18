import re

with open('live_runtime_template.html', 'r', encoding='utf-8') as f:
    html = f.read()

# We will replace Script 2 with our comprehensive Reactive Engine
new_script = r"""<script>
    // Screen Registry
    window.SCREENS_DATA = /*__SCREENS_JSON__*/;
    window.currentScreen = 1;
    window.isNativeMobile = false;

    // Toast Notification
    window.showToast = function(msg) {
      const toast = document.getElementById('app-toast');
      if (!toast) return;
      toast.textContent = msg;
      toast.classList.add('show');
      setTimeout(() => toast.classList.remove('show'), 2200);
    };

    // Synthesized Audio & Haptic Feedback Engine
    let audioContext = null;
    function getAudioContext() {
      if (!audioContext) {
        try { audioContext = new (window.AudioContext || window.webkitAudioContext)(); } catch(e) {}
      }
      return audioContext;
    }

    window.playTactileFeedback = function(type = 'click') {
      if (window.navigator && window.navigator.vibrate) {
        try { window.navigator.vibrate(type === 'success' ? [15, 40, 15] : 12); } catch(e) {}
      }
      if (window.soundMuted) return;
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
          osc.frequency.setValueAtTime(400, now);
          osc.frequency.exponentialRampToValueAtTime(180, now + 0.04);
          gain.gain.setValueAtTime(0.06, now);
          gain.gain.linearRampToValueAtTime(0.001, now + 0.04);
          osc.start(now);
          osc.stop(now + 0.04);
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
    };

    window.toggleSound = function() {
      window.soundMuted = !window.soundMuted;
      showToast(window.soundMuted ? 'Sound: Muted 🔕' : 'Sound: ON 🔔');
      const soundBtn = document.getElementById('sound-toggle-btn');
      if (soundBtn) {
        soundBtn.innerHTML = window.soundMuted ? 
          '<span class="material-symbols-outlined text-[16px] text-zinc-500">volume_off</span>' : 
          '<span class="material-symbols-outlined text-[16px]">volume_up</span>';
      }
    };

    // Navigation Engine
    window.goToScreen = function(targetNum) {
      targetNum = parseInt(targetNum, 10);
      if (isNaN(targetNum) || targetNum < 1 || targetNum > 38 || targetNum === window.currentScreen) return;

      const prevEl = document.getElementById(`screen-view-${window.currentScreen}`);
      const nextEl = document.getElementById(`screen-view-${targetNum}`);
      if (!nextEl) return;

      // Clear any running timers from previous screen
      clearInterval(window._otpTimer);
      clearInterval(window._cartLockTimer);
      clearInterval(window._shareTimer);
      clearInterval(window._urgentTimer);
      clearInterval(window._batchTimer);
      clearTimeout(window._handoffTimeout);

      if (prevEl) prevEl.classList.remove('active');
      nextEl.classList.add('active');

      window.currentScreen = targetNum;

      const screenContainer = document.getElementById('phone-screen');
      if (screenContainer) screenContainer.scrollTop = 0;

      updateDockUI();
      closeDrawer();
      closeInstructions();
      playTactileFeedback('click');

      // Initialize the controller for this screen
      if (window.ScreenControllers && window.ScreenControllers[targetNum]) {
        try {
          window.ScreenControllers[targetNum]();
        } catch(err) {
          console.error(`Error in ScreenController for ${targetNum}:`, err);
        }
      }
    };

    window.nextScreen = function() {
      const meta = window.SCREENS_DATA[window.currentScreen];
      if (meta && meta.default_next) {
        window.goToScreen(meta.default_next);
      } else {
        window.goToScreen((window.currentScreen % 38) + 1);
      }
    };

    window.prevScreen = function() {
      const meta = window.SCREENS_DATA[window.currentScreen];
      if (meta && meta.default_prev) {
        window.goToScreen(meta.default_prev);
      } else {
        window.goToScreen(window.currentScreen === 1 ? 38 : window.currentScreen - 1);
      }
    };

    function updateDockUI() {
      const meta = window.SCREENS_DATA[window.currentScreen];
      if (!meta) return;

      const numStr = String(window.currentScreen).padStart(2, '0');
      const dNum = document.getElementById('dock-screen-num');
      const dTitle = document.getElementById('dock-screen-title');
      const dPhase = document.getElementById('dock-screen-phase');
      const tBadge = document.getElementById('top-screen-badge');

      if (dNum) dNum.textContent = `${numStr}/38`;
      if (dTitle) dTitle.textContent = meta.title;
      if (dPhase) dPhase.textContent = meta.phase;
      if (tBadge) tBadge.textContent = `${numStr} · ${meta.title}`;

      const iTitle = document.getElementById('inst-title');
      const iDesc = document.getElementById('inst-desc');
      const iGuide = document.getElementById('inst-guide');
      if (iTitle) iTitle.textContent = `[${numStr}] ${meta.title}`;
      if (iDesc) iDesc.textContent = meta.description;
      if (iGuide) iGuide.textContent = meta.instructions;
    }

    window.toggleNativeMobile = function() {
      window.isNativeMobile = !window.isNativeMobile;
      document.body.classList.toggle('native-mobile', window.isNativeMobile);
      const btnText = document.getElementById('frame-btn-text');
      if (btnText) btnText.textContent = window.isNativeMobile ? 'Full Responsive' : 'Mobile Frame';
      showToast(window.isNativeMobile ? 'Full Responsive Viewport' : 'iPhone 16 Pro Frame');
    };

    window.setZoom = function(scale) {
      const mockup = document.getElementById('phone-container');
      if (mockup && !window.isNativeMobile) {
        mockup.style.transform = `scale(${scale})`;
      }
    };

    window.openScreensDrawer = function() {
      document.getElementById('drawer-overlay').classList.add('open');
    };
    window.closeDrawer = function(e) {
      if (!e || e.target === document.getElementById('drawer-overlay') || e.target.closest('#drawer-close-btn')) {
        document.getElementById('drawer-overlay').classList.remove('open');
      }
    };

    window.openInstructions = function() {
      document.getElementById('instructions-modal').classList.add('open');
    };
    window.closeInstructions = function(e) {
      if (!e || e.target === document.getElementById('instructions-modal') || e.target.closest('#inst-close-btn')) {
        document.getElementById('instructions-modal').classList.remove('open');
      }
    };

    function updateClock() {
      const now = new Date();
      let hours = now.getHours();
      const minutes = String(now.getMinutes()).padStart(2, '0');
      hours = hours % 12 || 12;
      const el = document.getElementById('iphone-clock');
      if (el) el.textContent = `${hours}:${minutes}`;
    }

    // Shared Cart Floating Bar Updater
    window._cartItems = 2;
    window._cartTotal = 1248;
    window.updateCartFloatingBar = function(deltaItems, deltaRupees) {
      window._cartItems = Math.max(0, (window._cartItems || 0) + deltaItems);
      window._cartTotal = Math.max(0, (window._cartTotal || 1248) + deltaRupees);
      const floatingBar = document.querySelector('#screen-view-13 [class*="fixed bottom-"]') || document.querySelector('#screen-view-13 [class*="sticky bottom-"]');
      if (floatingBar) {
        const textNodes = floatingBar.querySelectorAll('span');
        textNodes.forEach(span => {
          if (span.textContent.includes('ITEMS') || span.textContent.includes('₹')) {
            span.textContent = `${window._cartItems} ITEMS • ₹${window._cartTotal.toLocaleString('en-IN')}`;
          }
        });
      }
    };

    window.updateCatalogCart = function(el, delta) {
      playTactileFeedback('click');
      const counter = el.parentElement.querySelector('.qty-counter');
      let count = parseInt(counter.textContent, 10) + delta;
      if (count <= 0) {
        el.parentElement.outerHTML = '<button class="px-3 py-1 bg-surface-container-highest rounded-DEFAULT text-xs font-bold font-mono text-on-surface hover:bg-secondary hover:text-primary transition-all active:scale-95" onclick="window.updateCatalogCartAdd(this)">+ ADD</button>';
        window.updateCartFloatingBar(-1, -56);
      } else {
        counter.textContent = count;
        window.updateCartFloatingBar(delta, delta * 56);
      }
    };

    window.updateCatalogCartAdd = function(btn) {
      playTactileFeedback('click');
      btn.outerHTML = `
        <div class="flex items-center gap-2 bg-secondary text-primary font-bold px-2 py-1 rounded-DEFAULT text-xs">
          <span class="cursor-pointer px-1 text-sm select-none" onclick="window.updateCatalogCart(this, -1)">-</span>
          <span class="qty-counter font-mono">1</span>
          <span class="cursor-pointer px-1 text-sm select-none" onclick="window.updateCatalogCart(this, 1)">+</span>
        </div>
      `;
      window.updateCartFloatingBar(1, 56);
      showToast('Item added to collective cart! 🛒');
    };

    // Reactive Screen Controllers Definition
    window.ScreenControllers = {
      1: function() {
        const view = document.getElementById('screen-view-1');
        if (!view) return;
        const avatars = [
          { id: 'avatar-a', name: 'Aarav (Admin)', role: 'Flat 402 Lead • Created Sunday Haul' },
          { id: 'avatar-m', name: 'Maya', role: 'Split 50/50 • Paid ₹342 upfront' },
          { id: 'avatar-k', name: 'Kabir', role: 'Pending ₹342 • Reminder sent via WhatsApp' },
          { id: 'avatar-z', name: 'Zoya', role: 'Short ₹120 • Spot Me request active' }
        ];
        avatars.forEach(av => {
          const el = view.querySelector('#' + av.id);
          if (el) {
            el.style.cursor = 'pointer';
            el.onclick = () => {
              playTactileFeedback('click');
              showToast(`${av.name}: ${av.role}`);
              const toastText = view.querySelector('#toast-text');
              if (toastText) toastText.textContent = `${av.name}: ${av.role}`;
            };
          }
        });
      },

      2: function() {
        const view = document.getElementById('screen-view-2');
        if (!view) return;
        clearInterval(window._otpTimer);
        let timeLeft = 28;
        const timerEl = view.querySelector('#countdown-timer');
        if (timerEl) {
          timerEl.textContent = '0:28';
          window._otpTimer = setInterval(() => {
            timeLeft--;
            if (timeLeft <= 0) {
              clearInterval(window._otpTimer);
              timerEl.innerHTML = '<span class="text-secondary font-bold cursor-pointer hover:underline">RESEND OTP</span>';
              timerEl.onclick = () => {
                playTactileFeedback('click');
                showToast('New 6-digit OTP sent to +91 98765 43210 ✓');
                window.ScreenControllers[2]();
              };
            } else {
              timerEl.textContent = `0:${timeLeft < 10 ? '0' : ''}${timeLeft}`;
            }
          }, 1000);
        }
        const inputs = view.querySelectorAll('.otp-digit-box');
        inputs.forEach((inp, idx) => {
          inp.oninput = (e) => {
            if (inp.value.length >= 1) {
              inp.value = inp.value.slice(-1);
              if (idx < inputs.length - 1) inputs[idx + 1].focus();
            }
          };
          inp.onkeydown = (e) => {
            if (e.key === 'Backspace' && !inp.value && idx > 0) {
              inputs[idx - 1].focus();
            }
          };
        });
        const verifyBtn = view.querySelector('#verify-button') || view.querySelector('button[type="submit"]');
        if (verifyBtn) {
          verifyBtn.onclick = (e) => {
            e.preventDefault();
            playTactileFeedback('click');
            verifyBtn.innerHTML = '<span class="material-symbols-outlined animate-spin text-[18px]">progress_activity</span> VERIFYING...';
            setTimeout(() => {
              playTactileFeedback('success');
              showToast('Phone verified: +91 98765 43210 ✓');
              window.goToScreen(3);
            }, 350);
          };
        }
      },

      3: function() {
        const view = document.getElementById('screen-view-3');
        if (!view) return;
        const nameInput = view.querySelector('#name-input');
        const mainInitial = view.querySelector('#main-initial');
        const previewInitial = view.querySelector('#preview-initial');
        const previewName = view.querySelector('#preview-name');
        if (nameInput) {
          nameInput.oninput = () => {
            const val = nameInput.value.trim() || 'Aarav';
            const init = val.charAt(0).toUpperCase();
            if (mainInitial) mainInitial.textContent = init;
            if (previewInitial) previewInitial.textContent = init;
            if (previewName) previewName.textContent = val;
          };
        }
      },

      4: function() {
        const view = document.getElementById('screen-view-4');
        if (!view) return;
        const options = view.querySelectorAll('.hostel-option, [data-hostel], button[class*="border"]');
        options.forEach(opt => {
          opt.onclick = () => {
            playTactileFeedback('click');
            options.forEach(o => o.classList.remove('border-2', 'border-secondary', 'bg-secondary-container/20'));
            opt.classList.add('border-2', 'border-secondary', 'bg-secondary-container/20');
            showToast(`Hostel selected: ${opt.textContent.trim().split('\n')[0]}`);
          };
        });
      },

      5: function() {
        const view = document.getElementById('screen-view-5');
        if (!view) return;
        const cardCreate = view.querySelector('#card-create');
        const cardJoin = view.querySelector('#card-join');
        const confirmBtn = view.querySelector('#confirm-btn');
        if (cardJoin) {
          cardJoin.onclick = () => {
            playTactileFeedback('click');
            cardJoin.classList.add('border-2', 'border-secondary', 'bg-secondary-container/10');
            if (cardCreate) cardCreate.classList.remove('border-2', 'border-secondary', 'bg-secondary-container/10');
            if (confirmBtn) confirmBtn.textContent = 'JOIN FLAT 402 →';
            showToast('Joining Flat 402 (Hostel 14)');
          };
        }
        if (cardCreate) {
          cardCreate.onclick = () => {
            playTactileFeedback('click');
            cardCreate.classList.add('border-2', 'border-secondary', 'bg-secondary-container/10');
            if (cardJoin) cardJoin.classList.remove('border-2', 'border-secondary', 'bg-secondary-container/10');
            if (confirmBtn) confirmBtn.textContent = 'CREATE NEW FLAT →';
            showToast('Creating a new flat');
          };
        }
      },

      6: function() {
        const view = document.getElementById('screen-view-6');
        if (!view) return;
        const chips = view.querySelectorAll('.app-chip, [data-app]');
        chips.forEach(chip => {
          chip.onclick = () => {
            playTactileFeedback('click');
            chips.forEach(c => c.classList.remove('border-2', 'border-secondary', 'bg-secondary-container/20'));
            chip.classList.add('border-2', 'border-secondary', 'bg-secondary-container/20');
            const appId = chip.getAttribute('data-app') || 'gpay';
            showToast(`Selected UPI provider: ${appId.toUpperCase()}`);
          };
        });
      },

      7: function() {
        const view = document.getElementById('screen-view-7');
        if (!view) return;
        const haulCards = view.querySelectorAll('.haul-card, [data-haul-card], [class*="bg-surface-container"]');
        haulCards.forEach(card => {
          if (card.textContent.includes('BLINKIT') || card.textContent.includes('₹1,248') || card.textContent.includes('SUNDAY')) {
            card.style.cursor = 'pointer';
            card.onclick = (e) => {
              if (e.target.closest('button')) return;
              playTactileFeedback('click');
              window.goToScreen(16);
            };
          }
        });
      },

      9: function() {
        const view = document.getElementById('screen-view-9');
        if (!view) return;
        const qrToggle = view.querySelector('#qrToggleBtn');
        const qrDrawer = view.querySelector('#qrDrawer');
        if (qrToggle && qrDrawer) {
          qrToggle.onclick = () => {
            playTactileFeedback('click');
            qrDrawer.classList.toggle('hidden');
            qrDrawer.classList.toggle('flex');
          };
        }
        const copyBtn = view.querySelector('#copyLinkBtn');
        if (copyBtn) {
          copyBtn.onclick = () => {
            playTactileFeedback('success');
            showToast('Flat invite link copied to clipboard: stitch.app/flat402 ✓');
          };
        }
      },

      10: function() {
        const view = document.getElementById('screen-view-10');
        if (!view) return;
        const tabAll = view.querySelector('#tab-all');
        const tabUnread = view.querySelector('#tab-unread');
        const tabPayments = view.querySelector('#tab-payments');
        function selectTab(activeTab, filter) {
          playTactileFeedback('click');
          [tabAll, tabUnread, tabPayments].forEach(t => {
            if (t) {
              t.classList.remove('bg-primary', 'text-on-primary');
              t.classList.add('bg-surface-container-lowest', 'text-on-surface');
            }
          });
          if (activeTab) {
            activeTab.classList.remove('bg-surface-container-lowest', 'text-on-surface');
            activeTab.classList.add('bg-primary', 'text-on-primary');
          }
          showToast(`Showing ${filter} notifications`);
        }
        if (tabAll) tabAll.onclick = () => selectTab(tabAll, 'All');
        if (tabUnread) tabUnread.onclick = () => selectTab(tabUnread, 'Unread');
        if (tabPayments) tabPayments.onclick = () => selectTab(tabPayments, 'Payments');
      },

      11: function() {
        const view = document.getElementById('screen-view-11');
        if (!view) return;
        const stores = view.querySelectorAll('.store-card, [data-store], button[class*="border"]');
        stores.forEach(s => {
          s.onclick = () => {
            playTactileFeedback('click');
            stores.forEach(x => x.classList.remove('border-2', 'border-secondary', 'bg-secondary-container/20'));
            s.classList.add('border-2', 'border-secondary', 'bg-secondary-container/20');
            showToast(`Store selected: ${s.textContent.trim().split('\n')[0]}`);
          };
        });
        const clearBtn = view.querySelector('#clear-btn');
        const cartInput = view.querySelector('#cart-name-input');
        if (clearBtn && cartInput) {
          clearBtn.onclick = () => {
            cartInput.value = '';
            cartInput.focus();
          };
        }
      },

      12: function() {
        const view = document.getElementById('screen-view-12');
        if (!view) return;
        const copyBtn = view.querySelector('#copy-btn');
        if (copyBtn) {
          copyBtn.onclick = () => {
            playTactileFeedback('success');
            showToast('Cart link copied: flat.cart/c/sunday-restock-402 ✓');
            const copyText = view.querySelector('#copy-text');
            if (copyText) copyText.textContent = 'COPIED!';
          };
        }
      },

      13: function() {
        const view = document.getElementById('screen-view-13');
        if (!view) return;
        const pills = view.querySelectorAll('[class*="rounded-full px-3"]');
        pills.forEach(pill => {
          pill.onclick = () => {
            playTactileFeedback('click');
            pills.forEach(p => p.classList.remove('bg-primary', 'text-on-primary'));
            pill.classList.add('bg-primary', 'text-on-primary');
            showToast(`Category: ${pill.textContent.trim()}`);
          };
        });
        const addBtns = view.querySelectorAll('button');
        addBtns.forEach(btn => {
          if (btn.textContent.trim().includes('+ ADD') || btn.textContent.trim() === 'ADD') {
            btn.onclick = (e) => {
              e.stopPropagation();
              playTactileFeedback('click');
              btn.outerHTML = `
                <div class="flex items-center gap-2 bg-secondary text-primary font-bold px-2 py-1 rounded-DEFAULT text-xs">
                  <span class="cursor-pointer px-1 text-sm select-none" onclick="window.updateCatalogCart(this, -1)">-</span>
                  <span class="qty-counter font-mono">1</span>
                  <span class="cursor-pointer px-1 text-sm select-none" onclick="window.updateCatalogCart(this, 1)">+</span>
                </div>
              `;
              window.updateCartFloatingBar(1, 56);
              showToast('Added to cart! 🛒');
            };
          }
        });
        const cards = view.querySelectorAll('[class*="bg-surface-container"]');
        cards.forEach(card => {
          if (card.textContent.includes('Basmati') || card.textContent.includes('Rice') || card.textContent.includes('₹520')) {
            card.style.cursor = 'pointer';
            card.onclick = (e) => {
              if (e.target.closest('button') || e.target.closest('.qty-counter')) return;
              playTactileFeedback('click');
              window.goToScreen(15);
            };
          }
        });
      },

      14: function() {
        const view = document.getElementById('screen-view-14');
        if (!view) return;
        const searchInput = view.querySelector('#search-input');
        const clearBtn = view.querySelector('#clear-search-btn');
        if (clearBtn && searchInput) {
          clearBtn.onclick = () => {
            searchInput.value = '';
            searchInput.focus();
          };
        }
      },

      15: function() {
        const view = document.getElementById('screen-view-15');
        if (!view) return;
        let qty = 1;
        const basePrice = 520;
        const qtyMinus = view.querySelector('#qty-minus');
        const qtyPlus = view.querySelector('#qty-plus');
        const qtyVal = view.querySelector('#qty-val');
        const displayPrice = view.querySelector('#display-price');
        const addBtn = view.querySelector('#add-to-cart-btn') || view.querySelector('button[class*="bg-primary"]');

        function renderDetail() {
          if (qtyVal) qtyVal.textContent = qty;
          const total = qty * basePrice;
          if (displayPrice) displayPrice.textContent = `₹${total.toLocaleString('en-IN')}`;
          if (addBtn && addBtn.textContent.includes('ADD')) {
            addBtn.textContent = `ADD ${qty} TO CART • ₹${total.toLocaleString('en-IN')}`;
          }
        }
        if (qtyMinus) {
          qtyMinus.onclick = () => {
            if (qty > 1) { qty--; playTactileFeedback('click'); renderDetail(); }
          };
        }
        if (qtyPlus) {
          qtyPlus.onclick = () => {
            qty++; playTactileFeedback('click'); renderDetail();
          };
        }
      },

      16: function() {
        const view = document.getElementById('screen-view-16');
        if (!view) return;
        clearInterval(window._cartLockTimer);
        let secondsLeft = 14 * 60 + 58;
        const timerElem = view.querySelector('#countdown-timer');
        if (timerElem) {
          window._cartLockTimer = setInterval(() => {
            secondsLeft--;
            if (secondsLeft <= 0) {
              clearInterval(window._cartLockTimer);
              timerElem.textContent = '00:00';
              showToast('Cart lock expired!');
              window.goToScreen(24);
            } else {
              const mins = Math.floor(secondsLeft / 60).toString().padStart(2, '0');
              const secs = (secondsLeft % 60).toString().padStart(2, '0');
              timerElem.textContent = `${mins}:${secs}`;
            }
          }, 1000);
        }
      },

      17: function() {
        const view = document.getElementById('screen-view-17');
        if (!view) return;
        const modeCards = view.querySelectorAll('.mode-card, [data-mode]');
        modeCards.forEach(card => {
          card.onclick = () => {
            playTactileFeedback('click');
            modeCards.forEach(c => c.classList.remove('border-2', 'border-secondary', 'bg-secondary-container/10'));
            card.classList.add('border-2', 'border-secondary', 'bg-secondary-container/10');
            const mode = card.getAttribute('data-mode') || 'equal';
            showToast(`Split mode: ${mode.toUpperCase()}`);
          };
        });
      },

      18: function() {
        const view = document.getElementById('screen-view-18');
        if (!view) return;
        const sliders = view.querySelectorAll('.roommate-slider, input[type="range"]');
        const TOTAL = 1240;
        sliders.forEach((slider, idx) => {
          slider.oninput = () => {
            const pct = parseInt(slider.value, 10);
            const amt = Math.round((pct / 100) * TOTAL);
            const pctEl = view.querySelector(`#pct-val-${idx}`);
            const amtEl = view.querySelector(`#amt-val-${idx}`);
            const fillEl = view.querySelector(`#fill-bar-${idx}`);
            if (pctEl) pctEl.textContent = `${pct}%`;
            if (amtEl) amtEl.textContent = `₹${amt}`;
            if (fillEl) fillEl.style.width = `${pct}%`;
          };
        });
      },

      19: function() {
        const view = document.getElementById('screen-view-19');
        if (!view) return;
        const slots = view.querySelectorAll('.slot-pill, [data-slot]');
        slots.forEach(slot => {
          slot.onclick = () => {
            playTactileFeedback('click');
            slots.forEach(s => s.classList.remove('border-2', 'border-secondary', 'bg-secondary-container/20'));
            slot.classList.add('border-2', 'border-secondary', 'bg-secondary-container/20');
            showToast(`Delivery Slot: ${slot.textContent.trim().split('\n')[0]}`);
          };
        });
      },

      20: function() {
        const view = document.getElementById('screen-view-20');
        if (!view) return;
        clearInterval(window._shareTimer);
        let secondsRemaining = 582;
        const countdownEl = view.querySelector('#countdown');
        if (countdownEl) {
          window._shareTimer = setInterval(() => {
            if (secondsRemaining > 0) {
              secondsRemaining--;
              const mins = Math.floor(secondsRemaining / 60).toString().padStart(2, '0');
              const secs = (secondsRemaining % 60).toString().padStart(2, '0');
              countdownEl.textContent = `${mins}:${secs}`;
            }
          }, 1000);
        }
        const upiCards = view.querySelectorAll('.upi-card, [data-upi], [class*="border"]');
        const btnText = view.querySelector('#btn-text');
        upiCards.forEach(c => {
          c.onclick = () => {
            playTactileFeedback('click');
            upiCards.forEach(x => x.classList.remove('border-2', 'border-secondary', 'bg-secondary-container/20'));
            c.classList.add('border-2', 'border-secondary', 'bg-secondary-container/20');
            const app = c.getAttribute('data-upi') || 'GPay';
            if (btnText) btnText.textContent = `PAY ₹342 VIA ${app.toUpperCase()}`;
            showToast(`Selected UPI: ${app.toUpperCase()}`);
          };
        });
      },

      21: function() {
        const view = document.getElementById('screen-view-21');
        if (!view) return;
        clearTimeout(window._handoffTimeout);
        window._handoffTimeout = setTimeout(() => {
          if (window.currentScreen === 21) {
            playTactileFeedback('success');
            showToast('₹342 Paid successfully via UPI! ✓');
            window.goToScreen(22);
          }
        }, 2500);
      },

      22: function() {
        const view = document.getElementById('screen-view-22');
        if (!view) return;
        const copyBtn = view.querySelector('#copy-ref-btn');
        if (copyBtn) {
          copyBtn.onclick = () => {
            playTactileFeedback('success');
            copyBtn.textContent = 'COPIED ✓';
            showToast('UPI Ref ID copied: UPI/329482910482/OKAXIS');
          };
        }
      },

      25: function() {
        const view = document.getElementById('screen-view-25');
        if (!view) return;
        const nudgeBtn = view.querySelector('#nudge-button');
        if (nudgeBtn) {
          nudgeBtn.onclick = () => {
            playTactileFeedback('nudge');
            nudgeBtn.classList.add('scale-105', 'bg-secondary-container');
            showToast('Pinging Kabir & Zoya on WhatsApp & SMS! ✓');
            setTimeout(() => nudgeBtn.classList.remove('scale-105', 'bg-secondary-container'), 400);
          };
        }
        const zoyaCards = view.querySelectorAll('[class*="border"]');
        zoyaCards.forEach(zc => {
          if (zc.textContent.includes('Zoya') && (zc.textContent.includes('120') || zc.textContent.includes('Short') || zc.textContent.includes('Deficit'))) {
            zc.style.cursor = 'pointer';
            zc.onclick = () => {
              playTactileFeedback('click');
              window.goToScreen(26);
            };
          }
        });
      },

      26: function() {
        const view = document.getElementById('screen-view-26');
        if (!view) return;
        let selectedMode = 'spot';
        const cardSpot = view.querySelector('#card-spot');
        const cardPool = view.querySelector('#card-pool');
        const cardDrop = view.querySelector('#card-drop');
        const ctaBtn = view.querySelector('#primary-cta-btn') || view.querySelector('button[class*="bg-primary"]');

        function setSelection(mode) {
          selectedMode = mode;
          [cardSpot, cardPool, cardDrop].forEach(c => {
            if (c) c.classList.remove('border-2', 'border-secondary', 'bg-secondary-container/10');
          });
          if (mode === 'spot' && cardSpot) cardSpot.classList.add('border-2', 'border-secondary', 'bg-secondary-container/10');
          if (mode === 'pool' && cardPool) cardPool.classList.add('border-2', 'border-secondary', 'bg-secondary-container/10');
          if (mode === 'drop' && cardDrop) cardDrop.classList.add('border-2', 'border-secondary', 'bg-secondary-container/10');
          if (ctaBtn) {
            if (mode === 'spot') ctaBtn.textContent = 'SPOT ZOYA (₹120) →';
            else if (mode === 'pool') ctaBtn.textContent = 'SPLIT IN ROOM POOL →';
            else ctaBtn.textContent = 'DROP ZOYA ITEMS & DISPATCH →';
          }
          playTactileFeedback('click');
        }
        if (cardSpot) cardSpot.onclick = () => setSelection('spot');
        if (cardPool) cardPool.onclick = () => setSelection('pool');
        if (cardDrop) cardDrop.onclick = () => setSelection('drop');
        if (ctaBtn) {
          ctaBtn.onclick = () => {
            if (selectedMode === 'spot') window.goToScreen(27);
            else if (selectedMode === 'pool') window.goToScreen(28);
            else window.goToScreen(29);
          };
        }
      },

      27: function() {
        const view = document.getElementById('screen-view-27');
        if (!view) return;
        const chips = view.querySelectorAll('.date-chip, [data-date], [class*="rounded-full px-3"]');
        chips.forEach(c => {
          c.onclick = () => {
            playTactileFeedback('click');
            chips.forEach(x => x.classList.remove('bg-primary', 'text-on-primary'));
            c.classList.add('bg-primary', 'text-on-primary');
            showToast(`Payback date: ${c.textContent.trim()}`);
          };
        });
      },

      28: function() {
        const view = document.getElementById('screen-view-28');
        if (!view) return;
        let arjunAmt = 60;
        const arjunVal = view.querySelector('#arjun-val');
        const decBtn = view.querySelector('#btn-dec-arjun');
        const incBtn = view.querySelector('#btn-inc-arjun');
        const ring = view.querySelector('#pool-progress-ring');
        function updatePool() {
          if (arjunVal) arjunVal.textContent = `₹${arjunAmt}`;
          if (ring) {
            const offset = 427.26 - (arjunAmt / 120) * 427.26;
            ring.style.strokeDashoffset = offset;
          }
        }
        if (decBtn) {
          decBtn.onclick = () => {
            if (arjunAmt > 10) { arjunAmt -= 10; playTactileFeedback('click'); updatePool(); }
          };
        }
        if (incBtn) {
          incBtn.onclick = () => {
            if (arjunAmt < 120) { arjunAmt += 10; playTactileFeedback('click'); updatePool(); }
          };
        }
      },

      30: function() {
        const view = document.getElementById('screen-view-30');
        if (!view) return;
        const cards = view.querySelectorAll('.substitute-card, [class*="border p-"]');
        const voteBtn = view.querySelector('#vote-btn');
        cards.forEach(card => {
          card.onclick = () => {
            playTactileFeedback('click');
            cards.forEach(c => c.classList.remove('border-2', 'border-secondary', 'bg-secondary-container/10'));
            card.classList.add('border-2', 'border-secondary', 'bg-secondary-container/10');
            if (voteBtn) voteBtn.textContent = 'CONFIRM VOTE (3/4 ACCEPTED) →';
            showToast(`Selected substitute: ${card.textContent.trim().split('\n')[0]}`);
          };
        });
      },

      34: function() {
        const view = document.getElementById('screen-view-34');
        if (!view) return;
        const items = view.querySelectorAll('.item-checkbox, input[type="checkbox"], [class*="flex items-center gap-3 p-"]');
        const counterTag = view.querySelector('#counter-tag');
        items.forEach(item => {
          item.onclick = () => {
            playTactileFeedback('click');
            item.classList.toggle('line-through');
            item.classList.toggle('opacity-50');
            const checked = view.querySelectorAll('.line-through').length;
            if (counterTag) counterTag.textContent = `${5 - checked}/5 VERIFIED`;
          };
        });
      },

      35: function() {
        const view = document.getElementById('screen-view-35');
        if (!view) return;
        const pills = view.querySelectorAll('[id*="pill-"], [class*="rounded-full px-2.5"]');
        pills.forEach(p => {
          p.onclick = () => {
            playTactileFeedback('click');
            pills.forEach(x => x.classList.remove('bg-error', 'text-on-error', 'bg-primary', 'text-on-primary'));
            p.classList.add('bg-primary', 'text-on-primary');
            showToast(`Reason: ${p.textContent.trim()}`);
          };
        });
        const photoBtn = view.querySelector('#photo-dropzone') || view.querySelector('button[class*="border-dashed"]');
        if (photoBtn) {
          photoBtn.onclick = () => {
            playTactileFeedback('success');
            photoBtn.innerHTML = '<span class="material-symbols-outlined text-secondary text-2xl">check_circle</span> <span class="text-xs font-bold text-secondary">PHOTO_ATTACHED.JPG (1.2 MB)</span>';
            showToast('Photo proof uploaded! ✓');
          };
        }
      },

      36: function() {
        const view = document.getElementById('screen-view-36');
        if (!view) return;
        const filterBtns = view.querySelectorAll('.filter-btn, [class*="px-3 py-1.5"]');
        filterBtns.forEach(btn => {
          btn.onclick = () => {
            playTactileFeedback('click');
            filterBtns.forEach(b => b.classList.remove('bg-primary', 'text-on-primary'));
            btn.classList.add('bg-primary', 'text-on-primary');
            showToast(`Showing: ${btn.textContent.trim()}`);
          };
        });
      },

      37: function() {
        const view = document.getElementById('screen-view-37');
        if (!view) return;
        const remindBtns = view.querySelectorAll('button');
        remindBtns.forEach(b => {
          if (b.textContent.includes('REMIND') || b.textContent.includes('NUDGE')) {
            b.onclick = () => {
              playTactileFeedback('nudge');
              showToast('Payment reminder sent to Kabir on WhatsApp! 🔔');
            };
          }
        });
      }
    };

    // Keyboard Shortcuts
    document.addEventListener('keydown', function(e) {
      if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') return;
      if (e.key === 'ArrowRight' || e.key === ' ') {
        e.preventDefault();
        window.nextScreen();
      } else if (e.key === 'ArrowLeft') {
        e.preventDefault();
        window.prevScreen();
      } else if (e.key.toLowerCase() === 'm') {
        window.toggleNativeMobile();
      } else if (e.key.toLowerCase() === 's') {
        window.toggleSound();
      } else if (e.key === 'Escape') {
        window.closeDrawer();
        window.closeInstructions();
      }
    });

    // Populate screens drawer
    function buildScreensDrawer() {
      const drawerList = document.getElementById('drawer-screens-list');
      if (!drawerList) return;
      drawerList.innerHTML = '';

      let currentPhase = null;
      Object.keys(window.SCREENS_DATA).forEach(numStr => {
        const num = parseInt(numStr, 10);
        const item = window.SCREENS_DATA[num];

        if (item.phase !== currentPhase) {
          currentPhase = item.phase;
          const phaseHeader = document.createElement('div');
          phaseHeader.className = 'px-3 py-2 text-[10px] uppercase font-bold tracking-wider text-outline bg-[#1c1e1c] rounded mt-2 first:mt-0';
          phaseHeader.textContent = currentPhase;
          drawerList.appendChild(phaseHeader);
        }

        const btn = document.createElement('button');
        btn.className = `w-full text-left px-3 py-2 rounded-lg flex items-center justify-between text-xs hover:bg-[#282a28] transition-colors ${num === window.currentScreen ? 'bg-secondary/20 text-secondary font-bold' : 'text-zinc-300'}`;
        btn.onclick = () => { window.goToScreen(num); window.closeDrawer(); };
        btn.innerHTML = `
          <div class="flex items-center gap-2">
            <span class="font-mono text-[11px] opacity-60">${String(num).padStart(2, '0')}</span>
            <span class="truncate max-w-[200px]">${item.title}</span>
          </div>
          <span class="text-[9px] uppercase tracking-wider px-1.5 py-0.5 rounded bg-[#202220] text-outline font-mono">${item.tag}</span>
        `;
        drawerList.appendChild(btn);
      });
    }

    // App Initialization
    window.addEventListener('DOMContentLoaded', function() {
      updateClock();
      setInterval(updateClock, 30000);
      buildScreensDrawer();
      updateDockUI();

      // Initialize first screen controller
      if (window.ScreenControllers && window.ScreenControllers[1]) {
        window.ScreenControllers[1]();
      }

      // Universal click & delegation handler
      const screenContainer = document.getElementById('phone-screen');
      if (!screenContainer) return;

      screenContainer.addEventListener('click', function(e) {
        const btn = e.target.closest('button, a, [data-path], input[type="button"], [class*="cursor-pointer"]');
        if (!btn) return;

        playTactileFeedback('click');

        // 1. Bottom Navigation Tabs
        const path = btn.getAttribute('data-path');
        if (path) {
          e.preventDefault();
          if (path === 'carts') window.goToScreen(7);
          else if (path === 'orders') window.goToScreen(36);
          else if (path === 'ledger') window.goToScreen(37);
          else if (path === 'flat') window.goToScreen(9);
          return;
        }

        // 2. Back Chevrons
        const txt = btn.textContent.trim().toUpperCase();
        const hasBack = btn.querySelector('.material-symbols-outlined')?.textContent.trim() === 'arrow_back' || txt === 'ARROW_BACK';
        if (hasBack || btn.getAttribute('data-back')) {
          e.preventDefault();
          window.prevScreen();
          return;
        }

        // 3. Screen Specific Flows
        const sNum = window.currentScreen;
        if (sNum === 1 && (txt.includes('GET STARTED') || txt.includes('I HAVE AN ACCOUNT'))) {
          e.preventDefault();
          window.goToScreen(2);
        } else if (sNum === 2 && txt.includes('VERIFY')) {
          e.preventDefault();
          showToast('OTP Verified: +91 98765 43210 ✓');
          window.goToScreen(3);
        } else if (sNum === 3 && txt.includes('CONTINUE')) {
          e.preventDefault();
          window.goToScreen(4);
        } else if (sNum === 4 && txt.includes('CONTINUE')) {
          e.preventDefault();
          window.goToScreen(5);
        } else if (sNum === 5 && (txt.includes('CREATE') || txt.includes('JOIN') || txt.includes('CONFIRM'))) {
          e.preventDefault();
          showToast('Joined Flat 402!');
          window.goToScreen(6);
        } else if (sNum === 6 && (txt.includes('CONFIRM') || txt.includes('GO TO FLAT') || txt.includes('DONE'))) {
          e.preventDefault();
          window.goToScreen(7);
        } else if (sNum === 7 && (txt.includes('NEW CART') || txt.includes('+ NEW CART'))) {
          e.preventDefault();
          window.goToScreen(11);
        } else if (sNum === 8 && (txt.includes('NEW CART') || txt.includes('QUICK START'))) {
          e.preventDefault();
          window.goToScreen(11);
        } else if (sNum === 9 && txt.includes('INVITE')) {
          e.preventDefault();
          window.goToScreen(12);
        } else if (sNum === 11 && (txt.includes('START') || txt.includes('CREATE') || txt.includes('NEXT'))) {
          e.preventDefault();
          window.goToScreen(12);
        } else if (sNum === 12 && (txt.includes('START') || txt.includes('SHOPPING') || txt.includes('BROWSE'))) {
          e.preventDefault();
          window.goToScreen(13);
        } else if (sNum === 13 && (txt.includes('VIEW CART') || txt.includes('CART'))) {
          e.preventDefault();
          window.goToScreen(16);
        } else if (sNum === 14 && txt.includes('VIEW CART')) {
          e.preventDefault();
          window.goToScreen(16);
        } else if (sNum === 15 && (txt.includes('ADD TO CART') || txt.includes('CONFIRM'))) {
          e.preventDefault();
          showToast('Item added to Flat 402 cart!');
          window.goToScreen(16);
        } else if (sNum === 16 && (txt.includes('LOCK CART') || txt.includes('READY') || txt.includes('CHECKOUT'))) {
          e.preventDefault();
          window.goToScreen(17);
        } else if (sNum === 17 && txt.includes('CONFIRM')) {
          e.preventDefault();
          window.goToScreen(18);
        } else if (sNum === 18 && (txt.includes('CONFIRM') || txt.includes('SHARES'))) {
          e.preventDefault();
          showToast('Prorated shares locked!');
          window.goToScreen(19);
        } else if (sNum === 19 && (txt.includes('PAY') || txt.includes('PROCEED'))) {
          e.preventDefault();
          window.goToScreen(20);
        } else if (sNum === 20 && (txt.includes('GPAY') || txt.includes('PHONEPE') || txt.includes('PAY'))) {
          e.preventDefault();
          window.goToScreen(21);
        } else if (sNum === 21) {
          e.preventDefault();
          window.goToScreen(22);
        } else if (sNum === 22) {
          if (txt.includes('VIEW PAYMENT STATUS') || txt.includes('STATUS')) {
            e.preventDefault();
            window.goToScreen(25);
          } else if (txt.includes('SPOT HER') || txt.includes('SPOT')) {
            e.preventDefault();
            window.goToScreen(26);
          } else if (txt.includes('HOME') || txt.includes('DONE')) {
            e.preventDefault();
            window.goToScreen(7);
          }
        } else if (sNum === 23 && txt.includes('TRY AGAIN')) {
          e.preventDefault();
          window.goToScreen(21);
        } else if (sNum === 24 && txt.includes('REVIVE')) {
          e.preventDefault();
          window.goToScreen(32);
        } else if (sNum === 25 && txt.includes('LEDGER')) {
          e.preventDefault();
          window.goToScreen(37);
        } else if (sNum === 27 && (txt.includes('APPROVE') || txt.includes('CONFIRM') || txt.includes('SPOT'))) {
          e.preventDefault();
          showToast('Spot Me recorded in Flat Ledger!');
          window.goToScreen(22);
        } else if (sNum === 28 && (txt.includes('POOL') || txt.includes('CONTRIBUTE') || txt.includes('USE'))) {
          e.preventDefault();
          showToast('₹120 covered from Flat Pool!');
          window.goToScreen(22);
        } else if (sNum === 29 && (txt.includes('DROP') || txt.includes('DISPATCH'))) {
          e.preventDefault();
          showToast('Non-essential items dropped. Dispatching haul!');
          window.goToScreen(33);
        } else if (sNum === 30 && (txt.includes('VOTE') || txt.includes('ACCEPT'))) {
          e.preventDefault();
          showToast('Substitution approved!');
          window.goToScreen(19);
        } else if (sNum === 31 && txt.includes('ACCEPT')) {
          e.preventDefault();
          window.goToScreen(19);
        } else if (sNum === 32 && txt.includes('REVIVE')) {
          e.preventDefault();
          showToast('Cart revived!');
          window.goToScreen(16);
        } else if (sNum === 33 && (txt.includes('DELIVERED') || txt.includes('COLLECT') || txt.includes('GATE'))) {
          e.preventDefault();
          window.goToScreen(34);
        } else if (sNum === 34) {
          if (txt.includes('EVERYTHING') || txt.includes('CONFIRM')) {
            e.preventDefault();
            window.goToScreen(36);
          } else if (txt.includes('MISSING') || txt.includes('ISSUE')) {
            e.preventDefault();
            window.goToScreen(35);
          }
        } else if (sNum === 35 && (txt.includes('SUBMIT') || txt.includes('CLAIM'))) {
          e.preventDefault();
          showToast('Claim submitted! ₹56 credited to Flat Ledger.');
          window.goToScreen(37);
        } else if (sNum === 36 && txt.includes('FLAT 402')) {
          e.preventDefault();
          window.goToScreen(33);
        } else if (sNum === 37) {
          if (txt.includes('SETTLE') || txt.includes('UPI')) {
            e.preventDefault();
            window.goToScreen(21);
          } else if (txt.includes('BATCH')) {
            e.preventDefault();
            window.goToScreen(38);
          }
        } else if (sNum === 38 && (txt.includes('JOIN') || txt.includes('BATCH'))) {
          e.preventDefault();
          showToast('Joined Floor Batch! Saved ₹60 delivery fee.');
          window.goToScreen(11);
        }
      });
    });

    if (window.innerWidth <= 640) {
      window.toggleNativeMobile();
    }
  </script>
</body>
</html>
"""

# Replace existing script in html
pattern = r'<script>\s*// Screen Registry.*?</html>'
updated_html = re.sub(pattern, lambda _: new_script, html, flags=re.DOTALL)

with open('live_runtime_template.html', 'w', encoding='utf-8') as f:
    f.write(updated_html)

print("Updated live_runtime_template.html successfully!")
