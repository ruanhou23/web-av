# -*- coding: utf-8 -*-
with open("/home/ken/.gemini/antigravity/scratch/irregular-verbs-360/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Add Nav Tab in Sub-Navbar
nav_target = """          <button data-nav-tab="patterns" class="px-3 py-2 text-sm font-semibold rounded-lg border-b-2 border-transparent text-slate-500 dark:text-slate-400 hover:text-slate-700 dark:hover:text-slate-200 flex items-center space-x-2 whitespace-nowrap">
            <i class="fa-solid fa-layer-group"></i>
            <span>4 Nhóm quy tắc & Mẹo</span>
          </button>"""

nav_replacement = """          <button data-nav-tab="patterns" class="px-3 py-2 text-sm font-semibold rounded-lg border-b-2 border-transparent text-slate-500 dark:text-slate-400 hover:text-slate-700 dark:hover:text-slate-200 flex items-center space-x-2 whitespace-nowrap">
            <i class="fa-solid fa-layer-group"></i>
            <span>4 Nhóm quy tắc & Mẹo</span>
          </button>

          <button data-nav-tab="it-english" class="px-3.5 py-2 text-sm font-bold rounded-lg border-b-2 border-transparent text-slate-500 dark:text-slate-400 hover:text-indigo-600 dark:hover:text-indigo-400 flex items-center space-x-2 whitespace-nowrap group">
            <span class="w-2 h-2 rounded-full bg-emerald-500 animate-pulse"></span>
            <i class="fa-solid fa-laptop-code text-indigo-500"></i>
            <span class="bg-gradient-to-r from-indigo-600 to-cyan-500 bg-clip-text text-transparent font-extrabold">Tiếng Anh CNTT</span>
            <span class="px-2 py-0.5 text-[10px] font-bold rounded-full bg-indigo-100 dark:bg-indigo-900/60 text-indigo-700 dark:text-indigo-300">100 thuật ngữ</span>
          </button>"""

html = html.replace(nav_target, nav_replacement)

# 2. Add IT English View Section before </main>
it_section_html = """
    <!-- ========================================== -->
    <!-- VIEW 6: TIẾNG ANH CHUYÊN NGÀNH CNTT (IT ENGLISH) -->
    <!-- ========================================== -->
    <section id="it-english-view" class="hidden space-y-6">
      
      <!-- IT Hero Banner -->
      <div class="relative overflow-hidden rounded-3xl bg-gradient-to-r from-slate-900 via-indigo-950 to-slate-900 text-white p-6 sm:p-10 shadow-xl border border-indigo-500/20">
        <div class="relative z-10 max-w-3xl space-y-4">
          <div class="inline-flex items-center space-x-2 px-3 py-1 rounded-full bg-indigo-500/20 backdrop-blur-md text-xs font-semibold text-indigo-300 border border-indigo-400/30">
            <i class="fa-solid fa-code text-cyan-400"></i>
            <span>Chuyên đề: Tiếng Anh Chuyên Ngành Công Nghệ Thông Tin</span>
          </div>
          <h2 class="text-3xl sm:text-5xl font-black tracking-tight leading-tight">
            100 Thuật Ngữ CNTT Thực Chiến
          </h2>
          <p class="text-slate-300 text-sm sm:text-base leading-relaxed max-w-2xl">
            Làm chủ hệ thống thuật ngữ chuẩn mực về <strong>Lập trình, Cơ sở dữ liệu, An ninh mạng, Điện toán đám mây (DevOps), Trí tuệ nhân tạo (AI)</strong> và <strong>Phát triển Web/Mobile</strong> kèm phát âm bản ngữ và câu ngữ cảnh thực tế.
          </p>

          <!-- IT Search Bar -->
          <div class="pt-2">
            <div class="relative max-w-2xl">
              <div class="absolute inset-y-0 left-0 pl-4 flex items-center pointer-events-none text-slate-400">
                <i class="fa-solid fa-magnifying-glass text-lg text-indigo-400"></i>
              </div>
              <input type="text" id="it-search-input"
                     placeholder="Tìm thuật ngữ CNTT (vd: refactor, deploy, query, firewall, neural network, api...)"
                     class="w-full pl-12 pr-28 py-4 rounded-2xl bg-white/10 dark:bg-slate-900/90 text-white placeholder-slate-400 font-medium shadow-2xl focus:outline-none focus:ring-4 focus:ring-indigo-400/50 backdrop-blur-md transition-all border border-indigo-500/30">
              <div class="absolute inset-y-0 right-0 pr-3 flex items-center space-x-2">
                <button id="it-clear-search-btn" class="p-2 text-slate-400 hover:text-white transition-colors" title="Xóa tìm kiếm">
                  <i class="fa-solid fa-xmark"></i>
                </button>
              </div>
            </div>
          </div>
        </div>

        <div class="absolute right-0 bottom-0 translate-x-8 translate-y-8 opacity-10 pointer-events-none text-indigo-400">
          <i class="fa-solid fa-microchip text-[260px]"></i>
        </div>
      </div>

      <!-- IT Toolbar & Domains Filter -->
      <div class="bg-white dark:bg-slate-900 p-4 rounded-2xl border border-slate-200/80 dark:border-slate-800 shadow-sm space-y-4">
        
        <!-- Domain Pills -->
        <div class="flex items-center space-x-2 overflow-x-auto pb-1 no-scrollbar">
          <span class="text-xs font-bold text-slate-400 uppercase tracking-wider whitespace-nowrap mr-1">Chuyên ngành:</span>
          
          <button data-it-filter="all" class="px-3.5 py-1.5 rounded-xl text-xs font-semibold bg-indigo-600 text-white shadow-md transition-all whitespace-nowrap">
            🌟 Tất cả (100)
          </button>
          <button data-it-filter="programming" class="px-3.5 py-1.5 rounded-xl text-xs font-semibold bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300 hover:bg-slate-200 dark:hover:bg-slate-700 transition-all whitespace-nowrap">
            💻 Lập trình & Phần mềm
          </button>
          <button data-it-filter="database" class="px-3.5 py-1.5 rounded-xl text-xs font-semibold bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300 hover:bg-slate-200 dark:hover:bg-slate-700 transition-all whitespace-nowrap">
            🗄️ Cơ sở dữ liệu
          </button>
          <button data-it-filter="security" class="px-3.5 py-1.5 rounded-xl text-xs font-semibold bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300 hover:bg-slate-200 dark:hover:bg-slate-700 transition-all whitespace-nowrap">
            🛡️ Mạng & Bảo mật
          </button>
          <button data-it-filter="cloud" class="px-3.5 py-1.5 rounded-xl text-xs font-semibold bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300 hover:bg-slate-200 dark:hover:bg-slate-700 transition-all whitespace-nowrap">
            ☁️ Cloud & DevOps
          </button>
          <button data-it-filter="ai" class="px-3.5 py-1.5 rounded-xl text-xs font-semibold bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300 hover:bg-slate-200 dark:hover:bg-slate-700 transition-all whitespace-nowrap">
            🤖 Trí tuệ nhân tạo (AI)
          </button>
          <button data-it-filter="web" class="px-3.5 py-1.5 rounded-xl text-xs font-semibold bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300 hover:bg-slate-200 dark:hover:bg-slate-700 transition-all whitespace-nowrap">
            🌐 Phát triển Web & App
          </button>
          <button data-it-filter="saved" class="px-3.5 py-1.5 rounded-xl text-xs font-semibold bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300 hover:bg-slate-200 dark:hover:bg-slate-700 transition-all whitespace-nowrap">
            ⭐ Đã lưu
          </button>
          <button data-it-filter="mastered" class="px-3.5 py-1.5 rounded-xl text-xs font-semibold bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300 hover:bg-slate-200 dark:hover:bg-slate-700 transition-all whitespace-nowrap">
            ✅ Đã thuộc
          </button>
        </div>

        <!-- Mode controls: Grid, Table, Flashcards, Quiz -->
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 pt-2 border-t border-slate-100 dark:border-slate-800 text-sm">
          <div class="flex items-center space-x-3 text-xs font-semibold">
            <span id="it-search-result-count" class="font-bold text-slate-700 dark:text-slate-300 text-sm">
              100 / 100 thuật ngữ
            </span>
            <span class="text-slate-300 dark:text-slate-700">|</span>
            <span class="text-emerald-600 dark:text-emerald-400">Đã thuộc: <strong id="it-stat-mastered">0</strong></span>
            <span class="text-slate-300 dark:text-slate-700">|</span>
            <span class="text-amber-500">Đã lưu: <strong id="it-stat-saved">0</strong></span>
          </div>

          <!-- Switcher -->
          <div class="flex items-center bg-slate-100 dark:bg-slate-800 p-0.5 rounded-xl border border-slate-200 dark:border-slate-700">
            <button id="it-view-grid-btn" class="px-3 py-1.5 rounded-lg text-xs font-semibold bg-white dark:bg-slate-700 shadow-sm text-indigo-600 dark:text-indigo-400 transition-all" title="Xem thẻ ảnh trực quan">
              <i class="fa-solid fa-grip mr-1"></i>Thẻ thuật ngữ
            </button>
            <button id="it-view-table-btn" class="px-3 py-1.5 rounded-lg text-xs font-semibold text-slate-600 dark:text-slate-400 hover:text-slate-900 transition-all" title="Xem bảng danh sách">
              <i class="fa-solid fa-table-list mr-1"></i>Bảng
            </button>
            <button id="it-view-fc-btn" class="px-3 py-1.5 rounded-lg text-xs font-semibold text-slate-600 dark:text-slate-400 hover:text-slate-900 transition-all" title="Lật thẻ Flashcard">
              <i class="fa-solid fa-clone mr-1"></i>Flashcards
            </button>
            <button id="it-view-quiz-btn" class="px-3 py-1.5 rounded-lg text-xs font-semibold text-slate-600 dark:text-slate-400 hover:text-slate-900 transition-all" title="Luyện thi trắc nghiệm">
              <i class="fa-solid fa-circle-question mr-1"></i>Trắc nghiệm
            </button>
          </div>
        </div>

      </div>

      <!-- 1. IT Grid Cards Wrapper -->
      <div id="it-terms-grid-wrapper" class="space-y-6">
        <div id="it-terms-container" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
          <!-- Rendered by it_app.js -->
        </div>

        <div class="text-center pt-2 pb-6">
          <button id="it-load-more-btn" class="px-6 py-2.5 rounded-xl bg-indigo-600 hover:bg-indigo-700 text-white font-semibold text-sm shadow-md transition-all btn-press">
            Xem thêm thuật ngữ
          </button>
        </div>
      </div>

      <!-- 2. IT Table Wrapper -->
      <div id="it-terms-table-wrapper" class="hidden bg-white dark:bg-slate-800 rounded-2xl border border-slate-200 dark:border-slate-700 overflow-hidden shadow-sm">
        <div class="overflow-x-auto">
          <table class="w-full text-left border-collapse">
            <thead>
              <tr class="bg-slate-50 dark:bg-slate-900 border-b border-slate-200 dark:border-slate-700 text-xs uppercase font-bold text-slate-500 tracking-wider">
                <th class="py-3 px-4">STT</th>
                <th class="py-3 px-4">Thuật ngữ & Phiên âm</th>
                <th class="py-3 px-4">Chuyên ngành</th>
                <th class="py-3 px-4">Định nghĩa kỹ thuật</th>
                <th class="py-3 px-4">Câu ví dụ ngữ cảnh</th>
                <th class="py-3 px-4 text-right">Thao tác</th>
              </tr>
            </thead>
            <tbody id="it-table-body" class="divide-y divide-slate-100 dark:divide-slate-700/60 text-sm">
              <!-- Rendered by it_app.js -->
            </tbody>
          </table>
        </div>
      </div>

      <!-- 3. IT Flashcards Wrapper -->
      <div id="it-flashcards-wrapper" class="hidden max-w-2xl mx-auto space-y-6">
        <div class="flex items-center justify-between bg-white dark:bg-slate-900 p-4 rounded-2xl border border-slate-200 dark:border-slate-800 shadow-sm">
          <div class="flex items-center space-x-2">
            <span class="text-xs font-bold text-slate-400 uppercase">Thẻ CNTT:</span>
            <span id="it-fc-counter" class="text-sm font-extrabold text-indigo-600 dark:text-indigo-400">1 / 100</span>
          </div>
          <div class="flex-1 max-w-xs mx-4 bg-slate-100 dark:bg-slate-800 h-2.5 rounded-full overflow-hidden">
            <div id="it-fc-progress-bar" class="h-full bg-indigo-600 rounded-full transition-all duration-300" style="width: 1%"></div>
          </div>
          <button id="it-fc-flip-btn" class="px-4 py-1.5 rounded-lg bg-indigo-600 text-white font-bold text-xs shadow-md">
            Lật thẻ
          </button>
        </div>

        <!-- 3D Card -->
        <div class="perspective-1000 w-full min-h-[440px]">
          <div id="it-flashcard-wrapper" class="flashcard-wrapper relative w-full h-full cursor-pointer select-none transition-transform duration-500">
            <div class="flashcard-inner relative w-full h-full min-h-[440px] rounded-3xl shadow-xl transition-all duration-500">
              
              <!-- Front Side -->
              <div class="flashcard-front absolute inset-0 bg-white dark:bg-slate-800 rounded-3xl border-2 border-slate-200 dark:border-slate-700 p-6 flex flex-col justify-between backface-hidden overflow-hidden">
                <div class="flex items-center justify-between">
                  <div class="flex items-center space-x-2">
                    <span id="it-fc-front-id" class="px-3 py-1 rounded-full bg-slate-100 dark:bg-slate-700 text-slate-600 dark:text-slate-300 text-xs font-bold">#1</span>
                    <span id="it-fc-front-cat" class="px-3 py-1 rounded-full bg-indigo-100 dark:bg-indigo-900/60 text-indigo-700 dark:text-indigo-300 text-xs font-bold">Lập trình</span>
                  </div>
                  <span id="it-fc-front-concept" class="px-3 py-1 rounded-full bg-amber-50 dark:bg-amber-950/60 text-amber-700 dark:text-amber-300 text-xs font-bold flex items-center gap-1 border border-amber-200"></span>
                </div>

                <div class="relative w-full h-44 rounded-2xl overflow-hidden bg-slate-100 dark:bg-slate-900 my-2">
                  <img id="it-fc-front-img" src="" alt="IT illustration" class="w-full h-full object-cover" />
                </div>

                <div class="text-center space-y-1">
                  <div class="flex items-center justify-center gap-2">
                    <h3 id="it-fc-front-term" class="text-3xl font-black text-slate-900 dark:text-white"></h3>
                    <button id="it-fc-front-speak" class="w-9 h-9 rounded-full bg-indigo-50 dark:bg-slate-700 text-indigo-600 dark:text-indigo-400 flex items-center justify-center transition-all btn-press shadow" title="Phát âm">
                      <i class="fa-solid fa-volume-high text-sm"></i>
                    </button>
                  </div>
                  <p id="it-fc-front-ipa" class="text-slate-400 font-mono-ipa text-sm"></p>
                  <p id="it-fc-front-pos" class="text-xs text-indigo-500 font-semibold"></p>
                </div>

                <div class="text-center pt-2 border-t border-slate-100 dark:border-slate-700 text-xs text-slate-400">
                  <i class="fa-solid fa-arrow-rotate-left mr-1"></i>Chạm để lật xem định nghĩa kỹ thuật & câu ví dụ
                </div>
              </div>

              <!-- Back Side -->
              <div class="flashcard-back absolute inset-0 bg-white dark:bg-slate-800 rounded-3xl border-2 border-indigo-400 dark:border-indigo-600 p-6 flex flex-col justify-between backface-hidden rotate-y-180 overflow-y-auto">
                <div class="flex items-center justify-between border-b border-slate-100 dark:border-slate-700 pb-2">
                  <div class="flex items-center gap-2">
                    <span id="it-fc-back-term" class="text-xl font-black text-indigo-600 dark:text-indigo-400"></span>
                    <span id="it-fc-back-ipa" class="text-xs text-slate-400 font-mono-ipa"></span>
                  </div>
                  <button id="it-fc-back-speak" class="px-3 py-1 bg-indigo-100 dark:bg-indigo-900/60 hover:bg-indigo-200 text-indigo-700 dark:text-indigo-300 rounded-lg text-xs font-bold transition-colors">
                    <i class="fa-solid fa-volume-high mr-1"></i>Phát âm
                  </button>
                </div>

                <div class="bg-indigo-50/70 dark:bg-slate-900/80 p-4 rounded-2xl border border-indigo-100 dark:border-slate-700">
                  <span class="text-xs font-bold text-slate-400 uppercase tracking-wider">Định nghĩa chuyên ngành:</span>
                  <p id="it-fc-back-meaning" class="text-base font-semibold text-slate-800 dark:text-white mt-1 leading-relaxed"></p>
                </div>

                <div class="bg-slate-50 dark:bg-slate-900 p-4 rounded-2xl border border-slate-200 dark:border-slate-700 relative">
                  <div class="flex items-center justify-between mb-1">
                    <span class="text-xs font-bold text-indigo-600 dark:text-indigo-400 uppercase">Ví dụ câu thực tế trong IT:</span>
                    <button id="it-fc-back-speak-ex" class="text-indigo-600 hover:text-indigo-800 p-1" title="Nghe câu ví dụ">
                      <i class="fa-solid fa-volume-high text-xs"></i>
                    </button>
                  </div>
                  <p id="it-fc-back-example-en" class="italic text-slate-800 dark:text-slate-200 text-sm font-medium mb-1"></p>
                  <p id="it-fc-back-example-vi" class="text-slate-500 dark:text-slate-400 text-xs"></p>
                </div>

                <div class="text-center pt-2 border-t border-slate-100 dark:border-slate-700 text-xs text-slate-400">
                  Chạm để lật lại mặt trước
                </div>
              </div>

            </div>
          </div>
        </div>

        <!-- Rating Buttons -->
        <div class="grid grid-cols-2 gap-4">
          <button id="it-fc-review-btn" class="py-3 px-4 rounded-2xl bg-rose-50 hover:bg-rose-100 dark:bg-rose-950/40 text-rose-700 dark:text-rose-300 font-bold text-sm border border-rose-200 dark:border-rose-800 flex items-center justify-center space-x-2 btn-press">
            <i class="fa-solid fa-xmark text-lg"></i>
            <span>Chưa nhớ (Cần ôn lại)</span>
          </button>
          <button id="it-fc-master-btn" class="py-3 px-4 rounded-2xl bg-emerald-50 hover:bg-emerald-100 dark:bg-emerald-950/40 text-emerald-700 dark:text-emerald-300 font-bold text-sm border border-emerald-200 dark:border-emerald-800 flex items-center justify-center space-x-2 btn-press">
            <i class="fa-solid fa-check text-lg"></i>
            <span>Đã thuộc thuật ngữ</span>
          </button>
        </div>

        <!-- Navigation Buttons -->
        <div class="flex items-center justify-between pt-2">
          <button id="it-fc-prev-btn" class="px-5 py-2.5 rounded-xl bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 font-semibold text-sm hover:bg-slate-50 dark:hover:bg-slate-700 flex items-center space-x-2 btn-press shadow-sm">
            <i class="fa-solid fa-arrow-left"></i>
            <span>Thuật ngữ trước</span>
          </button>
          <button id="it-fc-next-btn" class="px-5 py-2.5 rounded-xl bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 font-semibold text-sm hover:bg-slate-50 dark:hover:bg-slate-700 flex items-center space-x-2 btn-press shadow-sm">
            <span>Thuật ngữ sau</span>
            <i class="fa-solid fa-arrow-right"></i>
          </button>
        </div>
      </div>

      <!-- 4. IT Quiz Wrapper -->
      <div id="it-quiz-wrapper" class="hidden max-w-2xl mx-auto space-y-6">
        <div id="it-quiz-active-card" class="bg-white dark:bg-slate-800 rounded-3xl border border-slate-200 dark:border-slate-700 p-6 sm:p-8 shadow-xl space-y-6">
          <div class="flex items-center justify-between text-xs font-bold text-slate-400 mb-1">
            <span id="it-quiz-progress-text">Câu 1 / 10</span>
            <div class="flex items-center space-x-3">
              <span id="it-quiz-streak" class="text-amber-500 font-bold"><i class="fa-solid fa-fire mr-1"></i>Streak: 0</span>
              <span id="it-quiz-score" class="text-indigo-600 dark:text-indigo-400 font-bold">Điểm: 0</span>
            </div>
          </div>
          <div class="w-full bg-slate-100 dark:bg-slate-700 h-2 rounded-full overflow-hidden">
            <div id="it-quiz-bar" class="h-full bg-indigo-600 rounded-full transition-all duration-300" style="width: 10%"></div>
          </div>

          <div class="text-center py-2 space-y-3">
            <div class="inline-flex items-center gap-2 px-4 py-1 rounded-full bg-indigo-50 dark:bg-slate-700 text-indigo-600 dark:text-indigo-400 font-bold text-sm">
              <span id="it-quiz-term-display"></span>
              <button id="it-quiz-speak" class="hover:text-indigo-800 transition-colors" title="Nghe thuật ngữ">
                <i class="fa-solid fa-volume-high text-xs"></i>
              </button>
            </div>
            <h3 id="it-quiz-prompt" class="text-2xl font-extrabold text-slate-900 dark:text-white leading-snug"></h3>
          </div>

          <div id="it-quiz-options-container" class="space-y-3"></div>

          <div id="it-quiz-expl-box" class="hidden p-5 rounded-2xl bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-slate-700 space-y-3">
            <div class="flex items-center justify-between">
              <span class="text-xs font-bold text-slate-400 uppercase">Giải nghĩa chi tiết:</span>
              <span id="it-quiz-expl-cat" class="text-xs font-bold px-2 py-0.5 rounded bg-indigo-100 text-indigo-700"></span>
            </div>
            <h4 id="it-quiz-expl-term" class="text-base font-bold text-indigo-600 dark:text-indigo-400"></h4>
            <p id="it-quiz-expl-full" class="text-sm font-semibold text-slate-800 dark:text-slate-200"></p>
            <p id="it-quiz-expl-ex" class="text-xs italic text-slate-500 dark:text-slate-400"></p>
            <div class="flex justify-end pt-2">
              <button id="it-quiz-next-btn" class="px-6 py-2.5 bg-indigo-600 hover:bg-indigo-700 text-white font-bold text-sm rounded-xl shadow-md btn-press flex items-center space-x-2">
                <span>Câu tiếp theo</span>
                <i class="fa-solid fa-arrow-right"></i>
              </button>
            </div>
          </div>
        </div>

        <div id="it-quiz-result-card" class="hidden bg-white dark:bg-slate-800 rounded-3xl border border-slate-200 dark:border-slate-700 p-8 shadow-2xl text-center space-y-6">
          <div class="w-20 h-20 rounded-full bg-indigo-100 dark:bg-indigo-900/60 text-indigo-500 flex items-center justify-center mx-auto text-4xl animate-gentle-bounce">
            <i class="fa-solid fa-award"></i>
          </div>
          <h3 class="text-3xl font-black text-slate-900 dark:text-white">Hoàn Thành Bài Thi CNTT!</h3>
          <div class="flex justify-center gap-6">
            <div class="p-4 bg-slate-50 dark:bg-slate-900 rounded-2xl border border-slate-100 dark:border-slate-700">
              <div class="text-xs text-slate-400 font-bold uppercase">Điểm số</div>
              <div id="it-quiz-final-score" class="text-2xl font-black text-indigo-600 dark:text-indigo-400 mt-1">100 / 100</div>
            </div>
            <div class="p-4 bg-slate-50 dark:bg-slate-900 rounded-2xl border border-slate-100 dark:border-slate-700">
              <div class="text-xs text-slate-400 font-bold uppercase">Độ chính xác</div>
              <div id="it-quiz-final-percent" class="text-2xl font-black text-emerald-600 dark:text-emerald-400 mt-1">100%</div>
            </div>
          </div>
          <div class="pt-2">
            <button id="it-quiz-restart-btn" class="px-6 py-3 bg-indigo-600 hover:bg-indigo-700 text-white font-bold text-sm rounded-xl shadow-md btn-press">
              <i class="fa-solid fa-rotate-right mr-1.5"></i>Làm lại bài thi mới
            </button>
          </div>
        </div>
      </div>

    </section>
"""

main_end = "</main>"
html = html.replace(main_end, it_section_html + "\n  " + main_end)

# 3. Add IT Term Modal before </body>
it_modal_html = """
  <!-- IT Term Detail Modal -->
  <div id="it-term-modal" class="hidden fixed inset-0 z-50 flex items-center justify-center p-4 sm:p-6 overflow-y-auto" role="dialog" aria-modal="true">
    <div id="it-modal-backdrop" class="fixed inset-0 bg-black/60 backdrop-blur-sm transition-opacity"></div>
    <div class="relative bg-white dark:bg-slate-800 rounded-3xl max-w-2xl w-full shadow-2xl border border-slate-200 dark:border-slate-700 overflow-hidden z-10 flex flex-col max-h-[90vh]">
      
      <!-- Modal Header -->
      <div class="relative h-56 w-full overflow-hidden bg-slate-100 dark:bg-slate-900 flex-shrink-0">
        <img id="it-modal-img" src="" alt="IT illustration" class="w-full h-full object-cover" />
        <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-black/30 to-transparent"></div>

        <div class="absolute top-4 left-4 flex items-center space-x-2 flex-wrap gap-y-1">
          <span id="it-modal-id" class="px-3 py-1 rounded-lg bg-black/50 backdrop-blur-md text-white font-bold text-xs border border-white/20"></span>
          <span id="it-modal-cat" class="px-3 py-1 rounded-lg bg-indigo-600/90 backdrop-blur-md text-white font-semibold text-xs"></span>
          <span id="it-modal-pos" class="px-2 py-0.5 rounded-md bg-white/20 backdrop-blur-md text-white font-bold text-[10px] uppercase"></span>
        </div>

        <div class="absolute top-4 right-4">
          <button id="it-modal-close-btn" class="w-9 h-9 rounded-full bg-black/40 hover:bg-black/70 backdrop-blur-md text-white flex items-center justify-center transition-colors" title="Đóng">
            <i class="fa-solid fa-xmark text-sm"></i>
          </button>
        </div>

        <div class="absolute bottom-4 left-4 right-4 text-white">
          <div class="flex items-end justify-between">
            <div>
              <div id="it-modal-concept" class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-md bg-black/60 backdrop-blur-md text-amber-300 font-semibold text-xs mb-1.5 border border-white/10"></div>
              <h2 id="it-modal-title" class="text-3xl sm:text-4xl font-black tracking-tight"></h2>
              <p id="it-modal-ipa" class="text-slate-300 font-mono-ipa text-sm mt-0.5"></p>
            </div>
            <button id="it-modal-speak-term" class="w-10 h-10 rounded-full bg-white/20 hover:bg-white/40 backdrop-blur-md text-white flex items-center justify-center transition-all btn-press shadow" title="Phát âm tiếng Anh">
              <i class="fa-solid fa-volume-high text-base"></i>
            </button>
          </div>
        </div>
      </div>

      <!-- Modal Body -->
      <div class="p-6 overflow-y-auto space-y-5">
        <div class="bg-indigo-50/60 dark:bg-slate-700/40 p-4 rounded-2xl border border-indigo-100 dark:border-slate-700">
          <span class="text-xs font-bold text-slate-400 uppercase tracking-wider">Định nghĩa chuyên ngành:</span>
          <p id="it-modal-meaning" class="text-base font-bold text-slate-800 dark:text-white mt-1 leading-relaxed"></p>
        </div>

        <div class="bg-slate-50 dark:bg-slate-900 p-4 rounded-2xl border border-slate-200 dark:border-slate-700 space-y-2">
          <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-indigo-600 dark:text-indigo-400 uppercase tracking-wider">Ngữ cảnh ứng dụng thực tế:</span>
            <button id="it-modal-speak-ex" class="text-indigo-600 dark:text-indigo-400 hover:text-indigo-800 text-xs font-semibold flex items-center gap-1">
              <i class="fa-solid fa-volume-high"></i> Nghe câu ví dụ
            </button>
          </div>
          <p id="it-modal-example-en" class="text-base font-semibold text-slate-800 dark:text-slate-100 leading-relaxed"></p>
          <p id="it-modal-example-vi" class="text-sm text-slate-500 dark:text-slate-400"></p>
        </div>
      </div>

      <!-- Modal Footer -->
      <div class="p-4 border-t border-slate-100 dark:border-slate-700 bg-slate-50/80 dark:bg-slate-900/80 flex items-center justify-between flex-shrink-0">
        <button id="it-modal-star-btn" class="px-4 py-2.5 rounded-xl border border-slate-200 dark:border-slate-700 hover:bg-slate-100 text-slate-700 dark:text-slate-200 text-sm font-semibold transition-colors btn-press">
          <i class="fa-regular fa-star mr-1.5"></i>Lưu thuật ngữ
        </button>
        <button id="it-modal-master-btn" class="px-5 py-2.5 rounded-xl bg-slate-100 text-slate-700 text-sm font-semibold transition-colors btn-press">
          <i class="fa-solid fa-check mr-1.5"></i>Đã thuộc
        </button>
      </div>

    </div>
  </div>
"""

html = html.replace("</body>", it_modal_html + "\n</body>")

# 4. Add scripts for it_terms_data.js and it_app.js before app.js
script_target = '<script src="verbs_data.js"></script>'
script_replacement = """<script src="verbs_data.js"></script>
  <script src="it_terms_data.js"></script>
  <script src="it_app.js"></script>"""

html = html.replace(script_target, script_replacement)

with open("/home/ken/.gemini/antigravity/scratch/irregular-verbs-360/index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Successfully injected IT English view, modal, nav tab, and scripts into index.html!")
