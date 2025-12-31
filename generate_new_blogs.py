
import os
import json

# Define the full list of posts (old + new, excluding crypto)
all_posts = [
    {
        "id": "kredi-notu",
        "slug": "kredi-notu-nasil-yukseltilir.html",
        "title": "Kredi Notu Nasıl Yükseltilir? En Etkili 5 Yöntem",
        "summary": "Bankalardan kredi veya kredi kartı alırken en önemli kriter olan kredi notunuzu yükseltmek için yapmanız gerekenler ve altın kurallar.",
        "category": "Finans",
        "image": "fa-chart-line",
        "color": "blue",
        "relatedTool": "kredi",
        "content": "<p>Kredi notu, finansal geçmişinizin bir özetidir.</p><h2>Ödemeleri Düzenli Yapın</h2><p>Gecikmiş borçlar notunuzu en çok düşüren faktördür.</p>"
    },
    {
        "id": "tevkifat-nedir",
        "slug": "kdv-tevkifati-nedir-kimler-yapar.html",
        "title": "KDV Tevkifatı Nedir? Kimler Tevkifat Yapar?",
        "summary": "İşletmeler için tevkifatlı fatura kesim süreçleri, 2/10, 5/10 oranlarının anlamı ve dikkat edilmesi gereken noktalar.",
        "category": "Vergi",
        "image": "fa-receipt",
        "color": "emerald",
        "relatedTool": "tevkifat",
        "content": "<p>Tevkifat, verginin bir kısmının alıcı tarafından ödenmesidir.</p>"
    },
    {
        "id": "enflasyon-nedir",
        "slug": "enflasyon-nedir-nasil-hesaplanir.html",
        "title": "Enflasyon Nedir? Bütçenizi Nasıl Etkiler?",
        "summary": "Enflasyonun alım gücüne etkisi, TÜFE ve ÜFE kavramları ve paranızı enflasyona karşı korumanın yolları.",
        "category": "Finans",
        "image": "fa-arrow-trend-up",
        "color": "red",
        "relatedTool": "mevduat",
        "content": "<p>Enflasyon, fiyatlar genel düzeyindeki artıştır.</p>"
    },
    {
        "id": "konut-kredisi",
        "slug": "konut-kredisi-cekerken-dikkat-edilmesi-gerekenler.html",
        "title": "Konut Kredisi Çekerken Dikkat Edilmesi Gerekenler",
        "summary": "Ev sahibi olma hayali kuranlar için faiz oranları, vade seçenekleri ve ek masraflar hakkında kapsamlı rehber.",
        "category": "Emlak",
        "image": "fa-house",
        "color": "orange",
        "relatedTool": "kredi",
        "content": "<p>Konut kredisi uzun vadeli bir borçlanmadır.</p>"
    },
    {
        "id": "ideal-kilo",
        "slug": "ideal-kilo-nasil-hesaplanir-formulu-nedir.html",
        "title": "İdeal Kilo Nasıl Hesaplanır? Bilimsel Formüller",
        "summary": "Sağlıklı bir yaşam için ideal kilonuzu öğrenin. Boy, yaş ve cinsiyete göre hesaplama yöntemleri.",
        "category": "Sağlık",
        "image": "fa-weight-scale",
        "color": "green",
        "relatedTool": "idealkilo",
        "content": "<p>İdeal kilo, sağlıklı yaşamın anahtarıdır.</p>"
    },
    {
        "id": "brut-net",
        "slug": "brutten-nete-maas-hesaplama-rehberi.html",
        "title": "Brütten Nete Maaş Hesaplama Rehberi",
        "summary": "Maaşınızdan yapılan kesintiler nelerdir? SGK primi, gelir vergisi ve damga vergisi hesaplamanın mantığı.",
        "category": "Finans",
        "image": "fa-money-bill-wave",
        "color": "blue",
        "relatedTool": "brut_net",
        "content": "<p>Brüt maaş, işverenin kasasından çıkan toplam tutardır (işveren maliyeti hariç).</p>"
    },
    {
        "id": "bmi-nedir",
        "slug": "vucut-kitle-indeksi-bmi-nedir.html",
        "title": "Vücut Kitle İndeksi (BMI) Nedir? Değerler Ne Anlama Gelir?",
        "summary": "Vücut kitle indeksinizi hesaplayarak obezite riskinizi öğrenin. Dünya Sağlık Örgütü standartlarına göre değerlerin analizi.",
        "category": "Sağlık",
        "image": "fa-person",
        "color": "green",
        "relatedTool": "bmi",
        "content": "<p>BMI, vücut ağırlığının boy uzunluğunun karesine bölünmesiyle hesaplanır.</p>"
    },
    {
        "id": "yuzde-hesaplama",
        "slug": "yuzde-hesaplama-formulu-ve-ornekleri.html",
        "title": "Yüzde Hesaplama Formülü ve Günlük Hayatta Kullanımı",
        "summary": "Matematiksel yüzde hesaplamanın en basit yolları. İndirim, zam ve kar marjı hesaplamalarında pratik yöntemler.",
        "category": "Eğitim",
        "image": "fa-percent",
        "color": "purple",
        "relatedTool": "yuzde",
        "content": "<p>Yüzde hesaplama hayatın her alanında karşımıza çıkar.</p>"
    },
    {
        "id": "su-tuketimi",
        "slug": "gunluk-su-tuketimi-ne-kadar-olmali.html",
        "title": "Günlük Su Tüketimi Ne Kadar Olmalı?",
        "summary": "Vücudunuzun ihtiyacı olan su miktarını hesaplayın. Yetersiz su tüketiminin zararları ve sağlıklı yaşam için öneriler.",
        "category": "Sağlık",
        "image": "fa-droplet",
        "color": "cyan",
        "relatedTool": "su",
        "content": "<p>Su hayattır.</p>"
    },
    {
        "slug": "doviz-yatirimi-mantikli-mi.html",
        "title": "Döviz Yatırımı Yapmak Mantıklı Mı? Riskler ve Fırsatlar",
        "summary": "Dolar ve Euro yatırımı yaparken dikkat edilmesi gerekenler. Döviz kurları neden dalgalanır?",
        "category": "Finans",
        "image": "fa-coins",
        "color": "green",
        "relatedTool": "mevduat",
        "content": "<p>Döviz yatırımı...</p>"
    },
    {
        "slug": "kredi-karti-puanlari-nasil-kullanilir.html",
        "title": "Kredi Kartı Puanları En Verimli Nasıl Kullanılır?",
        "summary": "Bankaların verdiği chip-para, maxipuan ve bonusları nakit gibi kullanmanın yolları.",
        "category": "Finans",
        "image": "fa-credit-card",
        "color": "blue",
        "relatedTool": "kk_asgari",
        "content": "<p>Puanları harcamak...</p>"
    },
    {
        "slug": "bireysel-emeklilik-sistemi-bes-nedir.html",
        "title": "Bireysel Emeklilik Sistemi (BES) Nedir? Devlet Katkısı %30",
        "summary": "Geleceğiniz için birikim yapmanın devlet destekli yolu. BES avantajları ve çıkış şartları.",
        "category": "Finans",
        "image": "fa-piggy-bank",
        "color": "purple",
        "relatedTool": "mevduat",
        "content": "<p>BES birikim...</p>"
    },
    {
        "slug": "altin-yatirimi-fiziki-mi-banka-mi.html",
        "title": "Altın Yatırımı: Fiziki mi Yoksa Banka Hesabı mı?",
        "summary": "Gram altın alırken hangisi daha karlı? Makas aralıkları ve saklama maliyetleri.",
        "category": "Yatırım",
        "image": "fa-gem",
        "color": "amber",
        "relatedTool": "mevduat",
        "content": "<p>Altın yatırımı...</p>"
    },
    {
        "slug": "intermittent-fasting-aralikli-oruc-nedir.html",
        "title": "Aralıklı Oruç (Intermittent Fasting) Nedir? Nasıl Yapılır?",
        "summary": "16/8 kuralı ile kilo verme yöntemi. Açlık penceresinde neler tüketilebilir?",
        "category": "Sağlık",
        "image": "fa-clock",
        "color": "indigo",
        "relatedTool": "ai_diyet",
        "content": "<p>Aralıklı oruç...</p>"
    },
    {
        "slug": "metabolizma-hizlandirma-yollari.html",
        "title": "Metabolizmayı Hızlandırmanın 10 Doğal Yolu",
        "summary": "Daha hızlı kilo vermek için metabolizma hızınızı artırın. Kahve, yeşil çay ve egzersiz.",
        "category": "Sağlık",
        "image": "fa-fire",
        "color": "red",
        "relatedTool": "bmr",
        "content": "<p>Metabolizma...</p>"
    },
    {
        "slug": "ders-calisma-teknikleri-pomodoro.html",
        "title": "Verimli Ders Çalışma Tekniği: Pomodoro",
        "summary": "25 dakika çalışma, 5 dakika mola. Odaklanma sorunu yaşayanlar için en iyi yöntem.",
        "category": "Eğitim",
        "image": "fa-stopwatch",
        "color": "red",
        "relatedTool": "sinav",
        "content": "<p>Pomodoro...</p>"
    },
    {
        "slug": "hizli-okuma-teknikleri.html",
        "title": "Hızlı Okuma Teknikleri ile Anlama Oranını Artırın",
        "summary": "Dakikada okunan kelime sayısını artırma egzersizleri ve göz kaslarını geliştirme.",
        "category": "Eğitim",
        "image": "fa-book-open",
        "color": "blue",
        "relatedTool": "kelime",
        "content": "<p>Hızlı okuma...</p>"
    },
    {
        "slug": "evde-spor-yaparak-zayiflama.html",
        "title": "Spor Salonuna Gitmeden Evde Zayıflama Rehberi",
        "summary": "Ekipmansız yapılabilecek en etkili egzersizler. Plank, Squat ve Şınav.",
        "category": "Sağlık",
        "image": "fa-dumbbell",
        "color": "orange",
        "relatedTool": "bmi",
        "content": "<p>Evde spor...</p>"
    },
    {
        "slug": "tasarruf-yapmanin-yollari.html",
        "title": "Para Biriktirmenin ve Tasarruf Yapmanın 7 Yolu",
        "summary": "Gereksiz harcamaları kısıp birikim yapmaya başlamak için pratik ipuçları.",
        "category": "Finans",
        "image": "fa-wallet",
        "color": "green",
        "relatedTool": "mevduat",
        "content": "<p>Tasarruf yapmak...</p>"
    },
    {
        "slug": "is-gorusmesinde-maas-pazarligi.html",
        "title": "İş Görüşmesinde Maaş Pazarlığı Nasıl Yapılır?",
        "summary": "Yeni bir işe girerken veya zam isterken maaş beklentinizi nasıl dile getirmelisiniz?",
        "category": "Kariyer",
        "image": "fa-briefcase",
        "color": "blue",
        "relatedTool": "net_brut",
        "content": "<p>Maaş pazarlığı...</p>"
    },
    {
        "slug": "kalori-acigi-ile-zayiflama.html",
        "title": "Kalori Açığı Oluşturarak Nasıl Zayıflanır?",
        "summary": "Kilo vermenin temel mantığı: Kalori açığı. Günlük ne kadar açık oluşturmalısınız?",
        "category": "Sağlık",
        "image": "fa-apple-whole",
        "color": "red",
        "relatedTool": "bmr",
        "content": "<p>Kalori açığı...</p>"
    },
    {
        "slug": "python-ile-yazilima-baslamak.html",
        "title": "Python ile Yazılıma Başlamak: Neden İlk Tercih Olmalı?",
        "summary": "Kodlama öğrenmek isteyenler için Python dilinin avantajları ve kullanım alanları.",
        "category": "Eğitim",
        "image": "fa-code",
        "color": "yellow",
        "relatedTool": "kelime",
        "content": "<p>Python...</p>"
    },
    {
        "slug": "cocuklar-icin-kodlama-egitimi.html",
        "title": "Çocuklar İçin Kodlama Eğitimi Neden Önemli?",
        "summary": "Erken yaşta algoritmik düşünme becerisi kazanmanın faydaları.",
        "category": "Eğitim",
        "image": "fa-child",
        "color": "purple",
        "relatedTool": "dikdortgen",
        "content": "<p>Kodlama eğitimi...</p>"
    },
    {
        "slug": "gunluk-yuruyusun-faydalari.html",
        "title": "Günde 10 Bin Adım Atmanın Faydaları Nelerdir?",
        "summary": "Düzenli yürüyüşün kalp sağlığından kilo kontrolüne kadar inanılmaz etkileri.",
        "category": "Sağlık",
        "image": "fa-person-walking",
        "color": "cyan",
        "relatedTool": "yakit",
        "content": "<p>Günlük yürüyüş...</p>"
    },
    # 6 New Posts
    {
        "slug": "yapay-zeka-gelecegi.html",
        "title": "Yapay Zeka Geleceği Nasıl Şekillendirecek?",
        "summary": "İş dünyasından sanata, yapay zekanın hayatımıza etkileri ve beklenen büyük değişimler.",
        "category": "Teknoloji",
        "image": "fa-robot",
        "color": "indigo",
        "relatedTool": "ai_asistan",
        "content": "<p>Yapay zeka (AI), sadece bir teknoloji trendi değil, insanlık tarihinin en büyük devrimlerinden biridir.</p>"
    },
    {
        "slug": "ev-almak-mi-kiralamak-mi.html",
        "title": "Ev Almak mı Yoksa Kiralamak mı Daha Mantıklı?",
        "summary": "Mevcut faiz oranları ve kira çarpanlarına göre finansal analiz. Hangi durumda ne yapılmalı?",
        "category": "Emlak",
        "image": "fa-house-chimney",
        "color": "orange",
        "relatedTool": "kredi",
        "content": "<p>Ev sahipliği, güvence hissi verse de finansal açıdan her zaman en iyi seçenek olmayabilir.</p>"
    },
    {
        "slug": "dengeli-beslenme-tabagi.html",
        "title": "Dengeli Beslenme Tabağı Nasıl Hazırlanır?",
        "summary": "Her öğünde bulunması gereken besin grupları. Karbonhidrat, protein ve yağ dengesi.",
        "category": "Sağlık",
        "image": "fa-carrot",
        "color": "green",
        "relatedTool": "makro",
        "content": "<p>Sağlıklı bir tabak, renkli ve çeşitlidir.</p>"
    },
    {
        "slug": "lgs-hazirlik-rehberi.html",
        "title": "LGS Hazırlık Sürecinde Başarı İçin 7 Altın Kural",
        "summary": "Sınav stresini yönetme, planlı çalışma ve deneme çözme stratejileri.",
        "category": "Eğitim",
        "image": "fa-pencil",
        "color": "blue",
        "relatedTool": "sinav",
        "content": "<p>LGS, disiplinli bir çalışma gerektirir.</p>"
    },
    {
        "slug": "kisisel-finans-yonetimi.html",
        "title": "Kişisel Finans Yönetimi: Gelir-Gider Dengesi",
        "summary": "Para nereye gidiyor? Harcamalarınızı kontrol altına alarak finansal özgürlüğe ulaşın.",
        "category": "Finans",
        "image": "fa-chart-pie",
        "color": "emerald",
        "relatedTool": "mevduat",
        "content": "<p>Bütçe yapmak, zenginleşmenin ilk kuralıdır.</p>"
    },
    {
        "slug": "su-icmenin-cilde-faydalari.html",
        "title": "Su İçmenin Cilt Sağlığına 5 İnanılmaz Faydası",
        "summary": "Daha parlak ve genç bir cilt için suyun önemi. Nem dengesi ve toksin atımı.",
        "category": "Güzellik",
        "image": "fa-droplet",
        "color": "cyan",
        "relatedTool": "su",
        "content": "<p>Cildiniz susuz kaldığında kurur ve yaşlanır.</p>"
    }
]

# 1. Update JS file
js_content = "const blogPosts = " + json.dumps(all_posts, ensure_ascii=False, indent=4) + ";\n\n"
js_content += """function getCurrentPost() {
    const path = window.location.pathname;
    const filename = path.split('/').pop();
    return blogPosts.find(p => p.slug === filename);
}"""

with open('assets/js/blog-data.js', 'w', encoding='utf-8') as f:
    f.write(js_content)
print("Updated assets/js/blog-data.js")

# 2. Define Template (Updated Header for Mobile 'Araçlar' AND Favicon)
template = """<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="HesaplaHadi Blog yazısı.">
    <title>Blog Detay - HesaplaHadi</title>
    <link rel="canonical" href="https://hesaplahadi.com/blog/template.html" />
    <link rel="icon" type="image/png" href="../assets/img/favicon.png">
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <link href="../assets/css/style.css" rel="stylesheet">
    <style>
        .prose h2 { font-size: 1.5rem; font-weight: 700; color: #1e293b; margin-top: 2rem; margin-bottom: 1rem; }
        .prose p { margin-bottom: 1rem; line-height: 1.7; color: #334155; }
        .prose ul { list-style-type: disc; padding-left: 1.5rem; margin-bottom: 1rem; }
        .prose li { margin-bottom: 0.5rem; }
    </style>
</head>
<body class="flex flex-col min-h-screen text-slate-800 bg-slate-50">

    <!-- Header -->
    <header class="bg-white/90 backdrop-blur-md shadow-sm sticky top-0 z-50 border-b border-slate-100">
        <div class="container mx-auto px-4 py-3 flex justify-between items-center">
            <a href="../index.html" class="flex items-center space-x-2 group">
                <div class="bg-gradient-to-br from-blue-600 to-indigo-700 text-white p-2.5 rounded-xl group-hover:shadow-lg group-hover:shadow-blue-500/30 transition duration-300">
                    <i class="fa-solid fa-calculator text-lg"></i>
                </div>
                <div class="leading-tight">
                    <h1 class="text-xl md:text-2xl font-extrabold tracking-tight text-slate-900">Hesapla<span class="text-blue-600">Hadi</span></h1>
                </div>
            </a>

            <!-- Mobile: Calculation Tools Button (Hesaplama Araçları) - USER REQUEST -->
            <a href="../index.html" class="md:hidden bg-blue-600 text-white px-3 py-1.5 rounded-lg text-xs font-bold border border-blue-700 flex items-center gap-1 hover:bg-blue-700 transition shadow-sm">
                <i class="fa-solid fa-calculator"></i> Hesaplama Araçları
            </a>

            <!-- Desktop Nav -->
            <div class="hidden md:flex items-center space-x-4 text-sm font-bold text-slate-600">
                <a href="../index.html" class="hover:text-blue-600 transition">Araçlar</a>
                <a href="index.html" class="text-blue-600">Blog</a>
            </div>
        </div>
    </header>

    <div class="container mx-auto px-4 py-8 lg:py-12 flex-grow">
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 lg:gap-12">

            <!-- Main Content -->
            <main class="lg:col-span-8">
                <!-- Breadcrumb -->
                <nav class="flex text-xs text-slate-500 mb-6 uppercase tracking-wide font-bold">
                    <a href="../index.html" class="hover:text-blue-600">Anasayfa</a>
                    <span class="mx-2">/</span>
                    <a href="index.html" class="hover:text-blue-600">Blog</a>
                    <span class="mx-2">/</span>
                    <span class="text-slate-800" id="crumb-title">...</span>
                </nav>

                <article>
                    <!-- Header -->
                    <header class="mb-8">
                        <div class="flex items-center gap-3 mb-4">
                            <span id="post-cat" class="bg-blue-100 text-blue-700 text-xs font-bold px-2.5 py-1 rounded-md uppercase tracking-wide">Kategori</span>
                        </div>
                        <h1 id="post-title" class="text-3xl md:text-4xl lg:text-5xl font-extrabold text-slate-900 leading-tight mb-6">...</h1>
                        <p id="post-summary" class="text-lg md:text-xl text-slate-600 leading-relaxed border-l-4 border-blue-500 pl-4">...</p>
                    </header>

                    <!-- Featured Image / Icon Area -->
                    <div class="bg-slate-100 rounded-2xl h-64 md:h-80 flex items-center justify-center mb-10 text-slate-300">
                         <i id="post-icon" class="fa-solid fa-image text-8xl opacity-50"></i>
                    </div>

                    <!-- Content Body -->
                    <div class="prose max-w-none" id="content-body">
                       <p>İçerik yükleniyor...</p>
                    </div>
                </article>
            </main>

            <!-- Sidebar -->
            <aside class="lg:col-span-4 space-y-8">
                <div class="bg-white rounded-2xl shadow-sm border border-slate-200 p-6 sticky top-24">
                    <h4 class="font-bold text-slate-900 mb-4 border-b pb-2 flex items-center gap-2">
                        <i class="fa-solid fa-list-ul text-blue-600"></i> İçindekiler
                    </h4>
                    <nav id="toc" class="text-sm space-y-2 text-slate-600"></nav>
                </div>

                <div id="cta-widget" class="hidden bg-gradient-to-br from-indigo-600 to-blue-700 rounded-2xl shadow-lg p-6 text-white text-center relative overflow-hidden">
                    <div class="absolute top-0 right-0 p-4 opacity-10">
                        <i class="fa-solid fa-calculator text-9xl transform rotate-12 translate-x-4 -translate-y-4"></i>
                    </div>
                    <div class="relative z-10">
                        <h3 class="text-xl font-bold mb-2">Hemen Hesaplayın!</h3>
                        <p class="text-blue-100 text-sm mb-6">Bu konuyla ilgili hesaplamalarınızı ücretsiz aracımızla saniyeler içinde yapın.</p>
                        <a href="#" id="cta-link" class="inline-block w-full bg-white text-blue-700 font-bold py-3 px-6 rounded-xl shadow-md hover:bg-blue-50 transition transform hover:scale-105">
                            Araca Git <i class="fa-solid fa-arrow-right ml-2"></i>
                        </a>
                    </div>
                </div>
            </aside>
        </div>
    </div>

    <footer class="bg-slate-900 text-slate-400 py-12 mt-auto border-t border-slate-800">
        <div class="container mx-auto px-4 text-center">
            <span class="text-2xl font-bold text-white tracking-tight">Hesapla<span class="text-blue-500">Hadi</span></span>
            <div class="text-xs text-slate-600 mt-6">&copy; 2026 HesaplaHadi.</div>
        </div>
    </footer>

    <script src="../assets/js/blog-data.js"></script>
    <script>
        function loadPostData() {
            const post = getCurrentPost();
            if(!post) return;

            document.title = `${post.title} - HesaplaHadi Blog`;
            document.querySelector('meta[name="description"]').setAttribute("content", post.summary);
            let canonical = document.querySelector('link[rel="canonical"]');
            canonical.href = `https://hesaplahadi.com/blog/${post.slug}`;

            document.getElementById('crumb-title').innerText = post.title;
            document.getElementById('post-cat').innerText = post.category;
            document.getElementById('post-title').innerText = post.title;
            document.getElementById('post-summary').innerText = post.summary;

            const iconEl = document.getElementById('post-icon');
            iconEl.className = `fa-solid ${post.image} text-8xl text-${post.color}-300`;

            if(post.relatedTool) {
                const cta = document.getElementById('cta-widget');
                const btn = document.getElementById('cta-link');
                let link = `../index.html#btn-${post.relatedTool}`;
                const standaloneMap = {
                    'kdv': '../kdv-hesaplama.html',
                    'tevkifat': '../tevkifat-hesaplama.html',
                    'kidem': '../kidem-tazminati.html',
                    'kredi': '../kredi-hesaplama.html',
                    'ai_asistan': '../ai-asistan.html'
                };
                if(standaloneMap[post.relatedTool]) link = standaloneMap[post.relatedTool];
                btn.href = link;
                cta.classList.remove('hidden');
            }
        }

        function generateTOC() {
            const content = document.getElementById('content-body');
            const tocNav = document.getElementById('toc');
            const headers = content.querySelectorAll('h2, h3');
            if(headers.length === 0) {
                tocNav.parentElement.classList.add('hidden');
                return;
            }
            headers.forEach((header, index) => {
                if(!header.id) header.id = `section-${index}`;
                const link = document.createElement('a');
                link.href = `#${header.id}`;
                link.innerText = header.innerText;
                link.className = `block toc-link hover:text-blue-600 transition truncate ${header.tagName === 'H3' ? 'pl-4 text-xs' : ''}`;
                link.onclick = (e) => {
                    e.preventDefault();
                    document.getElementById(header.id).scrollIntoView({behavior: 'smooth'});
                };
                tocNav.appendChild(link);
            });
        }

        window.onload = function() {
            loadPostData();
            setTimeout(generateTOC, 100);
        };
    </script>
</body>
</html>
"""

# 3. Regenerate Files
for post in all_posts:
    filepath = f"blog/{post['slug']}"
    html = template
    html = html.replace('<title>Blog Detay - HesaplaHadi</title>', f"<title>{post['title']} - HesaplaHadi</title>")
    html = html.replace('content="HesaplaHadi Blog yazısı."', f'content="{post["summary"]}"')
    html = html.replace('href="https://hesaplahadi.com/blog/template.html"', f'href="https://hesaplahadi.com/blog/{post["slug"]}"')

    html = html.replace('<h1 id="post-title" class="text-3xl md:text-4xl lg:text-5xl font-extrabold text-slate-900 leading-tight mb-6">...</h1>',
                        f'<h1 id="post-title" class="text-3xl md:text-4xl lg:text-5xl font-extrabold text-slate-900 leading-tight mb-6">{post["title"]}</h1>')

    html = html.replace('<p id="post-summary" class="text-lg md:text-xl text-slate-600 leading-relaxed border-l-4 border-blue-500 pl-4">...</p>',
                        f'<p id="post-summary" class="text-lg md:text-xl text-slate-600 leading-relaxed border-l-4 border-blue-500 pl-4">{post["summary"]}</p>')

    html = html.replace('<div class="prose max-w-none" id="content-body">\n                       <p>İçerik yükleniyor...</p>\n                    </div>',
                        f'<div class="prose max-w-none" id="content-body">{post["content"]}</div>')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Generated {filepath}")
