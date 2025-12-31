
import os

blog_posts = [
    {
        "slug": "enflasyon-nedir-nasil-hesaplanir.html",
        "title": "Enflasyon Nedir? Bütçenizi Nasıl Etkiler?",
        "summary": "Enflasyonun alım gücüne etkisi, TÜFE ve ÜFE kavramları ve paranızı enflasyona karşı korumanın yolları.",
        "content": """
            <p>Enflasyon, mal ve hizmetlerin fiyatlarının genel düzeyinde meydana gelen sürekli artıştır. Sadece belirli bir ürünün fiyatının artması enflasyon değildir; genel fiyat düzeyinin yükselmesi gerekir.</p>
            <h2>Enflasyon Türleri Nelerdir?</h2>
            <p>Ekonomide genellikle üç tür enflasyondan bahsedilir:</p>
            <ul>
                <li><strong>Talep Enflasyonu:</strong> Tüketim talebinin üretimden fazla olması durumunda ortaya çıkar.</li>
                <li><strong>Maliyet Enflasyonu:</strong> Üretim maliyetlerinin (enerji, hammadde vb.) artması sonucu fiyatlara yansımasıdır.</li>
                <li><strong>Beklenti Enflasyonu:</strong> Gelecekte fiyatların artacağı beklentisiyle bugünden yapılan zamlardır.</li>
            </ul>
            <h2>Paranızı Enflasyondan Nasıl Korursunuz?</h2>
            <p>Enflasyon dönemlerinde nakitte kalmak satın alma gücünüzü eritir. Yatırım araçları (altın, döviz, borsa veya mevduat) bu dönemde önem kazanır. Özellikle mevduat faizlerinin enflasyon oranına yakın veya üzerinde olması tasarruf sahipleri için kritiktir.</p>
            <h3>TÜFE ve ÜFE Nedir?</h3>
            <p>TÜFE (Tüketici Fiyat Endeksi), tüketicinin sepetindeki ürünlerin fiyat değişimini ölçerken, ÜFE (Üretici Fiyat Endeksi) üretim maliyetlerindeki değişimi gösterir.</p>
        """
    },
    {
        "slug": "konut-kredisi-cekerken-dikkat-edilmesi-gerekenler.html",
        "title": "Konut Kredisi Çekerken Dikkat Edilmesi Gerekenler",
        "summary": "Ev sahibi olma hayali kuranlar için faiz oranları, vade seçenekleri ve ek masraflar hakkında kapsamlı rehber.",
        "content": """
            <p>Konut kredisi, hayatımızda alacağımız en büyük finansal kararlardan biridir. Uzun vadeli bir borçlanma olduğu için detaylı planlama gerektirir.</p>
            <h2>1. Bütçenizi Doğru Belirleyin</h2>
            <p>Aylık kredi taksitinizin hane gelirinizin %40-50'sini geçmemesine özen gösterin. Aksi takdirde yaşam standartlarınız düşebilir ve ödeme güçlüğü çekebilirsiniz.</p>
            <h2>2. Dosya Masrafı ve Ekspertiz Ücreti</h2>
            <p>Kredi faiz oranının yanı sıra, bankaların talep ettiği dosya masrafları, ekspertiz ücreti ve sigorta bedellerini de toplam maliyete eklemeyi unutmayın. Yıllık Maliyet Oranı (YMO) karşılaştırması yapmak en doğrusudur.</p>
            <h2>3. Vade Seçimi</h2>
            <p>Vade uzadıkça aylık taksit düşer ancak bankaya ödeyeceğiniz toplam faiz artar. Bütçenizi zorlamayacak en kısa vadeyi seçmek, toplam geri ödemenizi minimize eder.</p>
            <h3>Erken Ödeme Cezası Var mı?</h3>
            <p>Konut kredilerinde, kredinin tamamını veya bir kısmını vadesinden önce ödemek isterseniz bankalar yasal olarak erken ödeme cezası (tazminatı) talep edebilir. Bu oran genellikle kalan anaparanın %1 veya %2'sidir.</p>
        """
    },
    {
        "slug": "ideal-kilo-nasil-hesaplanir-formulu-nedir.html",
        "title": "İdeal Kilo Nasıl Hesaplanır? Bilimsel Formüller",
        "summary": "Sağlıklı bir yaşam için ideal kilonuzu öğrenin. Boy, yaş ve cinsiyete göre hesaplama yöntemleri.",
        "content": """
            <p>İdeal kilo, kişinin sağlıklı bir yaşam sürdürebilmesi için boyuna ve cinsiyetine göre olması gereken ağırlıktır. Estetik kaygılardan ziyade sağlık açısından önemlidir.</p>
            <h2>Robinson Formülü</h2>
            <p>Erkekler ve kadınlar için farklı hesaplanan bu formül, 1983 yılında geliştirilmiştir.</p>
            <ul>
                <li><strong>Erkek:</strong> 52 kg + 1.9 kg (boyunuzun 152 cm üzerindeki her inç için)</li>
                <li><strong>Kadın:</strong> 49 kg + 1.7 kg (boyunuzun 152 cm üzerindeki her inç için)</li>
            </ul>
            <h2>Miller Formülü</h2>
            <p>Bir diğer yaygın formül ise Miller formülüdür. Bu formül de benzer şekilde boy uzunluğunu temel alır ancak katsayılar farklıdır.</p>
            <h2>İdeal Kilonun Önemi</h2>
            <p>İdeal kilonuzu korumak; kalp hastalıkları, diyabet ve eklem rahatsızlıkları riskini azaltır. Sitemizdeki hesaplama aracı bu formülleri kullanarak size en doğru sonucu verir.</p>
        """
    },
    {
        "slug": "brutten-nete-maas-hesaplama-rehberi.html",
        "title": "Brütten Nete Maaş Hesaplama Rehberi",
        "summary": "Maaşınızdan yapılan kesintiler nelerdir? SGK primi, gelir vergisi ve damga vergisi hesaplamanın mantığı.",
        "content": """
            <p>İş sözleşmelerinde genellikle brüt maaş üzerinden anlaşılır, ancak banka hesabınıza yatan tutar net maaştır. Aradaki fark, yasal kesintilerden kaynaklanır.</p>
            <h2>Kesintiler Nelerdir?</h2>
            <ul>
                <li><strong>SGK Primi (%14):</strong> Çalışanın sosyal güvenlik sistemine katkısıdır.</li>
                <li><strong>İşsizlik Sigortası Primi (%1):</strong> İşsiz kalınması durumunda fon oluşturur.</li>
                <li><strong>Gelir Vergisi (%15 - %40):</strong> Artan oranlı vergi dilimlerine göre hesaplanır. Yıl içinde geliriniz arttıkça vergi oranınız yükselebilir (Vergi Dilimi).</li>
                <li><strong>Damga Vergisi (%0.759):</strong> Maaş ödemesine ilişkin düzenlenen kağıtlar için alınır.</li>
            </ul>
            <h2>Vergi Dilimi Nedir?</h2>
            <p>Türkiye'de gelir vergisi sistemi artan oranlıdır. Yıl başından itibaren elde ettiğiniz kümülatif gelir belli sınırları aştığında, bir üst vergi dilimine girersiniz ve net maaşınız düşebilir. Bu nedenle Ocak ayındaki maaşınız ile Aralık ayındaki maaşınız farklı olabilir.</p>
        """
    },
    {
        "slug": "vucut-kitle-indeksi-bmi-nedir.html",
        "title": "Vücut Kitle İndeksi (BMI) Nedir? Değerler Ne Anlama Gelir?",
        "summary": "Vücut kitle indeksinizi hesaplayarak obezite riskinizi öğrenin. Dünya Sağlık Örgütü standartlarına göre değerlerin analizi.",
        "content": """
            <p>Vücut Kitle İndeksi (BMI), kilonuzun (kg) boyunuzun karesine (m²) bölünmesiyle elde edilen bir değerdir. Obezite sınıflandırmasında dünya genelinde kullanılan standart yöntemdir.</p>
            <h2>BMI Değerleri ve Anlamları</h2>
            <ul>
                <li><strong>0 - 18.4 (Zayıf):</strong> Boyunuza göre kilonuz yetersiz. Beslenme yetersizliği riski olabilir.</li>
                <li><strong>18.5 - 24.9 (Normal):</strong> İdeal kilonuzdasınız. Bu aralığı korumalısınız.</li>
                <li><strong>25.0 - 29.9 (Fazla Kilolu):</strong> İdeal kilonuzun üzerindesiniz. Egzersiz ve diyet önerilir.</li>
                <li><strong>30.0 ve üzeri (Obez):</strong> Sağlık riski taşıyorsunuz. Kalp, şeker ve tansiyon hastalıklarına yatkınlık artabilir.</li>
            </ul>
            <h2>BMI Yeterli mi?</h2>
            <p>BMI tek başına yeterli olmayabilir çünkü kas ve yağ oranını ayırt etmez. Sporcuların kas kütlesi fazla olduğu için BMI değeri yüksek çıkabilir ancak bu onların obez olduğu anlamına gelmez. Yine de genel nüfus için en pratik göstergedir.</p>
        """
    },
    {
        "slug": "yuzde-hesaplama-formulu-ve-ornekleri.html",
        "title": "Yüzde Hesaplama Formülü ve Günlük Hayatta Kullanımı",
        "summary": "Matematiksel yüzde hesaplamanın en basit yolları. İndirim, zam ve kar marjı hesaplamalarında pratik yöntemler.",
        "content": """
            <p>Yüzde hesaplama, bir bütünün 100 parçaya bölünmesi mantığına dayanır. Günlük hayatta mağaza indirimlerinden banka faizlerine kadar her yerde karşımıza çıkar.</p>
            <h2>Temel Formül</h2>
            <p>Bir sayının yüzdesini bulmak için: <code>(Sayı x Yüzde Oranı) / 100</code></p>
            <p>Örnek: 500 TL'nin %20'si -> 500 x 20 / 100 = 100 TL.</p>
            <h2>İndirim Hesaplama</h2>
            <p>Bir ürünün indirimli fiyatını bulmak için önce indirim miktarını bulup fiyattan çıkarabilir veya doğrudan kalan yüzde ile çarpabilirsiniz.</p>
            <p>Örnek: 100 TL'lik üründe %30 indirim varsa, ürün fiyatının %70'ini ödeyeceksiniz demektir (100 x 0.70 = 70 TL).</p>
            <h2>Yüzde Artış (Zam) Hesaplama</h2>
            <p>Maaş zammı gibi durumlarda: <code>Eski Maaş x (1 + Zam Oranı)</code></p>
            <p>Örnek: 10.000 TL maaşa %50 zam -> 10.000 x 1.50 = 15.000 TL.</p>
        """
    },
    {
        "slug": "gunluk-su-tuketimi-ne-kadar-olmali.html",
        "title": "Günlük Su Tüketimi Ne Kadar Olmalı?",
        "summary": "Vücudunuzun ihtiyacı olan su miktarını hesaplayın. Yetersiz su tüketiminin zararları ve sağlıklı yaşam için öneriler.",
        "content": """
            <p>Su, insan vücudunun %60'ını oluşturur ve hayati fonksiyonların devamlılığı için kritiktir. Peki günde kaç bardak su içmeliyiz?</p>
            <h2>Genel Kural: Kilo Başına 33ml</h2>
            <p>Uzmanlar genel olarak kilonuzun her bir kilogramı için yaklaşık 33 ml su içmenizi önerir. Örneğin 70 kg olan bir birey için: <code>70 x 0.033 = 2.31 Litre</code>.</p>
            <h2>Su İhtiyacını Artıran Faktörler</h2>
            <ul>
                <li><strong>Egzersiz:</strong> Spor yaparken terle kaybedilen sıvıyı yerine koymak için ekstra su içilmelidir.</li>
                <li><strong>Sıcak Hava:</strong> Yaz aylarında terleme arttığı için tüketim artırılmalıdır.</li>
                <li><strong>Hastalık:</strong> Ateş, kusma veya ishal gibi durumlarda vücut sıvı kaybeder.</li>
            </ul>
            <h2>Susuzluğun Belirtileri</h2>
            <p>Baş ağrısı, yorgunluk, odaklanma sorunu ve idrar renginin koyulaşması yetersiz su tüketiminin en belirgin işaretleridir. Susamayı beklemeden düzenli aralıklarla su içmek en doğrusudur.</p>
        """
    }
]

template_path = 'blog/template.html'
with open(template_path, 'r', encoding='utf-8') as f:
    template = f.read()

for post in blog_posts:
    filepath = f"blog/{post['slug']}"
    html = template
    # Replace content placeholder is implied, but looking at template.html, content is inside <div id="content-body">...</div>
    # The template has placeholder text. We should use regex or simple string replace if markers existed,
    # but the template currently has ` <p>İçerik yükleniyor...</p>`.

    # We will inject the content directly into the template string before writing.
    # Note: The template relies on JS to populate title/meta.
    # BUT for SEO, we want static content.
    # The prompt asked for static structure. The previous task updated JS.
    # To make it truly SEO friendly, we should replace the placeholders in HTML with actual data.

    html = html.replace('<title>Blog Detay - HesaplaHadi</title>', f"<title>{post['title']} - HesaplaHadi</title>")
    html = html.replace('content="HesaplaHadi Blog yazısı."', f'content="{post["summary"]}"')
    html = html.replace('href="https://hesaplahadi.com/blog/template.html"', f'href="https://hesaplahadi.com/blog/{post["slug"]}"')

    # Static Content Injection for Crawlers (Replacing the JS fallback placeholders)
    html = html.replace('<h1 id="post-title" class="text-3xl md:text-4xl lg:text-5xl font-extrabold text-slate-900 leading-tight mb-6">...</h1>',
                        f'<h1 id="post-title" class="text-3xl md:text-4xl lg:text-5xl font-extrabold text-slate-900 leading-tight mb-6">{post["title"]}</h1>')

    html = html.replace('<p id="post-summary" class="text-lg md:text-xl text-slate-600 leading-relaxed border-l-4 border-blue-500 pl-4">...</p>',
                        f'<p id="post-summary" class="text-lg md:text-xl text-slate-600 leading-relaxed border-l-4 border-blue-500 pl-4">{post["summary"]}</p>')

    html = html.replace('<div class="prose max-w-none" id="content-body">\n                       <!-- Content goes here -->\n                       <p>İçerik yükleniyor...</p>\n                    </div>',
                        f'<div class="prose max-w-none" id="content-body">{post["content"]}</div>')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Generated {filepath}")
