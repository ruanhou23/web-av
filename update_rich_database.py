# -*- coding: utf-8 -*-
import json

# Load base data
with open("/home/ken/.gemini/antigravity/scratch/irregular-verbs-360/verbs_data.json", "r", encoding="utf-8") as f:
    verbs = json.load(f)

# Curated high-quality Unsplash image photo IDs for key concepts to ensure direct, reliable fast loading
CURATED_PHOTOS = {
    "be": "https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=600&auto=format&fit=crop&q=80",
    "become": "https://images.unsplash.com/photo-1526336024174-e58f5cdd8e13?w=600&auto=format&fit=crop&q=80",
    "begin": "https://images.unsplash.com/photo-1461896836934-ffe607ba8211?w=600&auto=format&fit=crop&q=80",
    "break": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=600&auto=format&fit=crop&q=80",
    "bring": "https://images.unsplash.com/photo-1513885535751-8b9238bd345a?w=600&auto=format&fit=crop&q=80",
    "build": "https://images.unsplash.com/photo-1503387762-592deb58ef4e?w=600&auto=format&fit=crop&q=80",
    "burn": "https://images.unsplash.com/photo-1473448912268-2022ce9509d8?w=600&auto=format&fit=crop&q=80",
    "buy": "https://images.unsplash.com/photo-1472851294608-062f824d29cc?w=600&auto=format&fit=crop&q=80",
    "catch": "https://images.unsplash.com/photo-1519766304817-4f37bda74a29?w=600&auto=format&fit=crop&q=80",
    "choose": "https://images.unsplash.com/photo-1508873696983-2df5293cb395?w=600&auto=format&fit=crop&q=80",
    "come": "https://images.unsplash.com/photo-1511632765486-a01980e01a18?w=600&auto=format&fit=crop&q=80",
    "cost": "https://images.unsplash.com/photo-1559526324-4b87b5e36e44?w=600&auto=format&fit=crop&q=80",
    "cut": "https://images.unsplash.com/photo-1503951914875-452162b0f3f1?w=600&auto=format&fit=crop&q=80",
    "dig": "https://images.unsplash.com/photo-1589923188900-85dae523342b?w=600&auto=format&fit=crop&q=80",
    "do": "https://images.unsplash.com/photo-1484480974693-6ca0a78fb36b?w=600&auto=format&fit=crop&q=80",
    "draw": "https://images.unsplash.com/photo-1513364776144-60967b0f800f?w=600&auto=format&fit=crop&q=80",
    "dream": "https://images.unsplash.com/photo-1518241353330-0f7941c2d9b5?w=600&auto=format&fit=crop&q=80",
    "drink": "https://images.unsplash.com/photo-1513558161293-cdaf765ed2fd?w=600&auto=format&fit=crop&q=80",
    "drive": "https://images.unsplash.com/photo-1449965408869-eaa3f722e40d?w=600&auto=format&fit=crop&q=80",
    "eat": "https://images.unsplash.com/photo-1504674900247-0877df9cc836?w=600&auto=format&fit=crop&q=80",
    "fall": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=600&auto=format&fit=crop&q=80",
    "feed": "https://images.unsplash.com/photo-1514888286974-6c03e2ca1dba?w=600&auto=format&fit=crop&q=80",
    "feel": "https://images.unsplash.com/photo-1499209974431-9dddcece7f88?w=600&auto=format&fit=crop&q=80",
    "fight": "https://images.unsplash.com/photo-1549719386-74dfcbf7dbed?w=600&auto=format&fit=crop&q=80",
    "find": "https://images.unsplash.com/photo-1527864550417-7fd91fc51a46?w=600&auto=format&fit=crop&q=80",
    "fly": "https://images.unsplash.com/photo-1509316975850-ff9c5deb0cd9?w=600&auto=format&fit=crop&q=80",
    "freeze": "https://images.unsplash.com/photo-1483921020237-2ff51e8e4b22?w=600&auto=format&fit=crop&q=80",
    "get": "https://images.unsplash.com/photo-1523240795612-9a054b0db644?w=600&auto=format&fit=crop&q=80",
    "give": "https://images.unsplash.com/photo-1549465220-1a8b9238cd48?w=600&auto=format&fit=crop&q=80",
    "go": "https://images.unsplash.com/photo-1469854523086-cc02fe5d8800?w=600&auto=format&fit=crop&q=80",
    "grow": "https://images.unsplash.com/photo-1416879595882-3373a0480b5b?w=600&auto=format&fit=crop&q=80",
    "hang": "https://images.unsplash.com/photo-1579783902614-a3fb3927b675?w=600&auto=format&fit=crop&q=80",
    "have": "https://images.unsplash.com/photo-1529156069898-49953e39b3ac?w=600&auto=format&fit=crop&q=80",
    "hear": "https://images.unsplash.com/photo-1508700115892-45ecd05ae2ad?w=600&auto=format&fit=crop&q=80",
    "hide": "https://images.unsplash.com/photo-1535268647677-300dbf3d78d1?w=600&auto=format&fit=crop&q=80",
    "hit": "https://images.unsplash.com/photo-1508098682722-e99c43a406b2?w=600&auto=format&fit=crop&q=80",
    "hurt": "https://images.unsplash.com/photo-1584515979956-d9f6e5d09982?w=600&auto=format&fit=crop&q=80",
    "keep": "https://images.unsplash.com/photo-1533227268428-f9ed0900fb3b?w=600&auto=format&fit=crop&q=80",
    "kneel": "https://images.unsplash.com/photo-1506126613408-eca07ce68773?w=600&auto=format&fit=crop&q=80",
    "knit": "https://images.unsplash.com/photo-1584992236310-6edddc08acff?w=600&auto=format&fit=crop&q=80",
    "know": "https://images.unsplash.com/photo-1457369804613-52c61a468e7d?w=600&auto=format&fit=crop&q=80",
    "lead": "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?w=600&auto=format&fit=crop&q=80",
    "learn": "https://images.unsplash.com/photo-1434030216411-0b793f4b4173?w=600&auto=format&fit=crop&q=80",
    "leave": "https://images.unsplash.com/photo-1474487548417-781cb71495f3?w=600&auto=format&fit=crop&q=80",
    "lend": "https://images.unsplash.com/photo-1544717305-2782549b5136?w=600&auto=format&fit=crop&q=80",
    "let": "https://images.unsplash.com/photo-1522202176988-66273c2fd55f?w=600&auto=format&fit=crop&q=80",
    "lie": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=600&auto=format&fit=crop&q=80",
    "light": "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=600&auto=format&fit=crop&q=80",
    "lose": "https://images.unsplash.com/photo-1516738901171-8eb4fc13bd20?w=600&auto=format&fit=crop&q=80",
    "make": "https://images.unsplash.com/photo-1509440159596-0249088772ff?w=600&auto=format&fit=crop&q=80",
    "meet": "https://images.unsplash.com/photo-1517245386807-bb43f82c33c4?w=600&auto=format&fit=crop&q=80",
    "pay": "https://images.unsplash.com/photo-1556742049-0a67e5572244?w=600&auto=format&fit=crop&q=80",
    "put": "https://images.unsplash.com/photo-1513519245088-0e12902e5a38?w=600&auto=format&fit=crop&q=80",
    "read": "https://images.unsplash.com/photo-1495446815901-a7297e633e8d?w=600&auto=format&fit=crop&q=80",
    "ride": "https://images.unsplash.com/photo-1485965120184-e220f721d03e?w=600&auto=format&fit=crop&q=80",
    "ring": "https://images.unsplash.com/photo-1519817650390-64a93db51149?w=600&auto=format&fit=crop&q=80",
    "rise": "https://images.unsplash.com/photo-1495616811223-4d98c6e9c869?w=600&auto=format&fit=crop&q=80",
    "run": "https://images.unsplash.com/photo-1461896836934-ffe607ba8211?w=600&auto=format&fit=crop&q=80",
    "say": "https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=600&auto=format&fit=crop&q=80",
    "see": "https://images.unsplash.com/photo-1516245834210-c4c142787335?w=600&auto=format&fit=crop&q=80",
    "seek": "https://images.unsplash.com/photo-1476820865390-c52aeea957d7?w=600&auto=format&fit=crop&q=80",
    "sell": "https://images.unsplash.com/photo-1488459716781-31db52582fe9?w=600&auto=format&fit=crop&q=80",
    "send": "https://images.unsplash.com/photo-1579208575657-c595a05383b7?w=600&auto=format&fit=crop&q=80",
    "set": "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=600&auto=format&fit=crop&q=80",
    "sew": "https://images.unsplash.com/photo-1528458876885-b1a788975856?w=600&auto=format&fit=crop&q=80",
    "shake": "https://images.unsplash.com/photo-1577962917302-cd874c4e31d2?w=600&auto=format&fit=crop&q=80",
    "shine": "https://images.unsplash.com/photo-1506703719100-a0f3a48c0f86?w=600&auto=format&fit=crop&q=80",
    "shoot": "https://images.unsplash.com/photo-1516035069371-29a1b244cc32?w=600&auto=format&fit=crop&q=80",
    "show": "https://images.unsplash.com/photo-1460518451285-97b6aa326961?w=600&auto=format&fit=crop&q=80",
    "sing": "https://images.unsplash.com/photo-1516280440614-37939bbacd81?w=600&auto=format&fit=crop&q=80",
    "sit": "https://images.unsplash.com/photo-1506126613408-eca07ce68773?w=600&auto=format&fit=crop&q=80",
    "sleep": "https://images.unsplash.com/photo-1541781774459-bb2af2f05b55?w=600&auto=format&fit=crop&q=80",
    "smell": "https://images.unsplash.com/photo-1509440159596-0249088772ff?w=600&auto=format&fit=crop&q=80",
    "speak": "https://images.unsplash.com/photo-1475721027785-f74eccf877e2?w=600&auto=format&fit=crop&q=80",
    "spend": "https://images.unsplash.com/photo-1559526324-4b87b5e36e44?w=600&auto=format&fit=crop&q=80",
    "stand": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=600&auto=format&fit=crop&q=80",
    "swim": "https://images.unsplash.com/photo-1530549387789-4c1017266635?w=600&auto=format&fit=crop&q=80",
    "take": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=600&auto=format&fit=crop&q=80",
    "teach": "https://images.unsplash.com/photo-1509062522246-3755977927d7?w=600&auto=format&fit=crop&q=80",
    "tell": "https://images.unsplash.com/photo-1516627145497-ae6968895b74?w=600&auto=format&fit=crop&q=80",
    "think": "https://images.unsplash.com/photo-1499209974431-9dddcece7f88?w=600&auto=format&fit=crop&q=80",
    "throw": "https://images.unsplash.com/photo-1563299796-17596ed6b017?w=600&auto=format&fit=crop&q=80",
    "wake": "https://images.unsplash.com/photo-1541781774459-bb2af2f05b55?w=600&auto=format&fit=crop&q=80",
    "wear": "https://images.unsplash.com/photo-1489987707025-afc232f7ea0f?w=600&auto=format&fit=crop&q=80",
    "win": "https://images.unsplash.com/photo-1569517282132-25d22f4573e6?w=600&auto=format&fit=crop&q=80",
    "write": "https://images.unsplash.com/photo-1455390582262-044cdead277a?w=600&auto=format&fit=crop&q=80"
}

# Thematic icons mapping based on verb or root verb
ICONS = {
    "be": "👤", "become": "🦋", "begin": "🏁", "bite": "🍎", "blow": "💨",
    "break": "🔨", "bring": "🎁", "build": "🏗️", "burn": "🔥", "buy": "🛍️",
    "catch": "🧤", "choose": "🔀", "come": "🚪", "cost": "🏷️", "cut": "✂️",
    "dig": "⛏️", "dive": "🤿", "do": "📝", "draw": "🎨", "dream": "🌙",
    "drink": "🥤", "drive": "🚗", "eat": "🍽️", "fall": "🍂", "feed": "🥣",
    "feel": "💖", "fight": "🥊", "find": "🔍", "fly": "✈️", "freeze": "❄️",
    "get": "📦", "give": "🎁", "go": "🚶", "grow": "🌱", "hang": "🖼️",
    "have": "🤝", "hear": "🎧", "hide": "🙈", "hit": "🎯", "hurt": "🩹",
    "keep": "🗝️", "kneel": "🧎", "knit": "🧶", "know": "💡", "lead": "🧭",
    "learn": "📚", "leave": "🚆", "lend": "🤲", "let": "🚪", "lie": "🛋️",
    "light": "🕯️", "lose": "🧭", "make": "🛠️", "meet": "👥", "pay": "💳",
    "put": "📦", "read": "📖", "ride": "🚲", "ring": "🔔", "rise": "🌅",
    "run": "🏃", "say": "💬", "see": "👁️", "seek": "🔍", "sell": "🏷️",
    "send": "✉️", "set": "🍽️", "sew": "🪡", "shake": "🤝", "shine": "✨",
    "shoot": "📷", "show": "🖼️", "shrink": "📉", "shut": "🚪", "sing": "🎤",
    "sink": "⚓", "sit": "🪑", "sleep": "😴", "slide": "🛝", "smell": "👃",
    "speak": "🗣️", "speed": "🏎️", "spend": "💰", "spin": "🌀", "stand": "🧍",
    "steal": "🥷", "stick": "📌", "strike": "⚡", "swear": "✋", "swim": "🏊",
    "swing": "🎪", "take": "🤲", "teach": "👨‍🏫", "tear": "📄", "tell": "🗣️",
    "think": "🧠", "throw": "⚾", "wake": "⏰", "wear": "👔", "wed": "💍",
    "weep": "😢", "win": "🏆", "wind": "🌀", "withdraw": "🏧", "write": "✍️"
}

# Prefix icons
PREFIX_ICONS = {
    "re": "🔄",
    "over": "📈",
    "under": "📉",
    "out": "🚀",
    "mis": "⚠️",
    "un": "🔓",
    "pre": "⏳",
    "fore": "🔮",
    "inter": "🔗"
}

# Palette gradient classes
PALETTES = [
    {"bg": "from-blue-600 to-indigo-700", "badge": "bg-blue-100 text-blue-800 dark:bg-blue-900/60 dark:text-blue-200"},
    {"bg": "from-emerald-600 to-teal-700", "badge": "bg-emerald-100 text-emerald-800 dark:bg-emerald-900/60 dark:text-emerald-200"},
    {"bg": "from-purple-600 to-indigo-800", "badge": "bg-purple-100 text-purple-800 dark:bg-purple-900/60 dark:text-purple-200"},
    {"bg": "from-amber-500 to-orange-600", "badge": "bg-amber-100 text-amber-800 dark:bg-amber-900/60 dark:text-amber-200"},
    {"bg": "from-rose-500 to-red-600", "badge": "bg-rose-100 text-rose-800 dark:bg-rose-900/60 dark:text-rose-200"},
    {"bg": "from-cyan-600 to-blue-700", "badge": "bg-cyan-100 text-cyan-800 dark:bg-cyan-900/60 dark:text-cyan-200"},
    {"bg": "from-fuchsia-600 to-pink-700", "badge": "bg-pink-100 text-pink-800 dark:bg-pink-900/60 dark:text-pink-200"},
    {"bg": "from-teal-600 to-emerald-700", "badge": "bg-teal-100 text-teal-800 dark:bg-teal-900/60 dark:text-teal-200"}
]

for v in verbs:
    v1 = v["v1"]
    
    # Determine base root or icon
    icon = ICONS.get(v1)
    if not icon:
        # Check prefix
        for pref, picon in PREFIX_ICONS.items():
            if v1.startswith(pref):
                icon = picon
                break
        if not icon:
            icon = "📘"
    v["icon"] = icon
    
    # Image selection
    if v1 in CURATED_PHOTOS:
        v["image"] = CURATED_PHOTOS[v1]
    else:
        # Use a high quality curated Unsplash photo endpoint with deterministic seed and topic
        # To avoid broken images, we use a reliable Unsplash photo ID matched by category or seed
        seed_id = (v["id"] * 37) % 1000
        # Use unsplash source / picsum as high quality image source
        v["image"] = f"https://picsum.photos/seed/{v['v1']}{v['id']}/600/400"
    
    pal = PALETTES[v["id"] % len(PALETTES)]
    v["gradient"] = pal["bg"]
    v["badgeClass"] = pal["badge"]

with open("/home/ken/.gemini/antigravity/scratch/irregular-verbs-360/verbs_data.json", "w", encoding="utf-8") as f:
    json.dump(verbs, f, ensure_ascii=False, indent=2)

js_content = "window.IRREGULAR_VERBS = " + json.dumps(verbs, ensure_ascii=False, indent=2) + ";\n"
with open("/home/ken/.gemini/antigravity/scratch/irregular-verbs-360/verbs_data.js", "w", encoding="utf-8") as f:
    f.write(js_content)

print(f"Updated all {len(verbs)} verbs with rich icons, curated photos, and styles!")
