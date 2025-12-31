
import os

# Tool Data - Map IDs to Metadata
tools_meta = {
    "net_brut": {
        "title": "Netten Brüte Maaş Hesaplama 2026",
        "desc": "Net maaşınızdan brüt maaşınızı hesaplayın. SGK ve vergi kesintilerini görün.",
        "content": """
            <h2>Netten Brüte Maaş Nasıl Hesaplanır?</h2>
            <p>Net maaş, elinize geçen paradır. Brüt maaş ise bu tutara SGK primi, işsizlik sigortası, gelir vergisi ve damga vergisinin eklenmiş halidir. İşveren maliyetini hesaplamak için brüt maaş bilinmelidir.</p>
            <h3>Hesaplama Formülü</h3>
            <p>Netten Brüte giderken vergi dilimleri (oranları) yıl içindeki toplam matraha göre değiştiği için sabit bir çarpan yoktur. Genellikle Ocak ayı için <code>Net / 0.7149</code> formülü yaklaşık brüt değeri verir.</p>
        """
    },
    "brut_net": {
        "title": "Brütten Nete Maaş Hesaplama 2026",
        "desc": "Brüt maaşınızdan elinize geçecek net tutarı hesaplayın.",
        "content": """
            <h2>Brütten Nete Maaş Nasıl Hesaplanır?</h2>
            <p>Brüt maaştan yasal kesintiler (SGK %14, İşsizlik %1, Gelir Vergisi %15-40, Damga %0.759) düşüldükten sonra kalan tutar net maaştır.</p>
        """
    },
    "mevduat": {
        "title": "Mevduat Faizi Hesaplama - En Yüksek Getiri",
        "desc": "Vadeli mevduat faizi getirisi hesaplama. 32, 92 günlük kazancınızı öğrenin.",
        "content": """
            <h2>Mevduat Getirisi Nasıl Hesaplanır?</h2>
            <p><code>Anapara x Faiz Oranı x Gün Sayısı / 36500</code> formülü kullanılır. Elde edilen brüt faizden stopaj (%5 veya vadeye göre değişen oran) düşülerek net getiri bulunur.</p>
        """
    },
    "iban": {
        "title": "IBAN Doğrulama ve Çözümleme Aracı",
        "desc": "TR ile başlayan IBAN numarasının doğruluğunu kontrol edin.",
        "content": """
            <h2>IBAN Nedir?</h2>
            <p>International Bank Account Number (Uluslararası Banka Hesap Numarası), para transferlerinin hatasız gerçekleşmesi için geliştirilmiş bir standarttır. Türkiye'de IBAN 'TR' ile başlar ve toplam 26 hanelidir.</p>
        """
    },
    "indirim": {
        "title": "İndirim Hesaplama - Yüzde İndirim Tutarı",
        "desc": "Bir ürünün indirimli fiyatını ve ne kadar kazanç sağladığınızı hesaplayın.",
        "content": """
            <h2>İndirim Tutarı Nasıl Bulunur?</h2>
            <p>Etiket fiyatı ile indirim oranı çarpılarak indirim miktarı bulunur. Bu miktar etiket fiyatından düşüldüğünde indirimli fiyat elde edilir.</p>
        """
    },
    "karzarar": {
        "title": "Kâr Marjı ve Zarar Hesaplama",
        "desc": "Maliyet ve satış fiyatı üzerinden kar oranını hesaplayın.",
        "content": """
            <h2>Kâr Marjı Formülü</h2>
            <p><code>(Satış Fiyatı - Maliyet) / Maliyet x 100</code> formülü ile yüzde kar oranı bulunur.</p>
        """
    },
    "bilesik": {
        "title": "Bileşik Faiz Hesaplama",
        "desc": "Anaparanın faizinin de faiz kazandığı birikim hesaplaması.",
        "content": """
            <h2>Bileşik Faiz Nedir?</h2>
            <p>Her dönem kazanılan faizin anaparaya eklenerek bir sonraki dönemde bu yeni tutar üzerinden faiz işletilmesidir. Uzun vadeli yatırımlarda "kartopu etkisi" yaratır.</p>
        """
    },
    "kk_asgari": {
        "title": "Kredi Kartı Asgari Ödeme Hesaplama",
        "desc": "Kredi kartı dönem borcunuza göre ödemeniz gereken minimum tutar.",
        "content": """
            <h2>Asgari Ödeme Oranı Nedir?</h2>
            <p>BDDK düzenlemelerine göre limiti 25.000 TL altındaki kartlar için %20, üzerindeki kartlar için %40 asgari ödeme oranı uygulanır.</p>
        """
    },
    "komisyon": {
        "title": "Emlakçı Komisyonu Hesaplama",
        "desc": "Gayrimenkul alım satımında ödenmesi gereken emlakçı hizmet bedeli.",
        "content": """
            <h2>Yasal Komisyon Oranı</h2>
            <p>Taşınmaz Ticareti Hakkında Yönetmelik'e göre hizmet bedeli, satış bedelinin %2'si + KDV (Toplam %2.4) alıcıdan, %2'si + KDV satıcıdan olmak üzere toplam %4 + KDV'yi geçemez.</p>
        """
    },
    "zam": {
        "title": "Maaş Zam Oranı Hesaplama",
        "desc": "Mevcut maaşınıza yapılacak zam oranı ile yeni maaşınızı öğrenin.",
        "content": """
            <h2>Zamlı Maaş Nasıl Hesaplanır?</h2>
            <p>Mevcut maaşınızı (1 + Zam Oranı/100) ile çarparak yeni maaşınızı bulabilirsiniz.</p>
        """
    },
    # HEALTH
    "ai_diyet": {
        "title": "AI Diyetisyen - Kişiye Özel Beslenme Programı",
        "desc": "Yapay zeka destekli ücretsiz diyet listesi oluşturucu.",
        "content": """
            <h2>AI Diyetisyen Nasıl Çalışır?</h2>
            <p>Girdiğiniz boy, kilo ve hedef bilgilerini işleyen yapay zeka algoritmamız, kalori ihtiyacınıza uygun dengeli bir günlük menü hazırlar.</p>
        """
    },
    "bmi": {
        "title": "Vücut Kitle İndeksi (BMI) Hesaplama",
        "desc": "Boy ve kilonuza göre obezite durumunuzu öğrenin.",
        "content": """
            <h2>BMI Değerlendirmesi</h2>
            <p>18.5 altı zayıf, 18.5-25 arası normal, 25-30 arası fazla kilolu, 30 üzeri obez kabul edilir.</p>
        """
    },
    "idealkilo": {
        "title": "İdeal Kilo Hesaplama",
        "desc": "Boyunuza ve cinsiyetinize göre olmanız gereken sağlıklı kilo.",
        "content": """
            <h2>İdeal Kilo Formülleri</h2>
            <p>Robinson ve Miller gibi bilimsel formüller kullanılarak, iskelet yapınıza ve boyunuza en uygun sağlıklı kilo aralığı belirlenir.</p>
        """
    },
    "bmr": {
        "title": "Bazal Metabolizma Hızı (BMR) Hesaplama",
        "desc": "Vücudunuzun dinlenir haldeyken yaktığı kalori miktarı.",
        "content": """
            <h2>BMR Nedir?</h2>
            <p>Bazal Metabolizma Hızı, vücudun hayati fonksiyonlarını (nefes alma, kan dolaşımı vb.) sürdürebilmesi için gereken minimum enerji miktarıdır. Kilo vermek isteyenler için kritik bir veridir.</p>
        """
    },
    "makro": {
        "title": "Günlük Makro (Protein, Karbonhidrat, Yağ) Hesaplama",
        "desc": "Hedefinize göre almanız gereken besin değerleri.",
        "content": """
            <h2>Makro Besinler</h2>
            <p>Sağlıklı bir diyette enerjinin %45-65'i karbonhidratlardan, %20-35'i yağlardan ve %10-35'i proteinlerden gelmelidir.</p>
        """
    },
    "su": {
        "title": "Günlük Su İhtiyacı Hesaplama",
        "desc": "Kilonuza göre günde kaç litre su içmelisiniz?",
        "content": """
            <h2>Su Tüketim Kuralı</h2>
            <p>Genel kural olarak her 1 kg vücut ağırlığı için 33 ml su içilmelidir. Örneğin 60 kg bir kişi günde yaklaşık 2 litre su içmelidir.</p>
        """
    },
    "gebelik": {
        "title": "Gebelik Hesaplama ve Doğum Tarihi",
        "desc": "Son adet tarihinize (SAT) göre muhtemel doğum tarihini öğrenin.",
        "content": """
            <h2>Naegele Kuralı</h2>
            <p>Muhtemel doğum tarihi hesaplanırken son adet tarihinin ilk gününe 7 gün eklenir ve 3 ay geriye gidilir (veya 9 ay 10 gün eklenir).</p>
        """
    },
    "sigara": {
        "title": "Sigara Maliyeti Hesaplama",
        "desc": "Sigaraya harcadığınız parayla neler alabilirdiniz?",
        "content": """
            <h2>Sigaranın Ekonomik Yükü</h2>
            <p>Günde 1 paket sigara içen biri, yılda ortalama bir asgari ücret tutarını duman etmektedir. Bu araç size kaybettiğiniz serveti gösterir.</p>
        """
    },
    "nabiz": {
        "title": "Spor Nabız Aralığı Hesaplama",
        "desc": "Yağ yakımı ve kondisyon için ideal kalp atış hızınızı bulun.",
        "content": """
            <h2>Maksimum Nabız</h2>
            <p>Kabaca '220 - Yaş' formülü ile bulunur. Yağ yakımı için bu değerin %60-70 aralığında spor yapılmalıdır.</p>
        """
    },
    # EDUCATION
    "yuzde": {
        "title": "Yüzde Hesaplama Aracı",
        "desc": "Basit yüzde, artış ve azalış oranlarını hesaplayın.",
        "content": """
            <h2>Yüzde Nasıl Hesaplanır?</h2>
            <p>A sayısının %B'si: (A x B) / 100 formülü ile bulunur.</p>
        """
    },
    "sinav": {
        "title": "Üniversite Not Ortalaması (Vize-Final) Hesaplama",
        "desc": "Vize ve final notlarınızla ders geçme notunuzu hesaplayın.",
        "content": """
            <h2>Ortalama Ağırlıkları</h2>
            <p>Genellikle vize notunun %40'ı, final notunun %60'ı alınarak dönem sonu ortalaması belirlenir.</p>
        """
    },
    "takdir": {
        "title": "Takdir Teşekkür Hesaplama E-Okul",
        "desc": "Dönem ortalamasına göre belge durumunuzu sorgulayın.",
        "content": """
            <h2>Belge Alma Şartları</h2>
            <p>Dönem ağırlıklı not ortalaması 70.00-84.99 arası olanlar Teşekkür, 85.00 ve üzeri olanlar Takdir belgesi alır. Ayrıca zayıf ders olmaması ve devamsızlık sınırının aşılmaması gerekir.</p>
        """
    },
    "dikdortgen": {
        "title": "Dikdörtgen Alan ve Çevre Hesaplama",
        "desc": "En ve boy ölçüleriyle metrekare hesabı yapın.",
        "content": """
            <h2>Alan Hesabı</h2>
            <p>Alan = Uzun Kenar x Kısa Kenar. Özellikle oda, arsa veya halı büyüklüğü hesaplarken kullanılır.</p>
        """
    },
    "kelime": {
        "title": "Kelime ve Karakter Sayacı",
        "desc": "Metninizdeki toplam kelime ve harf sayısını analiz edin.",
        "content": """
            <h2>SEO İçin Kelime Sayısı</h2>
            <p>Blog yazıları ve makaleler için ideal uzunluk genellikle 600 kelime ve üzeridir. Bu araç ile içeriğinizin uzunluğunu kontrol edebilirsiniz.</p>
        """
    },
    # PRACTICAL
    "internet": {
        "title": "İnternet Hızı İndirme Süresi Hesaplama",
        "desc": "Dosya boyutu ve internet hızınıza göre indirme ne kadar sürer?",
        "content": """
            <h2>Mbps vs MB/s</h2>
            <p>İnternet hızları genellikle Mbps (Megabit) cinsinden verilirken, dosya boyutları MB (Megabyte) cinsindendir. 1 Byte = 8 bit olduğu için, 100 Mbps internet ile saniyede maksimum 12.5 MB veri indirebilirsiniz.</p>
        """
    },
    "yakit": {
        "title": "Yakıt Tüketimi Hesaplama",
        "desc": "Aracınızın km başına ne kadar yaktığını hesaplayın.",
        "content": """
            <h2>Yakıt Tasarrufu İpuçları</h2>
            <p>Ani hızlanmalardan kaçınmak, lastik basınçlarını kontrol etmek ve gereksiz yükleri boşaltmak yakıt tüketimini %10-20 oranında azaltabilir.</p>
        """
    },
    "yas": {
        "title": "Tam Yaş Hesaplama",
        "desc": "Doğum tarihinize göre gün, ay ve yıl cinsinden yaşınızı öğrenin.",
        "content": """
            <h2>Yaş Nasıl Hesaplanır?</h2>
            <p>Bugünün tarihinden doğum tarihiniz çıkarılarak bulunur. Artık yıllar (Şubat 29) hesaplamaya dahil edilir.</p>
        """
    },
    "gun": {
        "title": "İki Tarih Arası Gün Sayacı",
        "desc": "İki tarih arasında kaç gün, hafta veya ay var?",
        "content": """
            <h2>Kullanım Alanları</h2>
            <p>Vize süresi, askerlik şafağı, ilişki süresi veya proje teslim tarihi hesaplamalarında kullanılır.</p>
        """
    },
    "sifre": {
        "title": "Güçlü Şifre Oluşturucu",
        "desc": "Kırılması zor, rastgele ve güvenli şifreler üretin.",
        "content": """
            <h2>Güçlü Şifre Kriterleri</h2>
            <p>En az 12 karakter uzunluğunda, büyük-küçük harf, rakam ve özel karakter içeren şifreler güvenli kabul edilir.</p>
        """
    },
    "hiz": {
        "title": "Hız, Yol ve Zaman Hesaplama",
        "desc": "Gidilen mesafe ve süreye göre ortalama hızı bulun.",
        "content": """
            <h2>Fizik Formülü</h2>
            <p><code>Yol = Hız x Zaman</code> (x = v.t). Bu formülden yola çıkarak Hız = Yol / Zaman formülü elde edilir.</p>
        """
    }
}

html_template = """<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="{desc}">
    <title>{title} | HesaplaHadi</title>
    <link rel="canonical" href="https://hesaplahadi.com/{slug}" />
    <!-- JSON-LD -->
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "SoftwareApplication",
      "name": "{title}",
      "url": "https://hesaplahadi.com/{slug}",
      "description": "{desc}",
      "applicationCategory": "FinanceApplication",
      "operatingSystem": "All",
      "offers": {{ "@type": "Offer", "price": "0", "priceCurrency": "TRY" }}
    }}
    </script>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <link href="assets/css/style.css" rel="stylesheet">
</head>
<body class="flex flex-col min-h-screen text-slate-800">
    <!-- Header -->
    <header class="bg-white/90 backdrop-blur-md shadow-sm sticky top-0 z-50 border-b border-slate-100">
        <div class="container mx-auto px-4 py-3 flex justify-between items-center">
            <a href="index.html" class="flex items-center space-x-2 group">
                <div class="bg-gradient-to-br from-blue-600 to-indigo-700 text-white p-2.5 rounded-xl group-hover:shadow-lg group-hover:shadow-blue-500/30 transition duration-300">
                    <i class="fa-solid fa-calculator text-lg"></i>
                </div>
                <div class="leading-tight">
                    <h1 class="text-xl md:text-2xl font-extrabold tracking-tight text-slate-900">Hesapla<span class="text-blue-600">Hadi</span></h1>
                </div>
            </a>
            <div class="hidden md:flex items-center space-x-3 text-xs font-bold text-slate-600">
                <a href="index.html" class="hover:text-blue-600 transition">Araçlar</a>
                <a href="blog/index.html" class="hover:text-blue-600 transition">Blog</a>
                <a href="ai-asistan.html" class="flex items-center gap-2 bg-indigo-50 hover:bg-indigo-100 text-indigo-700 px-4 py-2 rounded-xl border border-indigo-100 transition duration-300">
                    <i class="fa-solid fa-wand-magic-sparkles"></i> <span>AI Asistan</span>
                </a>
            </div>
        </div>
    </header>

    <div class="container mx-auto px-4 py-8 grid grid-cols-1 lg:grid-cols-12 gap-8 flex-grow">
        <nav class="hidden lg:block lg:col-span-3 space-y-4">
            <div class="bg-white/80 backdrop-blur glass-panel rounded-2xl overflow-hidden flex flex-col sticky top-24">
                <div class="bg-slate-50/50 px-5 py-4 border-b border-slate-100 flex justify-between items-center shrink-0">
                    <h3 class="font-bold text-slate-700 text-sm uppercase tracking-wide">Hesaplama Araçları</h3>
                </div>
                <div id="sidebar-list" class="overflow-y-auto p-2 space-y-1"></div>
            </div>
        </nav>

        <main class="col-span-1 lg:col-span-6 space-y-6">
            <div class="bg-white/90 backdrop-blur rounded-2xl shadow-sm border border-slate-200 p-6 md:p-8 animate-slide-up relative">
                <div class="flex items-center gap-4 mb-6 pb-6 border-b border-slate-100">
                    <div class="p-3 bg-blue-100 rounded-2xl text-blue-600 shadow-sm"><i class="fa-solid fa-calculator text-xl"></i></div>
                    <div>
                        <h1 class="text-2xl font-bold text-slate-900 tracking-tight">{title_short}</h1>
                        <p class="text-xs text-slate-500 mt-1">{desc}</p>
                    </div>
                </div>

                <!-- Tool Inputs Container - ID MUST MATCH calculator.js expectation -->
                <div id="content-{tool_id}">
                    <div id="tool-placeholder"></div>
                </div>
            </div>

            <article class="bg-white rounded-2xl shadow-sm border border-slate-200 p-8 info-panel">
                {content}
            </article>
        </main>

        <aside class="col-span-1 lg:col-span-3 space-y-6">
             <div class="bg-white p-6 rounded-2xl shadow-sm border border-slate-200">
                <h4 class="font-bold text-xs text-slate-500 mb-4 uppercase tracking-wider border-b border-slate-100 pb-2 flex items-center gap-2">
                    <i class="fa-solid fa-fire text-orange-500"></i> Popüler
                </h4>
                <ul class="text-sm space-y-2 text-slate-600 font-medium">
                    <li class="cursor-pointer hover:text-blue-600 hover:bg-blue-50 p-2.5 rounded-lg transition" onclick="window.location.href='kdv-hesaplama.html'">KDV Hesaplama</li>
                    <li class="cursor-pointer hover:text-blue-600 hover:bg-blue-50 p-2.5 rounded-lg transition" onclick="window.location.href='kredi-hesaplama.html'">Kredi Hesaplama</li>
                </ul>
            </div>
        </aside>
    </div>

    <footer class="bg-slate-900 text-slate-400 py-12 mt-auto border-t border-slate-800">
        <div class="container mx-auto px-4 text-center">
            <span class="text-2xl font-bold text-white tracking-tight">Hesapla<span class="text-blue-500">Hadi</span></span>
            <div class="flex justify-center flex-wrap gap-6 text-sm font-medium mt-6 text-slate-300">
                <a href="index.html" class="hover:text-white transition">Ana Sayfa</a>
                <a href="blog/index.html" class="hover:text-white transition">Blog</a>
            </div>
            <div class="text-xs text-slate-600 mt-6">&copy; 2026 HesaplaHadi.</div>
        </div>
    </footer>
    <script src="assets/js/calculator.js"></script>
    <script>
        // Specific init for this tool
        window.addEventListener('load', () => {{
             // We need a function in calculator.js to render a specific tool into a specific container
             // or we modify renderTools to be more flexible.
             // For now, let's assume I will add 'renderSingleTool(toolId, containerId)' to calculator.js
             if(typeof renderSingleTool === 'function') {{
                 renderSingleTool('{tool_id}', 'tool-placeholder');
             }}
        }});
    </script>
</body>
</html>
"""

for tid, meta in tools_meta.items():
    slug_base = meta['title'].split(' - ')[0].lower().replace(' ', '-').replace('ı','i').replace('ş','s').replace('ü','u').replace('ö','o').replace('ç','c').replace('ğ','g').replace('(','').replace(')','').replace('?','')
    slug = slug_base + ".html"

    print(f"ID: {tid} -> Slug: {slug}")

    content = html_template.format(
        title=meta['title'],
        title_short=meta['title'].split(' - ')[0],
        desc=meta['desc'],
        slug=slug,
        tool_id=tid,
        content=meta['content']
    )

    with open(slug, 'w', encoding='utf-8') as f:
        f.write(content)
