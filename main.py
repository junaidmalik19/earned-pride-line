"""Write the earned-pride line to /output/entry.txt.

Gate: UTF-8 text, 1-240 characters, not only whitespace.
"""

import os

LINE = "After forty years of night shifts, she hung up her apron, and the whole kitchen crew stood in silence because nobody knew how to say thank you big enough."

if len(LINE) > 240 or not LINE.strip():
    raise SystemExit(f"line must be 1-240 characters, got {len(LINE)}")

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)

print(f"wrote /output/entry.txt: {len(LINE)} characters")
