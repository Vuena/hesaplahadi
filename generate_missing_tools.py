
import os

# Define only the new tools requested
new_tools_meta = {
    "ags": {
        "title": "AGS Puan Hesaplama - Akademik Gelişim Sınavı",
        "desc": "AGS sınav puanınızı ders netlerinize göre hesaplayın.",
        "content": """
            <h2>AGS Puanı Nasıl Hesaplanır?</h2>
            <p>Akademik Gelişim Sınavı (AGS), öğrencilerin akademik yeterliliklerini ölçmek için yapılan bir sınavdır. Puan hesaplaması, doğru ve yanlış cevaplarınızın nete dönüştürülmesi ve katsayılarla çarpılmasıyla yapılır.</p>
        """
    },
    "deger_artisi": {
        "title": "Değer Artış Kazancı Hesaplama",
        "desc": "Gayrimenkul satışında ödemeniz gereken değer artış kazancı vergisi.",
        "content": """
            <h2>Değer Artış Kazancı Nedir?</h2>
            <p>Gayrimenkullerin iktisap tarihinden itibaren 5 yıl içinde elden çıkarılmasından sağlanan kazançlar değer artış kazancı olarak vergilendirilir. Enflasyon düzeltmesi (ÜFE) uygulanarak vergi matrahı bulunur.</p>
        """
    },
    "ek_ders": {
        "title": "Ek Ders Ücreti Hesaplama 2026",
        "desc": "Öğretmenler için haftalık ve aylık ek ders ücreti hesaplama aracı.",
        "content": """
            <h2>Ek Ders Ücreti Katsayıları</h2>
            <p>Ek ders ücretleri memur maaş katsayısına göre belirlenir. Gündüz, gece, hafta sonu ve takviye kursu ücretleri farklılık gösterir. Vergi dilimi de net ele geçen tutarı etkiler.</p>
        """
    },
    "promil": {
        "title": "Promil Hesaplama - Alkol Oranı",
        "desc": "İçtiğiniz içkiye ve kilonuza göre tahmini kandaki alkol oranı.",
        "content": """
            <h2>Yasal Promil Sınırı</h2>
            <p>Türkiye'de hususi otomobil sürücüleri için yasal sınır 0.50 promildir. Diğer araç sürücüleri için bu sınır 0.20 promildir.</p>
        """
    },
    "tus": {
        "title": "TUS Puan Hesaplama",
        "desc": "Tıpta Uzmanlık Sınavı puanınızı netlerinize göre hesaplayın.",
        "content": """
            <h2>TUS Puan Sistemi</h2>
            <p>TUS puanı, Temel Tıp Bilimleri ve Klinik Tıp Bilimleri testlerinden alınan standart puanların ağırlıklı ortalaması ile hesaplanır.</p>
        """
    },
    "lgs": {
        "title": "LGS Puan Hesaplama 2026",
        "desc": "Liselere Geçiş Sistemi puanınızı ve yüzdelik diliminizi tahmin edin.",
        "content": """
            <h2>LGS Katsayıları</h2>
            <p>Türkçe, Matematik ve Fen Bilimleri testlerinin katsayısı 4, T.C. İnkılap Tarihi, Din Kültürü ve Yabancı Dil testlerinin katsayısı 1'dir.</p>
        """
    },
    "islah": {
        "title": "Islah Harcı Hesaplama",
        "desc": "Dava değerini artırma (ıslah) işlemi için gereken harç tutarı.",
        "content": """
            <h2>Islah Harcı Oranı</h2>
            <p>Islah edilen tutar üzerinden binde 68,31 oranında karar ve ilam harcının dörtte biri peşin olarak ödenir.</p>
        """
    },
    "taksimetre": {
        "title": "Taksimetre Hesaplama - Taksi Ücreti",
        "desc": "Gideceğiniz mesafeye göre tahmini taksi ücretini hesaplayın.",
        "content": """
            <h2>Taksi Açılış Ücretleri</h2>
            <p>Taksi ücreti hesaplanırken açılış ücreti, km başına ücret ve varsa köprü/otoyol geçiş ücretleri dikkate alınır. Minimum indi-bindi ücreti uygulanır.</p>
        """
    },
    "safak": {
        "title": "Şafak Hesaplama - Askerlik Terhis Tarihi",
        "desc": "Askerlik şafağınızı ve terhis tarihinizi hesaplayın.",
        "content": """
            <h2>Askerlik Süresi</h2>
            <p>Er ve erbaşlar için askerlik süresi 6 aydır. Yedek subay ve astsubaylar için ise 12 aydır. Yol izni ve kullanılan izinler şafak sayısını etkiler.</p>
        """
    },
    "yks": {
        "title": "YKS Net Hesaplama (TYT-AYT)",
        "desc": "Doğru ve yanlış sayılarınıza göre TYT ve AYT netlerinizi görün.",
        "content": """
            <h2>Net Nasıl Hesaplanır?</h2>
            <p>Her testte 4 yanlış 1 doğruyu götürür. Kalan doğru sayısı netinizi oluşturur. ÖSYM puanları bu netler üzerinden hesaplanır.</p>
        """
    },
    "kira": {
        "title": "Kira Artış Oranı Hesaplama",
        "desc": "TÜFE ve yasal sınırlara göre kira zam oranını hesaplayın.",
        "content": """
            <h2>Yasal Kira Artış Sınırı</h2>
            <p>Konut kiralarında artış oranı, 12 aylık TÜFE ortalamasını geçemez. (Not: %25 sınırı Temmuz 2024'te kalkmıştır).</p>
        """
    },
    "vekalet": {
        "title": "Vekalet Ücreti Hesaplama",
        "desc": "Avukatlık Asgari Ücret Tarifesine göre vekalet ücreti.",
        "content": """
            <h2>Nispi Vekalet Ücreti</h2>
            <p>Dava değerine göre değişen oranlarda (ilk dilim %16 gibi) hesaplanan ücrettir. Maktu ücretin altında olamaz.</p>
        """
    },
    "gano": {
        "title": "GANO Hesaplama - Akademik Ortalaması",
        "desc": "Dönemlik ve genel akademik not ortalamanızı hesaplayın.",
        "content": """
            <h2>GANO ve YANO</h2>
            <p>Derslerin kredi değerleri ile harf notu katsayılarının çarpımının toplam krediye bölünmesiyle bulunur.</p>
        """
    }
}

# The template MUST match the structure of index.html exactly, including the new mobile navigation
# We will verify this by ensuring the generated HTML contains the new search bars and burger menu
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
    <style>
        .drawer-open {{ transform: translateX(0); }}
        .drawer-closed {{ transform: translateX(-100%); }}
        .mask-visible {{ opacity: 1; pointer-events: auto; }}
        .mask-hidden {{ opacity: 0; pointer-events: none; }}
    </style>
</head>
<body class="flex flex-col min-h-screen text-slate-800 bg-slate-50">

    <!-- Mobile Sidebar Drawer -->
    <div id="drawer-mask" class="fixed inset-0 bg-black/50 z-[60] transition-opacity duration-300 mask-hidden" onclick="toggleDrawer()"></div>
    <aside id="drawer" class="fixed top-0 left-0 w-64 h-full bg-white z-[70] shadow-2xl transition-transform duration-300 drawer-closed overflow-y-auto">
        <div class="p-4 border-b border-slate-100 flex justify-between items-center">
             <span class="font-bold text-lg text-slate-800">Hesaplama Araçları</span>
             <button onclick="toggleDrawer()" class="text-slate-400 hover:text-slate-600"><i class="fa-solid fa-times text-xl"></i></button>
        </div>
        <div id="drawer-list" class="p-3 space-y-1"></div>
    </aside>

    <!-- Header -->
    <header class="bg-white/90 backdrop-blur-md shadow-sm sticky top-0 z-50 border-b border-slate-100">
        <div class="container mx-auto px-4 py-3">
            <div class="flex justify-between items-center">
                <!-- Left: Logo (No Hamburger) -->
                <div class="flex items-center gap-3">
                    <a href="index.html" class="flex items-center space-x-2 group">
                        <div class="bg-gradient-to-br from-blue-600 to-indigo-700 text-white p-2 rounded-lg group-hover:shadow-lg transition">
                            <i class="fa-solid fa-calculator text-base"></i>
                        </div>
                        <div class="leading-tight">
                            <h1 class="text-lg md:text-2xl font-extrabold tracking-tight text-slate-900">Hesapla<span class="text-blue-600">Hadi</span></h1>
                        </div>
                    </a>
                </div>

                <!-- Desktop Search -->
                <div class="hidden md:block relative w-96 mx-4">
                    <i class="fa-solid fa-search absolute left-3 top-3 text-slate-400 text-sm"></i>
                    <input type="text" id="desktop-tool-search" placeholder="Hesaplama aracı ara..." class="w-full pl-9 pr-4 py-2 bg-slate-50 border border-slate-200 rounded-lg text-sm focus:bg-white focus:border-blue-500 transition outline-none">
                    <div id="desktop-search-suggestions" class="absolute top-full left-0 w-full bg-white border border-slate-200 shadow-lg rounded-xl mt-1 z-50 hidden"></div>
                </div>

                <!-- Right: Actions -->
                <div class="flex items-center gap-3">
                    <!-- Desktop Nav -->
                    <div class="hidden md:flex items-center space-x-3 text-xs font-bold text-slate-600">
                        <a href="blog/index.html" class="hover:text-blue-600 px-2 py-2 transition">Blog</a>
                        <a href="ai-asistan.html" class="flex items-center gap-2 bg-indigo-50 hover:bg-indigo-100 text-indigo-700 px-4 py-2 rounded-xl border border-indigo-100 transition duration-300">
                            <i class="fa-solid fa-wand-magic-sparkles"></i>
                            <span>AI Asistan</span>
                        </a>
                    </div>

                    <!-- Mobile AI Button -->
                    <a href="ai-asistan.html" class="md:hidden flex items-center justify-center w-8 h-8 rounded-full bg-indigo-50 text-indigo-600 border border-indigo-100 hover:bg-indigo-100 transition">
                        <i class="fa-solid fa-wand-magic-sparkles text-sm"></i>
                    </a>

                    <!-- Mobile Stylized Blog Button -->
                    <a href="blog/index.html" class="md:hidden bg-gradient-to-r from-blue-600 to-blue-500 text-white text-[10px] font-bold px-3 py-1.5 rounded-full shadow-sm hover:shadow-md transition flex items-center gap-1">
                        <span>Blog</span> <i class="fa-solid fa-chevron-right text-[8px] opacity-70"></i>
                    </a>
                </div>
            </div>

            <!-- Mobile Search Bar (Below Header) -->
            <div class="md:hidden mt-3 relative">
                 <i class="fa-solid fa-search absolute left-3 top-3 text-slate-400 text-sm"></i>
                 <input type="text" id="mobile-tool-search" onkeyup="filterDrawerTools()" placeholder="Hesaplama aracı ara..." class="w-full pl-9 pr-4 py-2 bg-slate-50 border border-slate-200 rounded-lg text-sm focus:bg-white focus:border-blue-500 transition outline-none">
                 <div id="mobile-search-suggestions" class="absolute top-full left-0 w-full bg-white border border-slate-200 shadow-lg rounded-xl mt-1 z-50 hidden"></div>
            </div>

            <!-- Mobile Drawer Toggle (Below Search) -->
            <div class="md:hidden mt-3">
                <button onclick="toggleDrawer()" class="w-full bg-slate-800 text-white rounded-lg py-3 flex items-center justify-center gap-2 hover:bg-slate-700 transition shadow-sm">
                    <i class="fa-solid fa-bars"></i>
                    <span class="font-bold text-sm">Menü</span>
                </button>
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
                    <div id="tool-placeholder">
                        <p class="text-slate-500 text-sm italic">Bu araç şu anda geliştirilme aşamasındadır. Lütfen daha sonra tekrar deneyiniz veya AI Asistan'ı kullanınız.</p>
                    </div>
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
        // Drawer Logic
        function toggleDrawer() {{
            const d = document.getElementById('drawer');
            const m = document.getElementById('drawer-mask');
            if(d.classList.contains('drawer-closed')) {{
                d.classList.remove('drawer-closed');
                d.classList.add('drawer-open');
                m.classList.remove('mask-hidden');
                m.classList.add('mask-visible');
            }} else {{
                d.classList.remove('drawer-open');
                d.classList.add('drawer-closed');
                m.classList.remove('mask-visible');
                m.classList.add('mask-hidden');
            }}
        }}

        function filterDrawerTools() {{
            const q = document.getElementById('mobile-tool-search').value.toLowerCase();
            const drawerList = document.getElementById('drawer-list');
            const items = drawerList.querySelectorAll('a');

            items.forEach(item => {{
                if(item.classList.contains('cat-header')) return;
                const txt = item.innerText.toLowerCase();
                item.style.display = txt.includes(q) ? 'flex' : 'none';
            }});
        }}

        // Specific init for this tool
        window.addEventListener('load', () => {{
             if(typeof renderSingleTool === 'function') {{
                 renderSingleTool('{tool_id}', 'tool-placeholder');
             }}
        }});
    </script>
</body>
</html>
"""

for tid, meta in new_tools_meta.items():
    # Construct filename: {slug}.html
    # We must ensure the slug matches the 'link' property in calculator.js
    # Looking at calculator.js:
    # ags -> ags-puan-hesapla.html
    # deger_artisi -> deger-artisi-hesaplama.html
    # ek_ders -> ek-ders-hesaplama.html
    # promil -> promil-hesaplama.html
    # tus -> tus-puan-hesaplama.html
    # lgs -> lgs-puan-hesaplama.html
    # islah -> islah-harci-hesaplama.html
    # taksimetre -> taksimetre-hesaplama.html
    # safak -> safak-hesaplama.html
    # yks -> yks-net-hesaplama.html
    # kira -> kira-artis-hesaplama.html
    # vekalet -> vekalet-ucreti-hesaplama.html
    # gano -> gano-hesaplama.html

    slug_map = {
        "ags": "ags-puan-hesapla.html",
        "deger_artisi": "deger-artisi-hesaplama.html",
        "ek_ders": "ek-ders-hesaplama.html",
        "promil": "promil-hesaplama.html",
        "tus": "tus-puan-hesaplama.html",
        "lgs": "lgs-puan-hesaplama.html",
        "islah": "islah-harci-hesaplama.html",
        "taksimetre": "taksimetre-hesaplama.html",
        "safak": "safak-hesaplama.html",
        "yks": "yks-net-hesaplama.html",
        "kira": "kira-artis-hesaplama.html",
        "vekalet": "vekalet-ucreti-hesaplama.html",
        "gano": "gano-hesaplama.html"
    }

    slug = slug_map.get(tid)
    if not slug:
        print(f"Skipping {tid}, no slug found.")
        continue

    print(f"Generating {slug} for {tid}...")

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
