
import json
import os

# 20 New Topics
MORE_BLOG_TOPICS = [
    # Finance (2026 Focus)
    {
        "title": "2026 Gelir Vergisi Dilimleri ve Maaş Hesaplama",
        "slug": "2026-gelir-vergisi-dilimleri-ve-maas-etkisi.html",
        "keywords": "gelir vergisi 2026, maaş hesaplama, vergi dilimi",
        "intro": "2026 yılı itibarıyla güncellenen gelir vergisi tarifesi, net maaşları doğrudan etkiliyor. Hangi ayda bir üst dilime gireceğinizi ve maaşınızdaki kesintinin ne kadar olacağını önceden hesaplamak, bütçe planlamanız için kritik öneme sahip."
    },
    {
        "title": "Gümüş Yatırımı Kazandırır mı? 2026 Gümüş Tahminleri",
        "slug": "gumus-yatirimi-mantikli-mi-2026.html",
        "keywords": "gümüş hesaplama, gümüş fiyatları, emtia yatırımı",
        "intro": "Altının gölgesinde kalsa da 'fakirin altını' olarak bilinen gümüş, 2026 yılında endüstriyel talebin artmasıyla yeni bir ralli yapabilir. Gümüş gram fiyatı hesaplarken nelere dikkat etmelisiniz?"
    },
    {
        "title": "Esnek Hesap (KMH) Faizi Nasıl Hesaplanır?",
        "slug": "esnek-hesap-kmh-faizi-hesaplama-rehberi.html",
        "keywords": "esnek hesap faizi, kmh hesaplama, ek hesap maliyeti",
        "intro": "Acil nakit ihtiyaçlarında can simidi olan Kredili Mevduat Hesabı (KMH), kontrolsüz kullanıldığında yüksek faiz maliyeti çıkarabilir. Günlük işletilen faiz oranları ve vergi kesintileriyle borcunuzun nasıl büyüdüğünü öğrenin."
    },
    {
        "title": "Milli Piyango İkramiyesinden Ne Kadar Vergi Kesilir?",
        "slug": "milli-piyango-vergi-kesintisi-hesaplama.html",
        "keywords": "milli piyango vergi, iviv vergisi, ikramiye hesaplama",
        "intro": "Büyük ikramiye hayalleri kurarken, elinize geçecek net tutarı bilmekte fayda var. Veraset ve İntikal Vergisi (İVİV) kapsamında 2026 yılında ikramiyelerden yapılacak kesinti oranlarını ve istisna tutarlarını inceledik."
    },
    {
        "title": "Altılı Ganyan Birim Fiyatları ve Kupon Hesaplama",
        "slug": "altili-ganyan-birim-fiyat-ve-ikramiye-hesaplama.html",
        "keywords": "altılı ne verir, at yarışı hesaplama, tjk birim fiyat",
        "intro": "At yarışı tutkunları için kupon bedelini hesaplamak bazen karmaşık olabilir. Ayaklardaki at sayıları ve güncel birim fiyatlarla (2026 tarifesi) kuponunuzun maliyetini saniyeler içinde nasıl bulabilirsiniz?"
    },

    # Astrology
    {
        "title": "Ay Burcu Nedir? Duygusal Dünyanızı Keşfedin",
        "slug": "ay-burcu-nedir-ve-nasil-hesaplanir.html",
        "keywords": "ay burcu hesaplama, moon sign, astroloji",
        "intro": "Güneş burcunuz karakterinizi belirlerken, Ay burcunuz hislerinizi ve iç dünyanızı yönetir. 'Beni kimse anlamıyor' diyorsanız, belki de Ay burcunuzun özelliklerini göz ardı ediyorsunuzdur."
    },
    {
        "title": "Numeroloji ile İsim Analizi: Harflerin Gizli Gücü",
        "slug": "numeroloji-isim-analizi-ve-kader-sayisi.html",
        "keywords": "numeroloji hesaplama, isim analizi, kader sayısı",
        "intro": "İsminizdeki her harfin bir sayısal değeri ve enerjisi olduğunu biliyor muydunuz? Numeroloji hesaplamasıyla kader sayınızı bulun ve yaşam amacınıza dair ipuçlarını keşfedin."
    },
    {
        "title": "Solar Return (Güneş Dönüşü) Haritası Nedir?",
        "slug": "solar-return-gunes-donusu-haritasi-nedir.html",
        "keywords": "solar harita hesaplama, yıllık burç yorumu, astroloji",
        "intro": "Doğum gününüzden bir sonraki doğum gününüze kadar olan 1 yılı kapsayan Solar Return haritası, o yılın ana temasını belirler. 2026 yılında sizi nelerin beklediğini öğrenmek için solar haritanıza göz atın."
    },
    {
        "title": "Burç Uyumu Hesaplama: İlişkinizin Geleceği Var mı?",
        "slug": "burc-uyumu-ve-ask-hesaplama.html",
        "keywords": "burç hesaplama, ilişki uyumu, sinastri",
        "intro": "Aşk hayatınızda yıldızlar sizden yana mı? Hangi burçlar birbiriyle daha iyi anlaşır, hangileri zorlu bir sınav verir? Burç uyumu analiziyle ilişkinizin dinamiklerini çözün."
    },

    # Education
    {
        "title": "KPSS Önlisans Puanı Nasıl Hesaplanır? 2026 Beklentileri",
        "slug": "kpss-onlisans-puan-hesaplama-ve-net-dagilimi.html",
        "keywords": "kpss önlisans hesaplama, p93 puanı, memur atama",
        "intro": "Önlisans mezunları için memurluk kapısını aralayan KPSS'de her net altın değerinde. Genel Kültür ve Genel Yetenek testlerinin puan üzerindeki ağırlığı ve standart sapma etkisi hakkında bilmeniz gerekenler."
    },
    {
        "title": "Okul Başarısı ve Takdir Teşekkür Hesaplama Taktikleri",
        "slug": "takdir-tesekkur-almak-icin-kac-puan-gerekir.html",
        "keywords": "takdir teşekkür hesaplama, e-okul not, ortalama hesapla",
        "intro": "Dönem sonu yaklaşırken öğrencilerin en büyük heyecanı belge alıp alamayacaklarıdır. Hangi dersin ortalamaya etkisi daha fazla? Devamsızlık belge almanıza engel olur mu? Tüm detaylar burada."
    },
    {
        "title": "Akademik Teşvik Ödeneği Kimlere Verilir?",
        "slug": "akademik-tesvik-odenegi-hesaplama-ve-sartlari.html",
        "keywords": "akademik teşvik hesaplama, akademisyen maaşı, makale puanı",
        "intro": "Üniversitelerde görev yapan akademisyenlerin bilimsel faaliyetlerine göre aldıkları teşvik ödeneği, 2026 yılında güncellenen katsayılarla yeniden belirlendi. Puanınızı maksimize etmek için hangi yayınlara öncelik vermelisiniz?"
    },

    # Legal
    {
        "title": "Islah Harcı Nedir? Davalarda Ne Zaman Ödenir?",
        "slug": "islah-harci-hesaplama-ve-dava-sureci.html",
        "keywords": "ıslah harcı hesaplama, dava harçları, hukuk",
        "intro": "Dava değeri belirsiz alacak davalarında sıkça karşılaşılan 'ıslah' işlemi, ek bir harç ödemesi gerektirir. Islah harcının nasıl hesaplandığını ve süresinde ödenmemesinin sonuçlarını bir hukukçu gözüyle olmasa da pratik açıdan ele aldık."
    },
    {
        "title": "Denetimli Serbestlik ve İnfaz Hesaplama 2026",
        "slug": "denetimli-serbestlik-ve-yatar-hesaplama-2026.html",
        "keywords": "infaz hesaplama, cezaevi süresi, yatar hesapla",
        "intro": "Ceza hukukunda yapılan son düzenlemelerle infaz süreleri ve denetimli serbestlik koşulları değişti. Aldığınız cezanın ne kadarını kapalı, ne kadarını açık cezaevinde geçireceğinizi hesaplamanın yolları."
    },

    # Health & Lifestyle
    {
        "title": "Vücut Kitle İndeksi (BMI) Güvenilir mi?",
        "slug": "vucut-kitle-indeksi-bmi-gercegi.html",
        "keywords": "bmi hesaplama, ideal kilo, sağlık",
        "intro": "Kilo kontrolünde en sık kullanılan ölçüt olan BMI, kas kütlesi fazla olan sporcular için yanıltıcı olabilir mi? Sadece boy ve kiloya bakarak sağlık analizi yapmanın sınırlarını ve alternatif ölçüm yöntemlerini konuşuyoruz."
    },
    {
        "title": "Günlük Su İhtiyacı: Kilonuza Göre Kaç Litre İçmelisiniz?",
        "slug": "kilonuza-gore-gunluk-su-ihtiyaci-hesaplama.html",
        "keywords": "su ihtiyacı hesaplama, sağlık, hidrasyon",
        "intro": "Standart 'günde 2 litre' önerisi herkes için geçerli değildir. Kilonuz, aktivite düzeyiniz ve hava sıcaklığı su ihtiyacınızı belirler. Dehidrasyon yaşamamak için size özel su tüketim miktarını hesaplayın."
    },
    {
        "title": "Bazal Metabolizma Hızı (BMR) ve Kilo Verme İlişkisi",
        "slug": "bazal-metabolizma-hizi-bmr-ve-diyet.html",
        "keywords": "bmr hesaplama, kalori yakımı, diyet",
        "intro": "Hiçbir şey yapmadan, sadece uyuyarak kaç kalori yaktığınızı biliyor musunuz? Kilo vermek isteyenlerin önce kendi motor hacmini (BMR) bilmesi gerekir. İşte metabolizmanızı hızlandırmanın yolları."
    },
    {
        "title": "Muhabbet Kuşu Yaşı Hesaplama: Kuşunuz Genç mi Yaşlı mı?",
        "slug": "muhabbet-kusu-yasi-nasil-anlasilir.html",
        "keywords": "kuş yaşı hesaplama, evcil hayvan bakımı, kuş ömrü",
        "intro": "Minik dostunuzun gagasındaki renk değişimleri veya göz halkaları onun yaşı hakkında ipuçları verir. Kuşunuzun insan yılına göre yaşını hesaplayarak, ona uygun bakım ve beslenme programı uygulayabilirsiniz."
    },

    # Other / Utility
    {
        "title": "Kelime Sayacı ve SEO İçin İçerik Uzunluğu",
        "slug": "kelime-sayaci-ve-seo-uyumlu-makale-yazimi.html",
        "keywords": "kelime sayacı, karakter hesaplama, seo",
        "intro": "Dijital içerik üreticileri için metin uzunluğu, Google sıralamalarında önemli bir faktördür. İdeal bir blog yazısı kaç kelime olmalı? Anahtar kelime yoğunluğu nasıl ayarlanmalı? Araçlarımızla içeriklerinizi optimize edin."
    },
    {
        "title": "İnternet Hızı ve Dosya İndirme Süresi Hesaplama",
        "slug": "internet-hizi-ve-indirme-suresi-hesaplama.html",
        "keywords": "indirme süresi hesaplama, internet hızı, mbps",
        "intro": "10 GB'lık bir oyunun inmesi ne kadar sürer? Mbps ve MB/s arasındaki farkı anlamak, internet paketi seçerken doğru karar vermenizi sağlar. Hız testi sonuçlarınıza göre gerçek indirme sürenizi hesaplayın."
    }
]

TEMPLATE_BLOG = """<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="{intro}">
    <title>{title} | HesaplaHadi Blog</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <link href="../assets/css/style.css" rel="stylesheet">
</head>
<body class="bg-slate-50 font-sans text-slate-800">

    <!-- Header -->
    <header class="bg-white shadow-sm sticky top-0 z-50">
        <div class="container mx-auto px-4 py-4 flex justify-between items-center">
            <a href="../index.html" class="flex items-center gap-2 group">
                <div class="bg-blue-600 text-white p-2 rounded-lg group-hover:bg-blue-700 transition"><i class="fa-solid fa-calculator"></i></div>
                <span class="text-xl font-bold tracking-tight">Hesapla<span class="text-blue-600">Hadi</span></span>
            </a>
            <a href="../index.html" class="text-sm font-bold text-slate-600 hover:text-blue-600 transition">
                <i class="fa-solid fa-arrow-left mr-1"></i> Hesaplama Araçları
            </a>
        </div>
    </header>

    <!-- Content -->
    <main class="container mx-auto px-4 py-8 lg:py-12 max-w-4xl">
        <article class="bg-white rounded-3xl shadow-sm border border-slate-100 overflow-hidden">
            <div class="p-8 lg:p-12">
                <div class="flex items-center gap-3 text-xs font-bold text-blue-600 uppercase tracking-widest mb-4">
                    <span class="bg-blue-50 px-3 py-1 rounded-full">Blog</span>
                    <span class="text-slate-400">•</span>
                    <span>Rehber</span>
                </div>

                <h1 class="text-3xl lg:text-4xl font-black text-slate-900 mb-6 leading-tight">{title}</h1>

                <p class="text-lg text-slate-600 mb-8 leading-relaxed font-medium">{intro}</p>

                <div class="prose prose-slate prose-lg max-w-none">
                    <p>Günümüzde bilgiye ulaşmak kolay olsa da, doğru ve güncel veriyi analiz etmek her zamankinden daha önemli hale geldi. <strong>{keywords}</strong> konularında yaptığımız araştırmalar, kullanıcıların en çok merak ettiği noktaları aydınlatmayı amaçlıyor.</p>

                    <h3>Hesaplama Neden Önemli?</h3>
                    <p>Özellikle 2026 yılı gibi ekonomik ve yasal parametrelerin sıkça değiştiği dönemlerde, {title} gibi konuları manuel hesaplamak yanıltıcı olabilir. Sitemizdeki araçlar, en son resmi verilerle güncellenerek size hatasız sonuçlar sunar.</p>

                    <h3>Pratik İpuçları</h3>
                    <ul class="list-disc pl-5 space-y-2">
                        <li><strong>Güncellik:</strong> Kullandığınız hesaplama aracının 2026 verilerini içerdiğinden emin olun.</li>
                        <li><strong>Doğrulama:</strong> Kritik finansal kararlarınızda birden fazla kaynaktan teyit alın.</li>
                        <li><strong>Uzman Görüşü:</strong> Hesaplama sonuçları bir göstergedir, yasal veya tıbbi tavsiye yerine geçmez.</li>
                    </ul>

                    <h3>Detaylı Analiz</h3>
                    <p>Konunun uzmanları, {keywords} ile ilgili süreçlerde dikkatli olunması gerektiğini vurguluyor. Yapacağınız küçük bir hata, uzun vadede planlarınızı etkileyebilir. Bu nedenle HesaplaHadi üzerindeki ilgili aracı kullanarak simülasyonlar yapmanızı öneriyoruz.</p>

                    <div class="my-8 p-6 bg-indigo-50 rounded-2xl border border-indigo-100 flex flex-col md:flex-row items-center gap-6 text-center md:text-left">
                        <div class="bg-white p-4 rounded-full shadow-sm text-indigo-600 text-2xl"><i class="fa-solid fa-wand-magic-sparkles"></i></div>
                        <div>
                            <h4 class="font-bold text-indigo-900 text-lg mb-1">Kafanız mı Karıştı?</h4>
                            <p class="text-indigo-700 text-sm mb-0">Konuyla ilgili özel sorularınızı AI Asistanımıza sorun, size özel yanıtlar alın.</p>
                        </div>
                        <a href="../ai-asistan.html" class="whitespace-nowrap bg-indigo-600 text-white px-6 py-3 rounded-xl font-bold hover:bg-indigo-700 transition shadow-lg shadow-indigo-500/30">Asistana Sor</a>
                    </div>

                    <h3>Sonuç</h3>
                    <p>Bilgi güçtür. {title} konusundaki detaylara hakim olmak, hayatınızı kolaylaştırır ve daha doğru kararlar almanızı sağlar. Daha fazla rehber içerik için blogumuzu takip etmeye devam edin.</p>
                </div>
            </div>
        </article>
    </main>

    <footer class="bg-slate-900 text-slate-400 py-12 border-t border-slate-800 mt-12">
        <div class="container mx-auto px-4 text-center">
            <span class="text-2xl font-bold text-white tracking-tight">Hesapla<span class="text-blue-500">Hadi</span></span>
            <div class="flex justify-center flex-wrap gap-6 text-sm font-medium mt-6 text-slate-300">
                <a href="../index.html" class="hover:text-white transition">Ana Sayfa</a>
                <a href="../hakkimizda.html" class="hover:text-white transition">Hakkımızda</a>
                <a href="../gizlilik-politikasi.html" class="hover:text-white transition">Gizlilik Politikası</a>
                <a href="../iletisim.html" class="hover:text-white transition">İletişim</a>
                <a href="index.html" class="hover:text-white transition">Blog</a>
                <a href="../ai-asistan.html" class="hover:text-white transition">AI Asistan</a>
            </div>
            <div class="text-xs text-slate-600 mt-6">&copy; 2026 HesaplaHadi.</div>
        </div>
    </footer>
    <script src="../assets/js/calculator.js"></script>
</body>
</html>
"""

if not os.path.exists('blog'):
    os.makedirs('blog')

for post in MORE_BLOG_TOPICS:
    html = TEMPLATE_BLOG.format(
        title=post["title"],
        intro=post["intro"],
        keywords=post["keywords"]
    )
    filepath = os.path.join('blog', post["slug"])
    with open(filepath, 'w') as f:
        f.write(html)
    print(f"Created Extra Blog: {filepath}")
