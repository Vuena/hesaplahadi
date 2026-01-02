import os
import re

# Map of OLD_ID_BASE -> NEW_ID_BASE
# We will replace {OLD}-xyz with {NEW}-xyz in id attributes
ID_FIXES = {
    'solar_harita_hesaplama': 'solar_harita',
    'burc_hesaplama': 'burc',
    'cin_takvimi_cinsiyet_hesaplama': 'cin_takvimi',
    'dogum_haritasi_hesaplama': 'dogum_haritasi',
    'ay_burcu_hesaplama': 'ay_burcu',
    'dolar_enflasyonu_hesaplama': 'dolar_enflasyonu',
    'akademik_tesvik_hesaplama': 'akademik',
    'yukselen_burc_hesaplama': 'yukselen',
    'numeroloji_hesaplama': 'numeroloji',
    'milli_piyango_hesaplama': 'piyango'
}

def fix_html_files():
    html_files = [f for f in os.listdir('.') if f.endswith('.html')]

    for filepath in html_files:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content

        # 1. Fix JS Import
        # Replace tools-.js or tools-2026.js with tools.js
        content = content.replace('src="assets/js/tools-.js?v=1"', 'src="assets/js/tools.js?v=1"')
        content = content.replace('src="assets/js/tools-2026.js?v=1"', 'src="assets/js/tools.js?v=1"')

        # 2. Fix IDs
        for old_base, new_base in ID_FIXES.items():
            if old_base in content:
                # We need to be careful not to break other things, but IDs usually follow patterns like:
                # id="solar_harita_hesaplama-date" -> id="solar_harita-date"
                # id="res-solar_harita_hesaplama" -> id="res-solar_harita"
                # id="val-solar_harita_hesaplama" -> id="val-solar_harita"
                # id="detail-solar_harita_hesaplama" -> id="detail-solar_harita"
                # onclick="copyResult('solar_harita_hesaplama')" -> copyResult('solar_harita')

                content = content.replace(f'id="{old_base}', f'id="{new_base}')
                content = content.replace(f'id="res-{old_base}', f'id="res-{new_base}')
                content = content.replace(f'id="val-{old_base}', f'id="val-{new_base}')
                content = content.replace(f'id="detail-{old_base}', f'id="detail-{new_base}')
                content = content.replace(f"copyResult('{old_base}')", f"copyResult('{new_base}')")
                content = content.replace(f'id="btn-copy-{old_base}', f'id="btn-copy-{new_base}')

        if content != original_content:
            print(f"Fixing IDs and JS in {filepath}")
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)

if __name__ == "__main__":
    fix_html_files()
