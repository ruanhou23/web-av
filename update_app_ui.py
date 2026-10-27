# -*- coding: utf-8 -*-
with open("/home/ken/.gemini/antigravity/scratch/irregular-verbs-360/app.js", "r", encoding="utf-8") as f:
    app_js = f.read()

# Update createCardHTML in app.js to show conceptTag and icon badge
old_card_code = """          <!-- Action Buttons on Image -->
            <div class="absolute top-3 right-3 flex items-center space-x-1.5">
              <button class="btn-star w-8 h-8 rounded-full bg-black/40 hover:bg-black/70 backdrop-blur-md flex items-center justify-center text-white transition-colors" data-action="star" data-verb-id="${verb.id}" title="Lưu từ này">
                <i class="fa-${isSaved ? 'solid text-amber-400' : 'regular'} fa-star text-sm"></i>
              </button>
            </div>"""

new_card_code = """          <!-- Action Buttons on Image -->
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
            </div>"""

if old_card_code in app_js:
    app_js = app_js.replace(old_card_code, new_card_code)
    print("Replaced card code successfully")
else:
    print("Warning: old_card_code not found verbatim")

with open("/home/ken/.gemini/antigravity/scratch/irregular-verbs-360/app.js", "w", encoding="utf-8") as f:
    f.write(app_js)
