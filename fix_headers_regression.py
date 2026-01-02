import re
import os

# Same mapping
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

LOGO_HTML = '<h1 class="text-xl md:text-2xl font-extrabold tracking-tight text-slate-900">Hesapla<span class="text-blue-600">Hadi</span></h1>'

def fix_headers():
    for filename, new_name in renames.items():
        if not os.path.exists(filename):
            print(f"Skipping {filename}: Not found.")
            continue

        print(f"Fixing {filename}...")

        try:
            with open(filename, 'r', encoding='utf-8') as f:
                content = f.read()

            # 1. Restore Logo
            # The previous script replaced the Logo H1 with <h1>New Name</h1> (preserving attributes).
            # The Logo H1 attributes were: class="text-xl md:text-2xl font-extrabold tracking-tight text-slate-900"
            # So the file likely contains: <h1 class="text-xl md:text-2xl font-extrabold tracking-tight text-slate-900">New Name</h1>

            # Let's verify if the logo is broken by looking for "Hesapla<span"
            if 'Hesapla<span class="text-blue-600">Hadi</span>' not in content:
                # It's broken. We need to find the H1 that looks like the logo container but has the wrong text.
                # Or simply, find the first H1 in the header section.

                # Regex to find the first H1 that likely replaced the logo
                # It usually comes after <a href="index.html" ...>

                logo_broken_pattern = re.compile(r'(<a href="index\.html"[^>]*>\s*<div[^>]*>.*?</div>\s*<div[^>]*>\s*)<h1[^>]*>.*?</h1>(\s*</div>\s*</a>)', re.DOTALL)

                def logo_restore(match):
                    return f'{match.group(1)}{LOGO_HTML}{match.group(2)}'

                new_content = logo_broken_pattern.sub(logo_restore, content, count=1)

                if new_content != content:
                    print(f"  Restored Logo in {filename}")
                    content = new_content
                else:
                    print(f"  WARN: Could not auto-restore logo in {filename}. checking manual patterns.")
                    # Fallback: Just replace the specific string if attributes match exactly
                    broken_string = f'<h1 class="text-xl md:text-2xl font-extrabold tracking-tight text-slate-900">{new_name}</h1>'
                    if broken_string in content:
                         content = content.replace(broken_string, LOGO_HTML)
                         print("  Restored Logo via exact string match.")

            # 2. Ensure Content Title is Correct
            # The content title usually has class="text-2xl font-bold text-slate-900 tracking-tight" (or similar)
            # The previous script *also* updated this one to {New Name}, which is CORRECT for this one.
            # But let's make sure.

            # If the previous script ran twice or messy, let's just ensure the second H1 is correct?
            # Actually, the previous script replaced ALL H1s. So the content H1 is already {New Name}.
            # We just needed to fix the first one.

            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)

        except Exception as e:
            print(f"  Error processing {filename}: {e}")

if __name__ == "__main__":
    fix_headers()
