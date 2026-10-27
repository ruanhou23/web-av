# Check all verbs to categorize them by root concept
import json

with open("/home/ken/.gemini/antigravity/scratch/irregular-verbs-360/verbs_data.json") as f:
    verbs = json.load(f)

print(f"Total verbs: {len(verbs)}")
