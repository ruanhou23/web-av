/**
 * IT English (Tiếng Anh Chuyên Ngành Công Nghệ Thông Tin) Module
 * Handles Explorer, Flashcards, Quiz, Audio, and Storage for IT Terms
 */

(function () {
  'use strict';

  // Helper for non-accented search
  function removeVietnameseTones(str) {
    if (!str) return '';
    return str
      .normalize('NFD')
      .replace(/[\u0300-\u036f]/g, '')
      .replace(/đ/g, 'd')
      .replace(/Đ/g, 'D')
      .toLowerCase();
  }

  // Audio helper (reuses parent window.speechSynthesis or AudioService)
  const speakTerm = (text) => {
    if (!('speechSynthesis' in window) || !text) return;
    window.speechSynthesis.cancel();
    const utterance = new SpeechSynthesisUtterance(text.trim());
    utterance.rate = 0.9;
    utterance.pitch = 1.0;
    utterance.lang = 'en-US';
    window.speechSynthesis.speak(utterance);
  };

  const ITState = {
    terms: window.IT_TERMS_DATA || window.IT_TERMS_DATABASE || [],
    filteredTerms: [],
    searchQuery: '',
    activeFilter: 'all', // all, programming, dsa, database, networking, security, os_hardware, cloud_devops, web_mobile, ai_ml, qa_workplace, saved, mastered
    subView: 'grid', // grid, table, flashcards, quiz
    displayLimit: 36,

    // Storage
    savedIds: new Set(JSON.parse(localStorage.getItem('it_saved') || '[]')),
    masteredIds: new Set(JSON.parse(localStorage.getItem('it_mastered') || '[]')),
    reviewIds: new Set(JSON.parse(localStorage.getItem('it_review') || '[]')),

    // IT Flashcard
    fcList: [],
    fcIndex: 0,
    fcFlipped: false,

    // IT Quiz
    quizQuestions: [],
    quizIndex: 0,
    quizScore: 0,
    quizStreak: 0,
    quizAnswered: false,

    // Modal
    modalTerm: null,

    saveProgress() {
      localStorage.setItem('it_saved', JSON.stringify([...this.savedIds]));
      localStorage.setItem('it_mastered', JSON.stringify([...this.masteredIds]));
      localStorage.setItem('it_review', JSON.stringify([...this.reviewIds]));
      this.updateStatsUI();
    },

    toggleSave(id) {
      if (this.savedIds.has(id)) this.savedIds.delete(id);
      else this.savedIds.add(id);
      this.saveProgress();
    },

    toggleMastered(id) {
      if (this.masteredIds.has(id)) this.masteredIds.delete(id);
      else {
        this.masteredIds.add(id);
        this.reviewIds.delete(id);
      }
      this.saveProgress();
    },

    toggleReview(id) {
      if (this.reviewIds.has(id)) this.reviewIds.delete(id);
      else {
        this.reviewIds.add(id);
        this.masteredIds.delete(id);
      }
      this.saveProgress();
    },

    updateStatsUI() {
      const elMastered = document.getElementById('it-stat-mastered');
      const elSaved = document.getElementById('it-stat-saved');
      const elTotal = document.getElementById('it-stat-total');
      const elProgress = document.getElementById('it-stat-progress-bar');

      if (elMastered) elMastered.textContent = this.masteredIds.size;
      if (elSaved) elSaved.textContent = this.savedIds.size;
      if (elTotal) elTotal.textContent = `${this.terms.length} thuật ngữ`;
      if (elProgress) {
        const percent = Math.round((this.masteredIds.size / (this.terms.length || 1)) * 100);
        elProgress.style.width = `${percent}%`;
      }
    }
  };

  const ITApp = {
    initialized: false,

    init() {
      ITState.terms = window.IT_TERMS_DATA || window.IT_TERMS_DATABASE || [];
      ITState.filteredTerms = [...ITState.terms];
      ITState.updateStatsUI();

      if (!this.initialized) {
        this.setupEvents();
        this.initialized = true;
      }

      this.applyFilter();
    },

    setupEvents() {
      // Search
      const searchInput = document.getElementById('it-search-input');
      const clearBtn = document.getElementById('it-clear-search-btn');
      if (searchInput) {
        searchInput.addEventListener('input', (e) => {
          ITState.searchQuery = e.target.value;
          ITState.displayLimit = 36;
          this.applyFilter();
        });
      }
      if (clearBtn && searchInput) {
        clearBtn.addEventListener('click', () => {
          searchInput.value = '';
          ITState.searchQuery = '';
          ITState.displayLimit = 36;
          this.applyFilter();
          searchInput.focus();
        });
      }

      // Filter pills
      document.querySelectorAll('[data-it-filter]').forEach(btn => {
        btn.addEventListener('click', () => {
          document.querySelectorAll('[data-it-filter]').forEach(b => {
            b.classList.remove('bg-indigo-600', 'text-white', 'shadow-md');
            b.classList.add('bg-slate-100', 'dark:bg-slate-800', 'text-slate-700', 'dark:text-slate-300');
          });
          btn.classList.add('bg-indigo-600', 'text-white', 'shadow-md');
          btn.classList.remove('bg-slate-100', 'dark:bg-slate-800', 'text-slate-700', 'dark:text-slate-300');

          ITState.activeFilter = btn.dataset.itFilter;
          ITState.displayLimit = 36;
          this.applyFilter();
        });
      });

      // Sub-view buttons (Grid, Table, Flashcards, Quiz)
      const gridBtn = document.getElementById('it-view-grid-btn');
      const tableBtn = document.getElementById('it-view-table-btn');
      const fcBtn = document.getElementById('it-view-fc-btn');
      const quizBtn = document.getElementById('it-view-quiz-btn');

      const setSubView = (view) => {
        ITState.subView = view;
        [gridBtn, tableBtn, fcBtn, quizBtn].forEach(b => {
          if (b) {
            b.classList.remove('bg-white', 'dark:bg-slate-700', 'shadow-sm', 'text-indigo-600', 'dark:text-indigo-400');
            b.classList.add('text-slate-600', 'dark:text-slate-400');
          }
        });

        const activeBtn = view === 'grid' ? gridBtn : view === 'table' ? tableBtn : view === 'flashcards' ? fcBtn : quizBtn;
        if (activeBtn) {
          activeBtn.classList.add('bg-white', 'dark:bg-slate-700', 'shadow-sm', 'text-indigo-600', 'dark:text-indigo-400');
          activeBtn.classList.remove('text-slate-600', 'dark:text-slate-400');
        }

        document.getElementById('it-terms-grid-wrapper').classList.toggle('hidden', view !== 'grid');
        document.getElementById('it-terms-table-wrapper').classList.toggle('hidden', view !== 'table');
        document.getElementById('it-flashcards-wrapper').classList.toggle('hidden', view !== 'flashcards');
        document.getElementById('it-quiz-wrapper').classList.toggle('hidden', view !== 'quiz');

        if (view === 'grid' || view === 'table') {
          this.renderExplorer();
        } else if (view === 'flashcards') {
          this.initFlashcards();
        } else if (view === 'quiz') {
          this.startQuiz();
        }
      };

      if (gridBtn) gridBtn.addEventListener('click', () => setSubView('grid'));
      if (tableBtn) tableBtn.addEventListener('click', () => setSubView('table'));
      if (fcBtn) fcBtn.addEventListener('click', () => setSubView('flashcards'));
      if (quizBtn) quizBtn.addEventListener('click', () => setSubView('quiz'));

      // Load more
      const loadMoreBtn = document.getElementById('it-load-more-btn');
      if (loadMoreBtn) {
        loadMoreBtn.addEventListener('click', () => {
          ITState.displayLimit += 36;
          this.renderExplorer();
        });
      }

      // Modal close
      const modalClose = document.getElementById('it-modal-close-btn');
      const modalBackdrop = document.getElementById('it-modal-backdrop');
      if (modalClose) modalClose.addEventListener('click', () => this.closeModal());
      if (modalBackdrop) modalBackdrop.addEventListener('click', () => this.closeModal());

      // IT Flashcard controls
      const fcFlipBtn = document.getElementById('it-fc-flip-btn');
      const fcNextBtn = document.getElementById('it-fc-next-btn');
      const fcPrevBtn = document.getElementById('it-fc-prev-btn');
      const fcMasterBtn = document.getElementById('it-fc-master-btn');
      const fcReviewBtn = document.getElementById('it-fc-review-btn');
      const fcCardWrapper = document.getElementById('it-flashcard-wrapper');

      if (fcCardWrapper) {
        fcCardWrapper.addEventListener('click', (e) => {
          if (e.target.closest('button')) return;
          this.flipFlashcard();
        });
      }
      if (fcFlipBtn) fcFlipBtn.addEventListener('click', () => this.flipFlashcard());
      if (fcNextBtn) fcNextBtn.addEventListener('click', () => this.nextFlashcard());
      if (fcPrevBtn) fcPrevBtn.addEventListener('click', () => this.prevFlashcard());
      if (fcMasterBtn) fcMasterBtn.addEventListener('click', () => this.rateFlashcard(true));
      if (fcReviewBtn) fcReviewBtn.addEventListener('click', () => this.rateFlashcard(false));

      // IT Quiz restart
      const quizRestart = document.getElementById('it-quiz-restart-btn');
      if (quizRestart) quizRestart.addEventListener('click', () => this.startQuiz());
    },

    applyFilter() {
      const q = removeVietnameseTones(ITState.searchQuery.trim());
      const filter = ITState.activeFilter;

      let list = ITState.terms.filter(t => {
        if (filter !== 'all') {
          if (filter === 'saved' && !ITState.savedIds.has(t.id)) return false;
          if (filter === 'mastered' && !ITState.masteredIds.has(t.id)) return false;
          if (!['all', 'saved', 'mastered'].includes(filter)) {
            const dom = t.domain || t.subCategory;
            const matchesDomain = (
              dom === filter ||
              (filter === 'cloud' && dom === 'cloud_devops') ||
              (filter === 'ai' && dom === 'ai_ml') ||
              (filter === 'web' && dom === 'web_mobile')
            );
            if (!matchesDomain) return false;
          }
        }

        if (!q) return true;

        const termNorm = removeVietnameseTones(t.term);
        const meanNorm = removeVietnameseTones(t.meaning || t.meaning_vn);
        const exNorm = removeVietnameseTones(t.example || t.example_en);
        const exViNorm = removeVietnameseTones(t.exampleVi || t.example_vn);
        const tagNorm = removeVietnameseTones(t.conceptTag || t.concept_badge);
        const domNorm = removeVietnameseTones(t.subCategoryVi || t.domain_vn);

        return termNorm.includes(q) || meanNorm.includes(q) || exNorm.includes(q) || exViNorm.includes(q) || tagNorm.includes(q) || domNorm.includes(q);
      });

      ITState.filteredTerms = list;

      if (ITState.subView === 'grid' || ITState.subView === 'table') {
        this.renderExplorer();
      } else if (ITState.subView === 'flashcards') {
        this.initFlashcards();
      } else if (ITState.subView === 'quiz') {
        this.startQuiz();
      }
    },

    renderExplorer() {
      const countEl = document.getElementById('it-search-result-count');
      const gridContainer = document.getElementById('it-terms-container');
      const tableBody = document.getElementById('it-table-body');
      const loadMoreBtn = document.getElementById('it-load-more-btn');

      if (countEl) {
        countEl.textContent = `${ITState.filteredTerms.length} / ${ITState.terms.length} thuật ngữ`;
      }

      if (ITState.filteredTerms.length === 0) {
        if (gridContainer) {
          gridContainer.innerHTML = `
            <div class="col-span-full py-16 text-center text-slate-400">
              <i class="fa-solid fa-laptop-code text-5xl mb-3 text-slate-300 dark:text-slate-600"></i>
              <p class="text-lg font-medium text-slate-600 dark:text-slate-300">Không tìm thấy thuật ngữ CNTT nào</p>
              <p class="text-sm text-slate-400 mt-1">Thử tìm kiếm với từ khóa khác hoặc chuyển chuyên ngành.</p>
            </div>
          `;
        }
        if (loadMoreBtn) loadMoreBtn.classList.add('hidden');
        return;
      }

      const visibleList = ITState.filteredTerms.slice(0, ITState.displayLimit);

      // Render Grid Cards
      if (gridContainer) {
        gridContainer.innerHTML = visibleList.map(t => this.createCardHTML(t)).join('');
        this.attachCardEvents(gridContainer);
      }

      // Render Table Rows
      if (tableBody) {
        tableBody.innerHTML = visibleList.map(t => this.createTableRowHTML(t)).join('');
        this.attachTableEvents(tableBody);
      }

      // Load More Button
      if (loadMoreBtn) {
        if (ITState.displayLimit < ITState.filteredTerms.length) {
          loadMoreBtn.classList.remove('hidden');
          const remaining = ITState.filteredTerms.length - ITState.displayLimit;
          loadMoreBtn.textContent = `Xem thêm ${Math.min(36, remaining)} / ${remaining} thuật ngữ tiếp theo`;
        } else {
          loadMoreBtn.classList.add('hidden');
        }
      }
    },

    createCardHTML(item) {
      const isSaved = ITState.savedIds.has(item.id);
      const isMastered = ITState.masteredIds.has(item.id);

      return `
        <div class="it-card group relative bg-white dark:bg-slate-800 rounded-2xl border border-slate-200/80 dark:border-slate-700/80 shadow-sm hover:shadow-xl hover:-translate-y-1 transition-all duration-300 overflow-hidden flex flex-col cursor-pointer" data-term-id="${item.id}">
          
          <!-- Image Header with Tech Badge -->
          <div class="relative h-44 w-full overflow-hidden bg-slate-100 dark:bg-slate-900">
            <img src="${item.image}" alt="${item.term}" loading="lazy"
                 class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-105"
                 onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';" />
            
            <!-- Fallback SVG Art -->
            <div class="hidden absolute inset-0 bg-gradient-to-br ${item.gradient} flex-col items-center justify-center text-white p-4 text-center">
              <span class="text-4xl mb-2">${item.icon}</span>
              <span class="text-xl font-bold tracking-wide">${item.term}</span>
              <span class="text-xs text-white/80 font-mono-ipa mt-1">${item.ipa}</span>
            </div>

            <!-- Gradient Overlay -->
            <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-black/30 to-transparent"></div>

            <!-- Badges Top -->
            <div class="absolute top-3 left-3 flex items-center space-x-1.5 flex-wrap gap-y-1">
              <span class="px-2.5 py-1 text-xs font-bold rounded-lg bg-black/60 backdrop-blur-md text-white border border-white/20">
                #${item.id}
              </span>
              <span class="px-2.5 py-1 text-xs font-semibold rounded-lg bg-indigo-600/90 backdrop-blur-md text-white">
                ${item.subCategoryVi}
              </span>
              <span class="px-2 py-0.5 text-[10px] font-bold rounded-md bg-white/20 backdrop-blur-md text-white uppercase">
                ${item.partOfSpeech}
              </span>
            </div>

            <!-- Favorite Star Button -->
            <div class="absolute top-3 right-3">
              <button class="w-8 h-8 rounded-full bg-black/40 hover:bg-black/70 backdrop-blur-md flex items-center justify-center text-white transition-colors" data-action="it-star" data-term-id="${item.id}" title="Lưu thuật ngữ này">
                <i class="fa-${isSaved ? 'solid text-amber-400' : 'regular'} fa-star text-sm"></i>
              </button>
            </div>

            <!-- Visual Concept Tag on Image -->
            <div class="absolute bottom-14 left-3">
              <span class="px-2.5 py-1 text-[11px] font-semibold rounded-lg bg-black/70 backdrop-blur-md text-amber-300 border border-white/10 flex items-center gap-1.5 shadow">
                <span>${item.icon}</span>
                <span>${item.conceptTag}</span>
              </span>
            </div>

            <!-- Term Title Bottom -->
            <div class="absolute bottom-3 left-3 right-3 flex items-end justify-between text-white">
              <div>
                <h3 class="text-2xl font-black tracking-tight text-white flex items-center gap-2">
                  ${item.term}
                </h3>
                <span class="text-xs text-slate-300 font-mono-ipa">${item.ipa}</span>
              </div>
              <button class="w-9 h-9 rounded-full bg-white/20 hover:bg-white/40 backdrop-blur-md text-white flex items-center justify-center transition-all btn-press shadow" data-action="it-speak" data-text="${item.term}" title="Phát âm tiếng Anh">
                <i class="fa-solid fa-volume-high text-sm"></i>
              </button>
            </div>
          </div>

          <!-- Card Body -->
          <div class="p-4 flex-1 flex flex-col justify-between space-y-3">
            <div>
              <div class="text-[11px] font-bold uppercase tracking-wider text-slate-400 mb-1">Định nghĩa CNTT:</div>
              <p class="text-slate-800 dark:text-slate-200 text-sm font-semibold line-clamp-2">
                ${item.meaning}
              </p>
            </div>

            <!-- Example sentence box -->
            <div class="bg-indigo-50/60 dark:bg-slate-900/60 p-3 rounded-xl border border-indigo-100/60 dark:border-slate-700/60 text-xs text-slate-600 dark:text-slate-300">
              <div class="flex items-start justify-between gap-1 italic font-medium text-slate-800 dark:text-slate-200 mb-1">
                <span>"${item.example}"</span>
                <button class="text-indigo-600 dark:text-indigo-400 hover:text-indigo-800 p-1 rounded transition-colors flex-shrink-0" data-action="it-speak-ex" data-text="${item.example.replace(/"/g, '&quot;')}" title="Nghe câu ví dụ">
                  <i class="fa-solid fa-volume-low text-xs"></i>
                </button>
              </div>
              <div class="text-slate-500 dark:text-slate-400 line-clamp-1">
                ${item.exampleVi}
              </div>
            </div>

            <!-- Card Footer -->
            <div class="pt-2 border-t border-slate-100 dark:border-slate-700/60 flex items-center justify-between">
              <button class="px-3 py-1 rounded-lg text-xs font-semibold transition-all flex items-center gap-1.5 ${isMastered ? 'bg-emerald-500 text-white' : 'bg-slate-100 dark:bg-slate-700 text-slate-600 dark:text-slate-300 hover:bg-emerald-100 dark:hover:bg-emerald-900/40'}" data-action="it-master" data-term-id="${item.id}">
                <i class="fa-solid fa-check text-[10px]"></i>
                <span>${isMastered ? 'Đã thuộc' : 'Thuộc'}</span>
              </button>
              <span class="text-xs text-indigo-600 dark:text-indigo-400 font-semibold group-hover:translate-x-0.5 transition-transform flex items-center gap-1">
                Chi tiết <i class="fa-solid fa-chevron-right text-[10px]"></i>
              </span>
            </div>

          </div>

        </div>
      `;
    },

    createTableRowHTML(item) {
      const isSaved = ITState.savedIds.has(item.id);
      const isMastered = ITState.masteredIds.has(item.id);

      return `
        <tr class="border-b border-slate-100 dark:border-slate-800 hover:bg-slate-50/80 dark:hover:bg-slate-700/40 transition-colors cursor-pointer" data-term-id="${item.id}">
          <td class="py-3 px-4 text-xs font-bold text-slate-400">#${item.id}</td>
          <td class="py-3 px-4">
            <div class="flex items-center space-x-2.5">
              <span class="text-xl">${item.icon}</span>
              <div>
                <div class="font-bold text-slate-900 dark:text-white text-base">${item.term}</div>
                <div class="text-xs text-slate-400 font-mono-ipa">${item.ipa}</div>
              </div>
            </div>
          </td>
          <td class="py-3 px-4">
            <span class="px-2.5 py-1 text-xs font-bold rounded-lg bg-indigo-50 dark:bg-indigo-950/60 text-indigo-700 dark:text-indigo-300 border border-indigo-200/60 dark:border-indigo-800/60">
              ${item.subCategoryVi}
            </span>
          </td>
          <td class="py-3 px-4 text-sm text-slate-700 dark:text-slate-200 max-w-sm truncate font-medium">
            ${item.meaning}
          </td>
          <td class="py-3 px-4 text-xs italic text-slate-500 dark:text-slate-400 max-w-xs truncate">
            "${item.example}"
          </td>
          <td class="py-3 px-4 text-right space-x-1" onclick="event.stopPropagation()">
            <button class="w-8 h-8 rounded-lg bg-slate-100 dark:bg-slate-700 hover:bg-indigo-100 dark:hover:bg-indigo-900 text-slate-600 dark:text-slate-300 hover:text-indigo-600 transition-colors" data-action="it-speak" data-text="${item.term}" title="Phát âm">
              <i class="fa-solid fa-volume-high text-xs"></i>
            </button>
            <button class="w-8 h-8 rounded-lg bg-slate-100 dark:bg-slate-700 hover:bg-amber-100 text-slate-600 dark:text-slate-300 hover:text-amber-500 transition-colors" data-action="it-star" data-term-id="${item.id}" title="Lưu">
              <i class="fa-${isSaved ? 'solid text-amber-400' : 'regular'} fa-star text-xs"></i>
            </button>
            <button class="w-8 h-8 rounded-lg ${isMastered ? 'bg-emerald-500 text-white' : 'bg-slate-100 dark:bg-slate-700 text-slate-600 dark:text-slate-300 hover:bg-emerald-100 hover:text-emerald-600'} transition-colors" data-action="it-master" data-term-id="${item.id}" title="Đã thuộc">
              <i class="fa-solid fa-check text-xs"></i>
            </button>
          </td>
        </tr>
      `;
    },

    attachCardEvents(container) {
      container.querySelectorAll('.it-card').forEach(card => {
        card.addEventListener('click', (e) => {
          const actionBtn = e.target.closest('[data-action]');
          if (actionBtn) {
            e.stopPropagation();
            const action = actionBtn.dataset.action;
            const termId = parseInt(actionBtn.dataset.termId || card.dataset.termId);

            if (action === 'it-star') {
              ITState.toggleSave(termId);
              this.renderExplorer();
            } else if (action === 'it-master') {
              ITState.toggleMastered(termId);
              this.renderExplorer();
            } else if (action === 'it-speak') {
              speakTerm(actionBtn.dataset.text);
            } else if (action === 'it-speak-ex') {
              speakTerm(actionBtn.dataset.text);
            }
            return;
          }

          const termId = parseInt(card.dataset.termId);
          this.openModal(termId);
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
            const termId = parseInt(actionBtn.dataset.termId || row.dataset.termId);

            if (action === 'it-star') {
              ITState.toggleSave(termId);
              this.renderExplorer();
            } else if (action === 'it-master') {
              ITState.toggleMastered(termId);
              this.renderExplorer();
            } else if (action === 'it-speak') {
              speakTerm(actionBtn.dataset.text);
            }
            return;
          }

          const termId = parseInt(row.dataset.termId);
          this.openModal(termId);
        });
      });
    },

    // Modal
    openModal(termId) {
      const term = ITState.terms.find(t => t.id === termId);
      if (!term) return;

      ITState.modalTerm = term;
      const modal = document.getElementById('it-term-modal');
      if (!modal) return;

      document.getElementById('it-modal-id').textContent = `#${term.id}`;
      document.getElementById('it-modal-cat').textContent = term.subCategoryVi;
      document.getElementById('it-modal-pos').textContent = term.partOfSpeech;
      document.getElementById('it-modal-concept').innerHTML = `<span>${term.icon}</span> <span>${term.conceptTag}</span>`;
      document.getElementById('it-modal-title').textContent = term.term;
      document.getElementById('it-modal-ipa').textContent = term.ipa;
      document.getElementById('it-modal-meaning').textContent = term.meaning;
      document.getElementById('it-modal-example-en').textContent = `"${term.example}"`;
      document.getElementById('it-modal-example-vi').textContent = term.exampleVi;

      const img = document.getElementById('it-modal-img');
      if (img) img.src = term.image;

      document.getElementById('it-modal-speak-term').onclick = () => speakTerm(term.term);
      document.getElementById('it-modal-speak-ex').onclick = () => speakTerm(term.example);

      const starBtn = document.getElementById('it-modal-star-btn');
      const masterBtn = document.getElementById('it-modal-master-btn');

      const updateButtons = () => {
        const isSaved = ITState.savedIds.has(term.id);
        const isMastered = ITState.masteredIds.has(term.id);
        if (starBtn) {
          starBtn.innerHTML = `<i class="fa-${isSaved ? 'solid text-amber-400' : 'regular'} fa-star mr-1.5"></i> ${isSaved ? 'Đã lưu' : 'Lưu thuật ngữ'}`;
        }
        if (masterBtn) {
          masterBtn.innerHTML = `<i class="fa-solid fa-check mr-1.5"></i> ${isMastered ? 'Đã thuộc thuật ngữ này' : 'Đánh dấu đã thuộc'}`;
          masterBtn.className = `px-5 py-2.5 rounded-xl font-semibold text-sm transition-all btn-press ${isMastered ? 'bg-emerald-600 text-white' : 'bg-slate-100 dark:bg-slate-700 text-slate-700 dark:text-slate-200 hover:bg-emerald-500 hover:text-white'}`;
        }
      };

      if (starBtn) {
        starBtn.onclick = () => {
          ITState.toggleSave(term.id);
          updateButtons();
          this.renderExplorer();
        };
      }
      if (masterBtn) {
        masterBtn.onclick = () => {
          ITState.toggleMastered(term.id);
          updateButtons();
          this.renderExplorer();
        };
      }

      updateButtons();
      modal.classList.remove('hidden');
      document.body.classList.add('overflow-hidden');
    },

    closeModal() {
      const modal = document.getElementById('it-term-modal');
      if (modal) modal.classList.add('hidden');
      document.body.classList.remove('overflow-hidden');
    },

    // IT Flashcards
    initFlashcards() {
      ITState.fcList = ITState.filteredTerms.length > 0 ? [...ITState.filteredTerms] : [...ITState.terms];
      ITState.fcIndex = 0;
      ITState.fcFlipped = false;
      this.renderFlashcard();
    },

    renderFlashcard() {
      const list = ITState.fcList;
      if (!list.length) return;

      const item = list[ITState.fcIndex];
      const counterEl = document.getElementById('it-fc-counter');
      const barEl = document.getElementById('it-fc-progress-bar');
      const cardWrapper = document.getElementById('it-flashcard-wrapper');

      if (counterEl) counterEl.textContent = `${ITState.fcIndex + 1} / ${list.length}`;
      if (barEl) barEl.style.width = `${((ITState.fcIndex + 1) / list.length) * 100}%`;

      if (cardWrapper) {
        cardWrapper.classList.toggle('flashcard-flipped', ITState.fcFlipped);
      }

      // Front
      document.getElementById('it-fc-front-id').textContent = `#${item.id}`;
      document.getElementById('it-fc-front-cat').textContent = item.subCategoryVi;
      document.getElementById('it-fc-front-concept').innerHTML = `<span>${item.icon}</span> <span>${item.conceptTag}</span>`;
      document.getElementById('it-fc-front-term').textContent = item.term;
      document.getElementById('it-fc-front-ipa').textContent = item.ipa;
      document.getElementById('it-fc-front-pos').textContent = `[${item.partOfSpeech}]`;

      const imgFront = document.getElementById('it-fc-front-img');
      if (imgFront) imgFront.src = item.image;

      document.getElementById('it-fc-front-speak').onclick = (e) => {
        e.stopPropagation();
        speakTerm(item.term);
      };

      // Back
      document.getElementById('it-fc-back-term').textContent = item.term;
      document.getElementById('it-fc-back-ipa').textContent = item.ipa;
      document.getElementById('it-fc-back-meaning').textContent = item.meaning;
      document.getElementById('it-fc-back-example-en').textContent = `"${item.example}"`;
      document.getElementById('it-fc-back-example-vi').textContent = item.exampleVi;

      document.getElementById('it-fc-back-speak').onclick = (e) => {
        e.stopPropagation();
        speakTerm(item.term);
      };
      document.getElementById('it-fc-back-speak-ex').onclick = (e) => {
        e.stopPropagation();
        speakTerm(item.example);
      };
    },

    flipFlashcard() {
      ITState.fcFlipped = !ITState.fcFlipped;
      const cardWrapper = document.getElementById('it-flashcard-wrapper');
      if (cardWrapper) cardWrapper.classList.toggle('flashcard-flipped', ITState.fcFlipped);
    },

    nextFlashcard() {
      if (ITState.fcIndex < ITState.fcList.length - 1) ITState.fcIndex++;
      else ITState.fcIndex = 0;
      ITState.fcFlipped = false;
      this.renderFlashcard();
    },

    prevFlashcard() {
      if (ITState.fcIndex > 0) ITState.fcIndex--;
      else ITState.fcIndex = ITState.fcList.length - 1;
      ITState.fcFlipped = false;
      this.renderFlashcard();
    },

    rateFlashcard(isMastered) {
      const term = ITState.fcList[ITState.fcIndex];
      if (!term) return;
      if (isMastered) {
        ITState.masteredIds.add(term.id);
        ITState.reviewIds.delete(term.id);
      } else {
        ITState.reviewIds.add(term.id);
        ITState.masteredIds.delete(term.id);
      }
      ITState.saveProgress();
      this.nextFlashcard();
    },

    // IT Quiz
    startQuiz() {
      ITState.quizScore = 0;
      ITState.quizStreak = 0;
      ITState.quizIndex = 0;
      ITState.quizAnswered = false;

      const pool = [...ITState.terms].sort(() => Math.random() - 0.5);
      const selected = pool.slice(0, 10);

      ITState.quizQuestions = selected.map(term => {
        const prompt = `Thuật ngữ CNTT "${term.term}" [${term.subCategoryVi}] có nghĩa là gì?`;
        const correctAnswer = term.meaning.split(':')[0].trim();

        // 3 distractors
        const distractors = ITState.terms
          .filter(t => t.id !== term.id)
          .map(t => t.meaning.split(':')[0].trim())
          .filter((v, idx, s) => s.indexOf(v) === idx && v !== correctAnswer)
          .sort(() => Math.random() - 0.5)
          .slice(0, 3);

        const options = [correctAnswer, ...distractors].sort(() => Math.random() - 0.5);

        return {
          term,
          prompt,
          correctAnswer,
          options
        };
      });

      document.getElementById('it-quiz-active-card').classList.remove('hidden');
      document.getElementById('it-quiz-result-card').classList.add('hidden');
      this.renderQuizQuestion();
    },

    renderQuizQuestion() {
      const q = ITState.quizQuestions[ITState.quizIndex];
      if (!q) {
        this.finishQuiz();
        return;
      }

      ITState.quizAnswered = false;

      document.getElementById('it-quiz-progress-text').textContent = `Câu ${ITState.quizIndex + 1} / ${ITState.quizQuestions.length}`;
      document.getElementById('it-quiz-score').textContent = `Điểm: ${ITState.quizScore}`;
      document.getElementById('it-quiz-streak').innerHTML = `<i class="fa-solid fa-fire text-amber-500 mr-1"></i>Streak: ${ITState.quizStreak}`;
      document.getElementById('it-quiz-bar').style.width = `${((ITState.quizIndex + 1) / ITState.quizQuestions.length) * 100}%`;

      document.getElementById('it-quiz-term-display').textContent = `${q.term.term} (${q.term.ipa})`;
      document.getElementById('it-quiz-prompt').textContent = q.prompt;
      document.getElementById('it-quiz-speak').onclick = () => speakTerm(q.term.term);

      const optionsBox = document.getElementById('it-quiz-options-container');
      optionsBox.innerHTML = q.options.map((opt, idx) => `
        <button class="it-quiz-opt-btn w-full p-4 rounded-xl border-2 border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-800 text-left font-semibold text-slate-800 dark:text-slate-100 hover:border-indigo-500 dark:hover:border-indigo-400 hover:bg-indigo-50/50 dark:hover:bg-slate-700/60 transition-all flex items-center justify-between group btn-press" data-opt-idx="${idx}">
          <div class="flex items-center space-x-3">
            <span class="w-8 h-8 rounded-lg bg-slate-100 dark:bg-slate-700 text-slate-600 dark:text-slate-300 font-bold flex items-center justify-center text-sm group-hover:bg-indigo-600 group-hover:text-white transition-colors">
              ${idx + 1}
            </span>
            <span class="text-base">${opt}</span>
          </div>
          <span class="it-opt-icon opacity-0"></span>
        </button>
      `).join('');

      optionsBox.querySelectorAll('.it-quiz-opt-btn').forEach((btn, idx) => {
        btn.addEventListener('click', () => this.handleQuizAnswer(idx));
      });

      const explBox = document.getElementById('it-quiz-expl-box');
      if (explBox) explBox.classList.add('hidden');
    },

    handleQuizAnswer(optIdx) {
      if (ITState.quizAnswered) return;
      ITState.quizAnswered = true;

      const q = ITState.quizQuestions[ITState.quizIndex];
      const selected = q.options[optIdx];
      const isCorrect = selected === q.correctAnswer;
      const btns = document.querySelectorAll('.it-quiz-opt-btn');

      if (isCorrect) {
        ITState.quizScore += 10;
        ITState.quizStreak++;
        btns[optIdx].classList.add('border-emerald-500', 'bg-emerald-50', 'dark:bg-emerald-950/40', 'text-emerald-800', 'dark:text-emerald-200');
        btns[optIdx].querySelector('.it-opt-icon').innerHTML = '<i class="fa-solid fa-circle-check text-emerald-500 text-xl"></i>';
        btns[optIdx].querySelector('.it-opt-icon').classList.remove('opacity-0');
      } else {
        ITState.quizStreak = 0;
        btns[optIdx].classList.add('border-rose-500', 'bg-rose-50', 'dark:bg-rose-950/40', 'text-rose-800', 'dark:text-rose-200');
        btns[optIdx].querySelector('.it-opt-icon').innerHTML = '<i class="fa-solid fa-circle-xmark text-rose-500 text-xl"></i>';
        btns[optIdx].querySelector('.it-opt-icon').classList.remove('opacity-0');

        btns.forEach((btn, idx) => {
          if (q.options[idx] === q.correctAnswer) {
            btn.classList.add('border-emerald-500', 'bg-emerald-50/50', 'dark:bg-emerald-950/20');
            btn.querySelector('.it-opt-icon').innerHTML = '<i class="fa-solid fa-check text-emerald-500 text-lg"></i>';
            btn.querySelector('.it-opt-icon').classList.remove('opacity-0');
          }
        });
      }

      // Show explanation
      const explBox = document.getElementById('it-quiz-expl-box');
      if (explBox) {
        explBox.classList.remove('hidden');
        document.getElementById('it-quiz-expl-term').textContent = q.term.term;
        document.getElementById('it-quiz-expl-cat').textContent = q.term.subCategoryVi;
        document.getElementById('it-quiz-expl-full').textContent = q.term.meaning;
        document.getElementById('it-quiz-expl-ex').textContent = `"${q.term.example}" (${q.term.exampleVi})`;

        const nextBtn = document.getElementById('it-quiz-next-btn');
        if (nextBtn) {
          nextBtn.focus();
          nextBtn.onclick = () => {
            ITState.quizIndex++;
            this.renderQuizQuestion();
          };
        }
      }
    },

    finishQuiz() {
      document.getElementById('it-quiz-active-card').classList.add('hidden');
      const resCard = document.getElementById('it-quiz-result-card');
      resCard.classList.remove('hidden');

      const maxScore = ITState.quizQuestions.length * 10;
      const score = ITState.quizScore;
      const percent = Math.round((score / maxScore) * 100);

      document.getElementById('it-quiz-final-score').textContent = `${score} / ${maxScore}`;
      document.getElementById('it-quiz-final-percent').textContent = `${percent}%`;
    }
  };

  window.ITApp = ITApp;

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => ITApp.init());
  } else {
    ITApp.init();
  }
})();
