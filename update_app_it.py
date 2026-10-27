# -*- coding: utf-8 -*-
with open("/home/ken/.gemini/antigravity/scratch/irregular-verbs-360/app.js", "r", encoding="utf-8") as f:
    app_js = f.read()

# Update views list in switchTab
old_views = "const views = ['explorer-view', 'flashcards-view', 'quiz-view', 'typing-view', 'patterns-view'];"
new_views = "const views = ['explorer-view', 'flashcards-view', 'quiz-view', 'typing-view', 'patterns-view', 'it-english-view'];"
app_js = app_js.replace(old_views, new_views)

# Update tab init condition
old_tab_init = """      if (tabName === 'explorer') {
        this.renderExplorer();
      } else if (tabName === 'flashcards') {
        this.initFlashcards();
      } else if (tabName === 'quiz') {
        this.startQuiz();
      } else if (tabName === 'typing') {
        this.initTyping();
      }"""

new_tab_init = """      if (tabName === 'explorer') {
        this.renderExplorer();
      } else if (tabName === 'flashcards') {
        this.initFlashcards();
      } else if (tabName === 'quiz') {
        this.startQuiz();
      } else if (tabName === 'typing') {
        this.initTyping();
      } else if (tabName === 'it-english') {
        if (window.ITApp) window.ITApp.init();
      }"""

app_js = app_js.replace(old_tab_init, new_tab_init)

with open("/home/ken/.gemini/antigravity/scratch/irregular-verbs-360/app.js", "w", encoding="utf-8") as f:
    f.write(app_js)

print("Updated app.js with it-english tab support!")
