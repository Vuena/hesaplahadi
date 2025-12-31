const blogPosts = [
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
];

function getCurrentPost() {
    const path = window.location.pathname;
    const filename = path.split('/').pop();
    return blogPosts.find(p => p.slug === filename);
}