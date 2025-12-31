const blogPosts = [
    {
        id: "kredi-notu",
        slug: "kredi-notu-nasil-yukseltilir.html",
        title: "Kredi Notu Nasıl Yükseltilir? En Etkili 5 Yöntem",
        summary: "Bankalardan kredi veya kredi kartı alırken en önemli kriter olan kredi notunuzu yükseltmek için yapmanız gerekenler ve altın kurallar.",
        category: "Finans",
        date: "24 Mayıs 2026",
        image: "fa-chart-line", // FontAwesome icon class or image URL
        color: "blue", // Theme color
        relatedTool: "kredi" // ID of the tool in calculator.js
    },
    {
        id: "tevkifat-nedir",
        slug: "kdv-tevkifati-nedir-kimler-yapar.html", // Example placeholder
        title: "KDV Tevkifatı Nedir? Kimler Tevkifat Yapar?",
        summary: "İşletmeler için tevkifatlı fatura kesim süreçleri, 2/10, 5/10 oranlarının anlamı ve dikkat edilmesi gereken noktalar.",
        category: "Vergi",
        date: "22 Mayıs 2026",
        image: "fa-receipt",
        color: "emerald",
        relatedTool: "tevkifat"
    },
    {
        id: "yapay-zeka-butce",
        slug: "#", // Placeholder
        title: "Yapay Zeka ile Bütçe Planlama",
        summary: "AI araçlarını kullanarak aylık bütçenizi nasıl daha verimli yönetebilirsiniz? Tasarruf etmenin modern yolları.",
        category: "Teknoloji",
        date: "20 Mayıs 2026",
        image: "fa-robot",
        color: "indigo",
        relatedTool: "ai_asistan"
    }
];

// Helper to find current post metadata based on filename
function getCurrentPost() {
    const path = window.location.pathname;
    const filename = path.split('/').pop();
    return blogPosts.find(p => p.slug === filename);
}