import os
import re

# Blog Content Dictionary
blogs = {
    "blog/kdv-tevkifati-nedir-kimler-yapar.html": """
    <p class="lead">KDV tevkifatı, vergi güvenliğini sağlamak amacıyla Katma Değer Vergisi'nin (KDV) alıcı ve satıcı arasında bölüştürülerek ödenmesidir. Peki, kimler tevkifat yapmak zorundadır ve oranlar nasıl belirlenir?</p>

    <h2>KDV Tevkifatı Nedir?</h2>
    <p>Normal işleyişte, bir mal veya hizmet satıldığında KDV'nin tamamı satıcıya ödenir ve satıcı bu vergiyi devlete beyan eder. Ancak <strong>Tevkifatlı Fatura</strong> uygulamasında, KDV'nin belirlenen bir kısmı alıcı tarafından kesilerek (tevkif edilerek) doğrudan vergi dairesine ödenir. Satıcıya ise KDV'nin sadece kalan kısmı ödenir.</p>

    <h2>Kimler Tevkifat Yapar?</h2>
    <p>KDV tevkifatı yapma zorunluluğu bulunan kuruluşlar şunlardır:</p>
    <ul>
        <li>Genel bütçeye dahil daireler ve katma bütçeli idareler</li>
        <li>İl özel idareleri, belediyeler ve köyler</li>
        <li>Halka açık şirketler (Borsa İstanbul'da işlem görenler)</li>
        <li>Döner sermayeli kuruluşlar</li>
        <li>Bankalar, sigorta ve reasürans şirketleri</li>
        <li>Sendikalar ve vakıflar</li>
    </ul>

    <h2>Yaygın Tevkifat Oranları</h2>
    <p>Sektöre ve işin türüne göre oranlar değişmektedir:</p>
    <div class="overflow-x-auto my-4">
        <table class="w-full text-left border-collapse bg-white rounded-lg overflow-hidden shadow-sm border border-slate-200 text-sm">
            <thead class="bg-slate-100 text-slate-700">
                <tr>
                    <th class="p-3 border-b">Hizmet Türü</th>
                    <th class="p-3 border-b">Oran</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td class="p-3 border-b">Yapım İşleri</td>
                    <td class="p-3 border-b font-bold">4/10</td>
                </tr>
                <tr>
                    <td class="p-3 border-b">Temizlik, Çevre ve Bahçe Bakım</td>
                    <td class="p-3 border-b font-bold">9/10</td>
                </tr>
                <tr>
                    <td class="p-3 border-b">Servis Taşımacılığı</td>
                    <td class="p-3 border-b font-bold">5/10</td>
                </tr>
                <tr>
                    <td class="p-3 border-b">İşgücü Temin Hizmetleri</td>
                    <td class="p-3 border-b font-bold">9/10</td>
                </tr>
                <tr>
                    <td class="p-3 border-b">Yemek Servis Hizmetleri</td>
                    <td class="p-3 border-b font-bold">5/10</td>
                </tr>
            </tbody>
        </table>
    </div>

    <h2>Tevkifat Hesaplama Örneği</h2>
    <p>Bir temizlik şirketi, bir belediyeye 10.000 TL + KDV (%20) tutarında fatura kessin. Temizlik hizmetinde tevkifat oranı <strong>9/10</strong>'dur.</p>
    <ul>
        <li><strong>Mal Bedeli:</strong> 10.000 TL</li>
        <li><strong>Hesaplanan KDV (%20):</strong> 2.000 TL</li>
        <li><strong>Tevkifat Tutarı (9/10):</strong> 1.800 TL (Alıcı öder)</li>
        <li><strong>Beyan Edilecek KDV (1/10):</strong> 200 TL (Satıcıya ödenir)</li>
        <li><strong>Toplam Tahsilat:</strong> 10.200 TL</li>
    </ul>

    <p>Bu hesaplamaları manuel yapmak zor olabilir. Sitemizdeki <a href="../tevkifat-hesaplama.html" class="text-blue-600 font-bold hover:underline">Tevkifat Hesaplama Aracı</a> ile oranları seçerek saniyeler içinde doğru sonuca ulaşabilirsiniz.</p>
    """,

    "blog/yuzde-hesaplama-formulu-ve-ornekleri.html": """
    <p class="lead">Yüzde hesaplama, matematikten finansa, alışverişten istatistiğe kadar hayatın her alanında karşımıza çıkar. Peki, yüzde nasıl hesaplanır? En pratik formüller nelerdir?</p>

    <h2>Temel Yüzde Hesaplama Formülü</h2>
    <p>Bir sayının belirli bir yüzdesini bulmak için şu formül kullanılır:</p>
    <div class="bg-blue-50 p-4 rounded-lg border border-blue-100 text-center font-mono text-blue-800 font-bold my-4">
        (Sayı x Yüzde Oranı) / 100
    </div>
    <p><strong>Örnek:</strong> 200 TL'nin %30'u kaçtır?<br>
    <em>Hesaplama:</em> (200 x 30) / 100 = 6000 / 100 = <strong>60 TL</strong></p>

    <h2>Yüzde Artış ve Azalış Hesaplama</h2>
    <h3>1. Yüzde Arttırma (Zam Hesaplama)</h3>
    <p>Bir sayıyı belirli bir oranda artırmak için, sayının üzerine hesaplanan yüzdeyi eklersiniz. Pratik yol ise şudur: %20 artış için sayıyı <strong>1.20</strong> ile çarpmak.</p>
    <p><strong>Örnek:</strong> 1000 TL maaşa %25 zam gelirse:<br>
    1000 x 1.25 = 1.250 TL</p>

    <h3>2. Yüzde Azaltma (İndirim Hesaplama)</h3>
    <p>Bir malın fiyatından indirim yapmak için. Örneğin %10 indirim için sayıyı <strong>0.90</strong> ile çarpmak yeterlidir.</p>
    <p><strong>Örnek:</strong> 500 TL'lik bir üründe %10 indirim:<br>
    500 x 0.90 = 450 TL</p>

    <h2>Bir Sayı Diğerinin Yüzde Kaçıdır?</h2>
    <p>A sayısı B sayısının yüzde kaçıdır? Formül:</p>
    <div class="bg-blue-50 p-4 rounded-lg border border-blue-100 text-center font-mono text-blue-800 font-bold my-4">
        (A / B) x 100
    </div>
    <p><strong>Örnek:</strong> 50, 200'ün yüzde kaçıdır?<br>
    (50 / 200) x 100 = 0.25 x 100 = <strong>%25</strong></p>

    <h2>Pratik Hesaplama Aracı</h2>
    <p>Tüm bu işlemleri zihinden yapmak yerine, <a href="../yuzde-hesaplama-araci.html" class="text-blue-600 font-bold hover:underline">Yüzde Hesaplama Aracı</a>mızı kullanarak 5 farklı modda (artış, azalış, değişim oranı vb.) anında sonuç alabilirsiniz.</p>
    """,

    "blog/enflasyon-nedir-nasil-hesaplanir.html": """
    <p class="lead">Enflasyon, fiyatlar genel düzeyindeki sürekli artıştır. Paranın alım gücünün düşmesi anlamına gelir. Peki enflasyon sepeti nedir ve TÜFE nasıl hesaplanır?</p>

    <h2>Enflasyon Nedir?</h2>
    <p>Enflasyon, sadece tek bir ürünün fiyatının artması değil, ekonomideki mal ve hizmetlerin genel fiyat ortalamasının yükselmesidir. Yüksek enflasyon, aynı miktar para ile zamanla daha az ürün alınabilmesine neden olur.</p>

    <h2>Enflasyon Nasıl Hesaplanır? (TÜFE)</h2>
    <p>Türkiye'de enflasyon, Türkiye İstatistik Kurumu (TÜİK) tarafından hesaplanan <strong>Tüketici Fiyat Endeksi (TÜFE)</strong> ile ölçülür.</p>

    <h3>Enflasyon Sepeti Nedir?</h3>
    <p>TÜİK, ortalama bir hanehalkının harcamalarını temsil eden sanal bir "alışveriş sepeti" oluşturur. Bu sepette gıda, konut, ulaştırma, sağlık gibi ana harcama grupları bulunur. Her ay bu sepetteki ürünlerin fiyatları derlenir ve değişim hesaplanır.</p>

    <h2>Enflasyonun Etkileri</h2>
    <ul>
        <li><strong>Alım Gücü Düşer:</strong> Maaşınız aynı kalsa bile, fiyatlar arttığı için daha az ürün alırsınız.</li>
        <li><strong>Faiz Oranları:</strong> Merkez bankaları enflasyonu kontrol etmek için faiz oranlarını artırabilir.</li>
        <li><strong>Yatırım Kararları:</strong> Yüksek enflasyon ortamında nakitte kalmak kaybettirir, bu nedenle insanlar döviz, altın veya gayrimenkule yönelir.</li>
    </ul>

    <h2>Maaş Zamları ve Enflasyon</h2>
    <p>Genellikle maaş zamları, geçmiş 6 aylık enflasyon farkına göre belirlenir. Gelecekteki maaşınızı tahmin etmek için <a href="../maas-zam-orani-hesaplama.html" class="text-blue-600 font-bold hover:underline">Maaş Zam Oranı Hesaplama</a> aracımızı kullanabilirsiniz.</p>
    """,

    "blog/gunluk-su-tuketimi-ne-kadar-olmali.html": """
    <p class="lead">Su, insan vücudunun %60'ını oluşturur ve hayati fonksiyonların devamı için kritiktir. Peki günde kaç litre su içmelisiniz? İhtiyacınız kilonuza göre değişir mi?</p>

    <h2>Günlük Su İhtiyacı Nasıl Hesaplanır?</h2>
    <p>Genel bir kural olarak "günde 8 bardak" denilse de, aslında su ihtiyacı kişiseldir. Kilonuz, aktivite düzeyiniz ve hava sıcaklığı bu ihtiyacı değiştirir.</p>

    <h3>Basit Formül: Kilo x 0.033</h3>
    <p>Bilimsel olarak kabul gören en basit hesaplama yöntemi, kilonuzu 0.033 ile çarpmaktır.</p>
    <div class="bg-blue-50 p-4 rounded-lg border border-blue-100 text-center font-mono text-blue-800 font-bold my-4">
        Örnek: 70 kg bir birey için<br>
        70 x 0.033 = 2.31 Litre
    </div>

    <h2>Suyun Vücuda Faydaları</h2>
    <ul>
        <li><strong>Enerji Verir:</strong> Dehidrasyon yorgunluğun en büyük nedenidir.</li>
        <li><strong>Cildi Güzelleştirir:</strong> Yeterli su, cildin nem dengesini korur ve kırışıklıkları geciktirir.</li>
        <li><strong>Kilo Vermeye Yardımcıdır:</strong> Yemeklerden önce su içmek tokluk hissi yaratır ve metabolizmayı hızlandırır.</li>
        <li><strong>Böbrek Sağlığı:</strong> Toksinlerin atılması için böbreklerin suya ihtiyacı vardır.</li>
    </ul>

    <h2>Ne Zaman Su İçilmeli?</h2>
    <p>Susadığınızı hissettiğinizde zaten vücudunuz su kaybetmeye başlamış demektir. Bu nedenle susamayı beklemeden gün içine yayarak su içmelisiniz. Özellikle:</p>
    <ul>
        <li>Sabah uyanınca (Metabolizmayı başlatır)</li>
        <li>Yemeklerden 30 dakika önce</li>
        <li>Spor öncesi ve sonrası</li>
    </ul>

    <p>Kendi ihtiyacınızı tam olarak öğrenmek için <a href="../gunluk-su-i̇htiyaci-hesaplama.html" class="text-blue-600 font-bold hover:underline">Günlük Su İhtiyacı Hesaplama</a> aracımızı kullanın.</p>
    """,

    "blog/konut-kredisi-cekerken-dikkat-edilmesi-gerekenler.html": """
    <p class="lead">Ev sahibi olmak herkesin hayali. Ancak uzun vadeli bir borçlanma olan konut kredisini çekerken yapılan hatalar, bütçenizi yıllarca sarsabilir. İşte dikkat etmeniz gereken 5 altın kural.</p>

    <h2>1. Bütçenizi Doğru Analiz Edin</h2>
    <p>Kredi taksitlerinin aylık hane gelirinizin %40'ını geçmemesi önerilir. Eğer tüm maaşınızı krediye bağlarsanız, beklenmedik harcamalar karşısında zor durumda kalabilirsiniz.</p>

    <h2>2. Faiz Oranlarını Karşılaştırın</h2>
    <p>Küçük bir faiz farkı, 10 yıllık (120 ay) bir kredide on binlerce liralık fark yaratır. Bankaların sunduğu "masrafsız" gibi görünen ancak faizi yüksek tekliflere dikkat edin. Toplam geri ödeme tutarına odaklanın.</p>

    <h2>3. Vadeyi Doğru Belirleyin</h2>
    <p>Vade uzadıkça aylık taksit düşer ancak bankaya ödeyeceğiniz toplam faiz artar. Bütçenizi zorlamayacak en kısa vadeyi seçmek, uzun vadede tasarruf etmenizi sağlar.</p>

    <h2>4. Dosya Masrafı ve Sigortalar</h2>
    <p>Bankalar kredi verirken dosya masrafı, ekspertiz ücreti, DASK ve hayat sigortası gibi ek masraflar çıkarır. Hayat sigortasını dışarıdan daha uygun fiyata yaptırabileceğinizi unutmayın.</p>

    <h2>5. Erken Ödeme Cezasını Öğrenin</h2>
    <p>Konut kredilerinde, borcunuzu vadesinden önce kapatmak isterseniz banka sizden "Erken Ödeme Tazminatı" talep edebilir. Bu oran yasal olarak kalan anaparanın %2'sini geçemez.</p>

    <h3>Hesaplama Yapmadan Karar Vermeyin</h3>
    <p>Farklı faiz oranları ve vadelerle ne kadar ödeyeceğinizi görmek için <a href="../kredi-hesaplama.html" class="text-blue-600 font-bold hover:underline">Kredi Hesaplama Aracı</a>mızı kullanarak karşılaştırma yapın.</p>
    """
}

def update_blog_content():
    for filepath, content in blogs.items():
        if os.path.exists(filepath):
            with open(filepath, 'r', encoding='utf-8') as f:
                html = f.read()

            # Replace content inside <div class="prose max-w-none" id="content-body">...</div>
            # Regex match
            pattern = re.compile(r'(<div class="prose max-w-none" id="content-body">).*?(</div>)', re.DOTALL)

            if pattern.search(html):
                new_html = pattern.sub(f'\\1{content}\\2', html)
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_html)
                print(f"Updated content for {filepath}")
            else:
                print(f"Content container not found in {filepath}")
        else:
            print(f"File not found: {filepath}")

if __name__ == "__main__":
    update_blog_content()
