import re
import os

# Definitive mapping of filename -> New Title/Header
# Derived from the changes made in calculator.js
renames = {
    'enflasyon-alim-gucu-hesaplama.html': 'Enflasyon ve Alım Gücü Hesaplama',
    'freelancer-gelir-vergisi-hesaplama.html': 'Freelancer Gelir Vergisi Hesaplama',
    'dolar-hesaplama.html': 'Dolar ve Döviz Kar/Zarar Hesaplama',
    'asgari-ucret-hesaplama.html': 'Asgari Ücret Hesaplama',
    'memur-maas-zammi-hesaplama.html': 'Memur Zammı Hesaplama',
    'emekli-maas-hesaplama.html': 'Emekli Maaş Hesaplama',
    'mtv-hesaplama.html': 'MTV Hesaplama',
    'deger-artis-kazanci-hesaplama.html': 'Değer Artış Kazancı Hesaplama',
    'ucretli-ogretmen-maas-hesaplama.html': 'Ücretli Öğretmen Maaşı Hesaplama',
    'esnek-hesap-faiz-hesaplama.html': 'Esnek Hesap Faizi Hesaplama',
    'ikinci-el-tasit-kredisi-hesaplama.html': '2. El Taşıt Kredisi Hesaplama',
    'milli-piyango-hesaplama.html': 'Milli Piyango Vergi Hesaplama',
    'kpss-onlisans-puan-hesaplama.html': 'KPSS Önlisans Puan Hesaplama',
    'gunes-paneli-amortisman-hesaplama.html': 'Güneş Paneli Amortisman Hesaplama',
    'yumurta-haslama-suresi-hesaplama.html': 'Yumurta Haşlama Süresi Hesaplama',
    'i̇ki-tarih-arasi-gun-sayaci.html': 'İki Tarih Arası Gün Hesaplama',
    'instagram-etkilesim-orani-hesaplama.html': 'Instagram Etkileşim Oranı Hesaplama',
    'sosyal-medya-en-iyi-saat-hesaplama.html': 'Sosyal Medya En İyi Saat Hesaplama',
    'cin-takvimi-cinsiyet-hesaplama.html': 'Çin Takvimi Cinsiyet Hesaplama'
}

def update_headers():
    for filename, new_name in renames.items():
        if not os.path.exists(filename):
            print(f"Skipping {filename}: Not found.")
            continue

        print(f"Updating {filename} -> {new_name}")

        try:
            with open(filename, 'r', encoding='utf-8') as f:
                content = f.read()

            # 1. Update Title
            title_pattern = re.compile(r'<title>\s*(.*?)\s*\|\s*HesaplaHadi\s*</title>', re.IGNORECASE)

            def title_replacer(match):
                return f'<title> {new_name} | HesaplaHadi</title>'

            new_content = title_pattern.sub(title_replacer, content)

            # 2. Update H1
            h1_pattern = re.compile(r'(<h1[^>]*>)(.*?)(</h1>)', re.DOTALL | re.IGNORECASE)

            def h1_replacer(match):
                return f'{match.group(1)}{new_name}{match.group(3)}'

            new_content = h1_pattern.sub(h1_replacer, new_content)

            if content != new_content:
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"  Success: Updated {filename}")
            else:
                print(f"  No changes needed for {filename}")

        except Exception as e:
            print(f"  Error processing {filename}: {e}")

if __name__ == "__main__":
    update_headers()
