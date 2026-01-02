import os
import re

FILES_TO_CHECK = [
    'ay-burcu-hesaplama.html',
    'dolar-enflasyonu-hesaplama.html',
    'akademik-tesvik-hesaplama.html'
]

EXPECTED_IDS = {
    'ay-burcu-hesaplama.html': ['id="ay_burcu-date"', 'id="res-ay_burcu"'],
    'dolar-enflasyonu-hesaplama.html': ['id="dolar_enflasyonu-amt"', 'id="res-dolar_enflasyonu"'],
    'akademik-tesvik-hesaplama.html': ['id="akademik-art"', 'id="res-akademik"']
}

for fpath in FILES_TO_CHECK:
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check IDs
        ids = EXPECTED_IDS.get(fpath, [])
        missing = [i for i in ids if i not in content]

        if missing:
            print(f"FAIL: {fpath} is missing {missing}")
        else:
            print(f"PASS: {fpath} seems correct.")
    else:
        print(f"FAIL: {fpath} not found.")
