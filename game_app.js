/**
 * Puzzle Game Center - Trung Tâm Trò Chơi Tiếng Anh
 * Chế độ 1: Word Scramble Puzzle (Ghép chữ cái giải đố V1-V2-V3)
 * Chế độ 2: Triplet Match Puzzle (Ghép nối bộ ba V1 - V2 - V3)
 * Chế độ 3: Word Search 10x10 (Trò chơi khoanh chữ ma trận 10x10)
 */

(function () {
  'use strict';

  // 1. Web Audio API Sound Synthesizer (Zero-latency, no external files)
  let audioCtx = null;
  function getAudioContext() {
    if (!audioCtx) {
      const AudioCtx = window.AudioContext || window.webkitAudioContext;
      if (AudioCtx) audioCtx = new AudioCtx();
    }
    if (audioCtx && audioCtx.state === 'suspended') {
      audioCtx.resume();
    }
    return audioCtx;
  }

  const Sound = {
    playPop() {
      try {
        const ctx = getAudioContext();
        if (!ctx) return;
        const osc = ctx.createOscillator();
        const gain = ctx.createGain();
        osc.type = 'sine';
        osc.frequency.setValueAtTime(450, ctx.currentTime);
        osc.frequency.exponentialRampToValueAtTime(700, ctx.currentTime + 0.06);
        gain.gain.setValueAtTime(0.15, ctx.currentTime);
        gain.gain.exponentialRampToValueAtTime(0.01, ctx.currentTime + 0.06);
        osc.connect(gain);
        gain.connect(ctx.destination);
        osc.start();
        osc.stop(ctx.currentTime + 0.06);
      } catch (e) {}
    },

    playCorrect() {
      try {
        const ctx = getAudioContext();
        if (!ctx) return;
        const notes = [523.25, 659.25, 783.99, 1046.50]; // C5, E5, G5, C6
        notes.forEach((freq, idx) => {
          const osc = ctx.createOscillator();
          const gain = ctx.createGain();
          osc.type = 'triangle';
          osc.frequency.setValueAtTime(freq, ctx.currentTime + idx * 0.07);
          gain.gain.setValueAtTime(0.2, ctx.currentTime + idx * 0.07);
          gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + idx * 0.07 + 0.25);
          osc.connect(gain);
          gain.connect(ctx.destination);
          osc.start(ctx.currentTime + idx * 0.07);
          osc.stop(ctx.currentTime + idx * 0.07 + 0.25);
        });
      } catch (e) {}
    },

    playWrong() {
      try {
        const ctx = getAudioContext();
        if (!ctx) return;
        const osc = ctx.createOscillator();
        const gain = ctx.createGain();
        osc.type = 'sawtooth';
        osc.frequency.setValueAtTime(220, ctx.currentTime);
        osc.frequency.linearRampToValueAtTime(140, ctx.currentTime + 0.2);
        gain.gain.setValueAtTime(0.15, ctx.currentTime);
        gain.gain.exponentialRampToValueAtTime(0.01, ctx.currentTime + 0.2);
        osc.connect(gain);
        gain.connect(ctx.destination);
        osc.start();
        osc.stop(ctx.currentTime + 0.2);
      } catch (e) {}
    },

    playWin() {
      try {
        const ctx = getAudioContext();
        if (!ctx) return;
        const melody = [
          { f: 523.25, d: 0.12 },
          { f: 659.25, d: 0.12 },
          { f: 783.99, d: 0.12 },
          { f: 1046.50, d: 0.35 }
        ];
        let t = ctx.currentTime;
        melody.forEach(m => {
          const osc = ctx.createOscillator();
          const gain = ctx.createGain();
          osc.type = 'triangle';
          osc.frequency.setValueAtTime(m.f, t);
          gain.gain.setValueAtTime(0.25, t);
          gain.gain.exponentialRampToValueAtTime(0.001, t + m.d);
          osc.connect(gain);
          gain.connect(ctx.destination);
          osc.start(t);
          osc.stop(t + m.d);
          t += m.d + 0.02;
        });
      } catch (e) {}
    }
  };

  // Helper to pronounce word
  function speak(text) {
    if (!('speechSynthesis' in window)) return;
    window.speechSynthesis.cancel();
    const u = new SpeechSynthesisUtterance(text);
    u.lang = document.getElementById('accent-select')?.value || 'en-US';
    u.rate = 0.95;
    window.speechSynthesis.speak(u);
  }

  // 2. Confetti Particle Burst
  function triggerConfetti(x, y) {
    const canvas = document.getElementById('game-confetti-canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    canvas.width = canvas.parentElement.clientWidth;
    canvas.height = canvas.parentElement.clientHeight;

    const particles = [];
    const colors = ['#3b82f6', '#10b981', '#f59e0b', '#ec4899', '#8b5cf6', '#06b6d4'];

    const originX = x || canvas.width / 2;
    const originY = y || canvas.height / 3;

    for (let i = 0; i < 45; i++) {
      particles.push({
        x: originX,
        y: originY,
        vx: (Math.random() - 0.5) * 10,
        vy: (Math.random() - 0.7) * 12,
        size: Math.random() * 6 + 4,
        color: colors[Math.floor(Math.random() * colors.length)],
        rotation: Math.random() * 360,
        vRot: (Math.random() - 0.5) * 10,
        alpha: 1
      });
    }

    let frame = 0;
    function animate() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      particles.forEach(p => {
        p.x += p.vx;
        p.y += p.vy;
        p.vy += 0.35; // gravity
        p.rotation += p.vRot;
        p.alpha -= 0.02;

        ctx.save();
        ctx.globalAlpha = Math.max(0, p.alpha);
        ctx.translate(p.x, p.y);
        ctx.rotate((p.rotation * Math.PI) / 180);
        ctx.fillStyle = p.color;
        ctx.fillRect(-p.size / 2, -p.size / 2, p.size, p.size);
        ctx.restore();
      });

      frame++;
      if (frame < 60) {
        requestAnimationFrame(animate);
      } else {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
      }
    }
    animate();
  }

  // 3. Game Center State
  const GameState = {
    activeMode: 'scramble', // 'scramble', 'triplet', or 'wordsearch'
    score: 0,
    streak: 0,
    highScore: parseInt(localStorage.getItem('verb360_puzzle_highscore') || '0'),

    // --- Scramble Mode State ---
    scrambleCurrent: null, // verb object
    scrambleTargetForm: 'v2', // 'v1', 'v2', 'v3'
    scrambleWord: '', // string
    scrambleTiles: [], // array of { id, char, used }
    scrambleSlots: [], // array of { index, tileId, char }
    scrambleHistory: new Set(),

    // --- Triplet Match Mode State ---
    tripletSets: [], // 4 verbs selected
    tripletCards: [], // 12 cards { id, verbId, form, text, matched, selected }
    tripletSelected: [], // array of card objects
    tripletMatchesFound: 0,
    tripletTimer: 0,
    tripletInterval: null,
    tripletMoves: 0,

    // --- Word Search 10x10 State ---
    wsGridSize: 10,
    wsGrid: [], // 10x10 array of characters
    wsWords: [], // array of { word, verb, form, meaning, found, cells: [[r, c], ...], colorClass }
    wsFoundCount: 0,
    wsSelectedCells: [], // [[r, c], ...]
    wsStartCell: null, // { r, c }
    wsIsDragging: false,
    wsTimer: 0,
    wsInterval: null
  };

  // 4. Main Controller
  const GameApp = {
    initialized: false,

    init() {
      const verbs = window.IRREGULAR_VERBS || [];
      if (!verbs.length) return;

      this.updateScoreUI();

      if (!this.initialized) {
        this.setupEventListeners();
        this.initialized = true;
      }

      if (GameState.activeMode === 'scramble') {
        this.startNewScrambleRound();
      } else {
        this.startNewTripletGame();
      }
    },

    updateScoreUI() {
      const scoreEl = document.getElementById('game-score-display');
      const streakEl = document.getElementById('game-streak-display');
      const highEl = document.getElementById('game-highscore-display');
      if (scoreEl) scoreEl.textContent = GameState.score;
      if (streakEl) streakEl.innerHTML = `<i class="fa-solid fa-fire text-amber-500 mr-1"></i>Streak: ${GameState.streak}`;
      if (highEl) highEl.textContent = `Kỷ lục: ${GameState.highScore}`;
    },

    addScore(points) {
      GameState.score += points;
      GameState.streak += 1;
      if (GameState.score > GameState.highScore) {
        GameState.highScore = GameState.score;
        localStorage.setItem('verb360_puzzle_highscore', GameState.highScore.toString());
      }
      this.updateScoreUI();
    },

    resetStreak() {
      GameState.streak = 0;
      this.updateScoreUI();
    },

    setupEventListeners() {
      // Switch game mode buttons
      const btnScramble = document.getElementById('game-mode-scramble-btn');
      const btnTriplet = document.getElementById('game-mode-triplet-btn');
      const btnWordSearch = document.getElementById('game-mode-wordsearch-btn');

      if (btnScramble) {
        btnScramble.addEventListener('click', () => {
          this.switchGameMode('scramble');
        });
      }
      if (btnTriplet) {
        btnTriplet.addEventListener('click', () => {
          this.switchGameMode('triplet');
        });
      }
      if (btnWordSearch) {
        btnWordSearch.addEventListener('click', () => {
          this.switchGameMode('wordsearch');
        });
      }

      // --- Scramble Mode Controls ---
      const shuffleBtn = document.getElementById('scramble-shuffle-btn');
      const clearBtn = document.getElementById('scramble-clear-btn');
      const hintBtn = document.getElementById('scramble-hint-btn');
      const skipBtn = document.getElementById('scramble-skip-btn');

      if (shuffleBtn) shuffleBtn.addEventListener('click', () => this.shuffleScrambleTiles());
      if (clearBtn) clearBtn.addEventListener('click', () => this.clearScrambleSlots());
      if (hintBtn) hintBtn.addEventListener('click', () => this.giveScrambleHint());
      if (skipBtn) skipBtn.addEventListener('click', () => {
        Sound.playWrong();
        this.resetStreak();
        this.startNewScrambleRound();
      });

      // Keyboard typing support for Scramble mode
      window.addEventListener('keydown', (e) => {
        const gameSection = document.getElementById('games-view');
        if (!gameSection || gameSection.classList.contains('hidden')) return;
        if (GameState.activeMode !== 'scramble') return;

        if (e.key === 'Backspace') {
          this.removeLastScrambleSlot();
          return;
        }

        const char = e.key.toUpperCase();
        if (/^[A-Z]$/.test(char)) {
          // Find first unused tile with this char
          const tile = GameState.scrambleTiles.find(t => !t.used && t.char === char);
          if (tile) {
            this.placeScrambleTile(tile);
          }
        }
      });

      // --- Triplet Mode Controls ---
      const restartTripletBtn = document.getElementById('triplet-restart-btn');
      if (restartTripletBtn) {
        restartTripletBtn.addEventListener('click', () => this.startNewTripletGame());
      }

      // --- Word Search 10x10 Mode Controls ---
      const restartWsBtn = document.getElementById('ws-restart-btn');
      const hintWsBtn = document.getElementById('ws-hint-btn');
      if (restartWsBtn) {
        restartWsBtn.addEventListener('click', () => this.startNewWordSearchGame());
      }
      if (hintWsBtn) {
        hintWsBtn.addEventListener('click', () => this.giveWordSearchHint());
      }
    },

    switchGameMode(mode) {
      GameState.activeMode = mode;
      const btnScramble = document.getElementById('game-mode-scramble-btn');
      const btnTriplet = document.getElementById('game-mode-triplet-btn');
      const btnWordSearch = document.getElementById('game-mode-wordsearch-btn');
      const scrambleWrapper = document.getElementById('game-scramble-wrapper');
      const tripletWrapper = document.getElementById('game-triplet-wrapper');
      const wsWrapper = document.getElementById('game-wordsearch-wrapper');

      [btnScramble, btnTriplet, btnWordSearch].forEach(b => {
        if (b) {
          b.classList.remove('bg-white', 'dark:bg-slate-700', 'shadow-sm', 'text-emerald-700', 'dark:text-emerald-300', 'text-indigo-600', 'dark:text-indigo-400', 'text-amber-600', 'dark:text-amber-400');
          b.classList.add('text-white/80');
        }
      });

      const activeBtn = mode === 'scramble' ? btnScramble : mode === 'triplet' ? btnTriplet : btnWordSearch;
      if (activeBtn) {
        activeBtn.classList.add('bg-white', 'dark:bg-slate-700', 'shadow-sm', 'text-emerald-700', 'dark:text-emerald-300');
        activeBtn.classList.remove('text-white/80');
      }

      if (scrambleWrapper) scrambleWrapper.classList.toggle('hidden', mode !== 'scramble');
      if (tripletWrapper) tripletWrapper.classList.toggle('hidden', mode !== 'triplet');
      if (wsWrapper) wsWrapper.classList.toggle('hidden', mode !== 'wordsearch');

      if (mode === 'scramble') {
        this.startNewScrambleRound();
      } else if (mode === 'triplet') {
        this.startNewTripletGame();
      } else if (mode === 'wordsearch') {
        this.startNewWordSearchGame();
      }
    },

    // ==========================================
    // GAME MODE 1: WORD SCRAMBLE PUZZLE
    // ==========================================
    startNewScrambleRound() {
      const verbs = window.IRREGULAR_VERBS || [];
      if (!verbs.length) return;

      // Pick a verb that has clean letters
      const candidates = verbs.filter(v => {
        const v1 = v.v1.trim();
        const v2 = v.v2.split('/')[0].trim();
        const v3 = v.v3.split('/')[0].trim();
        return !v1.includes(' ') && !v2.includes(' ') && !v3.includes(' ') &&
               v2.length >= 3 && v2.length <= 8;
      });

      const selectedVerb = candidates[Math.floor(Math.random() * candidates.length)];
      GameState.scrambleCurrent = selectedVerb;

      // Randomly choose target form: 50% V2 (Quá khứ), 40% V3 (Phân từ), 10% V1
      const rand = Math.random();
      let targetForm = 'v2';
      let targetLabel = 'V2 (Quá khứ đơn)';
      let targetWord = selectedVerb.v2.split('/')[0].trim().toUpperCase();

      if (rand > 0.6) {
        targetForm = 'v3';
        targetLabel = 'V3 (Quá khứ phân từ)';
        targetWord = selectedVerb.v3.split('/')[0].trim().toUpperCase();
      } else if (rand < 0.15) {
        targetForm = 'v1';
        targetLabel = 'V1 (Nguyên thể)';
        targetWord = selectedVerb.v1.trim().toUpperCase();
      }

      GameState.scrambleTargetForm = targetForm;
      GameState.scrambleWord = targetWord;

      // Display question hints
      const targetLabelEl = document.getElementById('scramble-target-label');
      const v1DisplayEl = document.getElementById('scramble-v1-display');
      const meaningEl = document.getElementById('scramble-meaning-display');
      const iconEl = document.getElementById('scramble-icon-display');
      const ipaEl = document.getElementById('scramble-ipa-display');
      const feedbackEl = document.getElementById('scramble-feedback');

      if (targetLabelEl) targetLabelEl.textContent = targetLabel;
      if (v1DisplayEl) v1DisplayEl.textContent = selectedVerb.v1.toUpperCase();
      if (meaningEl) meaningEl.textContent = selectedVerb.meaning;
      if (iconEl) iconEl.textContent = selectedVerb.icon || '🧩';
      if (ipaEl) ipaEl.textContent = selectedVerb.ipa || '';
      if (feedbackEl) feedbackEl.innerHTML = '';

      // Prepare Scramble Tiles (randomized order)
      const letters = targetWord.split('');
      const shuffled = [...letters].sort(() => Math.random() - 0.5);

      // Ensure it's not accidentally identical to the target word
      if (shuffled.join('') === targetWord && letters.length > 2) {
        shuffled.reverse();
      }

      GameState.scrambleTiles = shuffled.map((char, idx) => ({
        id: idx,
        char,
        used: false
      }));

      // Initialize Empty Slots
      GameState.scrambleSlots = new Array(targetWord.length).fill(null);

      this.renderScrambleSlots();
      this.renderScrambleTiles();
    },

    renderScrambleSlots() {
      const container = document.getElementById('scramble-slots-container');
      if (!container) return;

      container.innerHTML = GameState.scrambleSlots.map((slot, idx) => {
        if (slot) {
          return `
            <div class="scramble-slot-filled w-12 h-14 sm:w-14 sm:h-16 rounded-2xl bg-gradient-to-b from-indigo-500 to-indigo-700 text-white font-black text-2xl sm:text-3xl flex items-center justify-center shadow-lg shadow-indigo-500/25 border-2 border-indigo-400 cursor-pointer transform hover:scale-105 active:scale-95 transition-all animate-pop" data-slot-idx="${idx}">
              ${slot.char}
            </div>
          `;
        } else {
          return `
            <div class="scramble-slot-empty w-12 h-14 sm:w-14 sm:h-16 rounded-2xl border-2 border-dashed border-slate-300 dark:border-slate-700 bg-slate-100/50 dark:bg-slate-800/50 flex items-center justify-center transition-colors">
              <span class="w-3 h-1 bg-slate-300 dark:bg-slate-700 rounded-full"></span>
            </div>
          `;
        }
      }).join('');

      // Click on filled slot to return tile to pool
      container.querySelectorAll('.scramble-slot-filled').forEach(el => {
        el.addEventListener('click', () => {
          const slotIdx = parseInt(el.dataset.slotIdx);
          this.removeScrambleSlot(slotIdx);
        });
      });
    },

    renderScrambleTiles() {
      const container = document.getElementById('scramble-tiles-container');
      if (!container) return;

      container.innerHTML = GameState.scrambleTiles.map(tile => {
        if (tile.used) {
          return `
            <div class="w-12 h-14 sm:w-14 sm:h-16 rounded-2xl border border-slate-200 dark:border-slate-800 bg-slate-100/30 dark:bg-slate-900/30 opacity-20 pointer-events-none"></div>
          `;
        } else {
          return `
            <button class="scramble-tile-btn w-12 h-14 sm:w-14 sm:h-16 rounded-2xl bg-white dark:bg-slate-800 text-slate-800 dark:text-slate-100 font-black text-2xl sm:text-3xl flex items-center justify-center shadow-md hover:shadow-xl hover:-translate-y-1 hover:border-indigo-400 border-2 border-slate-200 dark:border-slate-700 transition-all btn-press" data-tile-id="${tile.id}">
              ${tile.char}
            </button>
          `;
        }
      }).join('');

      container.querySelectorAll('.scramble-tile-btn').forEach(btn => {
        btn.addEventListener('click', () => {
          const tileId = parseInt(btn.dataset.tileId);
          const tile = GameState.scrambleTiles.find(t => t.id === tileId);
          if (tile) this.placeScrambleTile(tile);
        });
      });
    },

    placeScrambleTile(tile) {
      // Find first empty slot
      const firstEmptyIdx = GameState.scrambleSlots.findIndex(s => s === null);
      if (firstEmptyIdx === -1) return;

      Sound.playPop();
      tile.used = true;
      GameState.scrambleSlots[firstEmptyIdx] = {
        tileId: tile.id,
        char: tile.char
      };

      this.renderScrambleSlots();
      this.renderScrambleTiles();

      // Check if all slots are filled
      if (!GameState.scrambleSlots.some(s => s === null)) {
        this.checkScrambleAnswer();
      }
    },

    removeScrambleSlot(slotIdx) {
      const slot = GameState.scrambleSlots[slotIdx];
      if (!slot) return;

      Sound.playPop();
      const tile = GameState.scrambleTiles.find(t => t.id === slot.tileId);
      if (tile) tile.used = false;

      GameState.scrambleSlots[slotIdx] = null;

      // Shift filled slots to the left for clean appearance
      const filled = GameState.scrambleSlots.filter(s => s !== null);
      GameState.scrambleSlots = new Array(GameState.scrambleWord.length).fill(null);
      filled.forEach((s, i) => {
        GameState.scrambleSlots[i] = s;
      });

      this.renderScrambleSlots();
      this.renderScrambleTiles();
    },

    removeLastScrambleSlot() {
      // Find last filled slot
      for (let i = GameState.scrambleSlots.length - 1; i >= 0; i--) {
        if (GameState.scrambleSlots[i] !== null) {
          this.removeScrambleSlot(i);
          return;
        }
      }
    },

    clearScrambleSlots() {
      Sound.playPop();
      GameState.scrambleTiles.forEach(t => t.used = false);
      GameState.scrambleSlots = new Array(GameState.scrambleWord.length).fill(null);
      this.renderScrambleSlots();
      this.renderScrambleTiles();
    },

    shuffleScrambleTiles() {
      Sound.playPop();
      // Only shuffle unused tiles
      const unusedChars = GameState.scrambleTiles.filter(t => !t.used).map(t => t.char);
      unusedChars.sort(() => Math.random() - 0.5);

      let uIdx = 0;
      GameState.scrambleTiles.forEach(t => {
        if (!t.used) {
          t.char = unusedChars[uIdx++];
        }
      });

      this.renderScrambleTiles();
    },

    giveScrambleHint() {
      // Find the first incorrect or empty slot
      const targetChars = GameState.scrambleWord.split('');
      let targetIdx = -1;

      for (let i = 0; i < targetChars.length; i++) {
        if (!GameState.scrambleSlots[i] || GameState.scrambleSlots[i].char !== targetChars[i]) {
          targetIdx = i;
          break;
        }
      }

      if (targetIdx === -1) return;

      // Clear that slot if filled with wrong char
      if (GameState.scrambleSlots[targetIdx]) {
        this.removeScrambleSlot(targetIdx);
      }

      const neededChar = targetChars[targetIdx];
      // Find an unused tile with this char
      const tile = GameState.scrambleTiles.find(t => !t.used && t.char === neededChar);
      if (tile) {
        this.placeScrambleTile(tile);
      }
    },

    checkScrambleAnswer() {
      const currentWord = GameState.scrambleSlots.map(s => s.char).join('');
      const isCorrect = (currentWord === GameState.scrambleWord);
      const feedbackEl = document.getElementById('scramble-feedback');

      if (isCorrect) {
        Sound.playCorrect();
        this.addScore(100 + GameState.streak * 10);
        triggerConfetti();

        const v = GameState.scrambleCurrent;
        speak(v[GameState.scrambleTargetForm] || v.v1);

        if (feedbackEl) {
          feedbackEl.innerHTML = `
            <div class="inline-flex items-center space-x-2 px-4 py-2 rounded-xl bg-emerald-100 dark:bg-emerald-950/80 text-emerald-700 dark:text-emerald-300 border border-emerald-300 font-extrabold text-sm animate-bounce">
              <i class="fa-solid fa-circle-check text-base"></i>
              <span>Chính xác! ${GameState.scrambleWord} (+${100 + (GameState.streak - 1) * 10} điểm)</span>
            </div>
          `;
        }

        // Auto next word after 1.2s
        setTimeout(() => {
          this.startNewScrambleRound();
        }, 1200);
      } else {
        Sound.playWrong();
        this.resetStreak();

        // Shake animation on slots container
        const slotsEl = document.getElementById('scramble-slots-container');
        if (slotsEl) {
          slotsEl.classList.add('animate-shake');
          setTimeout(() => slotsEl.classList.remove('animate-shake'), 500);
        }

        if (feedbackEl) {
          feedbackEl.innerHTML = `
            <div class="inline-flex items-center space-x-2 px-3.5 py-1.5 rounded-xl bg-rose-100 dark:bg-rose-950/80 text-rose-700 dark:text-rose-300 border border-rose-300 font-bold text-xs">
              <i class="fa-solid fa-circle-xmark"></i>
              <span>Chưa đúng rồi! Thử lại hoặc bấm "Gợi ý" nhé.</span>
            </div>
          `;
        }
      }
    },

    // ==========================================
    // GAME MODE 2: TRIPLET MATCH PUZZLE (V1 - V2 - V3)
    // ==========================================
    startNewTripletGame() {
      const verbs = window.IRREGULAR_VERBS || [];
      if (!verbs.length) return;

      // Stop existing timer
      if (GameState.tripletInterval) {
        clearInterval(GameState.tripletInterval);
      }
      GameState.tripletTimer = 0;
      GameState.tripletMoves = 0;
      GameState.tripletMatchesFound = 0;
      GameState.tripletSelected = [];

      // Update Timer UI
      this.updateTripletTimerUI();
      GameState.tripletInterval = setInterval(() => {
        GameState.tripletTimer++;
        this.updateTripletTimerUI();
      }, 1000);

      // Pick 4 distinct verbs with clear V1, V2, V3
      const pool = verbs.filter(v => {
        const v1 = v.v1.trim();
        const v2 = v.v2.split('/')[0].trim();
        const v3 = v.v3.split('/')[0].trim();
        // Ensure V1, V2, V3 are visibly distinct for fun puzzle
        return v1 !== v2 && v2 !== v3 && !v1.includes(' ') && !v2.includes(' ');
      }).sort(() => Math.random() - 0.5);

      const selectedVerbs = pool.slice(0, 4);
      GameState.tripletSets = selectedVerbs;

      // Create 12 cards (3 per verb: V1, V2, V3)
      const colors = [
        { bg: 'from-blue-500 to-indigo-600', ring: 'ring-blue-400' },
        { bg: 'from-emerald-500 to-teal-600', ring: 'ring-emerald-400' },
        { bg: 'from-amber-500 to-orange-600', ring: 'ring-amber-400' },
        { bg: 'from-purple-500 to-pink-600', ring: 'ring-purple-400' }
      ];

      const cards = [];
      selectedVerbs.forEach((verb, vIdx) => {
        const v1 = verb.v1.trim();
        const v2 = verb.v2.split('/')[0].trim();
        const v3 = verb.v3.split('/')[0].trim();

        cards.push({ id: `c_${vIdx}_1`, verbId: verb.id, form: 'V1', text: v1, verb, color: colors[vIdx] });
        cards.push({ id: `c_${vIdx}_2`, verbId: verb.id, form: 'V2', text: v2, verb, color: colors[vIdx] });
        cards.push({ id: `c_${vIdx}_3`, verbId: verb.id, form: 'V3', text: v3, verb, color: colors[vIdx] });
      });

      // Shuffle cards thoroughly
      GameState.tripletCards = cards.sort(() => Math.random() - 0.5);

      const winCard = document.getElementById('triplet-win-card');
      const board = document.getElementById('triplet-board-grid');
      if (winCard) winCard.classList.add('hidden');
      if (board) board.classList.remove('hidden');

      this.renderTripletBoard();
    },

    updateTripletTimerUI() {
      const timerEl = document.getElementById('triplet-timer-display');
      const movesEl = document.getElementById('triplet-moves-display');
      if (timerEl) {
        const min = Math.floor(GameState.tripletTimer / 60);
        const sec = GameState.tripletTimer % 60;
        timerEl.textContent = `${min.toString().padStart(2, '0')}:${sec.toString().padStart(2, '0')}`;
      }
      if (movesEl) {
        movesEl.textContent = `${GameState.tripletMoves} lượt`;
      }
    },

    renderTripletBoard() {
      const container = document.getElementById('triplet-board-grid');
      if (!container) return;

      container.innerHTML = GameState.tripletCards.map(card => {
        const isSelected = GameState.tripletSelected.some(c => c.id === card.id);
        const isMatched = card.matched;

        if (isMatched) {
          return `
            <div class="h-24 sm:h-28 rounded-2xl bg-slate-100 dark:bg-slate-800/40 border border-slate-200/60 dark:border-slate-700/40 p-3 flex flex-col items-center justify-center opacity-40 select-none">
              <span class="text-xs font-bold text-slate-400 uppercase">${card.form}</span>
              <span class="text-base sm:text-lg font-bold text-slate-400 line-through">${card.text}</span>
            </div>
          `;
        }

        return `
          <div class="triplet-tile group h-24 sm:h-28 rounded-2xl bg-white dark:bg-slate-800 p-3.5 flex flex-col items-center justify-between shadow-md hover:shadow-xl hover:-translate-y-1 transition-all duration-200 cursor-pointer border-2 ${isSelected ? 'border-indigo-600 dark:border-indigo-400 bg-indigo-50/80 dark:bg-indigo-950/60 ring-4 ring-indigo-400/30' : 'border-slate-200 dark:border-slate-700'} btn-press select-none" data-card-id="${card.id}">
            
            <div class="w-full flex items-center justify-between">
              <span class="px-2 py-0.5 rounded-md text-[10px] font-black uppercase tracking-wider ${card.form === 'V1' ? 'bg-blue-100 text-blue-700 dark:bg-blue-900/60 dark:text-blue-300' : card.form === 'V2' ? 'bg-rose-100 text-rose-700 dark:bg-rose-900/60 dark:text-rose-300' : 'bg-amber-100 text-amber-700 dark:bg-amber-900/60 dark:text-amber-300'}">
                ${card.form}
              </span>
              <span class="text-base">${card.verb.icon || '⚡'}</span>
            </div>

            <div class="text-lg sm:text-xl font-black text-slate-800 dark:text-white tracking-wide text-center">
              ${card.text}
            </div>

            <div class="text-[10px] text-slate-400 italic text-center truncate max-w-full">
              ${card.verb.meaning.split(',')[0]}
            </div>

          </div>
        `;
      }).join('');

      container.querySelectorAll('.triplet-tile').forEach(tile => {
        tile.addEventListener('click', () => {
          const cardId = tile.dataset.cardId;
          this.handleTripletCardClick(cardId);
        });
      });
    },

    handleTripletCardClick(cardId) {
      const card = GameState.tripletCards.find(c => c.id === cardId);
      if (!card || card.matched) return;

      Sound.playPop();

      // Check if already selected -> deselect
      const selIdx = GameState.tripletSelected.findIndex(c => c.id === cardId);
      if (selIdx > -1) {
        GameState.tripletSelected.splice(selIdx, 1);
        this.renderTripletBoard();
        return;
      }

      // Add to selected
      if (GameState.tripletSelected.length < 3) {
        GameState.tripletSelected.push(card);
        this.renderTripletBoard();
      }

      // Check match when 3 cards are selected
      if (GameState.tripletSelected.length === 3) {
        GameState.tripletMoves++;
        this.updateTripletTimerUI();
        this.checkTripletMatch();
      }
    },

    checkTripletMatch() {
      const [c1, c2, c3] = GameState.tripletSelected;
      const isSameVerb = (c1.verbId === c2.verbId && c2.verbId === c3.verbId);
      const forms = new Set([c1.form, c2.form, c3.form]);
      const hasAllThreeForms = forms.has('V1') && forms.has('V2') && forms.has('V3');

      if (isSameVerb && hasAllThreeForms) {
        // MATCH SUCCESS!
        Sound.playCorrect();
        this.addScore(250);
        triggerConfetti();

        c1.matched = true;
        c2.matched = true;
        c3.matched = true;
        GameState.tripletMatchesFound++;
        GameState.tripletSelected = [];

        // Speak the completed verb
        speak(`${c1.verb.v1}, ${c1.verb.v2}, ${c1.verb.v3}`);

        setTimeout(() => {
          this.renderTripletBoard();
          if (GameState.tripletMatchesFound === 4) {
            this.finishTripletGame();
          }
        }, 300);
      } else {
        // MATCH FAILED
        Sound.playWrong();
        setTimeout(() => {
          GameState.tripletSelected = [];
          this.renderTripletBoard();
        }, 600);
      }
    },

    finishTripletGame() {
      if (GameState.tripletInterval) {
        clearInterval(GameState.tripletInterval);
      }
      Sound.playWin();
      this.addScore(500); // completion bonus
      triggerConfetti();

      const winCard = document.getElementById('triplet-win-card');
      const board = document.getElementById('triplet-board-grid');
      if (board) board.classList.add('hidden');
      if (winCard) winCard.classList.remove('hidden');

      const min = Math.floor(GameState.tripletTimer / 60);
      const sec = GameState.tripletTimer % 60;
      const timeStr = `${min > 0 ? min + ' phút ' : ''}${sec} giây`;

      const finalTimeEl = document.getElementById('triplet-final-time');
      const finalMovesEl = document.getElementById('triplet-final-moves');
      if (finalTimeEl) finalTimeEl.textContent = timeStr;
      if (finalMovesEl) finalMovesEl.textContent = `${GameState.tripletMoves} lượt`;
    },

    // ==========================================
    // GAME MODE 3: WORD SEARCH 10x10 (KHOANH CHỮ 10x10)
    // ==========================================
    startNewWordSearchGame() {
      const verbs = window.IRREGULAR_VERBS || [];
      if (!verbs.length) return;

      // Stop existing timer
      if (GameState.wsInterval) {
        clearInterval(GameState.wsInterval);
      }
      GameState.wsTimer = 0;
      GameState.wsFoundCount = 0;
      GameState.wsSelectedCells = [];
      GameState.wsStartCell = null;
      GameState.wsIsDragging = false;

      this.updateWordSearchTimerUI();
      GameState.wsInterval = setInterval(() => {
        GameState.wsTimer++;
        this.updateWordSearchTimerUI();
      }, 1000);

      // Initialize 10x10 Empty Grid
      const size = GameState.wsGridSize; // 10
      const grid = Array.from({ length: size }, () => Array(size).fill(''));

      // Filter good candidate verbs (word length between 3 and 7, no spaces)
      const pool = verbs.filter(v => {
        const v1 = v.v1.trim();
        const v2 = v.v2.split('/')[0].trim();
        const v3 = v.v3.split('/')[0].trim();
        return !v1.includes(' ') && !v2.includes(' ') && !v3.includes(' ');
      }).sort(() => Math.random() - 0.5);

      const WS_COLORS = [
        'bg-emerald-300/90 dark:bg-emerald-800 text-emerald-950 dark:text-emerald-100 ring-2 ring-emerald-500',
        'bg-amber-300/90 dark:bg-amber-800 text-amber-950 dark:text-amber-100 ring-2 ring-amber-500',
        'bg-sky-300/90 dark:bg-sky-800 text-sky-950 dark:text-sky-100 ring-2 ring-sky-500',
        'bg-rose-300/90 dark:bg-rose-800 text-rose-950 dark:text-rose-100 ring-2 ring-rose-500',
        'bg-purple-300/90 dark:bg-purple-800 text-purple-950 dark:text-purple-100 ring-2 ring-purple-500',
        'bg-teal-300/90 dark:bg-teal-800 text-teal-950 dark:text-teal-100 ring-2 ring-teal-500',
        'bg-orange-300/90 dark:bg-orange-800 text-orange-950 dark:text-orange-100 ring-2 ring-orange-500'
      ];

      const placedWords = [];
      const directions = [
        [0, 1],   // Right
        [1, 0],   // Down
        [1, 1],   // Down-Right
        [-1, 1]   // Up-Right
      ];

      for (const verb of pool) {
        if (placedWords.length >= 7) break;

        // Choose random form: V1, V2, or V3
        const rChoice = Math.random();
        let wordStr = '';
        let formName = 'V1';
        if (rChoice > 0.6) {
          wordStr = verb.v3.split('/')[0].trim().toUpperCase();
          formName = 'V3';
        } else if (rChoice > 0.3) {
          wordStr = verb.v2.split('/')[0].trim().toUpperCase();
          formName = 'V2';
        } else {
          wordStr = verb.v1.trim().toUpperCase();
          formName = 'V1';
        }

        if (wordStr.length < 3 || wordStr.length > 7) continue;
        if (placedWords.some(w => w.word === wordStr)) continue;

        // Try placing in grid
        let placed = false;
        for (let attempt = 0; attempt < 100; attempt++) {
          const [dr, dc] = directions[Math.floor(Math.random() * directions.length)];
          const r = Math.floor(Math.random() * size);
          const c = Math.floor(Math.random() * size);

          const endR = r + dr * (wordStr.length - 1);
          const endC = c + dc * (wordStr.length - 1);

          if (endR >= 0 && endR < size && endC >= 0 && endC < size) {
            let canPlace = true;
            const cells = [];
            for (let i = 0; i < wordStr.length; i++) {
              const cr = r + dr * i;
              const cc = c + dc * i;
              cells.push([cr, cc]);
              if (grid[cr][cc] !== '' && grid[cr][cc] !== wordStr[i]) {
                canPlace = false;
                break;
              }
            }

            if (canPlace) {
              for (let i = 0; i < wordStr.length; i++) {
                const [cr, cc] = cells[i];
                grid[cr][cc] = wordStr[i];
              }

              placedWords.push({
                word: wordStr,
                verb,
                form: formName,
                meaning: verb.meaning.split(',')[0],
                found: false,
                cells,
                colorClass: WS_COLORS[placedWords.length % WS_COLORS.length]
              });
              placed = true;
              break;
            }
          }
        }
      }

      // Fill remaining empty cells with random letters
      const alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
      for (let r = 0; r < size; r++) {
        for (let c = 0; c < size; c++) {
          if (grid[r][c] === '') {
            grid[r][c] = alphabet[Math.floor(Math.random() * alphabet.length)];
          }
        }
      }

      GameState.wsGrid = grid;
      GameState.wsWords = placedWords;

      const winCard = document.getElementById('ws-win-card');
      const gameArea = document.getElementById('ws-active-area');
      if (winCard) winCard.classList.add('hidden');
      if (gameArea) gameArea.classList.remove('hidden');

      this.renderWordSearchBoard();
      this.renderWordSearchList();
    },

    updateWordSearchTimerUI() {
      const timerEl = document.getElementById('ws-timer-display');
      const foundEl = document.getElementById('ws-found-counter');
      if (timerEl) {
        const min = Math.floor(GameState.wsTimer / 60);
        const sec = GameState.wsTimer % 60;
        timerEl.textContent = `${min.toString().padStart(2, '0')}:${sec.toString().padStart(2, '0')}`;
      }
      if (foundEl) {
        foundEl.textContent = `${GameState.wsFoundCount} / ${GameState.wsWords.length} từ`;
      }
    },

    renderWordSearchBoard() {
      const container = document.getElementById('ws-grid-container');
      if (!container) return;

      const size = GameState.wsGridSize;
      const grid = GameState.wsGrid;

      // Map found cells to color classes
      const foundCellMap = new Map();
      GameState.wsWords.filter(w => w.found).forEach(w => {
        w.cells.forEach(([r, c]) => {
          foundCellMap.set(`${r},${c}`, w.colorClass);
        });
      });

      const selKeySet = new Set(GameState.wsSelectedCells.map(([r, c]) => `${r},${c}`));

      let html = '';
      for (let r = 0; r < size; r++) {
        for (let c = 0; c < size; c++) {
          const key = `${r},${c}`;
          const isSelected = selKeySet.has(key);
          const foundColor = foundCellMap.get(key);

          let cellClass = 'bg-white dark:bg-slate-800 text-slate-800 dark:text-slate-100 hover:bg-indigo-50 dark:hover:bg-slate-700';
          if (isSelected) {
            cellClass = 'bg-indigo-600 text-white font-black scale-95 shadow-md ring-2 ring-indigo-400';
          } else if (foundColor) {
            cellClass = foundColor + ' font-black';
          }

          html += `
            <button class="ws-cell aspect-square rounded-lg sm:rounded-xl border border-slate-200/80 dark:border-slate-700/80 flex items-center justify-center font-bold text-xs sm:text-base select-none transition-all cursor-pointer ${cellClass}"
                    data-r="${r}" data-c="${c}">
              ${grid[r][c]}
            </button>
          `;
        }
      }
      container.innerHTML = html;

      // Event listeners for cells (Mouse drag & Touch & Two-Click)
      container.querySelectorAll('.ws-cell').forEach(btn => {
        const r = parseInt(btn.dataset.r);
        const c = parseInt(btn.dataset.c);

        btn.addEventListener('mousedown', (e) => {
          e.preventDefault();
          this.handleWordSearchCellDown(r, c);
        });

        btn.addEventListener('mouseenter', () => {
          this.handleWordSearchCellEnter(r, c);
        });

        btn.addEventListener('mouseup', () => {
          this.handleWordSearchCellUp();
        });

        // Touch support
        btn.addEventListener('touchstart', (e) => {
          e.preventDefault();
          this.handleWordSearchCellDown(r, c);
        });
      });

      // Global mouse up to finish selection if dragged outside grid
      const handleGlobalUp = () => {
        if (GameState.wsIsDragging) {
          this.handleWordSearchCellUp();
        }
      };
      window.removeEventListener('mouseup', handleGlobalUp);
      window.addEventListener('mouseup', handleGlobalUp);
    },

    renderWordSearchList() {
      const container = document.getElementById('ws-word-list-container');
      if (!container) return;

      container.innerHTML = GameState.wsWords.map(w => {
        return `
          <div class="px-3.5 py-2.5 rounded-2xl border transition-all flex items-center justify-between ${w.found ? 'bg-emerald-50 dark:bg-emerald-950/60 border-emerald-300 dark:border-emerald-800 text-emerald-800 dark:text-emerald-300 line-through opacity-80' : 'bg-slate-50 dark:bg-slate-800/80 border-slate-200 dark:border-slate-700 text-slate-800 dark:text-slate-100'}">
            <div class="flex items-center space-x-2">
              <span class="w-5 h-5 rounded-md flex items-center justify-center text-xs font-bold ${w.found ? 'bg-emerald-500 text-white' : 'bg-slate-200 dark:bg-slate-700 text-slate-600 dark:text-slate-300'}">
                ${w.found ? '<i class="fa-solid fa-check text-[10px]"></i>' : w.form}
              </span>
              <span class="font-black text-sm tracking-wide">${w.word}</span>
            </div>
            <span class="text-xs text-slate-500 dark:text-slate-400 italic">${w.meaning}</span>
          </div>
        `;
      }).join('');
    },

    handleWordSearchCellDown(r, c) {
      // If no start cell yet: set start
      if (!GameState.wsStartCell) {
        Sound.playPop();
        GameState.wsStartCell = { r, c };
        GameState.wsIsDragging = true;
        GameState.wsSelectedCells = [[r, c]];
        this.renderWordSearchBoard();
      } else {
        // Two-click selection mode: second click
        const line = this.calculateLine(GameState.wsStartCell.r, GameState.wsStartCell.c, r, c);
        if (line && line.length > 1) {
          GameState.wsSelectedCells = line;
          this.checkWordSearchSelection();
        } else {
          // Reset start cell to current
          Sound.playPop();
          GameState.wsStartCell = { r, c };
          GameState.wsIsDragging = true;
          GameState.wsSelectedCells = [[r, c]];
          this.renderWordSearchBoard();
        }
      }
    },

    handleWordSearchCellEnter(r, c) {
      if (!GameState.wsIsDragging || !GameState.wsStartCell) return;
      const line = this.calculateLine(GameState.wsStartCell.r, GameState.wsStartCell.c, r, c);
      if (line) {
        GameState.wsSelectedCells = line;
        this.renderWordSearchBoard();
      }
    },

    handleWordSearchCellUp() {
      if (!GameState.wsIsDragging) return;
      GameState.wsIsDragging = false;
      if (GameState.wsSelectedCells.length > 1) {
        this.checkWordSearchSelection();
      }
    },

    calculateLine(r1, c1, r2, c2) {
      const dr = r2 - r1;
      const dc = c2 - c1;
      const stepR = dr === 0 ? 0 : dr > 0 ? 1 : -1;
      const stepC = dc === 0 ? 0 : dc > 0 ? 1 : -1;

      const isHoriz = (dr === 0 && dc !== 0);
      const isVert = (dc === 0 && dr !== 0);
      const isDiag = (Math.abs(dr) === Math.abs(dc) && dr !== 0);

      if (!isHoriz && !isVert && !isDiag) return null;

      const length = Math.max(Math.abs(dr), Math.abs(dc)) + 1;
      const cells = [];
      for (let i = 0; i < length; i++) {
        cells.push([r1 + stepR * i, c1 + stepC * i]);
      }
      return cells;
    },

    checkWordSearchSelection() {
      const cells = GameState.wsSelectedCells;
      if (!cells || cells.length < 2) {
        GameState.wsStartCell = null;
        GameState.wsSelectedCells = [];
        this.renderWordSearchBoard();
        return;
      }

      const grid = GameState.wsGrid;
      const forwardStr = cells.map(([r, c]) => grid[r][c]).join('');
      const reverseStr = cells.map(([r, c]) => grid[r][c]).reverse().join('');

      // Find matching unfound word
      const match = GameState.wsWords.find(w => !w.found && (w.word === forwardStr || w.word === reverseStr));

      if (match) {
        Sound.playCorrect();
        match.found = true;
        match.cells = cells;
        GameState.wsFoundCount++;
        this.addScore(150);
        triggerConfetti();

        speak(`${match.word}. ${match.meaning}`);

        GameState.wsStartCell = null;
        GameState.wsSelectedCells = [];
        this.updateWordSearchTimerUI();
        this.renderWordSearchBoard();
        this.renderWordSearchList();

        if (GameState.wsFoundCount === GameState.wsWords.length) {
          this.finishWordSearchGame();
        }
      } else {
        Sound.playWrong();
        GameState.wsStartCell = null;
        GameState.wsSelectedCells = [];
        this.renderWordSearchBoard();
      }
    },

    giveWordSearchHint() {
      const unfound = GameState.wsWords.find(w => !w.found);
      if (!unfound) return;

      Sound.playPop();
      const [startR, startC] = unfound.cells[0];
      const cellEl = document.querySelector(`.ws-cell[data-r="${startR}"][data-c="${startC}"]`);
      if (cellEl) {
        cellEl.classList.add('ring-4', 'ring-amber-400', 'animate-bounce');
        setTimeout(() => {
          cellEl.classList.remove('ring-4', 'ring-amber-400', 'animate-bounce');
        }, 2000);
      }
    },

    finishWordSearchGame() {
      if (GameState.wsInterval) {
        clearInterval(GameState.wsInterval);
      }
      Sound.playWin();
      this.addScore(500); // completion bonus
      triggerConfetti();

      const winCard = document.getElementById('ws-win-card');
      const gameArea = document.getElementById('ws-active-area');
      if (gameArea) gameArea.classList.add('hidden');
      if (winCard) winCard.classList.remove('hidden');

      const min = Math.floor(GameState.wsTimer / 60);
      const sec = GameState.wsTimer % 60;
      const timeStr = `${min > 0 ? min + ' phút ' : ''}${sec} giây`;

      const finalTimeEl = document.getElementById('ws-final-time');
      const finalCountEl = document.getElementById('ws-final-count');
      if (finalTimeEl) finalTimeEl.textContent = timeStr;
      if (finalCountEl) finalCountEl.textContent = `${GameState.wsWords.length} / ${GameState.wsWords.length} từ`;
    }
  };

  window.GameApp = GameApp;

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => GameApp.init());
  } else {
    GameApp.init();
  }
})();
