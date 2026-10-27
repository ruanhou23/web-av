/**
 * 360 English Irregular Verbs Learning Application
 * Complete Interactive System with Speech API, Quizzes, Flashcards, and Practice Modes
 */

(function () {
  'use strict';

  // 1. Audio System (Speech Synthesis & Web Audio API FX)
  const AudioService = {
    audioCtx: null,
    voice: null,
    speechRate: 0.9,
    accent: 'en-US',

    init() {
      try {
        const AudioContext = window.AudioContext || window.webkitAudioContext;
        if (AudioContext) {
          this.audioCtx = new AudioContext();
        }
      } catch (e) {
        console.warn('Web Audio API not supported', e);
      }
      this.loadVoices();
      if ('speechSynthesis' in window) {
        window.speechSynthesis.onvoiceschanged = () => this.loadVoices();
      }
    },

    loadVoices() {
      if (!('speechSynthesis' in window)) return;
      const voices = window.speechSynthesis.getVoices();
      if (!voices.length) return;

      const langPrefix = this.accent === 'en-GB' ? 'en-GB' : 'en-US';
      const targetVoice = voices.find(v => v.lang.startsWith(langPrefix)) ||
        voices.find(v => v.lang.startsWith('en')) || voices[0];
      this.voice = targetVoice;
    },

    setAccent(accent) {
      this.accent = accent;
      this.loadVoices();
    },

    setRate(rate) {
      this.speechRate = parseFloat(rate) || 0.9;
    },

    speak(text, lang = 'en-US') {
      if (!('speechSynthesis' in window) || !text) return;
      window.speechSynthesis.cancel(); // Cancel ongoing speech

      const cleanText = text.replace(/[\/\(\)]/g, ' ').trim();
      const utterance = new SpeechSynthesisUtterance(cleanText);
      utterance.rate = this.speechRate;
      utterance.pitch = 1.0;
      utterance.lang = this.accent;
      if (this.voice) {
        utterance.voice = this.voice;
      }
      window.speechSynthesis.speak(utterance);
    },

    playSuccessSound() {
      if (!this.audioCtx) return;
      try {
        const ctx = this.audioCtx;
        if (ctx.state === 'suspended') ctx.resume();
        const now = ctx.currentTime;
        const freqs = [523.25, 659.25, 783.99, 1046.50]; // C5, E5, G5, C6 arpeggio
        freqs.forEach((freq, idx) => {
          const osc = ctx.createOscillator();
          const gain = ctx.createGain();
          osc.type = 'sine';
          osc.frequency.setValueAtTime(freq, now + idx * 0.08);
          gain.gain.setValueAtTime(0.12, now + idx * 0.08);
          gain.gain.exponentialRampToValueAtTime(0.001, now + idx * 0.08 + 0.25);
          osc.connect(gain);
          gain.connect(ctx.destination);
          osc.start(now + idx * 0.08);
          osc.stop(now + idx * 0.08 + 0.25);
        });
      } catch (e) { }
    },

    playErrorSound() {
      if (!this.audioCtx) return;
      try {
        const ctx = this.audioCtx;
        if (ctx.state === 'suspended') ctx.resume();
        const now = ctx.currentTime;
        const osc = ctx.createOscillator();
        const gain = ctx.createGain();
        osc.type = 'triangle';
        osc.frequency.setValueAtTime(220, now);
        osc.frequency.linearRampToValueAtTime(150, now + 0.25);
        gain.gain.setValueAtTime(0.15, now);
        gain.gain.exponentialRampToValueAtTime(0.001, now + 0.3);
        osc.connect(gain);
        gain.connect(ctx.destination);
        osc.start(now);
        osc.stop(now + 0.3);
      } catch (e) { }
    },

    playClickSound() {
      if (!this.audioCtx) return;
      try {
        const ctx = this.audioCtx;
        if (ctx.state === 'suspended') ctx.resume();
        const now = ctx.currentTime;
        const osc = ctx.createOscillator();
        const gain = ctx.createGain();
        osc.type = 'sine';
        osc.frequency.setValueAtTime(800, now);
        gain.gain.setValueAtTime(0.05, now);
        gain.gain.exponentialRampToValueAtTime(0.001, now + 0.04);
        osc.connect(gain);
        gain.connect(ctx.destination);
        osc.start(now);
        osc.stop(now + 0.04);
      } catch (e) { }
    }
  };

  // Helper for Vietnamese non-accented string comparison
  function removeVietnameseTones(str) {
    if (!str) return '';
    return str
      .normalize('NFD')
      .replace(/[\u0300-\u036f]/g, '')
      .replace(/đ/g, 'd')
      .replace(/Đ/g, 'D')
      .toLowerCase();
  }

  // 2. Application Core State
  const AppState = {
    verbs: window.IRREGULAR_VERBS || [],
    filteredVerbs: [],
    searchQuery: '',
    activeFilter: 'all', // all, common, AAA, ABB, ABA, ABC, saved, mastered, review
    sortMode: 'id-asc',
    currentTab: 'explorer', // explorer, flashcards, quiz, typing, patterns
    explorerDisplay: 'grid', // grid or table
    displayLimit: 36, // chunked rendering for performance
    
    // User progress state (localStorage)
    savedIds: new Set(JSON.parse(localStorage.getItem('verb360_saved') || '[]')),
    masteredIds: new Set(JSON.parse(localStorage.getItem('verb360_mastered') || '[]')),
    reviewIds: new Set(JSON.parse(localStorage.getItem('verb360_review') || '[]')),
    
    // Flashcard state
    flashcardList: [],
    flashcardIndex: 0,
    isFlashcardFlipped: false,
    hideMeaningFlashcard: false,
    
    // Quiz state
    quizQuestions: [],
    quizIndex: 0,
    quizScore: 0,
    quizStreak: 0,
    quizMaxStreak: 0,
    quizMode: 'mix', // mix, v2, v3, meaning, sentence
    quizAnswered: false,
    quizSelectedOption: null,
    
    // Typing state
    typingVerb: null,
    typingIndex: 0,
    typingStatus: 'idle', // idle, correct, incorrect
    
    // Detail Modal
    modalVerb: null,

    saveProgress() {
      localStorage.setItem('verb360_saved', JSON.stringify([...this.savedIds]));
      localStorage.setItem('verb360_mastered', JSON.stringify([...this.masteredIds]));
      localStorage.setItem('verb360_review', JSON.stringify([...this.reviewIds]));
      this.updateStatsUI();
    },

    toggleSave(id) {
      if (this.savedIds.has(id)) {
        this.savedIds.delete(id);
      } else {
        this.savedIds.add(id);
      }
      this.saveProgress();
    },

    toggleMastered(id) {
      if (this.masteredIds.has(id)) {
        this.masteredIds.delete(id);
      } else {
        this.masteredIds.add(id);
        this.reviewIds.delete(id);
      }
      this.saveProgress();
    },

    toggleReview(id) {
      if (this.reviewIds.has(id)) {
        this.reviewIds.delete(id);
      } else {
        this.reviewIds.add(id);
        this.masteredIds.delete(id);
      }
      this.saveProgress();
    },

    updateStatsUI() {
      const elMastered = document.getElementById('stat-mastered');
      const elReview = document.getElementById('stat-review');
      const elSaved = document.getElementById('stat-saved');
      const elProgressPercent = document.getElementById('stat-percent');
      const elProgressBar = document.getElementById('stat-progress-bar');

      const masteredCount = this.masteredIds.size;
      const reviewCount = this.reviewIds.size;
      const savedCount = this.savedIds.size;
      const percent = Math.round((masteredCount / this.verbs.length) * 100);

      if (elMastered) elMastered.textContent = masteredCount;
      if (elReview) elReview.textContent = reviewCount;
      if (elSaved) elSaved.textContent = savedCount;
      if (elProgressPercent) elProgressPercent.textContent = `${percent}%`;
      if (elProgressBar) elProgressBar.style.width = `${percent}%`;
    }
  };

  // 3. UI Controller & View Renderers
  const UI = {
    init() {
      AudioService.init();
      AppState.updateStatsUI();
      this.setupEventListeners();
      this.applyFilterAndSearch();
      this.initTheme();
    },

    initTheme() {
      const isDark = localStorage.getItem('verb360_theme') === 'dark' ||
        (!('verb360_theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches);
      if (isDark) {
        document.documentElement.classList.add('dark');
      } else {
        document.documentElement.classList.remove('dark');
      }
      this.updateThemeButton();
    },

    toggleTheme() {
      const isDark = document.documentElement.classList.toggle('dark');
      localStorage.setItem('verb360_theme', isDark ? 'dark' : 'light');
      this.updateThemeButton();
    },

    updateThemeButton() {
      const isDark = document.documentElement.classList.contains('dark');
      const btn = document.getElementById('theme-toggle-btn');
      if (btn) {
        btn.innerHTML = isDark
          ? '<i class="fa-solid fa-sun text-amber-400 text-lg"></i>'
          : '<i class="fa-solid fa-moon text-slate-600 text-lg"></i>';
      }
    },

    setupEventListeners() {
      // Navigation Tabs
      document.querySelectorAll('[data-nav-tab]').forEach(tab => {
        tab.addEventListener('click', () => {
          const target = tab.dataset.navTab;
          this.switchTab(target);
        });
      });

      // Category Group Buttons (Gom nhóm danh mục)
      document.querySelectorAll('[data-group]').forEach(btn => {
        btn.addEventListener('click', () => {
          if (!btn.dataset.navTab) {
            const group = btn.dataset.group;
            if (group === 'verbs') this.switchTab('explorer');
            else if (group === 'practice') this.switchTab('games');
            else if (group === 'tenses') this.switchTab('tenses');
            else if (group === 'it') this.switchTab('it-english');
          }
        });
      });

      // Search input
      const searchInput = document.getElementById('search-input');
      if (searchInput) {
        searchInput.addEventListener('input', (e) => {
          AppState.searchQuery = e.target.value;
          AppState.displayLimit = 36;
          this.applyFilterAndSearch();
        });

        // Clear search
        const clearBtn = document.getElementById('clear-search-btn');
        if (clearBtn) {
          clearBtn.addEventListener('click', () => {
            searchInput.value = '';
            AppState.searchQuery = '';
            AppState.displayLimit = 36;
            this.applyFilterAndSearch();
            searchInput.focus();
          });
        }
      }

      // Filter pills
      document.querySelectorAll('[data-filter-btn]').forEach(btn => {
        btn.addEventListener('click', () => {
          document.querySelectorAll('[data-filter-btn]').forEach(b => {
            b.classList.remove('bg-blue-600', 'text-white', 'shadow-md');
            b.classList.add('bg-slate-100', 'dark:bg-slate-800', 'text-slate-700', 'dark:text-slate-300');
          });
          btn.classList.add('bg-blue-600', 'text-white', 'shadow-md');
          btn.classList.remove('bg-slate-100', 'dark:bg-slate-800', 'text-slate-700', 'dark:text-slate-300');

          AppState.activeFilter = btn.dataset.filterBtn;
          AppState.displayLimit = 36;
          this.applyFilterAndSearch();
        });
      });

      // View toggle (Grid vs Table)
      const viewGridBtn = document.getElementById('view-grid-btn');
      const viewTableBtn = document.getElementById('view-table-btn');
      if (viewGridBtn && viewTableBtn) {
        viewGridBtn.addEventListener('click', () => {
          AppState.explorerDisplay = 'grid';
          viewGridBtn.classList.add('bg-white', 'dark:bg-slate-700', 'shadow-sm', 'text-blue-600', 'dark:text-blue-400');
          viewTableBtn.classList.remove('bg-white', 'dark:bg-slate-700', 'shadow-sm', 'text-blue-600', 'dark:text-blue-400');
          this.renderExplorer();
        });
        viewTableBtn.addEventListener('click', () => {
          AppState.explorerDisplay = 'table';
          viewTableBtn.classList.add('bg-white', 'dark:bg-slate-700', 'shadow-sm', 'text-blue-600', 'dark:text-blue-400');
          viewGridBtn.classList.remove('bg-white', 'dark:bg-slate-700', 'shadow-sm', 'text-blue-600', 'dark:text-blue-400');
          this.renderExplorer();
        });
      }

      // Sort Mode selector
      const sortSelect = document.getElementById('sort-select');
      if (sortSelect) {
        sortSelect.addEventListener('change', (e) => {
          AppState.sortMode = e.target.value;
          this.applyFilterAndSearch();
        });
      }

      // Load more button
      const loadMoreBtn = document.getElementById('load-more-btn');
      if (loadMoreBtn) {
        loadMoreBtn.addEventListener('click', () => {
          AppState.displayLimit += 36;
          this.renderExplorer();
        });
      }

      // Theme toggle button
      const themeBtn = document.getElementById('theme-toggle-btn');
      if (themeBtn) {
        themeBtn.addEventListener('click', () => this.toggleTheme());
      }

      // Accent setting selector
      const accentSelect = document.getElementById('accent-select');
      if (accentSelect) {
        accentSelect.addEventListener('change', (e) => {
          AudioService.setAccent(e.target.value);
        });
      }

      // Modal controls
      const modalCloseBtn = document.getElementById('modal-close-btn');
      const modalBackdrop = document.getElementById('modal-backdrop');
      if (modalCloseBtn) modalCloseBtn.addEventListener('click', () => this.closeModal());
      if (modalBackdrop) modalBackdrop.addEventListener('click', () => this.closeModal());

      const modalPrevBtn = document.getElementById('modal-prev-btn');
      const modalNextBtn = document.getElementById('modal-next-btn');
      if (modalPrevBtn) modalPrevBtn.addEventListener('click', () => this.navigateModal(-1));
      if (modalNextBtn) modalNextBtn.addEventListener('click', () => this.navigateModal(1));

      // Global Keyboard Shortcuts
      window.addEventListener('keydown', (e) => {
        // Esc closes modal
        if (e.key === 'Escape') {
          this.closeModal();
          return;
        }

        // Search shortcut (/ or Ctrl+K)
        if ((e.key === '/' || (e.ctrlKey && e.key.toLowerCase() === 'k')) && document.activeElement !== searchInput) {
          e.preventDefault();
          this.switchTab('explorer');
          if (searchInput) searchInput.focus();
          return;
        }

        // Flashcards navigation
        if (AppState.currentTab === 'flashcards') {
          if (e.code === 'Space') {
            e.preventDefault();
            this.flipFlashcard();
          } else if (e.key === 'ArrowRight' || e.key === 'KeyD') {
            e.preventDefault();
            this.nextFlashcard();
          } else if (e.key === 'ArrowLeft' || e.key === 'KeyA') {
            e.preventDefault();
            this.prevFlashcard();
          }
        }

        // Quiz options shortcut (1, 2, 3, 4)
        if (AppState.currentTab === 'quiz' && !AppState.quizAnswered) {
          const num = parseInt(e.key);
          if (num >= 1 && num <= 4) {
            e.preventDefault();
            this.handleQuizSelect(num - 1);
          }
        }
      });

      // Flashcard UI Controls
      const flipBtn = document.getElementById('fc-flip-btn');
      const fcNextBtn = document.getElementById('fc-next-btn');
      const fcPrevBtn = document.getElementById('fc-prev-btn');
      const fcCardWrapper = document.getElementById('flashcard-wrapper');
      const fcShuffleBtn = document.getElementById('fc-shuffle-btn');
      const fcMasterBtn = document.getElementById('fc-master-btn');
      const fcReviewBtn = document.getElementById('fc-review-btn');
      const fcStarBtn = document.getElementById('fc-star-btn');
      const fcToggleMeaningBtn = document.getElementById('fc-toggle-meaning');

      if (fcCardWrapper) fcCardWrapper.addEventListener('click', (e) => {
        // Don't flip if user clicked an audio or action button
        if (e.target.closest('button')) return;
        this.flipFlashcard();
      });
      if (flipBtn) flipBtn.addEventListener('click', () => this.flipFlashcard());
      if (fcNextBtn) fcNextBtn.addEventListener('click', () => this.nextFlashcard());
      if (fcPrevBtn) fcPrevBtn.addEventListener('click', () => this.prevFlashcard());
      if (fcShuffleBtn) fcShuffleBtn.addEventListener('click', () => this.shuffleFlashcards());
      if (fcMasterBtn) fcMasterBtn.addEventListener('click', () => this.rateCurrentFlashcard(true));
      if (fcReviewBtn) fcReviewBtn.addEventListener('click', () => this.rateCurrentFlashcard(false));
      if (fcStarBtn) fcStarBtn.addEventListener('click', () => this.toggleCurrentFlashcardStar());
      if (fcToggleMeaningBtn) fcToggleMeaningBtn.addEventListener('click', () => {
        AppState.hideMeaningFlashcard = !AppState.hideMeaningFlashcard;
        this.renderFlashcard();
      });

      // Quiz mode select
      const quizModeSelect = document.getElementById('quiz-mode-select');
      if (quizModeSelect) {
        quizModeSelect.addEventListener('change', (e) => {
          AppState.quizMode = e.target.value;
          this.startQuiz();
        });
      }

      // Quiz restart
      const quizRestartBtn = document.getElementById('quiz-restart-btn');
      if (quizRestartBtn) quizRestartBtn.addEventListener('click', () => this.startQuiz());

      // Typing practice controls
      const typingSubmitBtn = document.getElementById('typing-submit-btn');
      const typingSkipBtn = document.getElementById('typing-skip-btn');
      const typingV2Input = document.getElementById('typing-v2-input');
      const typingV3Input = document.getElementById('typing-v3-input');

      if (typingSubmitBtn) typingSubmitBtn.addEventListener('click', () => this.checkTypingAnswer());
      if (typingSkipBtn) typingSkipBtn.addEventListener('click', () => this.nextTypingVerb());
      if (typingV3Input) typingV3Input.addEventListener('keydown', (e) => {
        if (e.key === 'Enter') this.checkTypingAnswer();
      });
      if (typingV2Input) typingV2Input.addEventListener('keydown', (e) => {
        if (e.key === 'Enter') {
          if (typingV3Input) typingV3Input.focus();
        }
      });
    },

    switchTab(tabName) {
      AudioService.playClickSound();
      AppState.currentTab = tabName;

      // Map tabName to parent category group
      const TAB_GROUPS = {
        'explorer': 'verbs',
        'patterns': 'verbs',
        'flashcards': 'verbs',
        'tenses': 'tenses',
        'games': 'practice',
        'quiz': 'practice',
        'typing': 'practice',
        'it-english': 'it'
      };
      const activeGroup = TAB_GROUPS[tabName] || 'verbs';

      // Update Category Group Buttons Styling
      document.querySelectorAll('[data-group]').forEach(groupBtn => {
        const isCurrentGroup = groupBtn.dataset.group === activeGroup;
        if (isCurrentGroup) {
          groupBtn.classList.add('bg-white', 'dark:bg-slate-800', 'text-blue-600', 'dark:text-blue-400', 'shadow-sm', 'border-slate-200/80', 'dark:border-slate-700/80', 'font-bold');
          groupBtn.classList.remove('text-slate-600', 'dark:text-slate-400', 'font-semibold', 'hover:bg-white/60', 'dark:hover:bg-slate-800/60');
        } else {
          groupBtn.classList.remove('bg-white', 'dark:bg-slate-800', 'text-blue-600', 'dark:text-blue-400', 'shadow-sm', 'border-slate-200/80', 'dark:border-slate-700/80', 'font-bold');
          groupBtn.classList.add('text-slate-600', 'dark:text-slate-400', 'font-semibold', 'hover:bg-white/60', 'dark:hover:bg-slate-800/60');
        }
      });

      // Show/Hide matching subnav strip
      const subnavs = ['verbs', 'tenses', 'practice', 'it'];
      subnavs.forEach(g => {
        const subnavEl = document.getElementById(`subnav-${g}`);
        if (subnavEl) {
          if (g === activeGroup) {
            subnavEl.classList.remove('hidden');
          } else {
            subnavEl.classList.add('hidden');
          }
        }
      });

      // Update Sub-tab Buttons Active Styling
      document.querySelectorAll('.sub-tab-btn[data-nav-tab]').forEach(subBtn => {
        const isCurrentSub = subBtn.dataset.navTab === tabName;
        subBtn.classList.toggle('sub-tab-active', isCurrentSub);
        if (isCurrentSub) {
          subBtn.classList.add('bg-blue-100', 'dark:bg-blue-900/60', 'text-blue-700', 'dark:text-blue-300', 'font-bold', 'border-blue-200', 'dark:border-blue-800/80', 'shadow-2xs');
          subBtn.classList.remove('text-slate-600', 'dark:text-slate-400', 'font-semibold');
        } else {
          subBtn.classList.remove('bg-blue-100', 'dark:bg-blue-900/60', 'text-blue-700', 'dark:text-blue-300', 'font-bold', 'border-blue-200', 'dark:border-blue-800/80', 'shadow-2xs');
          subBtn.classList.add('text-slate-600', 'dark:text-slate-400', 'font-semibold');
        }
      });

      // Show/Hide Section Views
      const views = ['explorer-view', 'tenses-view', 'games-view', 'flashcards-view', 'quiz-view', 'typing-view', 'patterns-view', 'it-english-view'];
      views.forEach(v => {
        const el = document.getElementById(v);
        if (el) el.classList.add('hidden');
      });

      const activeView = document.getElementById(`${tabName}-view`);
      if (activeView) activeView.classList.remove('hidden');

      // Initialize tab specific logic
      if (tabName === 'explorer') {
        this.renderExplorer();
      } else if (tabName === 'tenses') {
        if (window.TensesApp) window.TensesApp.init();
      } else if (tabName === 'games') {
        if (window.GameApp) window.GameApp.init();
      } else if (tabName === 'flashcards') {
        this.initFlashcards();
      } else if (tabName === 'quiz') {
        this.startQuiz();
      } else if (tabName === 'typing') {
        this.initTyping();
      } else if (tabName === 'it-english') {
        if (window.ITApp) window.ITApp.init();
      }
      window.scrollTo({ top: 0, behavior: 'smooth' });
    },

    // 4. Filter & Search Logic
    applyFilterAndSearch() {
      const q = removeVietnameseTones(AppState.searchQuery.trim());
      const filter = AppState.activeFilter;

      let list = AppState.verbs.filter(v => {
        // Filter by category / status
        if (filter === 'common' && !v.isCommon) return false;
        if (filter === 'AAA' && v.pattern !== 'AAA') return false;
        if (filter === 'ABB' && v.pattern !== 'ABB') return false;
        if (filter === 'ABA' && v.pattern !== 'ABA') return false;
        if (filter === 'ABC' && v.pattern !== 'ABC') return false;
        if (filter === 'saved' && !AppState.savedIds.has(v.id)) return false;
        if (filter === 'mastered' && !AppState.masteredIds.has(v.id)) return false;
        if (filter === 'review' && !AppState.reviewIds.has(v.id)) return false;

        // Search query matching
        if (!q) return true;

        const v1Norm = removeVietnameseTones(v.v1);
        const v2Norm = removeVietnameseTones(v.v2);
        const v3Norm = removeVietnameseTones(v.v3);
        const meaningNorm = removeVietnameseTones(v.meaning);
        const exNorm = removeVietnameseTones(v.example);
        const exViNorm = removeVietnameseTones(v.exampleVi);
        const idStr = v.id.toString();

        return v1Norm.includes(q) ||
          v2Norm.includes(q) ||
          v3Norm.includes(q) ||
          meaningNorm.includes(q) ||
          exNorm.includes(q) ||
          exViNorm.includes(q) ||
          idStr === q;
      });

      // Sorting
      if (AppState.sortMode === 'az') {
        list.sort((a, b) => a.v1.localeCompare(b.v1));
      } else if (AppState.sortMode === 'za') {
        list.sort((a, b) => b.v1.localeCompare(a.v1));
      } else if (AppState.sortMode === 'id-desc') {
        list.sort((a, b) => b.id - a.id);
      } else if (AppState.sortMode === 'random') {
        list.sort(() => Math.random() - 0.5);
      } else {
        list.sort((a, b) => a.id - b.id);
      }

      AppState.filteredVerbs = list;
      this.renderExplorer();
    },

    // 5. Explorer Renderer
    renderExplorer() {
      const container = document.getElementById('verbs-container');
      const tableWrapper = document.getElementById('verbs-table-wrapper');
      const countEl = document.getElementById('search-result-count');
      const loadMoreBtn = document.getElementById('load-more-btn');

      if (countEl) {
        countEl.textContent = `${AppState.filteredVerbs.length} / ${AppState.verbs.length} động từ`;
      }

      if (AppState.filteredVerbs.length === 0) {
        if (container) {
          container.classList.remove('hidden');
          container.innerHTML = `
            <div class="col-span-full py-16 text-center text-slate-400">
              <i class="fa-solid fa-magnifying-glass text-5xl mb-4 text-slate-300 dark:text-slate-600"></i>
              <p class="text-lg font-medium text-slate-600 dark:text-slate-300">Không tìm thấy động từ nào phù hợp</p>
              <p class="text-sm text-slate-400 mt-1">Thử tìm kiếm với từ khóa khác hoặc xóa bộ lọc.</p>
            </div>
          `;
        }
        if (tableWrapper) tableWrapper.classList.add('hidden');
        if (loadMoreBtn) loadMoreBtn.classList.add('hidden');
        return;
      }

      const visibleList = AppState.filteredVerbs.slice(0, AppState.displayLimit);

      if (AppState.explorerDisplay === 'grid') {
        if (tableWrapper) tableWrapper.classList.add('hidden');
        if (container) {
          container.classList.remove('hidden');
          container.innerHTML = visibleList.map(v => this.createCardHTML(v)).join('');
          this.attachCardEvents(container);
        }
      } else {
        if (container) container.classList.add('hidden');
        if (tableWrapper) {
          tableWrapper.classList.remove('hidden');
          const tbody = document.getElementById('verbs-table-body');
          if (tbody) {
            tbody.innerHTML = visibleList.map(v => this.createTableRowHTML(v)).join('');
            this.attachTableEvents(tbody);
          }
        }
      }

      // Show / hide Load More button
      if (loadMoreBtn) {
        if (AppState.displayLimit < AppState.filteredVerbs.length) {
          loadMoreBtn.classList.remove('hidden');
          loadMoreBtn.textContent = `Xem thêm ${Math.min(36, AppState.filteredVerbs.length - AppState.displayLimit)} từ tiếp theo`;
        } else {
          loadMoreBtn.classList.add('hidden');
        }
      }
    },

    createCardHTML(verb) {
      const isSaved = AppState.savedIds.has(verb.id);
      const isMastered = AppState.masteredIds.has(verb.id);
      const isReview = AppState.reviewIds.has(verb.id);

      return `
        <div class="verb-card group relative bg-white dark:bg-slate-800 rounded-2xl border border-slate-200/80 dark:border-slate-700/80 shadow-sm hover:shadow-xl hover:-translate-y-1 transition-all duration-300 overflow-hidden flex flex-col cursor-pointer" data-verb-id="${verb.id}">
          <!-- Card Image Header -->
          <div class="relative h-44 w-full overflow-hidden bg-slate-100 dark:bg-slate-900">
            <img src="${verb.image}" alt="${verb.v1}" loading="lazy"
                 class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-105"
                 onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';" />
            
            <!-- Fallback SVG Art Badge if Image Fails or is Offline -->
            <div class="img-fallback hidden absolute inset-0 bg-gradient-to-br ${verb.gradient} flex-col items-center justify-center text-white p-4 text-center">
              <span class="text-4xl mb-2">${verb.icon}</span>
              <span class="text-xl font-bold tracking-wide">${verb.v1}</span>
              <span class="text-xs text-white/80 italic font-mono-ipa mt-1">${verb.ipa}</span>
            </div>

            <!-- Gradient Overlay for readability -->
            <div class="absolute inset-0 bg-gradient-to-t from-black/70 via-black/20 to-transparent"></div>

            <!-- Top Header Badges -->
            <div class="absolute top-3 left-3 flex items-center space-x-1.5">
              <span class="px-2.5 py-1 text-xs font-bold rounded-lg bg-black/50 backdrop-blur-md text-white border border-white/20">
                #${verb.id}
              </span>
              <span class="px-2.5 py-1 text-xs font-semibold rounded-lg bg-blue-600/80 backdrop-blur-md text-white">
                ${verb.pattern}
              </span>
              ${verb.isCommon ? `
                <span class="px-2 py-1 text-[10px] font-bold rounded-lg bg-amber-500/90 backdrop-blur-md text-white uppercase tracking-wider">
                  <i class="fa-solid fa-fire mr-1"></i>Hot
                </span>
              ` : ''}
            </div>

            <!-- Action Buttons on Image -->
            <div class="absolute top-3 right-3 flex items-center space-x-1.5">
              <button class="btn-star w-8 h-8 rounded-full bg-black/40 hover:bg-black/70 backdrop-blur-md flex items-center justify-center text-white transition-colors" data-action="star" data-verb-id="${verb.id}" title="Lưu từ này">
                <i class="fa-${isSaved ? 'solid text-amber-400' : 'regular'} fa-star text-sm"></i>
              </button>
            </div>

            <!-- Concept Visual Tag Badge -->
            <div class="absolute bottom-14 left-3">
              <span class="px-2.5 py-1 text-[11px] font-semibold rounded-lg bg-black/60 backdrop-blur-md text-amber-300 border border-white/10 flex items-center gap-1.5 shadow">
                <span>${verb.icon}</span>
                <span>${verb.conceptTag || verb.meaning.split(',')[0]}</span>
              </span>
            </div>

            <!-- Verb Title on Bottom of Image -->
            <div class="absolute bottom-3 left-3 right-3 flex items-end justify-between text-white">
              <div>
                <h3 class="text-2xl font-extrabold tracking-tight text-white flex items-center gap-2">
                  ${verb.v1}
                  <span class="text-sm font-normal text-slate-300 font-mono-ipa">${verb.ipa}</span>
                </h3>
              </div>
              <button class="btn-speak w-9 h-9 rounded-full bg-white/20 hover:bg-white/40 backdrop-blur-md text-white flex items-center justify-center transition-all btn-press shadow" data-action="speak-v1" data-word="${verb.v1}" title="Phát âm V1">
                <i class="fa-solid fa-volume-high text-sm"></i>
              </button>
            </div>
          </div>

          <!-- Card Body Content -->
          <div class="p-4 flex-1 flex flex-col justify-between">
            <!-- Conjugation Badges -->
            <div class="grid grid-cols-2 gap-2 mb-3">
              <div class="bg-slate-50 dark:bg-slate-700/50 p-2.5 rounded-xl border border-slate-100 dark:border-slate-700 flex flex-col">
                <span class="text-[10px] font-bold uppercase tracking-wider text-slate-400 dark:text-slate-400">V2 (Quá khứ)</span>
                <span class="font-bold text-slate-800 dark:text-slate-100 text-sm mt-0.5 truncate" title="${verb.v2}">
                  ${verb.v2}
                </span>
              </div>
              <div class="bg-slate-50 dark:bg-slate-700/50 p-2.5 rounded-xl border border-slate-100 dark:border-slate-700 flex flex-col">
                <span class="text-[10px] font-bold uppercase tracking-wider text-slate-400 dark:text-slate-400">V3 (Phân từ)</span>
                <span class="font-bold text-slate-800 dark:text-slate-100 text-sm mt-0.5 truncate" title="${verb.v3}">
                  ${verb.v3}
                </span>
              </div>
            </div>

            <!-- Meaning in Vietnamese -->
            <div class="mb-3">
              <div class="text-xs text-slate-400 font-semibold mb-0.5">Dịch nghĩa:</div>
              <p class="text-slate-700 dark:text-slate-200 font-medium text-sm line-clamp-2">
                ${verb.meaning}
              </p>
            </div>

            <!-- Example Sentence Box -->
            <div class="bg-blue-50/60 dark:bg-slate-900/60 p-3 rounded-xl border border-blue-100/60 dark:border-slate-700/60 text-xs text-slate-600 dark:text-slate-300 mb-3 relative group/ex">
              <div class="font-medium text-slate-800 dark:text-slate-200 italic mb-1 flex items-start justify-between gap-1">
                <span>"${this.highlightVerbInText(verb.example, [verb.v1, verb.v2, verb.v3])}"</span>
                <button class="btn-speak-ex text-blue-600 dark:text-blue-400 hover:text-blue-800 p-1 rounded transition-colors flex-shrink-0" data-action="speak-sentence" data-sentence="${verb.example.replace(/"/g, '&quot;')}" title="Nghe câu ví dụ">
                  <i class="fa-solid fa-volume-low text-xs"></i>
                </button>
              </div>
              <div class="text-slate-500 dark:text-slate-400 line-clamp-1">
                ${verb.exampleVi}
              </div>
            </div>

            <!-- Footer Action Status Buttons -->
            <div class="pt-2 border-t border-slate-100 dark:border-slate-700/60 flex items-center justify-between">
              <div class="flex items-center space-x-1.5">
                <button class="btn-master px-2.5 py-1 rounded-lg text-xs font-semibold transition-all flex items-center gap-1 ${isMastered ? 'bg-emerald-500 text-white' : 'bg-slate-100 dark:bg-slate-700 text-slate-600 dark:text-slate-300 hover:bg-emerald-100 dark:hover:bg-emerald-900/40'}" data-action="master" data-verb-id="${verb.id}">
                  <i class="fa-solid fa-check text-[10px]"></i>
                  <span>${isMastered ? 'Đã thuộc' : 'Thuộc'}</span>
                </button>
                <button class="btn-review px-2.5 py-1 rounded-lg text-xs font-semibold transition-all flex items-center gap-1 ${isReview ? 'bg-rose-500 text-white' : 'bg-slate-100 dark:bg-slate-700 text-slate-600 dark:text-slate-300 hover:bg-rose-100 dark:hover:bg-rose-900/40'}" data-action="review" data-verb-id="${verb.id}">
                  <i class="fa-solid fa-rotate-right text-[10px]"></i>
                  <span>${isReview ? 'Cần ôn' : 'Ôn tập'}</span>
                </button>
              </div>
              <span class="text-xs text-blue-600 dark:text-blue-400 font-semibold group-hover:translate-x-0.5 transition-transform flex items-center gap-1">
                Chi tiết <i class="fa-solid fa-chevron-right text-[10px]"></i>
              </span>
            </div>
          </div>
        </div>
      `;
    },

    createTableRowHTML(verb) {
      const isSaved = AppState.savedIds.has(verb.id);
      const isMastered = AppState.masteredIds.has(verb.id);

      return `
        <tr class="border-b border-slate-100 dark:border-slate-800 hover:bg-slate-50/80 dark:hover:bg-slate-700/40 transition-colors cursor-pointer" data-verb-id="${verb.id}">
          <td class="py-3 px-4 text-xs font-bold text-slate-400">#${verb.id}</td>
          <td class="py-3 px-4">
            <div class="flex items-center space-x-2">
              <span class="text-lg">${verb.icon}</span>
              <div>
                <div class="font-bold text-slate-900 dark:text-white text-base">${verb.v1}</div>
                <div class="text-xs text-slate-400 font-mono-ipa">${verb.ipa}</div>
              </div>
            </div>
          </td>
          <td class="py-3 px-4 font-semibold text-slate-700 dark:text-slate-200">${verb.v2}</td>
          <td class="py-3 px-4 font-semibold text-slate-700 dark:text-slate-200">${verb.v3}</td>
          <td class="py-3 px-4 text-sm text-slate-600 dark:text-slate-300 max-w-xs truncate">${verb.meaning}</td>
          <td class="py-3 px-4">
            <span class="px-2 py-0.5 text-xs font-bold rounded bg-slate-100 dark:bg-slate-700 text-slate-600 dark:text-slate-300">
              ${verb.pattern}
            </span>
          </td>
          <td class="py-3 px-4 text-right space-x-1" onclick="event.stopPropagation()">
            <button class="w-8 h-8 rounded-lg bg-slate-100 dark:bg-slate-700 hover:bg-blue-100 dark:hover:bg-blue-900 text-slate-600 dark:text-slate-300 hover:text-blue-600 transition-colors" data-action="speak-v1" data-word="${verb.v1}" title="Phát âm">
              <i class="fa-solid fa-volume-high text-xs"></i>
            </button>
            <button class="w-8 h-8 rounded-lg bg-slate-100 dark:bg-slate-700 hover:bg-amber-100 text-slate-600 dark:text-slate-300 hover:text-amber-500 transition-colors" data-action="star" data-verb-id="${verb.id}" title="Đánh dấu sao">
              <i class="fa-${isSaved ? 'solid text-amber-400' : 'regular'} fa-star text-xs"></i>
            </button>
            <button class="w-8 h-8 rounded-lg ${isMastered ? 'bg-emerald-500 text-white' : 'bg-slate-100 dark:bg-slate-700 text-slate-600 dark:text-slate-300 hover:bg-emerald-100 hover:text-emerald-600'} transition-colors" data-action="master" data-verb-id="${verb.id}" title="Đã thuộc">
              <i class="fa-solid fa-check text-xs"></i>
            </button>
          </td>
        </tr>
      `;
    },

    highlightVerbInText(text, forms) {
      if (!text) return '';
      // Simple highlight for verb tokens in the sentence
      const cleanForms = forms.flatMap(f => f.split('/')).map(s => s.trim().toLowerCase());
      const words = text.split(/(\s+|,|\.|\?|!)/);
      return words.map(w => {
        const cleanW = w.toLowerCase().replace(/[^a-z]/g, '');
        if (cleanForms.includes(cleanW)) {
          return `<span class="highlight-verb">${w}</span>`;
        }
        return w;
      }).join('');
    },

    attachCardEvents(container) {
      container.querySelectorAll('.verb-card').forEach(card => {
        card.addEventListener('click', (e) => {
          const actionBtn = e.target.closest('[data-action]');
          if (actionBtn) {
            e.stopPropagation();
            const action = actionBtn.dataset.action;
            const verbId = parseInt(actionBtn.dataset.verbId || card.dataset.verbId);
            const verb = AppState.verbs.find(v => v.id === verbId);

            if (action === 'star') {
              AppState.toggleSave(verbId);
              this.renderExplorer();
            } else if (action === 'master') {
              AppState.toggleMastered(verbId);
              this.renderExplorer();
            } else if (action === 'review') {
              AppState.toggleReview(verbId);
              this.renderExplorer();
            } else if (action === 'speak-v1') {
              AudioService.speak(actionBtn.dataset.word);
            } else if (action === 'speak-sentence') {
              AudioService.speak(actionBtn.dataset.sentence);
            }
            return;
          }

          // Open Full Modal Detail
          const verbId = parseInt(card.dataset.verbId);
          this.openModal(verbId);
        });
      });
    },

    attachTableEvents(tbody) {
      tbody.querySelectorAll('tr').forEach(row => {
        row.addEventListener('click', (e) => {
          const actionBtn = e.target.closest('[data-action]');
          if (actionBtn) {
            e.stopPropagation();
            const action = actionBtn.dataset.action;
            const verbId = parseInt(actionBtn.dataset.verbId || row.dataset.verbId);

            if (action === 'star') {
              AppState.toggleSave(verbId);
              this.renderExplorer();
            } else if (action === 'master') {
              AppState.toggleMastered(verbId);
              this.renderExplorer();
            } else if (action === 'speak-v1') {
              AudioService.speak(actionBtn.dataset.word);
            }
            return;
          }

          const verbId = parseInt(row.dataset.verbId);
          this.openModal(verbId);
        });
      });
    },

    // 6. Word Detail Modal
    openModal(verbId) {
      const verb = AppState.verbs.find(v => v.id === verbId);
      if (!verb) return;

      AppState.modalVerb = verb;
      AudioService.playClickSound();

      const modal = document.getElementById('word-modal');
      if (!modal) return;

      // Populate Modal Content
      document.getElementById('modal-id-badge').textContent = `#${verb.id}`;
      document.getElementById('modal-pattern-badge').textContent = `Dạng: ${verb.pattern}`;
      const modalConcept = document.getElementById('modal-concept-tag');
      if (modalConcept) {
        modalConcept.innerHTML = `<span>${verb.icon}</span> <span>${verb.conceptTag || verb.meaning.split(',')[0]}</span>`;
      }
      document.getElementById('modal-v1').textContent = verb.v1;
      document.getElementById('modal-ipa').textContent = verb.ipa;
      document.getElementById('modal-meaning').textContent = verb.meaning;
      document.getElementById('modal-v2').textContent = verb.v2;
      document.getElementById('modal-v3').textContent = verb.v3;

      document.getElementById('modal-example-en').innerHTML = `"${this.highlightVerbInText(verb.example, [verb.v1, verb.v2, verb.v3])}"`;
      document.getElementById('modal-example-vi').textContent = verb.exampleVi;

      // Image & Fallback
      const img = document.getElementById('modal-img');
      const fallback = document.getElementById('modal-img-fallback');
      if (img && fallback) {
        img.style.display = 'block';
        fallback.style.display = 'none';
        img.src = verb.image;
        img.onerror = () => {
          img.style.display = 'none';
          fallback.style.display = 'flex';
          fallback.className = `modal-img-fallback absolute inset-0 bg-gradient-to-br ${verb.gradient} flex flex-col items-center justify-center text-white`;
          fallback.innerHTML = `
            <span class="text-6xl mb-2">${verb.icon}</span>
            <span class="text-3xl font-bold">${verb.v1}</span>
            <span class="text-sm font-mono-ipa opacity-80 mt-1">${verb.ipa}</span>
          `;
        };
      }

      // Audio Buttons in Modal
      document.getElementById('modal-speak-v1').onclick = () => AudioService.speak(verb.v1);
      document.getElementById('modal-speak-v2').onclick = () => AudioService.speak(verb.v2);
      document.getElementById('modal-speak-v3').onclick = () => AudioService.speak(verb.v3);
      document.getElementById('modal-speak-all').onclick = () => {
        AudioService.speak(`${verb.v1}. ${verb.v2}. ${verb.v3}`);
      };
      document.getElementById('modal-speak-example').onclick = () => {
        AudioService.speak(verb.example);
      };

      // Modal Status Toggle Buttons
      const modalStarBtn = document.getElementById('modal-star-btn');
      const modalMasterBtn = document.getElementById('modal-master-btn');

      const updateModalButtons = () => {
        const isSaved = AppState.savedIds.has(verb.id);
        const isMastered = AppState.masteredIds.has(verb.id);
        if (modalStarBtn) {
          modalStarBtn.innerHTML = `<i class="fa-${isSaved ? 'solid text-amber-400' : 'regular'} fa-star mr-1.5"></i> ${isSaved ? 'Đã lưu' : 'Lưu từ'}`;
        }
        if (modalMasterBtn) {
          modalMasterBtn.innerHTML = `<i class="fa-solid fa-check mr-1.5"></i> ${isMastered ? 'Đã thuộc từ này' : 'Đánh dấu đã thuộc'}`;
          modalMasterBtn.className = `px-4 py-2.5 rounded-xl font-semibold text-sm transition-all btn-press ${isMastered ? 'bg-emerald-600 text-white' : 'bg-slate-100 dark:bg-slate-700 text-slate-700 dark:text-slate-200 hover:bg-emerald-500 hover:text-white'}`;
        }
      };

      if (modalStarBtn) {
        modalStarBtn.onclick = () => {
          AppState.toggleSave(verb.id);
          updateModalButtons();
          this.renderExplorer();
        };
      }

      if (modalMasterBtn) {
        modalMasterBtn.onclick = () => {
          AppState.toggleMastered(verb.id);
          updateModalButtons();
          this.renderExplorer();
        };
      }

      updateModalButtons();

      modal.classList.remove('hidden');
      document.body.classList.add('overflow-hidden');
    },

    closeModal() {
      const modal = document.getElementById('word-modal');
      if (modal) modal.classList.add('hidden');
      document.body.classList.remove('overflow-hidden');
    },

    navigateModal(direction) {
      if (!AppState.modalVerb) return;
      const currentIdx = AppState.filteredVerbs.findIndex(v => v.id === AppState.modalVerb.id);
      if (currentIdx === -1) return;

      let nextIdx = currentIdx + direction;
      if (nextIdx < 0) nextIdx = AppState.filteredVerbs.length - 1;
      if (nextIdx >= AppState.filteredVerbs.length) nextIdx = 0;

      const nextVerb = AppState.filteredVerbs[nextIdx];
      this.openModal(nextVerb.id);
    },

    // 7. Flashcards Controller
    initFlashcards() {
      // Use currently filtered verbs or all verbs
      AppState.flashcardList = AppState.filteredVerbs.length > 0 ? [...AppState.filteredVerbs] : [...AppState.verbs];
      AppState.flashcardIndex = 0;
      AppState.isFlashcardFlipped = false;
      this.renderFlashcard();
    },

    renderFlashcard() {
      const list = AppState.flashcardList;
      if (!list.length) return;

      const verb = list[AppState.flashcardIndex];
      const cardWrapper = document.getElementById('flashcard-wrapper');
      const counterEl = document.getElementById('fc-counter');
      const barEl = document.getElementById('fc-progress-bar');

      if (counterEl) counterEl.textContent = `${AppState.flashcardIndex + 1} / ${list.length}`;
      if (barEl) barEl.style.width = `${((AppState.flashcardIndex + 1) / list.length) * 100}%`;

      // Reset flip state on new card
      if (cardWrapper) {
        if (AppState.isFlashcardFlipped) {
          cardWrapper.classList.add('flashcard-flipped');
        } else {
          cardWrapper.classList.remove('flashcard-flipped');
        }
      }

      // Populate Front Side
      document.getElementById('fc-front-id').textContent = `#${verb.id}`;
      document.getElementById('fc-front-pattern').textContent = verb.pattern;
      const fcConcept = document.getElementById('fc-front-concept');
      if (fcConcept) {
        fcConcept.innerHTML = `<span>${verb.icon}</span> <span>${verb.conceptTag || verb.meaning.split(',')[0]}</span>`;
      }
      document.getElementById('fc-front-v1').textContent = verb.v1;
      document.getElementById('fc-front-ipa').textContent = verb.ipa;

      const meaningFront = document.getElementById('fc-front-meaning');
      if (meaningFront) {
        if (AppState.hideMeaningFlashcard) {
          meaningFront.innerHTML = `<span class="italic text-slate-400 dark:text-slate-500">Đã ẩn nghĩa (lật thẻ để xem)</span>`;
        } else {
          meaningFront.textContent = verb.meaning;
        }
      }

      const fcFrontImg = document.getElementById('fc-front-img');
      const fcFrontFallback = document.getElementById('fc-front-fallback');
      if (fcFrontImg && fcFrontFallback) {
        fcFrontImg.style.display = 'block';
        fcFrontFallback.style.display = 'none';
        fcFrontImg.src = verb.image;
        fcFrontImg.onerror = () => {
          fcFrontImg.style.display = 'none';
          fcFrontFallback.style.display = 'flex';
          fcFrontFallback.className = `absolute inset-0 bg-gradient-to-br ${verb.gradient} flex flex-col items-center justify-center text-white`;
          fcFrontFallback.innerHTML = `
            <span class="text-6xl mb-2">${verb.icon}</span>
            <span class="text-2xl font-bold">${verb.v1}</span>
          `;
        };
      }

      // Populate Back Side
      document.getElementById('fc-back-v1').textContent = verb.v1;
      document.getElementById('fc-back-v2').textContent = verb.v2;
      document.getElementById('fc-back-v3').textContent = verb.v3;
      document.getElementById('fc-back-meaning').textContent = verb.meaning;
      document.getElementById('fc-back-example-en').innerHTML = `"${this.highlightVerbInText(verb.example, [verb.v1, verb.v2, verb.v3])}"`;
      document.getElementById('fc-back-example-vi').textContent = verb.exampleVi;

      // Audio buttons on card
      document.getElementById('fc-front-speak').onclick = (e) => {
        e.stopPropagation();
        AudioService.speak(verb.v1);
      };
      document.getElementById('fc-back-speak-all').onclick = (e) => {
        e.stopPropagation();
        AudioService.speak(`${verb.v1}. ${verb.v2}. ${verb.v3}`);
      };
      document.getElementById('fc-back-speak-ex').onclick = (e) => {
        e.stopPropagation();
        AudioService.speak(verb.example);
      };

      // Star status on flashcard
      const isSaved = AppState.savedIds.has(verb.id);
      const fcStarBtn = document.getElementById('fc-star-btn');
      if (fcStarBtn) {
        fcStarBtn.innerHTML = `<i class="fa-${isSaved ? 'solid text-amber-400' : 'regular'} fa-star text-lg"></i>`;
      }
    },

    flipFlashcard() {
      AudioService.playClickSound();
      AppState.isFlashcardFlipped = !AppState.isFlashcardFlipped;
      const cardWrapper = document.getElementById('flashcard-wrapper');
      if (cardWrapper) {
        cardWrapper.classList.toggle('flashcard-flipped', AppState.isFlashcardFlipped);
      }
    },

    nextFlashcard() {
      if (AppState.flashcardIndex < AppState.flashcardList.length - 1) {
        AppState.flashcardIndex++;
      } else {
        AppState.flashcardIndex = 0; // Loop back
      }
      AppState.isFlashcardFlipped = false;
      this.renderFlashcard();
    },

    prevFlashcard() {
      if (AppState.flashcardIndex > 0) {
        AppState.flashcardIndex--;
      } else {
        AppState.flashcardIndex = AppState.flashcardList.length - 1;
      }
      AppState.isFlashcardFlipped = false;
      this.renderFlashcard();
    },

    shuffleFlashcards() {
      AudioService.playClickSound();
      AppState.flashcardList.sort(() => Math.random() - 0.5);
      AppState.flashcardIndex = 0;
      AppState.isFlashcardFlipped = false;
      this.renderFlashcard();
    },

    rateCurrentFlashcard(isMastered) {
      const currentVerb = AppState.flashcardList[AppState.flashcardIndex];
      if (!currentVerb) return;

      if (isMastered) {
        AudioService.playSuccessSound();
        AppState.masteredIds.add(currentVerb.id);
        AppState.reviewIds.delete(currentVerb.id);
      } else {
        AudioService.playErrorSound();
        AppState.reviewIds.add(currentVerb.id);
        AppState.masteredIds.delete(currentVerb.id);
      }
      AppState.saveProgress();
      this.nextFlashcard();
    },

    toggleCurrentFlashcardStar() {
      const currentVerb = AppState.flashcardList[AppState.flashcardIndex];
      if (!currentVerb) return;
      AppState.toggleSave(currentVerb.id);
      this.renderFlashcard();
    },

    // 8. Interactive Quiz System
    startQuiz() {
      AppState.quizScore = 0;
      AppState.quizStreak = 0;
      AppState.quizMaxStreak = 0;
      AppState.quizIndex = 0;
      AppState.quizAnswered = false;
      AppState.quizSelectedOption = null;

      // Generate 10 randomized quiz questions
      const pool = [...AppState.verbs].sort(() => Math.random() - 0.5);
      const count = 10;
      const selectedVerbs = pool.slice(0, count);

      AppState.quizQuestions = selectedVerbs.map(verb => {
        let qType = AppState.quizMode;
        if (qType === 'mix') {
          const types = ['v2', 'v3', 'meaning', 'sentence'];
          qType = types[Math.floor(Math.random() * types.length)];
        }

        let prompt = '';
        let correctAnswer = '';
        let optionPoolKey = 'v2';

        if (qType === 'v2') {
          prompt = `Dạng Quá khứ (V2) của động từ "${verb.v1}" là gì?`;
          correctAnswer = verb.v2;
          optionPoolKey = 'v2';
        } else if (qType === 'v3') {
          prompt = `Dạng Quá khứ phân từ (V3) của động từ "${verb.v1}" là gì?`;
          correctAnswer = verb.v3;
          optionPoolKey = 'v3';
        } else if (qType === 'meaning') {
          prompt = `Động từ "${verb.v1}" có nghĩa tiếng Việt là gì?`;
          correctAnswer = verb.meaning;
          optionPoolKey = 'meaning';
        } else if (qType === 'sentence') {
          // Fill in blank
          prompt = `Điền dạng đúng của "${verb.v1}" vào câu: "${verb.example.replace(new RegExp(verb.v1 + '|' + verb.v2.split('/')[0].trim() + '|' + verb.v3.split('/')[0].trim(), 'gi'), '_____')}"`;
          correctAnswer = verb.v2.split('/')[0].trim();
          optionPoolKey = 'v2';
        }

        // Generate 3 distractors
        const distractors = AppState.verbs
          .filter(v => v.id !== verb.id)
          .map(v => v[optionPoolKey].split('/')[0].trim())
          .filter((v, idx, self) => self.indexOf(v) === idx && v !== correctAnswer)
          .sort(() => Math.random() - 0.5)
          .slice(0, 3);

        const options = [correctAnswer, ...distractors].sort(() => Math.random() - 0.5);

        return {
          verb,
          type: qType,
          prompt,
          correctAnswer,
          options
        };
      });

      document.getElementById('quiz-active-card').classList.remove('hidden');
      document.getElementById('quiz-result-card').classList.add('hidden');
      this.renderQuizQuestion();
    },

    renderQuizQuestion() {
      const q = AppState.quizQuestions[AppState.quizIndex];
      if (!q) {
        this.finishQuiz();
        return;
      }

      AppState.quizAnswered = false;
      AppState.quizSelectedOption = null;

      document.getElementById('quiz-progress-text').textContent = `Câu ${AppState.quizIndex + 1} / ${AppState.quizQuestions.length}`;
      document.getElementById('quiz-score-display').textContent = `Điểm: ${AppState.quizScore}`;
      document.getElementById('quiz-streak-display').innerHTML = `<i class="fa-solid fa-fire text-amber-500 mr-1"></i>Streak: ${AppState.quizStreak}`;
      document.getElementById('quiz-progress-bar').style.width = `${((AppState.quizIndex + 1) / AppState.quizQuestions.length) * 100}%`;

      document.getElementById('quiz-prompt').textContent = q.prompt;
      document.getElementById('quiz-verb-display').textContent = `${q.verb.v1} (${q.verb.ipa})`;

      // Audio prompt button
      document.getElementById('quiz-speak-prompt').onclick = () => AudioService.speak(q.verb.v1);

      // Render Options
      const optionsContainer = document.getElementById('quiz-options-container');
      optionsContainer.innerHTML = q.options.map((opt, idx) => `
        <button class="quiz-option-btn w-full p-4 rounded-xl border-2 border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-800 text-left font-semibold text-slate-800 dark:text-slate-100 hover:border-blue-500 dark:hover:border-blue-400 hover:bg-blue-50/50 dark:hover:bg-slate-700/60 transition-all duration-150 flex items-center justify-between group shadow-sm btn-press" data-opt-index="${idx}">
          <div class="flex items-center space-x-3">
            <span class="w-8 h-8 rounded-lg bg-slate-100 dark:bg-slate-700 text-slate-600 dark:text-slate-300 font-bold flex items-center justify-center text-sm group-hover:bg-blue-600 group-hover:text-white transition-colors">
              ${idx + 1}
            </span>
            <span class="text-base">${opt}</span>
          </div>
          <span class="opt-icon opacity-0 transition-opacity"></span>
        </button>
      `).join('');

      optionsContainer.querySelectorAll('.quiz-option-btn').forEach((btn, idx) => {
        btn.addEventListener('click', () => this.handleQuizSelect(idx));
      });

      // Explanation box (hidden until answered)
      const explBox = document.getElementById('quiz-explanation-box');
      if (explBox) explBox.classList.add('hidden');
    },

    handleQuizSelect(optIdx) {
      if (AppState.quizAnswered) return;
      AppState.quizAnswered = true;
      AppState.quizSelectedOption = optIdx;

      const q = AppState.quizQuestions[AppState.quizIndex];
      const selectedText = q.options[optIdx];
      const isCorrect = selectedText === q.correctAnswer;

      const optionsBtns = document.querySelectorAll('.quiz-option-btn');

      if (isCorrect) {
        AudioService.playSuccessSound();
        AppState.quizScore += 10;
        AppState.quizStreak++;
        if (AppState.quizStreak > AppState.quizMaxStreak) {
          AppState.quizMaxStreak = AppState.quizStreak;
        }

        optionsBtns[optIdx].classList.remove('border-slate-200', 'dark:border-slate-700');
        optionsBtns[optIdx].classList.add('border-emerald-500', 'bg-emerald-50', 'dark:bg-emerald-950/40', 'text-emerald-800', 'dark:text-emerald-200');
        optionsBtns[optIdx].querySelector('.opt-icon').innerHTML = '<i class="fa-solid fa-circle-check text-emerald-500 text-xl"></i>';
        optionsBtns[optIdx].querySelector('.opt-icon').classList.remove('opacity-0');
      } else {
        AudioService.playErrorSound();
        AppState.quizStreak = 0;

        optionsBtns[optIdx].classList.remove('border-slate-200', 'dark:border-slate-700');
        optionsBtns[optIdx].classList.add('border-rose-500', 'bg-rose-50', 'dark:bg-rose-950/40', 'text-rose-800', 'dark:text-rose-200');
        optionsBtns[optIdx].querySelector('.opt-icon').innerHTML = '<i class="fa-solid fa-circle-xmark text-rose-500 text-xl"></i>';
        optionsBtns[optIdx].querySelector('.opt-icon').classList.remove('opacity-0');

        // Highlight correct option
        optionsBtns.forEach((btn, idx) => {
          if (q.options[idx] === q.correctAnswer) {
            btn.classList.add('border-emerald-500', 'bg-emerald-50/50', 'dark:bg-emerald-950/20');
            btn.querySelector('.opt-icon').innerHTML = '<i class="fa-solid fa-check text-emerald-500 text-lg"></i>';
            btn.querySelector('.opt-icon').classList.remove('opacity-0');
          }
        });
      }

      // Show explanation box
      const explBox = document.getElementById('quiz-explanation-box');
      if (explBox) {
        explBox.classList.remove('hidden');
        document.getElementById('quiz-expl-v1').textContent = q.verb.v1;
        document.getElementById('quiz-expl-v2').textContent = q.verb.v2;
        document.getElementById('quiz-expl-v3').textContent = q.verb.v3;
        document.getElementById('quiz-expl-meaning').textContent = q.verb.meaning;
        document.getElementById('quiz-expl-sentence').textContent = `"${q.verb.example}" (${q.verb.exampleVi})`;

        const nextBtn = document.getElementById('quiz-next-btn');
        if (nextBtn) {
          nextBtn.focus();
          nextBtn.onclick = () => {
            AppState.quizIndex++;
            this.renderQuizQuestion();
          };
        }
      }
    },

    finishQuiz() {
      document.getElementById('quiz-active-card').classList.add('hidden');
      const resultCard = document.getElementById('quiz-result-card');
      resultCard.classList.remove('hidden');

      const maxScore = AppState.quizQuestions.length * 10;
      const score = AppState.quizScore;
      const percent = Math.round((score / maxScore) * 100);

      document.getElementById('quiz-final-score').textContent = `${score} / ${maxScore}`;
      document.getElementById('quiz-final-percent').textContent = `${percent}%`;
      document.getElementById('quiz-max-streak').textContent = AppState.quizMaxStreak;

      let msg = 'Rất tốt! Bạn đang tiến bộ từng ngày!';
      if (percent === 100) {
        msg = 'Xuất sắc! Bạn đã trả lời đúng 100% câu hỏi! 🎉';
        AudioService.playSuccessSound();
      } else if (percent < 60) {
        msg = 'Hãy tiếp tục luyện tập thêm nhé, kiên trì là chìa khóa thành công!';
      }
      document.getElementById('quiz-feedback-msg').textContent = msg;
    },

    // 9. Typing Practice System
    initTyping() {
      AppState.typingIndex = 0;
      this.renderTypingVerb();
    },

    renderTypingVerb() {
      const verb = AppState.verbs[AppState.typingIndex];
      if (!verb) return;
      AppState.typingVerb = verb;

      document.getElementById('typing-v1-display').textContent = verb.v1;
      document.getElementById('typing-ipa-display').textContent = verb.ipa;
      document.getElementById('typing-meaning-display').textContent = verb.meaning;
      document.getElementById('typing-counter').textContent = `Từ ${AppState.typingIndex + 1} / ${AppState.verbs.length}`;

      const v2Input = document.getElementById('typing-v2-input');
      const v3Input = document.getElementById('typing-v3-input');
      const feedback = document.getElementById('typing-feedback');

      if (v2Input) {
        v2Input.value = '';
        v2Input.className = 'w-full px-4 py-3 rounded-xl border-2 border-slate-300 dark:border-slate-600 bg-white dark:bg-slate-700 text-slate-800 dark:text-white font-semibold text-lg focus:outline-none focus:border-blue-500';
      }
      if (v3Input) {
        v3Input.value = '';
        v3Input.className = 'w-full px-4 py-3 rounded-xl border-2 border-slate-300 dark:border-slate-600 bg-white dark:bg-slate-700 text-slate-800 dark:text-white font-semibold text-lg focus:outline-none focus:border-blue-500';
      }
      if (feedback) feedback.classList.add('hidden');

      const img = document.getElementById('typing-img');
      if (img) img.src = verb.image;

      if (v2Input) v2Input.focus();
    },

    checkTypingAnswer() {
      const verb = AppState.typingVerb;
      if (!verb) return;

      const v2Input = document.getElementById('typing-v2-input');
      const v3Input = document.getElementById('typing-v3-input');
      const feedback = document.getElementById('typing-feedback');

      const userV2 = v2Input.value.trim().toLowerCase();
      const userV3 = v3Input.value.trim().toLowerCase();

      // Check against acceptable forms
      const validV2 = verb.v2.toLowerCase().split('/').map(s => s.trim());
      const validV3 = verb.v3.toLowerCase().split('/').map(s => s.trim());

      const isV2Correct = validV2.includes(userV2);
      const isV3Correct = validV3.includes(userV3);

      v2Input.className = `w-full px-4 py-3 rounded-xl border-2 ${isV2Correct ? 'border-emerald-500 bg-emerald-50 dark:bg-emerald-950/40 text-emerald-800 dark:text-emerald-200' : 'border-rose-500 bg-rose-50 dark:bg-rose-950/40 text-rose-800 dark:text-rose-200'} font-semibold text-lg`;
      v3Input.className = `w-full px-4 py-3 rounded-xl border-2 ${isV3Correct ? 'border-emerald-500 bg-emerald-50 dark:bg-emerald-950/40 text-emerald-800 dark:text-emerald-200' : 'border-rose-500 bg-rose-50 dark:bg-rose-950/40 text-rose-800 dark:text-rose-200'} font-semibold text-lg`;

      if (feedback) {
        feedback.classList.remove('hidden');
        if (isV2Correct && isV3Correct) {
          AudioService.playSuccessSound();
          feedback.innerHTML = `
            <div class="p-4 rounded-xl bg-emerald-100 dark:bg-emerald-900/40 border border-emerald-300 dark:border-emerald-700 text-emerald-800 dark:text-emerald-200 flex items-center justify-between">
              <div class="flex items-center gap-2">
                <i class="fa-solid fa-circle-check text-xl"></i>
                <span class="font-bold">Chính xác 100%!</span>
              </div>
              <button id="typing-next-btn" class="px-4 py-2 bg-emerald-600 hover:bg-emerald-700 text-white rounded-lg font-semibold text-sm transition-colors shadow">
                Từ tiếp theo <i class="fa-solid fa-arrow-right ml-1"></i>
              </button>
            </div>
          `;
          document.getElementById('typing-next-btn').onclick = () => this.nextTypingVerb();
          document.getElementById('typing-next-btn').focus();
        } else {
          AudioService.playErrorSound();
          feedback.innerHTML = `
            <div class="p-4 rounded-xl bg-rose-100 dark:bg-rose-900/40 border border-rose-300 dark:border-rose-700 text-rose-800 dark:text-rose-200">
              <div class="flex items-center gap-2 font-bold mb-2">
                <i class="fa-solid fa-circle-xmark text-xl"></i>
                <span>Chưa chính xác! Đáp án đúng:</span>
              </div>
              <div class="text-sm space-y-1">
                <div>• V2: <strong class="underline">${verb.v2}</strong></div>
                <div>• V3: <strong class="underline">${verb.v3}</strong></div>
              </div>
              <div class="mt-3 flex justify-end">
                <button id="typing-next-btn" class="px-4 py-2 bg-rose-600 hover:bg-rose-700 text-white rounded-lg font-semibold text-sm transition-colors shadow">
                  Bỏ qua & Sang từ tiếp theo <i class="fa-solid fa-arrow-right ml-1"></i>
                </button>
              </div>
            </div>
          `;
          document.getElementById('typing-next-btn').onclick = () => this.nextTypingVerb();
        }
      }
    },

    nextTypingVerb() {
      if (AppState.typingIndex < AppState.verbs.length - 1) {
        AppState.typingIndex++;
      } else {
        AppState.typingIndex = 0;
      }
      this.renderTypingVerb();
    }
  };

  // Run on DOM loaded
  document.addEventListener('DOMContentLoaded', () => {
    UI.init();
  });
})();
