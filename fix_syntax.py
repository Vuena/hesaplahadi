
import os

path = 'assets/js/calculator.js'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# The pattern to fix:
# The regex stopped early at toLocaleString({...}) so we have the new function followed by the tail of the old function.
# Look for the new function closing brace, followed by garbage.

garbage_pattern = "})+' TL', `Enflasyon Katsayısı: ${r.toFixed(2)}x`); }"

if garbage_pattern in content:
    content = content.replace(garbage_pattern, "")
    print("Fixed garbage in calculator.js")
else:
    print("Garbage pattern not found, checking for variations.")
    # Maybe it included the first closing brace?
    # New function ends with `}`.
    # The tail starts with `)+' TL'...`

    # Let's just find the specific block and clean it up.
    # The new function ends with `(${s} -> ${e})`); \n}`

    # We can search for the end of the new function and cut until the next `function` or end of file?
    # No, that's risky.

    # Let's search for the specific broken string I saw in read_file output.
    broken_tail = "})+' TL', `Enflasyon Katsayısı: ${r.toFixed(2)}x`); }"
    if broken_tail in content:
         content = content.replace(broken_tail, "")
         print("Fixed broken tail.")

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
