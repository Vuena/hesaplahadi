
import os
import re

TOOLS_TO_CHECK = [
    'hangi-gun-hesaplama.html',
    'tarihe-gun-ekleme-hesaplama.html',
    'vize-final-hesaplama.html',
    'universite-not-ortalamasi-hesaplama.html',
    'asgari-ucret-hesaplama.html',
    'memur-maas-zammi-hesaplama.html',
    'mtv-hesaplama-2026.html',
    'kidem-tazminati-hesaplama.html',
    'emekli-maas-hesaplama-2026.html',
    'kdv-hesaplama.html',
    'tyt-ayt-net-hesaplama.html',
    'kredi-hesaplama.html',
    'tevkifat-hesaplama.html'
]

SEO_CONTENT = """
        <article class="bg-white rounded-2xl shadow-sm border border-slate-200 p-8 info-panel">
            <h2 class="text-xl font-bold text-slate-800 mb-4">{title} Nedir?</h2>
            <p class="mb-4">Bu hesaplama aracı, {title} işlemlerinizi 2026 güncel verilerine ve formüllerine dayanarak saniyeler içinde gerçekleştirmenizi sağlar. Karmaşık matematiksel işlemlerle uğraşmadan, sadece gerekli bilgileri girerek en doğru sonuca ulaşabilirsiniz.</p>

            <h3 class="text-lg font-bold text-slate-800 mb-3">{title} Nasıl Hesaplanır?</h3>
            <p class="mb-4">Hesaplama işlemi, ilgili yasal düzenlemeler, matematiksel formüller veya güncel katsayılar kullanılarak yapılır. Aracımız, girdiğiniz verileri işleyerek size net, brüt veya oransal sonuçları detaylı bir şekilde sunar. İşlem adımları otomatikleştirilmiştir ve kullanıcı hatasını en aza indirir.</p>

            <h3 class="text-lg font-bold text-slate-800 mb-3">Sıkça Sorulan Sorular</h3>
            <p class="mb-2"><strong>Bu sonuçlar güvenilir mi?</strong><br>Evet, araçlarımız düzenli olarak 2026 parametrelerine (vergi dilimleri, katsayılar vb.) göre güncellenmektedir. Ancak resmi işlemlerde nihai teyit için ilgili kurumlarla görüşmeniz önerilir.</p>
            <p class="mb-2"><strong>Hesaplama ücretli mi?</strong><br>Hayır, tüm hesaplama araçlarımız tamamen ücretsizdir ve sınırsız sayıda işlem yapabilirsiniz.</p>

            <div class="p-4 bg-indigo-50 rounded-xl border border-indigo-100 mt-4">
                <p class="text-sm text-indigo-800 font-medium flex items-center gap-2">
                    <i class="fa-solid fa-wand-magic-sparkles"></i>
                    Daha karmaşık sorularınız mı var? <a href="ai-asistan.html" class="underline hover:text-indigo-600">Yapay Zeka Asistanımıza</a> sormayı deneyin.
                </p>
            </div>
        </article>
"""

def inject_seo():
    for filename in TOOLS_TO_CHECK:
        if not os.path.exists(filename):
            print(f"Skipping {filename} (Not found)")
            continue

        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check if article exists
        if '<article class="bg-white rounded-2xl shadow-sm border border-slate-200 p-8 info-panel">' in content:
            print(f"SEO content already exists in {filename}")
            continue

        # Extract title for dynamic text
        title_match = re.search(r'<h1.*?>(.*?)</h1>', content)
        title = title_match.group(1).replace('<span class="text-blue-600">', '').replace('</span>', '') if title_match else "Hesaplama Aracı"

        new_block = SEO_CONTENT.format(title=title)

        # Inject before </main>
        if '</main>' in content:
            new_content = content.replace('</main>', f'{new_block}\n</main>')
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Injected SEO content into {filename}")
        else:
            print(f"Could not find </main> in {filename}")

if __name__ == '__main__':
    inject_seo()
