# -*- coding: utf-8 -*-
"""Compile all 10 domains (1,000 core IT terms) into it_terms_data.json and it_terms_data.js
Ensures full dual-key compatibility for both modern and legacy property accesses.
"""

import json
import os

import domain_01_programming
import domain_02_dsa
import domain_03_database
import domain_04_networking
import domain_05_security
import domain_06_os_hardware
import domain_07_cloud_devops
import domain_08_web_mobile
import domain_09_ai_ml
import domain_10_qa_workplace

DOMAIN_GRADIENTS = {
    "programming": "from-blue-600 to-indigo-800",
    "dsa": "from-emerald-600 to-teal-800",
    "database": "from-amber-600 to-orange-800",
    "networking": "from-cyan-600 to-blue-800",
    "security": "from-rose-600 to-red-800",
    "os_hardware": "from-purple-600 to-indigo-900",
    "cloud_devops": "from-sky-600 to-blue-900",
    "web_mobile": "from-violet-600 to-purple-800",
    "ai_ml": "from-fuchsia-600 to-pink-800",
    "qa_workplace": "from-teal-600 to-emerald-800",
}

domains = [
    ("Domain 1: Programming & Architecture", domain_01_programming.terms),
    ("Domain 2: Data Structures & Algorithms", domain_02_dsa.terms),
    ("Domain 3: Databases & Data Engineering", domain_03_database.terms),
    ("Domain 4: Networking & Protocols", domain_04_networking.terms),
    ("Domain 5: Cybersecurity & Cryptography", domain_05_security.terms),
    ("Domain 6: Operating Systems & Hardware", domain_06_os_hardware.terms),
    ("Domain 7: Cloud Computing & DevOps", domain_07_cloud_devops.terms),
    ("Domain 8: Web, API & Mobile Engineering", domain_08_web_mobile.terms),
    ("Domain 9: AI, Machine Learning & LLMs", domain_09_ai_ml.terms),
    ("Domain 10: QA, Testing, Agile & Workplace", domain_10_qa_workplace.terms),
]

all_terms = []
term_id = 1

print("=" * 60)
print("COMPILING 1,000 CORE IT TERMS DATABASE (DUAL-KEYED)")
print("=" * 60)

for name, term_list in domains:
    print(f"{name}: {len(term_list)} terms")
    for item in term_list:
        term, ipa, pos, dom_slug, dom_vn, meaning_vn, ex_en, ex_vn, badge, icon, img = item
        grad = DOMAIN_GRADIENTS.get(dom_slug, "from-indigo-600 to-blue-800")
        
        all_terms.append({
            "id": term_id,
            "term": term,
            "ipa": ipa,
            "pos": pos,
            "partOfSpeech": pos,
            "domain": dom_slug,
            "subCategory": dom_slug,
            "domain_vn": dom_vn,
            "subCategoryVi": dom_vn,
            "meaning_vn": meaning_vn,
            "meaning": meaning_vn,
            "example_en": ex_en,
            "example": ex_en,
            "example_vn": ex_vn,
            "exampleVi": ex_vn,
            "concept_badge": badge,
            "conceptTag": badge,
            "icon": icon,
            "image": img,
            "gradient": grad
        })
        term_id += 1

print("-" * 60)
print(f"Total compiled terms: {len(all_terms)}")

# Save to JSON
json_path = "/home/ken/.gemini/antigravity/scratch/irregular-verbs-360/it_terms_data.json"
with open(json_path, "w", encoding="utf-8") as f:
    json.dump(all_terms, f, ensure_ascii=False, indent=2)
print(f"Saved JSON database: {json_path} ({os.path.getsize(json_path):,} bytes)")

# Save to JS
js_path = "/home/ken/.gemini/antigravity/scratch/irregular-verbs-360/it_terms_data.js"
with open(js_path, "w", encoding="utf-8") as f:
    f.write("// Tiếng Anh Chuyên Ngành Công Nghệ Thông Tin (IT English) - 1,000 Thuật Ngữ Cốt Lõi\n")
    f.write(f"// Tổng số thuật ngữ: {len(all_terms)} từ vựng qua 10 chuyên ngành CNTT\n")
    f.write("const IT_TERMS_DATABASE = ")
    json.dump(all_terms, f, ensure_ascii=False, indent=2)
    f.write(";\n\n")
    f.write("const IT_TERMS_DATA = IT_TERMS_DATABASE;\n")
    f.write("if (typeof window !== 'undefined') {\n")
    f.write("  window.IT_TERMS_DATA = IT_TERMS_DATABASE;\n")
    f.write("  window.IT_TERMS_DATABASE = IT_TERMS_DATABASE;\n")
    f.write("}\n")
    f.write("if (typeof module !== 'undefined' && module.exports) {\n")
    f.write("  module.exports = { IT_TERMS_DATABASE, IT_TERMS_DATA };\n")
    f.write("}\n")
print(f"Saved JS database: {js_path} ({os.path.getsize(js_path):,} bytes)")
print("=" * 60)
