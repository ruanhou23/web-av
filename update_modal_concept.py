# -*- coding: utf-8 -*-
with open("/home/ken/.gemini/antigravity/scratch/irregular-verbs-360/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Add modal-concept-tag in modal header
old_modal_header = """        <!-- Badges on top -->
        <div class="absolute top-4 left-4 flex items-center space-x-2">
          <span id="modal-id-badge" class="px-3 py-1 rounded-lg bg-black/50 backdrop-blur-md text-white font-bold text-xs border border-white/20"></span>
          <span id="modal-pattern-badge" class="px-3 py-1 rounded-lg bg-blue-600/90 backdrop-blur-md text-white font-semibold text-xs"></span>
        </div>"""

new_modal_header = """        <!-- Badges on top -->
        <div class="absolute top-4 left-4 flex items-center space-x-2 flex-wrap gap-y-1">
          <span id="modal-id-badge" class="px-3 py-1 rounded-lg bg-black/50 backdrop-blur-md text-white font-bold text-xs border border-white/20"></span>
          <span id="modal-pattern-badge" class="px-3 py-1 rounded-lg bg-blue-600/90 backdrop-blur-md text-white font-semibold text-xs"></span>
          <span id="modal-concept-tag" class="px-3 py-1 rounded-lg bg-black/60 backdrop-blur-md text-amber-300 font-semibold text-xs border border-white/20 flex items-center gap-1.5 shadow"></span>
        </div>"""

html = html.replace(old_modal_header, new_modal_header)

# Also add concept tag to flashcard front
old_fc_header = """              <!-- Front Header -->
              <div class="flex items-center justify-between">
                <span id="fc-front-id" class="px-3 py-1 rounded-full bg-slate-100 dark:bg-slate-700 text-slate-600 dark:text-slate-300 text-xs font-bold">#1</span>
                <span id="fc-front-pattern" class="px-3 py-1 rounded-full bg-blue-100 dark:bg-blue-900/60 text-blue-700 dark:text-blue-300 text-xs font-bold">ABB</span>
              </div>"""

new_fc_header = """              <!-- Front Header -->
              <div class="flex items-center justify-between">
                <div class="flex items-center space-x-2">
                  <span id="fc-front-id" class="px-3 py-1 rounded-full bg-slate-100 dark:bg-slate-700 text-slate-600 dark:text-slate-300 text-xs font-bold">#1</span>
                  <span id="fc-front-pattern" class="px-3 py-1 rounded-full bg-blue-100 dark:bg-blue-900/60 text-blue-700 dark:text-blue-300 text-xs font-bold">ABB</span>
                </div>
                <span id="fc-front-concept" class="px-3 py-1 rounded-full bg-amber-50 dark:bg-amber-950/60 text-amber-700 dark:text-amber-300 border border-amber-200 dark:border-amber-800 text-xs font-bold flex items-center gap-1"></span>
              </div>"""

html = html.replace(old_fc_header, new_fc_header)

with open("/home/ken/.gemini/antigravity/scratch/irregular-verbs-360/index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("Updated index.html modal and flashcard concept badges")

# Now update app.js to populate these tags
with open("/home/ken/.gemini/antigravity/scratch/irregular-verbs-360/app.js", "r", encoding="utf-8") as f:
    app_js = f.read()

# Update openModal
old_modal_assign = """      document.getElementById('modal-id-badge').textContent = `#${verb.id}`;
      document.getElementById('modal-pattern-badge').textContent = `Dạng: ${verb.pattern}`;
      document.getElementById('modal-v1').textContent = verb.v1;"""

new_modal_assign = """      document.getElementById('modal-id-badge').textContent = `#${verb.id}`;
      document.getElementById('modal-pattern-badge').textContent = `Dạng: ${verb.pattern}`;
      const modalConcept = document.getElementById('modal-concept-tag');
      if (modalConcept) {
        modalConcept.innerHTML = `<span>${verb.icon}</span> <span>${verb.conceptTag || verb.meaning.split(',')[0]}</span>`;
      }
      document.getElementById('modal-v1').textContent = verb.v1;"""

app_js = app_js.replace(old_modal_assign, new_modal_assign)

# Update renderFlashcard
old_fc_assign = """      document.getElementById('fc-front-id').textContent = `#${verb.id}`;
      document.getElementById('fc-front-pattern').textContent = verb.pattern;
      document.getElementById('fc-front-v1').textContent = verb.v1;"""

new_fc_assign = """      document.getElementById('fc-front-id').textContent = `#${verb.id}`;
      document.getElementById('fc-front-pattern').textContent = verb.pattern;
      const fcConcept = document.getElementById('fc-front-concept');
      if (fcConcept) {
        fcConcept.innerHTML = `<span>${verb.icon}</span> <span>${verb.conceptTag || verb.meaning.split(',')[0]}</span>`;
      }
      document.getElementById('fc-front-v1').textContent = verb.v1;"""

app_js = app_js.replace(old_fc_assign, new_fc_assign)

with open("/home/ken/.gemini/antigravity/scratch/irregular-verbs-360/app.js", "w", encoding="utf-8") as f:
    f.write(app_js)
print("Updated app.js assignments")
