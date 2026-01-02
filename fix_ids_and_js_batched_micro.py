import os
import re

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

def fix_html_files(batch_index):
    all_files = sorted([f for f in os.listdir('.') if f.endswith('.html')])
    batch_size = 5
    start = batch_index * batch_size
    end = start + batch_size
    batch_files = all_files[start:end]

    print(f"Processing batch {batch_index} (Files {start}-{end}): {len(batch_files)} files.")

    for filepath in batch_files:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content

        # 1. Fix JS Import
        content = content.replace('src="assets/js/tools-.js?v=1"', 'src="assets/js/tools.js?v=1"')
        content = content.replace('src="assets/js/tools-2026.js?v=1"', 'src="assets/js/tools.js?v=1"')

        # 2. Fix IDs
        for old_base, new_base in ID_FIXES.items():
            if old_base in content:
                content = content.replace(f'id="{old_base}', f'id="{new_base}')
                content = content.replace(f'id="res-{old_base}', f'id="res-{new_base}')
                content = content.replace(f'id="val-{old_base}', f'id="val-{new_base}')
                content = content.replace(f'id="detail-{old_base}', f'id="detail-{new_base}')
                content = content.replace(f"copyResult('{old_base}')", f"copyResult('{new_base}')")
                content = content.replace(f'id="btn-copy-{old_base}', f'id="btn-copy-{new_base}')

        if content != original_content:
            print(f"Fixing {filepath}")
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)

if __name__ == "__main__":
    import sys
    batch = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    fix_html_files(batch)
