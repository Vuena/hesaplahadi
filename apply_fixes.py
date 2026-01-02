import os
import re
import shutil

# --- CONFIGURATION ---
RENAMES = {
    'brutten-nete-maas-hesaplama-2026.html': 'brutten-nete-maas-hesaplama.html',
    'emekli-maas-hesaplama-2026.html': 'emekli-maas-hesaplama.html',
    'mtv-hesaplama-2026.html': 'mtv-hesaplama.html',
    'netten-brute-maas-hesaplama-2026.html': 'netten-brute-maas-hesaplama.html',
}

FUNCTION_FIXES = {
    'calc_cin_takvimi_cinsiyet_hesaplama': 'calc_cin_takvimi',
    'calc_dogum_haritasi_hesaplama': 'calc_dogum_haritasi',
    'calc_burc_hesaplama': 'calc_burc',
    'calc_piyango': 'calc_milli_piyango',
    'calc_ay_burcu_hesaplama': 'calc_ay_burcu',
    'calc_dolar_enflasyonu_hesaplama': 'calc_dolar_enflasyonu',
    'calc_akademik_tesvik_hesaplama': 'calc_akademik',
    'calc_yukselen_burc_hesaplama': 'calc_yukselen',
    'calc_numeroloji_hesaplama': 'calc_numeroloji'
}

# --- 1. RENAME FILES ---
print("--- Renaming Files ---")
for old_name, new_name in RENAMES.items():
    if os.path.exists(old_name):
        print(f"Renaming {old_name} -> {new_name}")
        shutil.move(old_name, new_name)
    else:
        print(f"File not found: {old_name}")

# --- 2. UPDATE CONTENT (Links, Text, Onclicks) ---
print("\n--- Updating Content ---")
html_files = [f for f in os.listdir('.') if f.endswith('.html')]
js_files = ['assets/js/calculator.js', 'assets/js/tools-2026.js']
all_files = html_files + js_files

for filepath in all_files:
    if not os.path.exists(filepath): continue

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # A. Update Links (for renamed files)
    for old_name, new_name in RENAMES.items():
        content = content.replace(old_name, new_name)

    # B. Update Function Calls (Onclicks) - Only for HTML files
    if filepath.endswith('.html'):
        for old_func, new_func in FUNCTION_FIXES.items():
            # Use regex to ensure we replace the function call
            # onclick="old_func()" or onclick="old_func("
            pattern = r'onclick=["\']\s*' + re.escape(old_func) + r'\s*\('
            replacement = f'onclick="{new_func}('
            content = re.sub(pattern, replacement, content)

    # C. Remove "2026" Text (Only for HTML files)
    if filepath.endswith('.html'):
        # Remove "2026" from Title tag
        content = re.sub(r'(<title>.*?)\s*2026\s*(.*?</title>)', r'\1 \2', content)

        # Remove "2026" from Meta Description
        content = re.sub(r'(<meta\s+name="description"\s+content=".*?)\s*2026\s*(.*?")', r'\1 \2', content)

        # Remove "2026" from H tags and Paragraphs (Simple text removal)
        # Be careful not to break HTML structure.
        # We will replace " 2026" with "" and "2026 " with "" to handle spacing.
        content = content.replace(' 2026', '')
        content = content.replace('2026 ', '')
        content = content.replace('2026', '') # Fallback

        # Cleanup double spaces created by removal
        content = content.replace('  ', ' ')

        # Special case: "&copy; 2026" -> "&copy; 2026" (Wait, user said remove 2026 ibaresini.
        # Usually copyright stays. But strict instruction: "remove 2026".
        # I will leave copyright alone if it looks like a year, but the prompt was "2026 ibaresini kaldır".
        # Let's remove it from copyright too to be safe/compliant with "absolute" request,
        # or change it to just "HesaplaHadi" without year.
        # Actually, standard is to have year. I'll change "&copy; 2026" to "&copy;"
        content = content.replace('&copy; 2026', '&copy;')

    if content != original_content:
        print(f"Updating {filepath}")
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

print("\n--- Done ---")
