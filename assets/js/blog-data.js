
const blogPosts = [
    {
        id: "kredi-notu",
        slug: "kredi-notu-nasil-yukseltilir.html",
        title: "Kredi Notu Nasıl Yükseltilir? En Etkili 5 Yöntem",
        summary: "Bankalardan kredi veya kredi kartı alırken en önemli kriter olan kredi notunuzu yükseltmek için yapmanız gerekenler ve altın kurallar.",
        category: "Finans",
        image: "fa-chart-line",
        color: "blue",
        relatedTool: "kredi"
    },
    {
        id: "tevkifat-nedir",
        slug: "kdv-tevkifati-nedir-kimler-yapar.html",
        title: "KDV Tevkifatı Nedir? Kimler Tevkifat Yapar?",
        summary: "İşletmeler için tevkifatlı fatura kesim süreçleri, 2/10, 5/10 oranlarının anlamı ve dikkat edilmesi gereken noktalar.",
        category: "Vergi",
        image: "fa-receipt",
        color: "emerald",
        relatedTool: "tevkifat"
    },
    // New Posts
    {
        id: "enflasyon-nedir",
        slug: "enflasyon-nedir-nasil-hesaplanir.html",
        title: "Enflasyon Nedir? Bütçenizi Nasıl Etkiler?",
        summary: "Enflasyonun alım gücüne etkisi, TÜFE ve ÜFE kavramları ve paranızı enflasyona karşı korumanın yolları.",
        category: "Finans",
        image: "fa-arrow-trend-up",
        color: "red",
        relatedTool: "mevduat"
    },
    {
        id: "konut-kredisi",
        slug: "konut-kredisi-cekerken-dikkat-edilmesi-gerekenler.html",
        title: "Konut Kredisi Çekerken Dikkat Edilmesi Gerekenler",
        summary: "Ev sahibi olma hayali kuranlar için faiz oranları, vade seçenekleri ve ek masraflar hakkında kapsamlı rehber.",
        category: "Emlak",
        image: "fa-house",
        color: "orange",
        relatedTool: "kredi"
    },
    {
        id: "ideal-kilo",
        slug: "ideal-kilo-nasil-hesaplanir-formulu-nedir.html",
        title: "İdeal Kilo Nasıl Hesaplanır? Bilimsel Formüller",
        summary: "Sağlıklı bir yaşam için ideal kilonuzu öğrenin. Boy, yaş ve cinsiyete göre hesaplama yöntemleri.",
        category: "Sağlık",
        image: "fa-weight-scale",
        color: "green",
        relatedTool: "idealkilo"
    },
    {
        id: "brut-net",
        slug: "brutten-nete-maas-hesaplama-rehberi.html",
        title: "Brütten Nete Maaş Hesaplama Rehberi",
        summary: "Maaşınızdan yapılan kesintiler nelerdir? SGK primi, gelir vergisi ve damga vergisi hesaplamanın mantığı.",
        category: "Finans",
        image: "fa-money-bill-wave",
        color: "blue",
        relatedTool: "brut_net"
    },
    {
        id: "bmi-nedir",
        slug: "vucut-kitle-indeksi-bmi-nedir.html",
        title: "Vücut Kitle İndeksi (BMI) Nedir? Değerler Ne Anlama Gelir?",
        summary: "Vücut kitle indeksinizi hesaplayarak obezite riskinizi öğrenin. Dünya Sağlık Örgütü standartlarına göre değerlerin analizi.",
        category: "Sağlık",
        image: "fa-person",
        color: "green",
        relatedTool: "bmi"
    },
    {
        id: "yuzde-hesaplama",
        slug: "yuzde-hesaplama-formulu-ve-ornekleri.html",
        title: "Yüzde Hesaplama Formülü ve Günlük Hayatta Kullanımı",
        summary: "Matematiksel yüzde hesaplamanın en basit yolları. İndirim, zam ve kar marjı hesaplamalarında pratik yöntemler.",
        category: "Eğitim",
        image: "fa-percent",
        color: "purple",
        relatedTool: "yuzde"
    },
    {
        id: "su-tuketimi",
        slug: "gunluk-su-tuketimi-ne-kadar-olmali.html",
        title: "Günlük Su Tüketimi Ne Kadar Olmalı?",
        summary: "Vücudunuzun ihtiyacı olan su miktarını hesaplayın. Yetersiz su tüketiminin zararları ve sağlıklı yaşam için öneriler.",
        category: "Sağlık",
        image: "fa-droplet",
        color: "cyan",
        relatedTool: "su"
    }
];

function getCurrentPost() {
    const path = window.location.pathname;
    const filename = path.split('/').pop();
    return blogPosts.find(p => p.slug === filename);
}