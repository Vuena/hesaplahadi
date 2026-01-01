
import os

BLOG_TEMPLATE = """<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="{desc}">
    <title>{title} | HesaplaHadi Blog</title>
    <link rel="canonical" href="https://hesaplahadi.com/blog/{filename}">
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <link href="../assets/css/style.css" rel="stylesheet">
</head>
<body class="flex flex-col min-h-screen text-slate-800 bg-slate-50">

    <!-- Header -->
    <header class="bg-white/90 backdrop-blur-md shadow-sm sticky top-0 z-50 border-b border-slate-100">
        <div class="container mx-auto px-4 py-3 flex justify-between items-center">
            <a href="../index.html" class="flex items-center space-x-2 group">
                <div class="flex items-center justify-center bg-gradient-to-br from-blue-600 to-indigo-700 text-white p-2.5 rounded-xl group-hover:shadow-lg group-hover:shadow-blue-500/30 transition duration-300 flex-shrink-0">
                    <i class="fa-solid fa-calculator text-lg"></i>
                </div>
                <div class="leading-tight">
                    <h1 class="text-xl md:text-2xl font-extrabold tracking-tight text-slate-900">Hesapla<span class="text-blue-600">Hadi</span></h1>
                </div>
            </a>
            <a href="../index.html" class="text-sm font-bold text-slate-600 hover:text-blue-600 transition">Hesaplama Araçları</a>
        </div>
    </header>

    <!-- Content -->
    <main class="container mx-auto px-4 py-8 max-w-4xl">
        <article class="bg-white rounded-2xl shadow-sm border border-slate-200 p-8 md:p-12">
            <h1 class="text-3xl md:text-4xl font-black text-slate-900 mb-6 leading-tight">{title}</h1>

            <div class="prose prose-slate max-w-none text-slate-600 leading-relaxed">
                <p class="text-lg font-medium text-slate-800 mb-6">{intro}</p>

                {body}

                <div class="mt-8 p-6 bg-blue-50 rounded-xl border border-blue-100">
                    <h3 class="font-bold text-blue-900 mb-2">Hemen Hesaplayın</h3>
                    <p class="text-sm text-blue-800 mb-4">Bu konuyla ilgili hesaplamalarınızı yapmak için aracımızı kullanın.</p>
                    <a href="../index.html" class="inline-flex items-center gap-2 bg-blue-600 hover:bg-blue-700 text-white px-6 py-3 rounded-xl font-bold transition shadow-lg shadow-blue-500/20">
                        <i class="fa-solid fa-calculator"></i> Hesaplama Araçlarına Git
                    </a>
                </div>
            </div>
        </article>
    </main>

    <!-- Footer -->
    <footer class="bg-slate-900 text-slate-400 py-12 mt-auto border-t border-slate-800">
        <div class="container mx-auto px-4 text-center">
            <div class="text-xs text-slate-600">&copy; 2026 HesaplaHadi.</div>
        </div>
    </footer>

</body>
</html>
"""

BLOG_POSTS = [
    {
        "filename": "2026-asgari-ucret-tahminleri.html",
        "title": "2026 Asgari Ücret Tahminleri ve Olası Senaryolar",
        "desc": "2026 yılı asgari ücret beklentileri, enflasyon hedefleri ve ekonomik göstergelere göre maaş artış senaryoları.",
        "intro": "Milyonlarca çalışanın merakla beklediği 2026 asgari ücret zammı için geri sayım başladı. Enflasyon verileri ve hükümetin orta vadeli program hedefleri doğrultusunda masada hangi rakamlar var?",
        "body": """
        <h3>Enflasyon ve Refah Payı Etkisi</h3>
        <p>2026 yılı için belirlenecek asgari ücrette en belirleyici faktör şüphesiz enflasyon oranları olacak. Merkez Bankası'nın yıl sonu enflasyon tahminleri ve piyasa beklentileri, yapılacak zammın alt sınırını belirliyor. Uzmanlar, %25 ile %35 arasında bir artışın makul olabileceğini öngörüyor. Ancak refah payı eklemesiyle bu oranın daha da yukarı çıkması muhtemel.</p>

        <h3>Net Asgari Ücret Ne Kadar Olacak?</h3>
        <p>Mevcut ekonomik koşullar göz önüne alındığında, net asgari ücretin 25.000 TL bandını zorlaması bekleniyor. İşveren maliyetleri ve istihdamın korunması dengesi gözetilerek yapılacak pazarlıklarda, Türk-İş ve TİSK'in talepleri belirleyici olacak. Özellikle büyükşehirlerdeki yaşam maliyeti artışı, bölgesel asgari ücret tartışmalarını da yeniden gündeme getirebilir.</p>

        <h3>Satın Alma Gücü ve Gelecek Beklentileri</h3>
        <p>Sadece rakamsal artış değil, asgari ücretin alım gücünün korunması da büyük önem taşıyor. 2026 yılında beklenen dezenflasyon süreciyle birlikte, yapılacak zammın yıl içinde erimemesi hedefleniyor. Çalışanların temel ihtiyaçlarını karşılayabilmesi için gıda ve kira enflasyonunun seyri yakından takip edilecek.</p>
        """
    },
    {
        "filename": "2026-memur-ve-emekli-zammi.html",
        "title": "2026 Ocak Memur ve Emekli Zammı Ne Kadar Olacak?",
        "desc": "Memur ve emekliler için 2026 Ocak ayı zam oranları, toplu sözleşme ve enflasyon farkı hesaplamaları.",
        "intro": "2026 yılına girerken memur ve emeklilerin gözü kulağı Ocak ayı zammında. Toplu sözleşme gereği yapılacak artışlara eklenecek enflasyon farkı ile birlikte maaşlar ne kadar yükselecek?",
        "body": """
        <h3>Toplu Sözleşme ve Enflasyon Farkı</h3>
        <p>Memur maaş zammı hesaplanırken, öncelikle toplu sözleşmede belirlenen oran (%6) dikkate alınıyor. Bunun üzerine, 2025 yılının ikinci yarısında gerçekleşen enflasyonun, bir önceki dönem verilen zammı aşan kısmı 'enflasyon farkı' olarak ekleniyor. Şu anki projeksiyonlara göre, toplam zammın %10-15 bandında olması bekleniyor.</p>

        <h3>En Düşük Memur Maaşı</h3>
        <p>Yapılacak artışla birlikte en düşük memur maaşının önemli bir eşiği aşması öngörülüyor. Aile yardımı, çocuk yardımı gibi ek ödemelerin de katsayı artışıyla yükselmesi, memur bütçesine olumlu yansıyacak. Özellikle büyükşehirlerde görev yapan memurlar için kira yardımı gibi ek düzenlemelerin yapılıp yapılmayacağı da merak konusu.</p>

        <h3>Emekliler İçin Beklentiler</h3>
        <p>SSK ve Bağ-Kur emeklileri için durum doğrudan 6 aylık enflasyon oranına bağlı. Kök maaş düzenlemesi ve en düşük emekli aylığının artırılması gibi formüller de masada. Emeklilerin alım gücünü korumak adına seyyanen bir artış yapılıp yapılmayacağı, Ocak ayı başında netleşecek en kritik konulardan biri.</p>
        """
    },
    {
        "filename": "2026-altin-piyasasi-yorum.html",
        "title": "2026 Altın Fiyatları: Yatırımcıları Neler Bekliyor?",
        "desc": "2026 yılında gram altın ve ons altın fiyat tahminleri, uzman yorumları ve yatırım stratejileri.",
        "intro": "Güvenli liman altın, 2026 yılında da yatırımcıların radarında. Küresel faiz politikaları, jeopolitik riskler ve merkez bankalarının alımları altın fiyatlarını nasıl etkileyecek?",
        "body": """
        <h3>FED Faiz Kararları ve Ons Altın</h3>
        <p>ABD Merkez Bankası (FED) faiz indirim döngüsüne devam ederse, dolar endeksindeki zayıflama ons altına yarayabilir. Uzmanlar, ons altının 2026 yılında yeni rekorlar deneyebileceğini belirtiyor. Düşük faiz ortamı, getirisi olmayan emtialara olan talebi genellikle artırır.</p>

        <h3>Gram Altın ve Dolar/TL Etkisi</h3>
        <p>İç piyasada gram altın fiyatı, hem ons altına hem de Dolar/TL kuruna bağlı. Dolar kurundaki kontrollü yükseliş ve ons altındaki değerlenme, gram altını 2026 yılında da cazip bir yatırım aracı yapmaya devam edebilir. Özellikle uzun vadeli düşünen tasarruf sahipleri için altın, enflasyona karşı koruma kalkanı işlevini sürdürüyor.</p>

        <h3>Yatırım Stratejileri</h3>
        <p>2026 portföylerinde altına yer vermek, risk dağılımı açısından mantıklı görünüyor. Fiziksel altın, altın fonları veya banka altın hesapları üzerinden yatırım yapılabilir. Ancak, kısa vadeli dalgalanmalardan ziyade orta ve uzun vadeli trendlere odaklanmak, yatırımcılar için daha sağlıklı sonuçlar doğuracaktır.</p>
        """
    },
    {
        "filename": "yks-2026-hazirlik-rehberi.html",
        "title": "YKS 2026 Hazırlık Rehberi ve Puan Hesaplama Taktikleri",
        "desc": "2026 YKS sınavına hazırlananlar için çalışma programı, net hesaplama yöntemleri ve motivasyon ipuçları.",
        "intro": "Üniversite hayali kuran milyonlarca genç için YKS 2026 maratonu başlıyor. Sistemli çalışma, doğru kaynak seçimi ve stratejik net hesaplamalarıyla hedeflerinize nasıl ulaşırsınız?",
        "body": """
        <h3>TYT ve AYT Dengesi</h3>
        <p>Sınav başarısının anahtarı, TYT (Temel Yeterlilik Testi) ve AYT (Alan Yeterlilik Testi) çalışmalarını dengeli yürütmekten geçiyor. TYT'de hız ve pratik, AYT'de ise derinlemesine bilgi ve yorum gücü ön plana çıkıyor. Çalışma programınızı oluştururken, eksik olduğunuz konulara ağırlık vermeli ancak güçlü yönlerinizi de pekiştirmeyi ihmal etmemelisiniz.</p>

        <h3>Puan ve Sıralama Hesaplama</h3>
        <p>Deneme sınavlarından sonra netlerinizi doğru analiz etmek, gelişiminizi görmek açısından kritiktir. Sitemizdeki YKS Puan Hesaplama aracını kullanarak, farklı net senaryolarına göre tahmini sıralamanızı görebilirsiniz. Unutmayın, ÖSYM'nin standart sapma hesaplamaları her yıl sınavın zorluğuna göre değişebilir, bu yüzden hedefinizi her zaman yüksek tutun.</p>

        <h3>Motivasyon ve Süreklilik</h3>
        <p>Uzun soluklu bir süreç olan sınav hazırlığında motivasyonu korumak zordur. Küçük hedefler koymak, düzenli mola vermek ve uyku düzenine dikkat etmek başarınızı artırır. "Yapabilirim" inancını kaybetmeden, disiplinli bir şekilde çalışmaya devam edin. 2026 yılı sizin yılınız olabilir!</p>
        """
    },
    {
        "filename": "2026-mtv-oranlari.html",
        "title": "2026 MTV Oranları ve Araç Sahiplerine Maliyeti",
        "desc": "2026 yılı Motorlu Taşıtlar Vergisi (MTV) zammı, araç gruplerine göre vergi tutarları ve ödeme takvimi.",
        "intro": "Araç sahipleri için her yılın başında gündeme gelen en önemli konulardan biri Motorlu Taşıtlar Vergisi (MTV). 2026 yılında yeniden değerleme oranıyla birlikte MTV tutarları ne kadar artacak?",
        "body": """
        <h3>Yeniden Değerleme Oranı ve Zam Beklentisi</h3>
        <p>MTV artış oranı, her yıl Ekim ayında açıklanan Üretici Fiyat Endeksi'ne (ÜFE) göre belirlenen Yeniden Değerleme Oranı ile netleşir. Ancak Cumhurbaşkanı'nın bu oranı düşürme veya artırma yetkisi bulunmaktadır. 2026 yılı için enflasyon beklentileri ışığında, MTV zammının %40-%50 bandında olabileceği konuşuluyor.</p>

        <h3>Elektrikli Araçlarda MTV</h3>
        <p>Çevreci dönüşümle birlikte elektrikli araçların (TOGG dahil) MTV oranları da merak konusu. Elektrikli araçlar için uygulanan indirimli MTV tarifesi 2026'da da devam edecek mi? Genellikle elektrikli araçların vergisi, eş değer içten yanmalı motorlu araçların vergisinin dörtte biri oranında uygulanmaktadır.</p>

        <h3>Ödeme Takvimi</h3>
        <p>2026 yılı MTV ödemeleri, geçmiş yıllarda olduğu gibi Ocak ve Temmuz aylarında iki eşit taksit halinde yapılacak. Ödemelerinizi GİB (Gelir İdaresi Başkanlığı) üzerinden, banka şubelerinden veya mobil bankacılık uygulamalarından gerçekleştirebilirsiniz. Gecikme faiziyle karşılaşmamak için tarihleri not etmeyi unutmayın.</p>
        """
    }
]

def create_blogs():
    if not os.path.exists('blog'):
        os.makedirs('blog')

    for post in BLOG_POSTS:
        content = BLOG_TEMPLATE.format(
            title=post['title'],
            desc=post['desc'],
            intro=post['intro'],
            body=post['body'],
            filename=post['filename']
        )
        filepath = os.path.join('blog', post['filename'])
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Created blog: {filepath}")

if __name__ == '__main__':
    create_blogs()
