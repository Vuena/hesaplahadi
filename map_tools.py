import os

# --- 1. Mapping: Requested Name -> Filename & Title ---
TOOLS_MAP = [
    # Existing to Update
    {"filename": "kidem-tazminati.html", "new_filename": "kidem-tazminati-hesaplama.html", "title": "Kıdem Tazminatı Hesaplama 2026", "keywords": ["tazminat hesaplama", "kıdem tazminatı tavan"], "category": "finance"},
    {"filename": "brutten-nete-maas-hesaplama-2026.html", "title": "Brütten Nete Maaş Hesaplama 2026", "keywords": ["net hesaplama", "asgari ücret hesaplama"], "category": "finance"},
    {"filename": "maas-zam-orani-hesaplama.html", "title": "Maaş Zam Oranı Hesaplama 2026", "keywords": ["maas yüzde hesaplama", "memur maaş zammı hesaplama", "zam oranı hesaplama"], "category": "finance"},
    {"filename": "universite-not-ortalamasi-vize-final-hesaplama.html", "title": "Üniversite Not Ortalaması Hesaplama", "keywords": ["vize final hesaplama", "ortalama hesaplama"], "category": "education"},
    {"filename": "i̇ki-tarih-arasi-gun-sayaci.html", "title": "İki Tarih Arası Gün Sayacı", "keywords": ["tarih hesaplama"], "category": "utility"},
    {"filename": "takdir-tesekkur-hesaplama-e-okul.html", "title": "Takdir Teşekkür Hesaplama 2026", "keywords": ["okul puan hesaplama"], "category": "education"},
    {"filename": "mevduat-faizi-hesaplama.html", "title": "Mevduat Faizi Hesaplama 2026", "keywords": ["faiz hesaplama"], "category": "finance"},
    {"filename": "yakit-tuketimi-hesaplama.html", "title": "Yakıt Tüketimi Hesaplama 2026", "keywords": ["yakıt hesaplama"], "category": "vehicle"},

    # New to Create - Astrology
    {"filename": "yukselen-burc-hesaplama.html", "title": "Yükselen Burç Hesaplama", "keywords": ["yükselen burcu hesaplama", "astroloji"], "category": "astrology", "input_type": "birth_time"},
    {"filename": "burc-hesaplama.html", "title": "Burç Hesaplama", "keywords": ["burç bulma", "hangi burç"], "category": "astrology", "input_type": "date"},
    {"filename": "ay-burcu-hesaplama.html", "title": "Ay Burcu Hesaplama", "keywords": ["ay burcu", "moon sign"], "category": "astrology", "input_type": "birth_time"},
    {"filename": "dogum-haritasi-hesaplama.html", "title": "Doğum Haritası Hesaplama", "keywords": ["doğum haritası", "natal harita"], "category": "astrology", "input_type": "birth_time"},
    {"filename": "cin-takvimi-cinsiyet-hesaplama.html", "title": "Çin Takvimi Cinsiyet Hesaplama", "keywords": ["çin takvimi", "cinsiyet hesaplama"], "category": "astrology", "input_type": "date_age"},
    {"filename": "numeroloji-hesaplama.html", "title": "Numeroloji Hesaplama", "keywords": ["isim analizi", "numeroloji"], "category": "astrology", "input_type": "text"},
    {"filename": "solar-harita-hesaplama.html", "title": "Solar Harita Hesaplama", "keywords": ["solar return", "güneş dönüşü"], "category": "astrology", "input_type": "birth_time"},

    # New to Create - Finance/Currency (User Input)
    {"filename": "altin-hesaplama.html", "title": "Altın Hesaplama", "keywords": ["gram altın", "çeyrek altın"], "category": "finance", "input_type": "currency"},
    {"filename": "gumus-hesaplama.html", "title": "Gümüş Hesaplama", "keywords": ["gümüş fiyatı", "gümüş gram"], "category": "finance", "input_type": "currency"},
    {"filename": "dolar-hesaplama.html", "title": "Dolar Hesaplama", "keywords": ["dolar tl", "kur hesaplama"], "category": "finance", "input_type": "currency"},
    {"filename": "euro-hesaplama.html", "title": "Euro Hesaplama", "keywords": ["euro tl", "döviz hesaplama"], "category": "finance", "input_type": "currency"},
    {"filename": "dolar-enflasyonu-hesaplama.html", "title": "Dolar Enflasyonu Hesaplama", "keywords": ["dolar değer kaybı", "enflasyon"], "category": "finance", "input_type": "inflation"},
    {"filename": "esnek-hesap-faiz-hesaplama.html", "title": "Esnek Hesap Faiz Hesaplama", "keywords": ["kmh faizi", "ek hesap"], "category": "finance", "input_type": "interest"},
    {"filename": "deger-artis-kazanci-hesaplama.html", "title": "Değer Artış Kazancı Hesaplama", "keywords": ["gayrimenkul vergi", "değer artış"], "category": "finance", "input_type": "real_estate"},
    {"filename": "milli-piyango-hesaplama.html", "title": "Milli Piyango Vergisi Hesaplama", "keywords": ["piyango vergi", "ikramiye kesinti"], "category": "finance", "input_type": "tax"},
    {"filename": "altili-ne-verir-hesaplama.html", "title": "Altılı Ne Verir Hesaplama", "keywords": ["at yarışı", "altılı ganyan", "tjk"], "category": "gaming", "input_type": "betting"},

    # New to Create - Vehicle/Tax
    {"filename": "mtv-hesaplama-2026.html", "title": "MTV Hesaplama 2026", "keywords": ["motorlu taşıtlar vergisi", "araç vergisi"], "category": "vehicle", "input_type": "mtv"},
    {"filename": "ikinci-el-tasit-kredisi-hesaplama.html", "title": "2. El Taşıt Kredisi Hesaplama", "keywords": ["araç kredisi", "oto kredi"], "category": "finance", "input_type": "loan"},

    # New to Create - Legal
    {"filename": "islah-harci-hesaplama.html", "title": "Islah Harcı Hesaplama 2026", "keywords": ["dava harcı", "ıslah"], "category": "legal", "input_type": "legal_fee"},
    {"filename": "vekalet-ucreti-hesaplama.html", "title": "Vekalet Ücreti Hesaplama 2026", "keywords": ["avukatlık ücreti", "karşı vekalet"], "category": "legal", "input_type": "legal_fee"},
    {"filename": "infaz-hesaplama.html", "title": "İnfaz Hesaplama 2026", "keywords": ["yatar hesaplama", "ceza infaz"], "category": "legal", "input_type": "legal_time"},

    # New to Create - Education
    {"filename": "yks-siralama-hesaplama.html", "title": "YKS Sıralama Hesaplama 2026", "keywords": ["tyt ayt puan", "üniversite sıralama"], "category": "education", "input_type": "exam_score"},
    {"filename": "tyt-ayt-net-hesaplama.html", "title": "TYT AYT Net Hesaplama", "keywords": ["yks net hesaplama", "doğru yanlış"], "category": "education", "input_type": "exam_net"},
    {"filename": "kpss-onlisans-puan-hesaplama.html", "title": "KPSS Önlisans Puan Hesaplama", "keywords": ["kpss puan", "memur atama"], "category": "education", "input_type": "exam_score"},
    {"filename": "edebiyat-not-hesaplama.html", "title": "Edebiyat Not Hesaplama", "keywords": ["ders notu", "ortalama"], "category": "education", "input_type": "grade"},
    {"filename": "deneme-puan-hesaplama.html", "title": "Deneme Puan Hesaplama", "keywords": ["lgs deneme", "yks deneme"], "category": "education", "input_type": "exam_score"},
    {"filename": "akademik-tesvik-hesaplama.html", "title": "Akademik Teşvik Hesaplama 2026", "keywords": ["akademisyen puan", "teşvik ödeneği"], "category": "education", "input_type": "academic"},
    {"filename": "ucretli-ogretmen-maas-hesaplama.html", "title": "Ücretli Öğretmen Maaş Hesaplama 2026", "keywords": ["ek ders", "öğretmen maaşı"], "category": "finance", "input_type": "salary"},

    # New to Create - Other
    {"filename": "kopek-yasi-hesaplama.html", "title": "Köpek Yaşı Hesaplama", "keywords": ["köpek insan yaşı"], "category": "other", "input_type": "pet_age"},
    {"filename": "kedi-yasi-hesaplama.html", "title": "Kedi Yaşı Hesaplama", "keywords": ["kedi insan yaşı"], "category": "other", "input_type": "pet_age"},
    {"filename": "kus-yasi-hesaplama.html", "title": "Kuş Yaşı Hesaplama", "keywords": ["muhabbet kuşu yaşı"], "category": "other", "input_type": "pet_age"},
    {"filename": "mesai-hesaplama.html", "title": "Mesai Ücreti Hesaplama 2026", "keywords": ["fazla mesai", "overtime"], "category": "finance", "input_type": "salary"},
    {"filename": "emekli-maas-hesaplama-2026.html", "title": "Emekli Maaş Hesaplama 2026", "keywords": ["emekli zammı", "ssk bağkur"], "category": "finance", "input_type": "salary"},
    {"filename": "kira-zammi-hesaplama.html", "title": "Kira Zammı Hesaplama 2026", "keywords": ["kira artış oranı", "tefe tüfe"], "category": "finance", "input_type": "rent"},
    {"filename": "zekat-hesaplama.html", "title": "Zekat Hesaplama", "keywords": ["zekat ne kadar", "fitre"], "category": "finance", "input_type": "religious"},
]

# --- 2. SEO Content Generation ---

def generate_seo_text(tool):
    t = tool["title"]
    k = ", ".join(tool["keywords"])

    # Generic templates based on category to ensure >400 chars

    if tool["category"] == "astrology":
        return f"""
        <article class="bg-white rounded-2xl shadow-sm border border-slate-200 p-8 info-panel">
            <h2 class="text-xl font-bold text-slate-800 mb-4">{t} Hakkında Bilmeniz Gerekenler</h2>
            <p class="mb-4">Astroloji dünyasında <strong>{t}</strong>, kişisel potansiyellerinizi, karakter özelliklerinizi ve gelecekteki olası etkileri anlamanız için kullanılan temel yöntemlerden biridir. Gezegenlerin konumları, doğum saatiniz ve doğum yeriniz gibi faktörler, bu hesaplamanın doğruluğunu doğrudan etkiler.</p>

            <h3 class="text-lg font-bold text-slate-800 mb-3">Neden {t} Yapmalısınız?</h3>
            <p class="mb-4">Doğum haritanızdaki, yükselen burcunuzdaki veya ay burcunuzdaki konumlanmalar, sadece kişilik özelliklerinizi değil, aynı zamanda ilişkilerinizi, kariyer tercihlerinizi ve yaşam yolculuğunuzdaki dönüm noktalarını da şekillendirir. <strong>{t} aracı</strong> sayesinde karmaşık astronomik tablolarla uğraşmadan, saniyeler içinde kişisel astrolojik verilerinize ulaşabilirsiniz.</p>

            <h3 class="text-lg font-bold text-slate-800 mb-3">Hesaplama Nasıl Çalışır?</h3>
            <p class="mb-4">Sistemimiz, girdiğiniz tarih ve saat verilerini kullanarak güncel astrolojik veritabanı (efemeris) mantığıyla yaklaşık konumları belirler. Özellikle <strong>2026 yılı astrolojik etkileri</strong> göz önüne alındığında, burçlarınızın size neler fısıldadığını öğrenmek için bu aracı güvenle kullanabilirsiniz. Sonuçlar size özel yorumlarla birlikte sunulmaktadır.</p>

            <h3 class="text-lg font-bold text-slate-800 mb-3">Astrolojik Terimler ve Anlamları</h3>
            <p class="mb-4">Yükselen burç (Ascendant), dış dünyaya gösterdiğiniz yüzü temsil ederken; Ay burcu (Moon Sign) duygusal dünyanızı ve içgüdülerinizi yansıtır. Güneş burcunuz (Sun Sign) ise temel kimliğinizdir. Bu üçlü kombinasyon, astrolojik kimliğinizin %70'ini oluşturur. Aracımızla tüm bu detayları keşfedin.</p>

            <p>Daha detaylı analizler ve yapay zeka destekli yorumlar için sonuç ekranındaki <strong>AI Asistan</strong> butonunu kullanmayı unutmayın.</p>
        </article>
        """

    elif tool["category"] == "finance":
        return f"""
        <article class="bg-white rounded-2xl shadow-sm border border-slate-200 p-8 info-panel">
            <h2 class="text-xl font-bold text-slate-800 mb-4">{t} ve Finansal Planlama</h2>
            <p class="mb-4">Finansal kararlar alırken doğru verilerle hareket etmek hayati önem taşır. <strong>{t}</strong> aracımız, 2026 yılı güncel ekonomik parametreleri, vergi dilimleri ve enflasyon tahminleri dikkate alınarak tasarlanmıştır. İster yatırım yapın, ister borçlanın, ister maaş hesabınızı kontrol edin; doğru hesaplama size para kazandırır.</p>

            <h3 class="text-lg font-bold text-slate-800 mb-3">2026 Yılında Dikkat Edilmesi Gerekenler</h3>
            <p class="mb-4">Ocak 2026 itibarıyla değişen asgari ücret, vergi oranları ve harç tutarları, tüm finansal dengeleri etkilemektedir. Aracımız, bu yeni dönemdeki katsayıları ve yasal düzenlemeleri (Resmi Gazete verileri ışığında) baz alarak size en gerçekçi sonucu (tahmini) sunar. Özellikle <strong>{k}</strong> konularında yapacağınız hatalı bir hesaplama, bütçenizde ciddi sapmalara yol açabilir.</p>

            <h3 class="text-lg font-bold text-slate-800 mb-3">Hesaplama Mantığı</h3>
            <p class="mb-4">Finansal hesaplamalarımızda net bugünkü değer, bileşik faiz formülleri ve yasal kesinti oranları (Damga Vergisi, Gelir Vergisi vb.) otomatik olarak uygulanır. Kullanıcı dostu arayüzümüz sayesinde, karmaşık formüllerle uğraşmadan sadece temel verileri girerek net sonuca ulaşabilirsiniz.</p>

            <h3 class="text-lg font-bold text-slate-800 mb-3">Yatırım ve Tasarruf İpuçları</h3>
            <p class="mb-4">Elde ettiğiniz sonuçları değerlendirirken, enflasyonun etkisini ve paranın zaman değerini göz ardı etmeyin. Aracımız size sadece bugünkü durumu değil, gelecekteki projeksiyonları da anlamanız için yardımcı olur. Ek olarak, yapay zeka asistanımızla sonuçlarınızı detaylıca analiz edebilir, yatırım tavsiyesi olmamak kaydıyla finansal okuryazarlığınızı geliştirecek öneriler alabilirsiniz.</p>
        </article>
        """

    elif tool["category"] == "legal":
        return f"""
        <article class="bg-white rounded-2xl shadow-sm border border-slate-200 p-8 info-panel">
            <h2 class="text-xl font-bold text-slate-800 mb-4">{t} ve Hukuki Süreçler</h2>
            <p class="mb-4">Hukuki süreçlerde maliyetlerin ve sürelerin doğru hesaplanması, hak kaybına uğramamak adına kritiktir. <strong>{t}</strong> aracımız, Adalet Bakanlığı'nın 2026 yılı tarifeleri, avukatlık asgari ücret tarifesi ve ilgili kanun maddeleri esas alınarak hazırlanmıştır.</p>

            <h3 class="text-lg font-bold text-slate-800 mb-3">Yasal Dayanaklar ve 2026 Tarifesi</h3>
            <p class="mb-4">Her yıl güncellenen harçlar, vekalet ücretleri ve infaz oranları, hukuki hesaplamaların temelini oluşturur. Aracımız, <strong>{k}</strong> gibi konularda en güncel katsayıları kullanır. Ancak unutulmamalıdır ki, her dava dosyası kendine has özellikler taşır ve buradaki hesaplamalar genel bilgilendirme amacı güder. Kesin sonuçlar için mutlaka bir hukukçudan destek almalısınız.</p>

            <h3 class="text-lg font-bold text-slate-800 mb-3">Hesaplama Aracı Nasıl Kullanılır?</h3>
            <p class="mb-4">İlgili dava türünü, tutarı veya süreyi girdiğinizde, sistemimiz yasal kesintileri ve eklemeleri yaparak size tahmini bir sonuç sunar. İnfaz hesaplamalarında denetimli serbestlik süreleri, ıslah harcında dava değeri artış oranı gibi detaylar otomatik olarak dikkate alınır.</p>

            <p>Hukuki terimler karmaşık olabilir; bu nedenle aracımızda sade ve anlaşılır bir dil kullanılmıştır. Sonuç ekranında çıkan verileri, dava dilekçelerinizde veya bütçe planlamanızda referans olarak kullanabilirsiniz.</p>
        </article>
        """

    elif tool["category"] == "education":
        return f"""
        <article class="bg-white rounded-2xl shadow-sm border border-slate-200 p-8 info-panel">
            <h2 class="text-xl font-bold text-slate-800 mb-4">{t} ile Başarınızı Planlayın</h2>
            <p class="mb-4">Eğitim hayatında notlar, puanlar ve sıralamalar, hedeflerinize ulaşmanızdaki en önemli göstergelerdir. <strong>{t}</strong> aracımız, MEB ve ÖSYM'nin güncel müfredatına, katsayılarına ve sınav sistemlerine (2025-2026 Eğitim Öğretim Yılı) tam uyumlu olarak çalışır.</p>

            <h3 class="text-lg font-bold text-slate-800 mb-3">Puan ve Sıralama Hesaplama Mantığı</h3>
            <p class="mb-4">Sınav sistemlerinde (YKS, KPSS, LGS vb.) standart sapma, okul puanı eklemesi ve ders katsayıları her yıl değişiklik gösterebilir. Aracımız, geçmiş yılların yığılmalı verilerini ve bu yılın zorluk derecesi tahminlerini kullanarak size en yakın sonucu (tahmini) vermeyi amaçlar. <strong>{k}</strong> hesaplamalarınızı yaparken bu detayları göz önünde bulunduruyoruz.</p>

            <h3 class="text-lg font-bold text-slate-800 mb-3">Not Hesaplama ve Akademik Hedefler</h3>
            <p class="mb-4">Üniversite veya lise not ortalamalarınızı hesaplarken, kredili sistem veya ağırlıklı ortalama gibi faktörleri manuel hesaplamak zordur. Aracımızla vize, final ve proje notlarınızı girerek dönem sonu harf notunuzu veya genel ortalamanızı saniyeler içinde görebilirsiniz. Başarıya giden yolda stratejik planlama yapmak için bu verileri kullanın.</p>

            <p>Sonuçlarınızı analiz etmek ve çalışma programı önerileri almak için AI asistanımıza danışabilirsiniz.</p>
        </article>
        """

    elif tool["category"] == "vehicle":
        return f"""
        <article class="bg-white rounded-2xl shadow-sm border border-slate-200 p-8 info-panel">
            <h2 class="text-xl font-bold text-slate-800 mb-4">{t} ve Araç Maliyetleri</h2>
            <p class="mb-4">Araç sahipleri için MTV, yakıt tüketimi ve diğer vergiler, yıllık bütçenin önemli bir kalemini oluşturur. <strong>{t}</strong> aracımız, 2026 yılı yeniden değerleme oranlarına göre güncellenmiş vergi dilimlerini ve güncel akaryakıt fiyat ortalamalarını kullanır.</p>

            <h3 class="text-lg font-bold text-slate-800 mb-3">2026 MTV ve Vergi Düzenlemeleri</h3>
            <p class="mb-4">Motorlu Taşıtlar Vergisi (MTV), aracın yaşına, motor hacmine ve tescil tarihine göre değişir. 2026 yılında beklenen artış oranları sistemimize entegre edilmiştir. Aracımızla plakanızı girmeden, sadece araç özelliklerini seçerek ödeyeceğiniz tutarı (Ocak ve Temmuz taksitleri dahil) öğrenebilirsiniz.</p>

            <h3 class="text-lg font-bold text-slate-800 mb-3">Yakıt ve İşletme Giderleri</h3>
            <p class="mb-4">Sadece vergi değil, yakıt tüketimi de araç maliyetinin büyük bir parçasıdır. <strong>{k}</strong> yaparken, fabrika verileri ile gerçek yol koşulları arasındaki farkı gözetiyoruz. Aracımız, seyahat planlamanızda size yol gösterici olacaktır.</p>

            <p>Elektrikli araçlar ve hibrit modeller için özel indirimli tarifeler de hesaplama modülümüzde mevcuttur.</p>
        </article>
        """

    else: # General / Other
        return f"""
        <article class="bg-white rounded-2xl shadow-sm border border-slate-200 p-8 info-panel">
            <h2 class="text-xl font-bold text-slate-800 mb-4">{t} Aracı</h2>
            <p class="mb-4">Günlük hayatta karşılaştığınız pratik hesaplama ihtiyaçları için geliştirdiğimiz <strong>{t}</strong>, karmaşık işlemleri basite indirger. İster evcil hayvanınızın yaşını merak edin, ister emekli maaşınızı sorgulayın; en doğru ve güncel verilerle yanınızdayız.</p>

            <h3 class="text-lg font-bold text-slate-800 mb-3">Nasıl Hesaplanır?</h3>
            <p class="mb-4">Bu hesaplama aracı, bilimsel formüller veya genel kabul görmüş katsayılar (örneğin kedi/köpek yaşı için 1 insan yılı = 7 kedi yılı gibi genellemelerin ötesinde, türe özgü eğriler) kullanılarak hazırlanmıştır. <strong>{k}</strong> gibi konularda merakınızı gidermek ve bilgi sahibi olmak için idealdir.</p>

            <h3 class="text-lg font-bold text-slate-800 mb-3">2026 Güncellemeleri</h3>
            <p class="mb-4">Tüm araçlarımız gibi bu araç da 2026 yılına ait beklenen veriler ve trendler ışığında güncellenmiştir. Kullanıcı deneyimini ön planda tutan arayüzümüzle, herhangi bir teknik bilgiye ihtiyaç duymadan sonucunuzu anında alırsınız.</p>

            <p>Hesaplama sonucunda aklınıza takılan sorular olursa, sayfanın altındaki yapay zeka asistanımıza sormaktan çekinmeyin.</p>
        </article>
        """

# Generate dictionaries for script usage
import json
print(json.dumps(TOOLS_MAP))
