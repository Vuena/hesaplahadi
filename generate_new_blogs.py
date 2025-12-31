
import os

new_posts = [
    {
        "slug": "doviz-yatirimi-mantikli-mi.html",
        "title": "Döviz Yatırımı Yapmak Mantıklı Mı? Riskler ve Fırsatlar",
        "summary": "Dolar ve Euro yatırımı yaparken dikkat edilmesi gerekenler. Döviz kurları neden dalgalanır?",
        "category": "Finans",
        "image": "fa-coins",
        "color": "green",
        "relatedTool": "mevduat",
        "content": """
            <p>Döviz yatırımı, Türkiye'de en popüler tasarruf yöntemlerinden biridir. Ancak her yatırım aracı gibi riskleri de barındırır.</p>
            <h2>Döviz Kurları Neden Değişir?</h2>
            <p>Faiz kararları, enflasyon oranları ve küresel ekonomik gelişmeler kurları doğrudan etkiler.</p>
            <h2>Sepet Yapmak</h2>
            <p>Tüm birikiminizi tek bir para biriminde tutmak yerine Dolar, Euro ve Altın gibi farklı araçlara bölmek riski azaltır.</p>
        """
    },
    {
        "slug": "kredi-karti-puanlari-nasil-kullanilir.html",
        "title": "Kredi Kartı Puanları En Verimli Nasıl Kullanılır?",
        "summary": "Bankaların verdiği chip-para, maxipuan ve bonusları nakit gibi kullanmanın yolları.",
        "category": "Finans",
        "image": "fa-credit-card",
        "color": "blue",
        "relatedTool": "kk_asgari",
        "content": """
            <p>Kredi kartı puanları, harcama yaparken kazandığınız sadakat ödülleridir. Bu puanların son kullanma tarihi olduğunu unutmayın.</p>
            <h2>Akaryakıt ve Market Alışverişleri</h2>
            <p>Puanları kullanmanın en pratik yolu, anlaşmalı market ve benzin istasyonlarında harcamaktır. Bazı sitelerde uçak bileti alımında katlı puan avantajı sağlanabilir.</p>
        """
    },
    {
        "slug": "bireysel-emeklilik-sistemi-bes-nedir.html",
        "title": "Bireysel Emeklilik Sistemi (BES) Nedir? Devlet Katkısı %30",
        "summary": "Geleceğiniz için birikim yapmanın devlet destekli yolu. BES avantajları ve çıkış şartları.",
        "category": "Finans",
        "image": "fa-piggy-bank",
        "color": "purple",
        "relatedTool": "mevduat",
        "content": """
            <p>BES, sosyal güvenlik sistemine ek olarak ikinci bir emeklilik geliri sağlamayı amaçlar.</p>
            <h2>Devlet Katkısı Avantajı</h2>
            <p>Yatırdığınız her 100 TL için devlet 30 TL katkı payı ekler. Bu %30'luk anında getiri, başka hiçbir risksiz yatırım aracında yoktur.</p>
        """
    },
    {
        "slug": "altin-yatirimi-fiziki-mi-banka-mi.html",
        "title": "Altın Yatırımı: Fiziki mi Yoksa Banka Hesabı mı?",
        "summary": "Gram altın alırken hangisi daha karlı? Makas aralıkları ve saklama maliyetleri.",
        "category": "Yatırım",
        "image": "fa-gem",
        "color": "amber",
        "relatedTool": "mevduat",
        "content": """
            <p>Geleneksel yatırım aracımız altın, güvenli liman olma özelliğini koruyor.</p>
            <h2>Fiziki Altın</h2>
            <p>Saklama riski vardır (hırsızlık vb.) ancak alım-satım makası genellikle kuyumcularda daha düşüktür.</p>
            <h2>Banka Altın Hesabı</h2>
            <p>Çalınma riski yoktur ve 7/24 işlem yapılabilir. Ancak bankaların alış-satış kurları arasındaki fark (makas) mesai saatleri dışında açılabilir.</p>
        """
    },
    {
        "slug": "intermittent-fasting-aralikli-oruc-nedir.html",
        "title": "Aralıklı Oruç (Intermittent Fasting) Nedir? Nasıl Yapılır?",
        "summary": "16/8 kuralı ile kilo verme yöntemi. Açlık penceresinde neler tüketilebilir?",
        "category": "Sağlık",
        "image": "fa-clock",
        "color": "indigo",
        "relatedTool": "ai_diyet",
        "content": """
            <p>Aralıklı oruç, ne yediğinizden çok ne zaman yediğinize odaklanan bir beslenme modelidir.</p>
            <h2>16/8 Metodu</h2>
            <p>Günün 16 saati aç kalıp (uyku dahil), yemek yemenin sadece 8 saatlik bir dilimde serbest olduğu yöntemdir. Genellikle 12:00-20:00 arası yemek yenir.</p>
        """
    },
    {
        "slug": "metabolizma-hizlandirma-yollari.html",
        "title": "Metabolizmayı Hızlandırmanın 10 Doğal Yolu",
        "summary": "Daha hızlı kilo vermek için metabolizma hızınızı artırın. Kahve, yeşil çay ve egzersiz.",
        "category": "Sağlık",
        "image": "fa-fire",
        "color": "red",
        "relatedTool": "bmr",
        "content": """
            <p>Metabolizma hızı, vücudun yaktığı kalori miktarını belirler.</p>
            <h2>Protein Tüketimi</h2>
            <p>Proteinlerin sindirimi için vücut daha fazla enerji harcar (Termik Etki). Bu da metabolizmayı %15-30 oranında hızlandırabilir.</p>
            <h2>Soğuk Su İçmek</h2>
            <p>Vücut suyu ısıtmak için enerji harcar. Günde 2 litre soğuk su içmek ekstra kalori yakımı sağlar.</p>
        """
    },
    {
        "slug": "ders-calisma-teknikleri-pomodoro.html",
        "title": "Verimli Ders Çalışma Tekniği: Pomodoro",
        "summary": "25 dakika çalışma, 5 dakika mola. Odaklanma sorunu yaşayanlar için en iyi yöntem.",
        "category": "Eğitim",
        "image": "fa-stopwatch",
        "color": "red",
        "relatedTool": "sinav",
        "content": """
            <p>Pomodoro tekniği, zamanı bloklara bölerek beynin odaklanma süresini maksimumda tutmayı hedefler.</p>
            <h2>Nasıl Uygulanır?</h2>
            <ol>
                <li>Hedefinizi belirleyin.</li>
                <li>Zamanlayıcıyı 25 dakikaya kurun ve sadece çalışın.</li>
                <li>Zil çalınca 5 dakika mola verin.</li>
                <li>Her 4 döngüde bir 15-30 dakika uzun mola verin.</li>
            </ol>
        """
    },
    {
        "slug": "hizli-okuma-teknikleri.html",
        "title": "Hızlı Okuma Teknikleri ile Anlama Oranını Artırın",
        "summary": "Dakikada okunan kelime sayısını artırma egzersizleri ve göz kaslarını geliştirme.",
        "category": "Eğitim",
        "image": "fa-book-open",
        "color": "blue",
        "relatedTool": "kelime",
        "content": """
            <p>Hızlı okuma, sadece hızlı gitmek değil, bütünü görmektir.</p>
            <h2>İç Seslendirmeyi Durdurun</h2>
            <p>Okurken kelimeleri içinizden seslendirmek (subvokalizasyon) hızınızı konuşma hızıyla sınırlar (150-200 kelime/dk). Gözlerinizle tarayarak okumayı öğrenmelisiniz.</p>
        """
    },
    {
        "slug": "evde-spor-yaparak-zayiflama.html",
        "title": "Spor Salonuna Gitmeden Evde Zayıflama Rehberi",
        "summary": "Ekipmansız yapılabilecek en etkili egzersizler. Plank, Squat ve Şınav.",
        "category": "Sağlık",
        "image": "fa-dumbbell",
        "color": "orange",
        "relatedTool": "bmi",
        "content": """
            <p>Kilo vermek için pahalı spor salonlarına ihtiyacınız yok.</p>
            <h2>HIIT Kardiyo</h2>
            <p>Yüksek yoğunluklu aralıklı antrenman (HIIT), kısa sürede maksimum kalori yakımı sağlar. 20 dakikalık bir HIIT, 1 saatlik yürüyüşten daha etkili olabilir.</p>
        """
    },
    {
        "slug": "kripto-para-vergilendirme.html",
        "title": "Türkiye'de Kripto Para Vergilendirmesi Var Mı?",
        "summary": "Bitcoin ve altcoin kazançları vergiye tabi mi? Yasal düzenlemelerde son durum.",
        "category": "Finans",
        "image": "fa-bitcoin",
        "color": "orange",
        "relatedTool": "karzarar",
        "content": """
            <p>Kripto varlıklar, son yılların en çok konuşulan yatırım araçlarıdır.</p>
            <h2>Mevcut Durum</h2>
            <p>Şu an için bireysel yatırımcıların alım-satım kazançlarına yönelik doğrudan bir gelir vergisi düzenlemesi netleşmemiştir. Ancak meclis gündemindeki yasa tasarısı ile işlem vergisi (binde oranlarda) getirilmesi planlanmaktadır.</p>
        """
    }
]

# 1. Update blog-data.js (Append logic)
import json

# Read existing JS content (it's not JSON, it's JS code)
# I'll append the new objects to the existing JS object structure string hackily or re-write it.
# Easier to re-write blog-data.js completely if I have the full list.
# I will define the FULL list here (previous 7 + original 2 + new 10) to be safe.

# Reconstructing previous posts from memory/context
existing_posts = [
    {
        "id": "kredi-notu",
        "slug": "kredi-notu-nasil-yukseltilir.html",
        "title": "Kredi Notu Nasıl Yükseltilir? En Etkili 5 Yöntem",
        "summary": "Bankalardan kredi veya kredi kartı alırken en önemli kriter olan kredi notunuzu yükseltmek için yapmanız gerekenler ve altın kurallar.",
        "category": "Finans",
        "image": "fa-chart-line",
        "color": "blue",
        "relatedTool": "kredi"
    },
    {
        "id": "tevkifat-nedir",
        "slug": "kdv-tevkifati-nedir-kimler-yapar.html",
        "title": "KDV Tevkifatı Nedir? Kimler Tevkifat Yapar?",
        "summary": "İşletmeler için tevkifatlı fatura kesim süreçleri, 2/10, 5/10 oranlarının anlamı ve dikkat edilmesi gereken noktalar.",
        "category": "Vergi",
        "image": "fa-receipt",
        "color": "emerald",
        "relatedTool": "tevkifat"
    },
    {
        "id": "enflasyon-nedir",
        "slug": "enflasyon-nedir-nasil-hesaplanir.html",
        "title": "Enflasyon Nedir? Bütçenizi Nasıl Etkiler?",
        "summary": "Enflasyonun alım gücüne etkisi, TÜFE ve ÜFE kavramları ve paranızı enflasyona karşı korumanın yolları.",
        "category": "Finans",
        "image": "fa-arrow-trend-up",
        "color": "red",
        "relatedTool": "mevduat"
    },
    {
        "id": "konut-kredisi",
        "slug": "konut-kredisi-cekerken-dikkat-edilmesi-gerekenler.html",
        "title": "Konut Kredisi Çekerken Dikkat Edilmesi Gerekenler",
        "summary": "Ev sahibi olma hayali kuranlar için faiz oranları, vade seçenekleri ve ek masraflar hakkında kapsamlı rehber.",
        "category": "Emlak",
        "image": "fa-house",
        "color": "orange",
        "relatedTool": "kredi"
    },
    {
        "id": "ideal-kilo",
        "slug": "ideal-kilo-nasil-hesaplanir-formulu-nedir.html",
        "title": "İdeal Kilo Nasıl Hesaplanır? Bilimsel Formüller",
        "summary": "Sağlıklı bir yaşam için ideal kilonuzu öğrenin. Boy, yaş ve cinsiyete göre hesaplama yöntemleri.",
        "category": "Sağlık",
        "image": "fa-weight-scale",
        "color": "green",
        "relatedTool": "idealkilo"
    },
    {
        "id": "brut-net",
        "slug": "brutten-nete-maas-hesaplama-rehberi.html",
        "title": "Brütten Nete Maaş Hesaplama Rehberi",
        "summary": "Maaşınızdan yapılan kesintiler nelerdir? SGK primi, gelir vergisi ve damga vergisi hesaplamanın mantığı.",
        "category": "Finans",
        "image": "fa-money-bill-wave",
        "color": "blue",
        "relatedTool": "brut_net"
    },
    {
        "id": "bmi-nedir",
        "slug": "vucut-kitle-indeksi-bmi-nedir.html",
        "title": "Vücut Kitle İndeksi (BMI) Nedir? Değerler Ne Anlama Gelir?",
        "summary": "Vücut kitle indeksinizi hesaplayarak obezite riskinizi öğrenin. Dünya Sağlık Örgütü standartlarına göre değerlerin analizi.",
        "category": "Sağlık",
        "image": "fa-person",
        "color": "green",
        "relatedTool": "bmi"
    },
    {
        "id": "yuzde-hesaplama",
        "slug": "yuzde-hesaplama-formulu-ve-ornekleri.html",
        "title": "Yüzde Hesaplama Formülü ve Günlük Hayatta Kullanımı",
        "summary": "Matematiksel yüzde hesaplamanın en basit yolları. İndirim, zam ve kar marjı hesaplamalarında pratik yöntemler.",
        "category": "Eğitim",
        "image": "fa-percent",
        "color": "purple",
        "relatedTool": "yuzde"
    },
    {
        "id": "su-tuketimi",
        "slug": "gunluk-su-tuketimi-ne-kadar-olmali.html",
        "title": "Günlük Su Tüketimi Ne Kadar Olmalı?",
        "summary": "Vücudunuzun ihtiyacı olan su miktarını hesaplayın. Yetersiz su tüketiminin zararları ve sağlıklı yaşam için öneriler.",
        "category": "Sağlık",
        "image": "fa-droplet",
        "color": "cyan",
        "relatedTool": "su"
    }
]

# Combine lists
full_list = existing_posts + new_posts

# Write blog-data.js
js_content = "const blogPosts = " + json.dumps(full_list, ensure_ascii=False, indent=4) + ";\n\n"
js_content += """function getCurrentPost() {
    const path = window.location.pathname;
    const filename = path.split('/').pop();
    return blogPosts.find(p => p.slug === filename);
}"""

with open('assets/js/blog-data.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

print("Updated blog-data.js")

# 2. Generate new HTML files
template_path = 'blog/template.html'
with open(template_path, 'r', encoding='utf-8') as f:
    template = f.read()

for post in new_posts:
    filepath = f"blog/{post['slug']}"
    html = template

    # Simple Replace Strategy (Same as before)
    html = html.replace('<title>Blog Detay - HesaplaHadi</title>', f"<title>{post['title']} - HesaplaHadi</title>")
    html = html.replace('content="HesaplaHadi Blog yazısı."', f'content="{post["summary"]}"')
    html = html.replace('href="https://hesaplahadi.com/blog/template.html"', f'href="https://hesaplahadi.com/blog/{post["slug"]}"')

    # Static Content Injection
    html = html.replace('<h1 id="post-title" class="text-3xl md:text-4xl lg:text-5xl font-extrabold text-slate-900 leading-tight mb-6">...</h1>',
                        f'<h1 id="post-title" class="text-3xl md:text-4xl lg:text-5xl font-extrabold text-slate-900 leading-tight mb-6">{post["title"]}</h1>')

    html = html.replace('<p id="post-summary" class="text-lg md:text-xl text-slate-600 leading-relaxed border-l-4 border-blue-500 pl-4">...</p>',
                        f'<p id="post-summary" class="text-lg md:text-xl text-slate-600 leading-relaxed border-l-4 border-blue-500 pl-4">{post["summary"]}</p>')

    html = html.replace('<div class="prose max-w-none" id="content-body">\n                       <!-- Content goes here -->\n                       <p>İçerik yükleniyor...</p>\n                    </div>',
                        f'<div class="prose max-w-none" id="content-body">{post["content"]}</div>')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Generated {filepath}")
