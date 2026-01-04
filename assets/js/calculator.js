// API Key Obfuscation
const _k = "QUl6YVN5Qzh6SGxSTkZvck1peW5tM01qUnFNc3RvWjRNczBwQVdR";
const apiKey = atob(_k);

// --- TOOL CONFIGURATION (Central Source of Truth) ---
const tools = [
    // 1. YAPAY ZEKA
    { id: 'ai_asistan', cat: 'Yapay Zeka', name: 'AI Hesaplama Asistanı', link: 'ai-asistan.html', color:'indigo' },
    { id: 'ai_diyet', cat: 'Yapay Zeka', name: 'AI Diyetisyen', link: 'ai-diyetisyen.html', color:'indigo' },
    { id: 'token', cat: 'Yapay Zeka', name: 'AI Token Maliyet Hesaplama', link: 'yapay-zeka-token-maliyet-hesaplama.html', color:'indigo' },

    // 2. FİNANS & VERGİ
    { id: 'enflasyon', cat: 'Finans', name: 'Enflasyon ve Alım Gücü Hesaplama', link: 'enflasyon-alim-gucu-hesaplama.html', color:'blue' },
    { id: 'freelancer', cat: 'Finans', name: 'Freelancer Gelir Vergisi Hesaplama', link: 'freelancer-gelir-vergisi-hesaplama.html', color:'blue' },
    { id: 'dolar', cat: 'Finans', name: 'Dolar ve Döviz Kar/Zarar Hesaplama', link: 'dolar-hesaplama.html', color:'blue' },
    { id: 'kdv', cat: 'Finans', name: 'KDV Hesaplama', link: 'kdv-hesaplama.html', color:'blue', inputs: [{}, {opts:['%1','%10','%20']}] },
    { id: 'tevkifat', cat: 'Finans', name: 'KDV Tevkifat Hesaplama', link: 'tevkifat-hesaplama.html', color:'blue' },
    { id: 'kidem', cat: 'Finans', name: 'Kıdem Tazminatı Hesaplama', link: 'kidem-tazminati-hesaplama.html', color:'blue' },
    { id: 'kredi', cat: 'Finans', name: 'Kredi Hesaplama', link: 'kredi-hesaplama.html', color:'blue' },
    { id: 'net_brut', cat: 'Finans', name: 'Netten Brüte Maaş Hesaplama', link: 'netten-brute-maas-hesaplama.html', color:'blue' },
    { id: 'brut_net', cat: 'Finans', name: 'Brütten Nete Maaş Hesaplama', link: 'brutten-nete-maas-hesaplama.html', color:'blue' },
    { id: 'mevduat', cat: 'Finans', name: 'Mevduat Getirisi Hesaplama', link: 'mevduat-faizi-hesaplama.html', color:'blue' },
    { id: 'iban', cat: 'Finans', name: 'IBAN Doğrulama Aracı', link: 'iban-dogrulama-ve-cozumleme-araci.html', color:'blue' },
    { id: 'indirim', cat: 'Finans', name: 'İndirim Hesaplama', link: 'i̇ndirim-hesaplama.html', color:'blue' },
    { id: 'karzarar', cat: 'Finans', name: 'Kâr Marjı Hesaplama', link: 'kâr-marji-ve-zarar-hesaplama.html', color:'blue' },
    { id: 'bilesik', cat: 'Finans', name: 'Bileşik Faiz Hesaplama', link: 'bilesik-faiz-hesaplama.html', color:'blue' },
    { id: 'kk_asgari', cat: 'Finans', name: 'K.K. Asgari Ödeme Hesaplama', link: 'kredi-karti-asgari-odeme-hesaplama.html', color:'blue' },
    { id: 'komisyon', cat: 'Finans', name: 'Emlak Komisyonu Hesaplama', link: 'emlakci-komisyonu-hesaplama.html', color:'blue' },
    { id: 'zam', cat: 'Finans', name: 'Maaş Zam Hesaplama', link: 'maas-zam-orani-hesaplama.html', color:'blue' },
    { id: 'asgari', cat: 'Finans', name: 'Asgari Ücret Hesaplama', link: 'asgari-ucret-hesaplama.html', color:'blue' },
    { id: 'memur', cat: 'Finans', name: 'Memur Zammı Hesaplama', link: 'memur-maas-zammi-hesaplama.html', color:'blue' },
    { id: 'kira', cat: 'Finans', name: 'Kira Zammı Hesaplama', link: 'kira-zammi-hesaplama.html', color:'blue' },
    { id: 'emekli', cat: 'Finans', name: 'Emekli Maaş Hesaplama', link: 'emekli-maas-hesaplama.html', color:'blue' },
    { id: 'mtv', cat: 'Finans', name: 'MTV Hesaplama', link: 'mtv-hesaplama.html', color:'blue' },
    { id: 'deger', cat: 'Finans', name: 'Değer Artış Kazancı Hesaplama', link: 'deger-artis-kazanci-hesaplama.html', color:'blue' },
    { id: 'ucretli', cat: 'Finans', name: 'Ücretli Öğretmen Maaşı Hesaplama', link: 'ucretli-ogretmen-maas-hesaplama.html', color:'blue' },
    { id: 'altin', cat: 'Finans', name: 'Altın Hesaplama', link: 'altin-hesaplama.html', color:'blue' },
    { id: 'gumus', cat: 'Finans', name: 'Gümüş Hesaplama', link: 'gumus-hesaplama.html', color:'blue' },
    { id: 'euro', cat: 'Finans', name: 'Euro Hesaplama', link: 'euro-hesaplama.html', color:'blue' },
    { id: 'esnek', cat: 'Finans', name: 'Esnek Hesap Faizi Hesaplama', link: 'esnek-hesap-faiz-hesaplama.html', color:'blue' },
    { id: 'tasit2', cat: 'Finans', name: '2. El Taşıt Kredisi Hesaplama', link: 'ikinci-el-tasit-kredisi-hesaplama.html', color:'blue' },
    { id: 'piyango', cat: 'Finans', name: 'Milli Piyango Vergi Hesaplama', link: 'milli-piyango-hesaplama.html', color:'blue' },
    { id: 'vekalet', cat: 'Finans', name: 'Vekalet Ücreti Hesaplama', link: 'vekalet-ucreti-hesaplama.html', color:'blue' },
    { id: 'zekat', cat: 'Finans', name: 'Zekat Hesaplama', link: 'zekat-hesaplama.html', color:'blue' },
    { id: 'islah', cat: 'Finans', name: 'Islah Harcı Hesaplama', link: 'islah-harci-hesaplama.html', color:'blue' },
    { id: 'dolar_enf', cat: 'Finans', name: 'Dolar Enflasyonu Hesaplama', link: 'dolar-enflasyonu-hesaplama.html', color:'blue' },

    // 3. SAĞLIK
    { id: 'oruc', cat: 'Sağlık', name: 'Aralıklı Oruç (IF)', link: 'aralikli-oruc-hesaplama.html', color:'green' },
    { id: 'uyku', cat: 'Sağlık', name: 'Uyku Döngüsü Hesaplama', link: 'uyku-dongusu-hesaplama.html', color:'green' },
    { id: 'sigara', cat: 'Sağlık', name: 'Sigara Bırakma Hesaplama', link: 'sigara-maliyeti-hesaplama.html', color:'green' },
    { id: 'bmi', cat: 'Sağlık', name: 'Vücut Kitle İndeksi Hesaplama', link: 'vucut-kitle-i̇ndeksi-bmi-hesaplama.html', color:'green' },
    { id: 'idealkilo', cat: 'Sağlık', name: 'İdeal Kilo Hesaplama', link: 'i̇deal-kilo-hesaplama.html', color:'green' },
    { id: 'bmr', cat: 'Sağlık', name: 'Bazal Metabolizma Hesaplama', link: 'bazal-metabolizma-hizi-bmr-hesaplama.html', color:'green' },
    { id: 'makro', cat: 'Sağlık', name: 'Günlük Makro İhtiyacı Hesaplama', link: 'gunluk-makro-protein,-karbonhidrat,-yag-hesaplama.html', color:'green' },
    { id: 'su', cat: 'Sağlık', name: 'Su Tüketimi Hesaplama', link: 'gunluk-su-i̇htiyaci-hesaplama.html', color:'green' },
    { id: 'gebelik', cat: 'Sağlık', name: 'Doğum Tarihi (SAT) Hesaplama', link: 'gebelik-hesaplama-ve-dogum-tarihi.html', color:'green' },
    { id: 'nabiz', cat: 'Sağlık', name: 'Spor Nabız Aralığı Hesaplama', link: 'spor-nabiz-araligi-hesaplama.html', color:'green' },
    { id: 'kaf', cat: 'Sağlık', name: 'Kafein Tolerans Hesaplama', link: 'kahve-tolerans-hesaplama.html', color:'green' },

    // 4. EĞİTİM & MATEMATİK
    { id: 'yuzde', cat: 'Eğitim', name: 'Yüzde Hesaplama', link: 'yuzde-hesaplama-araci.html', color:'purple' },
    { id: 'sinav', cat: 'Eğitim', name: 'Üniversite Not Ort. Hesaplama', link: 'universite-not-ortalamasi-vize-final-hesaplama.html', color:'purple' },
    { id: 'takdir', cat: 'Eğitim', name: 'Takdir / Teşekkür Hesaplama', link: 'takdir-tesekkur-hesaplama-e-okul.html', color:'purple' },
    { id: 'dikdortgen', cat: 'Eğitim', name: 'Alan Hesaplama', link: 'dikdortgen-alan-ve-cevre-hesaplama.html', color:'purple' },
    { id: 'kelime', cat: 'Eğitim', name: 'Kelime ve Karakter Sayacı', link: 'kelime-ve-karakter-sayaci.html', color:'purple' },
    { id: 'vf', cat: 'Eğitim', name: 'Vize Final Hesaplama', link: 'vize-final-hesaplama.html', color:'purple' },
    { id: 'gpa', cat: 'Eğitim', name: 'Not Ortalaması (GNO) Hesaplama', link: 'universite-not-ortalamasi-hesaplama.html', color:'purple' },
    { id: 'timer', cat: 'Eğitim', name: 'Sınav Geri Sayım', link: 'sinav-geri-sayim-sayaci.html', color:'purple' },
    { id: 'akademik', cat: 'Eğitim', name: 'Akademik Teşvik Hesaplama', link: 'akademik-tesvik-hesaplama.html', color:'purple' },
    { id: 'deneme', cat: 'Eğitim', name: 'Deneme Puanı Hesaplama', link: 'deneme-puan-hesaplama.html', color:'purple' },
    { id: 'edebiyat', cat: 'Eğitim', name: 'Edebiyat Not Hesaplama', link: 'edebiyat-not-hesaplama.html', color:'purple' },
    { id: 'kpss', cat: 'Eğitim', name: 'KPSS Önlisans Puan Hesaplama', link: 'kpss-onlisans-puan-hesaplama.html', color:'purple' },
    { id: 'tyt', cat: 'Eğitim', name: 'TYT AYT Net Hesaplama', link: 'tyt-ayt-net-hesaplama.html', color:'purple' },
    { id: 'yks', cat: 'Eğitim', name: 'YKS Sıralama Hesaplama', link: 'yks-siralama-hesaplama.html', color:'purple' },

    // 5. PRATİK & ARAÇLAR
    { id: 'day', cat: 'Pratik', name: 'Hangi Gün?', link: 'hangi-gun-hesaplama.html', color:'orange' },
    { id: 'date_add', cat: 'Pratik', name: 'Tarihe Gün Ekleme Hesaplama', link: 'tarihe-gun-ekleme-hesaplama.html', color:'orange' },
    { id: 'hiz', cat: 'Pratik', name: 'Hız / Zaman Hesaplama', link: 'hiz,-yol-ve-zaman-hesaplama.html', color:'gray' },
    { id: 'elk', cat: 'Pratik', name: 'Elektrik Faturası Hesaplama', link: 'elektrik-faturasi-hesaplama.html', color:'orange' },
    { id: 'ev', cat: 'Pratik', name: 'Elektrikli Araç Şarj Hesaplama', link: 'elektrikli-arac-sarj-hesaplama.html', color:'orange' },
    { id: 'solar', cat: 'Pratik', name: 'Güneş Paneli Amortisman Hesaplama', link: 'gunes-paneli-amortisman-hesaplama.html', color:'orange' },
    { id: 'co2', cat: 'Pratik', name: 'Karbon Ayak İzi Hesaplama', link: 'karbon-ayak-izi-hesaplama.html', color:'green' },
    { id: 'yum', cat: 'Pratik', name: 'Yumurta Haşlama Süresi Hesaplama', link: 'yumurta-haslama-suresi-hesaplama.html', color:'orange' },
    { id: 'raffle', cat: 'Pratik', name: 'Çekiliş Aracı', link: 'cekilis-araci.html', color:'orange' },
    { id: 'qr', cat: 'Pratik', name: 'QR Kod Oluşturucu', link: 'qr-kod-olusturucu.html', color:'gray' },
    { id: 'sifre', cat: 'Pratik', name: 'Güçlü Şifre Oluşturucu', link: 'guclu-sifre-olusturucu.html', color:'gray' },
    { id: 'kedi', cat: 'Pratik', name: 'Kedi Yaşı Hesaplama', link: 'kedi-yasi-hesaplama.html', color:'orange' },
    { id: 'kopek', cat: 'Pratik', name: 'Köpek Yaşı Hesaplama', link: 'kopek-yasi-hesaplama.html', color:'orange' },
    { id: 'kus', cat: 'Pratik', name: 'Kuş Yaşı Hesaplama', link: 'kus-yasi-hesaplama.html', color:'orange' },
    { id: 'internet', cat: 'Pratik', name: 'İnternet Hızı Hesaplama', link: 'i̇nternet-hizi-i̇ndirme-suresi-hesaplama.html', color:'gray' },
    { id: 'yakit', cat: 'Pratik', name: 'Yakıt Tüketimi Hesaplama', link: 'yakit-tuketimi-hesaplama.html', color:'orange' },
    { id: 'tarih_sayac', cat: 'Pratik', name: 'İki Tarih Arası Gün Hesaplama', link: 'i̇ki-tarih-arasi-gun-sayaci.html', color:'orange' },
    { id: 'infaz', cat: 'Pratik', name: 'İnfaz Hesaplama', link: 'infaz-hesaplama.html', color:'orange' },
    { id: 'mesai', cat: 'Pratik', name: 'Mesai Hesaplama', link: 'mesai-hesaplama.html', color:'orange' },
    { id: 'altili', cat: 'Pratik', name: 'Altılı Ne Verir', link: 'altili-ne-verir-hesaplama.html', color:'orange' },
    { id: 'tam_yas', cat: 'Pratik', name: 'Tam Yaş Hesaplama', link: 'tam-yas-hesaplama.html', color:'orange' },

    // 6. DİJİTAL & SOSYAL MEDYA
    { id: 'smedya', cat: 'Dijital', name: 'Sosyal Medya Gelir Hesaplama', link: 'tiktok-youtube-gelir-hesaplama.html', color:'pink' },
    { id: 'insta', cat: 'Dijital', name: 'Instagram Etkileşim Oranı Hesaplama', link: 'instagram-etkilesim-orani-hesaplama.html', color:'pink' },
    { id: 'best_time', cat: 'Dijital', name: 'Sosyal Medya En İyi Saat Hesaplama', link: 'sosyal-medya-en-iyi-saat-hesaplama.html', color:'pink' },

    // 7. ASTROLOJİ
    { id: 'solar_map', cat: 'Astroloji', name: 'Solar Harita Hesaplama', link: 'solar-harita-hesaplama.html', color:'purple' },
    { id: 'dogum', cat: 'Astroloji', name: 'Doğum Haritası Hesaplama', link: 'dogum-haritasi-hesaplama.html', color:'purple' },
    { id: 'yukselen', cat: 'Astroloji', name: 'Yükselen Burç Hesaplama', link: 'yukselen-burc-hesaplama.html', color:'purple' },
    { id: 'burc', cat: 'Astroloji', name: 'Burç Hesaplama', link: 'burc-hesaplama.html', color:'purple' },
    { id: 'ay_burcu', cat: 'Astroloji', name: 'Ay Burcu Hesaplama', link: 'ay-burcu-hesaplama.html', color:'purple' },
    { id: 'numeroloji', cat: 'Astroloji', name: 'Numeroloji Hesaplama', link: 'numeroloji-hesaplama.html', color:'purple' },
    { id: 'cin', cat: 'Astroloji', name: 'Çin Takvimi Cinsiyet Hesaplama', link: 'cin-takvimi-cinsiyet-hesaplama.html', color:'purple' },

    // 8. E-TİCARET
    { id: 'trendyol', cat: 'E-Ticaret', name: 'Trendyol Komisyon Hesaplama', link: 'trendyol-komisyon-hesaplama.html', color:'orange' },
    { id: 'n11', cat: 'E-Ticaret', name: 'N11 Komisyon Hesaplama', link: 'n11-komisyon-hesaplama.html', color:'red' },
    { id: 'hepsiburada', cat: 'E-Ticaret', name: 'Hepsiburada Komisyon Hesaplama', link: 'hepsiburada-komisyon-hesaplama.html', color:'orange' },
    { id: 'amazon', cat: 'E-Ticaret', name: 'Amazon Komisyon Hesaplama', link: 'amazon-komisyon-hesaplama.html', color:'gray' },
    { id: 'ciceksepeti', cat: 'E-Ticaret', name: 'Çiçeksepeti Komisyon Hesaplama', link: 'ciceksepeti-komisyon-hesaplama.html', color:'blue' }
];

// --- RENDER SIDEBAR ---
function renderSidebar() {
    const cats = [...new Set(tools.map(t => t.cat))];
    const currentPath = window.location.pathname.split('/').pop() || 'index.html';

    const containers = ['sidebar-list', 'drawer-list'];

    containers.forEach(id => {
        const container = document.getElementById(id);
        if(!container) return;

        // Skip if content already exists (static SEO content)
        // We check for 'cat-header' class as a marker of populated content
        if(container.querySelector('.cat-header')) return;

        container.innerHTML = ''; // Clear

        cats.forEach(cat => {
            const header = document.createElement('div');
            header.className = 'cat-header'; header.innerText = cat;
            container.appendChild(header);

            tools.filter(t => t.cat === cat).forEach(t => {
                const a = document.createElement('a');
                a.href = t.link;
                a.className = 'w-full text-left px-4 py-3 rounded-xl text-xs font-medium transition flex items-center nav-item gap-3 mb-1 text-slate-500 hover:bg-slate-50 hover:text-blue-600 block';
                if(currentPath === t.link) {
                    a.classList.add('nav-active', 'bg-blue-50', 'text-blue-600');
                }

                let icon = '<span class="w-1.5 h-1.5 rounded-full bg-slate-300"></span>';
                if(t.cat === 'Yapay Zeka') icon = '<i class="fa-solid fa-wand-magic-sparkles text-indigo-500"></i>';
                if(t.cat === 'E-Ticaret') icon = '<i class="fa-solid fa-shop text-orange-500"></i>';

                a.innerHTML = `${icon} ${t.name}`;
                container.appendChild(a);
            });
        });

        // Strict Cleanup: Remove "Tüm Hesaplamalar" link from drawer if present
        if(id === 'drawer-list') {
            const links = container.querySelectorAll('a');
            links.forEach(link => {
                const txt = link.innerText.toLowerCase();
                if(txt.includes('tüm hesaplama') || txt.includes('tum hesaplama')) {
                    link.remove();
                }
            });
        }
    });
}

// --- GEMINI API HELPER ---
async function callGemini(userPrompt, systemPrompt) {
    const today = new Date().toDateString();
    const lastDate = localStorage.getItem('ai_last_date');
    let count = parseInt(localStorage.getItem('ai_daily_count') || '0');

    if (lastDate !== today) {
        count = 0;
        localStorage.setItem('ai_last_date', today);
    }

    if (count >= 50) {
        throw new Error('Günlük soru limitine (50) ulaştınız. Yarın tekrar deneyin.');
    }

    const url = `https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-preview-09-2025:generateContent?key=${apiKey}`;
    const payload = {
        contents: [{ parts: [{ text: userPrompt }] }],
        systemInstruction: { parts: [{ text: systemPrompt }] }
    };

    for (let i = 0; i < 3; i++) {
        try {
            const response = await fetch(url, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(payload)
            });
            const data = await response.json();
            if (!response.ok) throw new Error(data.error?.message || response.statusText);

            localStorage.setItem('ai_daily_count', (count + 1).toString());
            return data.candidates[0].content.parts[0].text;
        } catch (error) {
            if (i === 2) throw error;
            await new Promise(r => setTimeout(r, 1000));
        }
    }
}

// --- COOKIE & UTILS ---
function checkCookies() {
    if(!localStorage.getItem('cookiesAccepted')) {
        setTimeout(() => {
            const b = document.getElementById('cookie-banner');
            if(b) b.classList.remove('translate-y-full');
        }, 1000);
    }
}
function acceptCookies() {
    localStorage.setItem('cookiesAccepted','true');
    const b = document.getElementById('cookie-banner');
    if(b) b.classList.add('translate-y-full');
}

function copyResult(id) {
    const val = document.getElementById(`val-${id}`).innerText;
    const btn = document.getElementById(`btn-copy-${id}`);
    navigator.clipboard.writeText(val).then(() => {
        const h = btn.innerHTML; btn.innerHTML = '<i class="fa-solid fa-check"></i>';
        setTimeout(()=>btn.innerHTML=h, 1500);
    }).catch(e => console.error(e));
}

// --- HELPERS ---
function getVal(t,i) { return document.getElementById(`${t}-${i}`).value; }
function getNum(t,i) { return parseFloat(getVal(t,i))||0; }
function showRes(id, mainTxt, detailTxt = '') {
    const r = document.getElementById(`res-${id}`);
    document.getElementById(`val-${id}`).innerHTML = mainTxt;
    document.getElementById(`detail-${id}`).innerHTML = detailTxt;

    const existingHelp = r.querySelector('.ai-help-link');
    if(existingHelp) existingHelp.remove();

    const tool = tools.find(t => t.id === id);
    if(tool && tool.cat !== 'Yapay Zeka' && !tool.id.startsWith('ai_')) {
        const div = document.createElement('div');
        div.className = 'mt-4 p-4 bg-indigo-50 border border-indigo-100 rounded-xl text-center shadow-sm ai-help-link block';
        div.style.display = 'block';
        div.innerHTML = '<a href="ai-asistan.html" class="block text-xs font-bold text-indigo-600 hover:text-indigo-800 transition"><i class="fa-solid fa-wand-magic-sparkles mb-1 text-lg block"></i> Bir hata olduğunu mu düşünüyorsunuz? Ai Asistanımıza sormayı deneyin!</a>';
        r.appendChild(div);
    }

    r.classList.remove('hidden');
    r.scrollIntoView({behavior:'smooth', block:'nearest'});
}

// --- DRAWER FUNCTIONS ---
function toggleDrawer() {
    const d = document.getElementById('drawer');
    const m = document.getElementById('drawer-mask');
    if(!d || !m) return;

    if(d.classList.contains('drawer-closed')) {
        d.classList.remove('drawer-closed'); d.classList.add('drawer-open');
        m.classList.remove('mask-hidden'); m.classList.add('mask-visible');
    } else {
        d.classList.remove('drawer-open'); d.classList.add('drawer-closed');
        m.classList.remove('mask-visible'); m.classList.add('mask-hidden');
    }
}

function filterDrawerTools() {
    const qInput = document.getElementById('mobile-tool-search');
    if(!qInput) return;
    const q = qInput.value.toLowerCase();
    const drawerList = document.getElementById('drawer-list');
    if(!drawerList) return;
    const items = drawerList.querySelectorAll('a');

    items.forEach(item => {
        if(item.classList.contains('cat-header')) return;
        const txt = item.innerText.toLowerCase();
        item.style.display = txt.includes(q) ? 'flex' : 'none';
    });
}

function initDrawer() {
    if(!document.getElementById('drawer')) {
        // High Z-Index to ensure it overlays everything including sticky headers
        // Use z-[990] and z-[1000] as per HEAD but logic from fix
        const drawerHTML = `
    <div id="drawer-mask" class="fixed inset-0 bg-black/50 z-[990] transition-opacity duration-300 mask-hidden" onclick="toggleDrawer()"></div>
    <aside id="drawer" class="fixed top-0 left-0 w-64 h-full bg-white z-[1000] shadow-2xl transition-transform duration-300 drawer-closed overflow-y-auto">
        <div class="p-4 border-b border-slate-100 flex justify-between items-center">
             <span class="font-bold text-lg text-slate-800">Hesaplama Araçları</span>
             <button onclick="toggleDrawer()" class="text-slate-400 hover:text-slate-600"><i class="fa-solid fa-times text-xl"></i></button>
        </div>
        <div id="drawer-list" class="p-3 space-y-1"></div>
    </aside>`;
        document.body.insertAdjacentHTML('afterbegin', drawerHTML);
    }
}

// --- CALC LOGIC ---
function calc_kdv() { const amt=getNum('kdv','amt'); let rVal=getVal('kdv','rate'); let rate=0; if(rVal==='custom'){rate=getNum('kdv','custom-rate')/100;}else{rate=parseFloat(rVal)/100;} if(rate<0||isNaN(rate))rate=0; const t=getVal('kdv','type'); let n=0,tx=0,tot=0; if(t==='include'){tot=amt;n=tot/(1+rate);tx=tot-n;}else{n=amt;tx=n*rate;tot=n+tx;} const f=(n)=>n.toLocaleString('tr-TR',{minimumFractionDigits:2})+' TL'; const rn=document.getElementById('kdv-res-net'); const rt=document.getElementById('kdv-res-tax'); const rtt=document.getElementById('kdv-res-total'); const rd=document.getElementById('res-kdv'); const vd=document.getElementById('val-kdv'); if(rn&&rt&&rtt){rn.innerText=f(n);rt.innerText=f(tx);rtt.innerText=f(tot);if(vd)vd.innerText=f(tot);rd.classList.remove('hidden');rd.scrollIntoView({behavior:'smooth',block:'nearest'});}}
window.cpi_data = {
    1999: 27.8,
    2000: 38.65,
    2001: 65.12,
    2002: 84.46,
    2003: 100.0,
    2004: 109.32,
    2005: 117.76,
    2006: 129.12,
    2007: 139.96,
    2008: 154.04,
    2009: 164.09,
    2010: 174.6,
    2011: 192.84,
    2012: 204.72,
    2013: 219.87,
    2014: 237.83,
    2015: 258.79,
    2016: 280.86,
    2017: 314.34,
    2018: 378.15,
    2019: 422.93,
    2020: 484.67,
    2021: 659.54,
    2022: 1083.43,
    2023: 1785.17,
    2024: 2577.43,
    2025: 3028.47,
    2026: 3322.24,
};
function calc_enflasyon() {
    const a=getNum('enflasyon','amt');
    const s=parseInt(getVal('enflasyon','start'));
    const e=parseInt(getVal('enflasyon','end'));
    const i1=window.cpi_data[s]||100;
    const i2=window.cpi_data[e]||100;
    const r=i2/i1;
    showRes('enflasyon',(a*r).toLocaleString('tr-TR',{maximumFractionDigits:2})+' TL', `Enflasyon Katsayısı: ${r.toFixed(2)}x (${s} -> ${e})`);
}

function calc_freelancer() { const i=getNum('freelancer','income'); const e=getNum('freelancer','expense'); const k=parseFloat(getVal('freelancer','kdv'))/100; const y=document.getElementById('freelancer-genc').checked; const ka=i*k; let p=i-e; if(y&&p>0)p=Math.max(0,p-230000); let t=0,rem=p; if(rem>0){const a=Math.min(rem,150000);t+=a*0.15;rem-=a;} if(rem>0){const a=Math.min(rem,280000);t+=a*0.20;rem-=a;} if(rem>0){const a=Math.min(rem,550000);t+=a*0.27;rem-=a;} if(rem>0){t+=rem*0.35;} showRes('freelancer',(i-e-t).toLocaleString('tr-TR',{maximumFractionDigits:2})+' TL', `Vergi: ${t.toLocaleString('tr-TR')} TL | KDV: ${ka.toLocaleString('tr-TR')} TL`); }
function calc_dolar() { const m=getVal('dolar','mode'); const a=getNum('dolar','amt'); if(m==='conv'){showRes('dolar',(a*getNum('dolar','rate')).toLocaleString('tr-TR',{maximumFractionDigits:2})+' TL','');}else{const b=getNum('dolar','buy'),s=getNum('dolar','sell'),c=a*b,r=a*s,p=r-c;const cl=p>=0?'text-green-600':'text-red-600';showRes('dolar',`<span class="${cl}">${p.toLocaleString('tr-TR',{maximumFractionDigits:2})} TL</span>`,`ROI: %${((p/c)*100).toFixed(2)}`);}}
function calc_yakit() { const d=getNum('yakit','km'),c=getNum('yakit','lit'),p=getNum('yakit','pr'),t=getVal('yakit','type'); const tc=(d/100)*c*p; let u='Lt'; if(t==='ev') u='kWh'; showRes('yakit',tc.toLocaleString('tr-TR',{maximumFractionDigits:2})+' TL', `Km Başı: ${(tc/d).toFixed(2)} TL | Tüketim: ${((d/100)*c).toFixed(1)} ${u}`); }
function calc_oruc() { const s=getVal('oruc','start'); if(!s)return; const h=parseInt(getVal('oruc','type')); const [hr,mn]=s.split(':').map(Number); const d=new Date(); d.setHours(hr,mn,0); const e=new Date(d.getTime()+h*3600000); const ee=new Date(e.getTime()+(24-h)*3600000); showRes('oruc',e.toLocaleTimeString('tr-TR',{hour:'2-digit',minute:'2-digit'}), `Yeme Penceresi: ${e.toLocaleTimeString('tr-TR',{hour:'2-digit',minute:'2-digit'})} - ${ee.toLocaleTimeString('tr-TR',{hour:'2-digit',minute:'2-digit'})}`); }
function calc_uyku() { const s=getVal('uyku','wake'); if(!s)return; const [h,m]=s.split(':').map(Number); const d=new Date(); d.setHours(h,m,0); const t=[]; for(let i=4;i<=6;i++)t.push(new Date(d.getTime()-(i*90+15)*60000).toLocaleTimeString('tr-TR',{hour:'2-digit',minute:'2-digit'})); showRes('uyku',t.reverse().join(' veya '),''); }
function calc_sigara() { const p=getNum('sigara','price'),q=getNum('sigara','daily'),d=new Date(getVal('sigara','date')); if(isNaN(d))return; const dif=Math.ceil(Math.abs(new Date()-d)/(864e5)); showRes('sigara',(dif*q*(p/20)).toLocaleString('tr-TR',{maximumFractionDigits:2})+' TL', `${dif} gün.`); }
function calc_smedya() { const v = getNum('smedya', 'views'); const cpm = getNum('smedya', 'cpm'); const rev = (v / 1000) * cpm; showRes('smedya', rev.toLocaleString('tr-TR', {maximumFractionDigits:2}) + ' TL', `İzlenme: ${v.toLocaleString()} | 1000 Gösterim Başı: ${cpm} TL`); }
function calc_insta() { const f = getNum('insta', 'followers'); const l = getNum('insta', 'likes'); const c = getNum('insta', 'comments'); if(f === 0) return; const rate = ((l + c) / f) * 100; let eval = "Düşük"; if(rate > 1) eval = "Ortalama"; if(rate > 3.5) eval = "İyi"; if(rate > 6) eval = "Mükemmel"; showRes('insta', '%' + rate.toFixed(2), `Durum: <strong>${eval}</strong>`); }
function calc_best_time() { const p = getVal('best', 'plat'); let t = "", d = ""; if(p === 'ig') { t = "09:00 - 13:00"; d = "Çarşamba ve Cuma günleri etkileşim en yüksek."; } else if(p === 'tt') { t = "19:00 - 23:00"; d = "Genç kitle akşam saatlerinde ve hafta sonu aktiftir."; } else if(p === 'yt') { t = "14:00 - 16:00"; d = "Perşembe ve Cuma günleri yükleme yapmak hafta sonu izlenmesini artırır."; } else if(p === 'tw') { t = "08:00 - 10:00"; d = "Haber akışı sabah saatlerinde yoğundur."; } else if(p === 'li') { t = "08:00 - 11:00"; d = "Salı, Çarşamba, Perşembe (Mesai saatleri)."; } showRes('best', t, d); }
function calc_qr() { const t = getVal('qr', 'text'); if(!t) return; const url = `https://api.qrserver.com/v1/create-qr-code/?size=200x200&data=${encodeURIComponent(t)}`; const container = document.getElementById('qr-output'); container.innerHTML = `<img src="${url}" alt="QR Kod" class="mx-auto rounded-lg shadow-sm"> <a href="${url}" download="qr.png" target="_blank" class="block mt-4 text-xs font-bold text-blue-600 hover:underline">Resmi İndir / Aç</a>`; document.getElementById('res-qr').classList.remove('hidden'); }
function calc_sifre() { const l = getNum('sifre', 'len'); const charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+"; let r = ""; const values = new Uint32Array(l); crypto.getRandomValues(values); for(let i=0; i<l; i++) r += charset[values[i] % charset.length]; const entropy = l * 6.1; let crackTime = "Anında"; const seconds = Math.pow(2, entropy) / 1000000000000; if(seconds > 31536000000) crackTime = "Yüzyıllar"; else if(seconds > 31536000) crackTime = Math.round(seconds/31536000) + " Yıl"; else if(seconds > 86400) crackTime = Math.round(seconds/86400) + " Gün"; else if(seconds > 3600) crackTime = Math.round(seconds/3600) + " Saat"; showRes('sifre', r, `Tahmini Kırılma Süresi: ${crackTime}`); }
function calc_elk() { const w = getNum('elk', 'watt'); const h = getNum('elk', 'hours'); const p = getNum('elk', 'price'); const dailyKwh = (w * h) / 1000; const dailyCost = dailyKwh * p; const monthlyCost = dailyCost * 30; showRes('elk', monthlyCost.toLocaleString('tr-TR', {maximumFractionDigits: 2}) + ' TL', `Günlük: ${dailyCost.toFixed(2)} TL | Aylık Tüketim: ${(dailyKwh*30).toFixed(1)} kWh`); }
function calc_kaf() { const intake = parseFloat(getVal('kaf', 'type')); const tTime = getVal('kaf', 'time'); const sTime = getVal('kaf', 'sleep'); if(!tTime || !sTime) return; const [h1, m1] = tTime.split(':').map(Number); const [h2, m2] = sTime.split(':').map(Number); let diff = (h2 + m2/60) - (h1 + m1/60); if(diff < 0) diff += 24; const remaining = intake * Math.pow(0.5, diff / 5); let status = "Uykuya dalabilirsiniz."; let color = "text-green-600"; if(remaining > 50) { status = "Uyku sorunu yaşayabilirsiniz!"; color = "text-red-600"; } else if(remaining > 20) { status = "Hafif etki sürebilir."; color = "text-orange-500"; } showRes('kaf', `${Math.round(remaining)} mg`, `<span class="${color}">${status}</span> (${diff.toFixed(1)} saat sonra)`); }
function calc_yumurta() { const min = parseFloat(getVal('yum', 'type')); const sizeAdd = parseFloat(getVal('yum', 'size')); const total = min + sizeAdd; showRes('yum', `${total} Dakika`, 'Su kaynadıktan sonra yumurtayı atın ve süreyi başlatın.'); }
function calc_raffle() { const text = document.getElementById('raffle-list').value.trim(); if(!text) return; const count = getNum('raffle', 'count'); const lines = text.split('\n').map(l => l.trim()).filter(l => l.length > 0); if(lines.length === 0) return; if(lines.length < count) { showRes('raffle', 'Hata', 'Katılımcı sayısı kazanan sayısından az olamaz.'); return; } for (let i = lines.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [lines[i], lines[j]] = [lines[j], lines[i]]; } const winners = lines.slice(0, count); let html = ""; winners.forEach((w, i) => { html += `${i+1}. ${w}\n`; }); showRes('raffle', html, `Toplam ${lines.length} katılımcı arasından.`); }
function calc_co2() { const car=getNum('co2','car'); const plane=getNum('co2','plane'); const meat=getVal('co2','meat'); let total=car*0.17+plane*250; if(meat==='high')total+=2000; else if(meat==='med')total+=1500; else if(meat==='low')total+=1000; else total+=500; showRes('co2',`${(total/1000).toFixed(2)} Ton CO2`,'Ortalama: 7 Ton'); }
function calc_ev() { const cap=getNum('ev','cap'); const power=parseFloat(getVal('ev','power')); const curr=getNum('ev','curr'); const target=getNum('ev','target'); if(power===0)return; const need=(target-curr); if(need<=0){showRes('ev','0 Dk','');return;} const kwh=cap*(need/100); const h=(kwh/power)*1.1; const hr=Math.floor(h); const mn=Math.round((h-hr)*60); let p=3.5; if(power>22)p=8.0; showRes('ev',`${hr} Saat ${mn} Dk`,`Maliyet: ${(kwh*p).toFixed(0)} TL`); }
function calc_solar() { const cost=getNum('solar','cost'); const save=getNum('solar','save'); if(save===0)return; const m=cost/save; showRes('solar',`${(m/12).toFixed(1)} Yıl`,`${Math.round(m)} ay`); }
function calc_token() { const w=getNum('token','words'); const m=getVal('token','model'); const t=w*1.5; let p=0; if(m==='gpt-4o')p=5; if(m==='gpt-4o-mini')p=0.15; if(m.includes('claude'))p=3; if(m.includes('turbo'))p=10; const c=(t/1e6)*p; showRes('token',`$${c.toFixed(4)}`,`~${(c*35).toFixed(2)} TL`); }
let timerInterval; function calc_timer() { clearInterval(timerInterval); const t=document.getElementById('timer-select').value; let d; if(t==='yks')d=new Date('2026-06-20T10:00:00'); else if(t==='kpss')d=new Date('2026-07-14T10:00:00'); else if(t==='lgs')d=new Date('2026-06-06T09:30:00'); else { const i=document.getElementById('timer-date').value; if(!i)return; d=new Date(i+'T09:00:00'); } const u=()=>{ const n=new Date(); const dif=d-n; if(dif<=0){clearInterval(timerInterval);document.getElementById('val-timer').innerHTML="Süre Doldu";return;} const dd=Math.floor(dif/864e5); const hh=Math.floor((dif%864e5)/36e5); const mm=Math.floor((dif%36e5)/6e4); const ss=Math.floor((dif%6e4)/1e3); document.getElementById('t-d').innerText=dd; document.getElementById('t-h').innerText=hh; document.getElementById('t-m').innerText=mm; document.getElementById('t-s').innerText=ss; }; u(); document.getElementById('res-timer').classList.remove('hidden'); timerInterval=setInterval(u,1000); }

// --- STANDARD STUBS ---
function calc_tevkifat() { const a=getNum('tevkifat','amt'); const r=[0.01,0.1,0.2][getVal('tevkifat','rate')]; const tn=[2,3,4,5,7,9][getVal('tevkifat','tev')]; const t=getVal('tevkifat','type'); let m,ft; if(t==1){m=a/(1+r);ft=a-m;}else{m=a;ft=a*r;} const w=ft*tn/10, d=ft-w, p=m+d; showRes('tevkifat', p.toLocaleString('tr-TR',{minimumFractionDigits:2})+' TL', `KDV: ${ft.toFixed(2)} | Tevkifat (${tn}/10): -${w.toFixed(2)} | Beyan: ${d.toFixed(2)}`); }
function calc_kredi() { const p=getNum('kredi','amt'), t=getNum('kredi','term'), r=getNum('kredi','rate')/100; const x=Math.pow(1+r,t), pay=p*(r*x)/(x-1); showRes('kredi', pay.toLocaleString('tr-TR',{maximumFractionDigits:2})+' TL/Ay', `Toplam Geri Ödeme: ${(pay*t).toLocaleString('tr-TR')} TL`); }
function calc_kidem() { const s = new Date(getVal('kidem','start')); const e = new Date(getVal('kidem','end')); let sal = getNum('kidem','salary'); if (isNaN(s)||isNaN(e)||!sal) return; if (sal > 60000) sal = 60000; const diffTime = Math.abs(e - s); const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24)); const tenureYears = diffDays / 365; let years = e.getFullYear() - s.getFullYear(); let months = e.getMonth() - s.getMonth(); let days = e.getDate() - s.getDate(); if (days < 0) { months--; days += new Date(e.getFullYear(), e.getMonth(), 0).getDate(); } if (months < 0) { years--; months += 12; } const gross = sal * tenureYears; const net = gross * 0.99241; showRes('kidem', `${net.toLocaleString('tr-TR', {maximumFractionDigits: 2})} TL`, `${years} Yıl ${months} Ay ${days} Gün`); }
async function calc_ai_asistan() { const q = getVal('ai_asistan', 'q'); if(!q) return; showRes('ai_asistan', '<i class="fa-solid fa-spinner fa-spin"></i> Düşünüyorum...', ''); try { const answer = await callGemini(q, "Sen yardımsever ve zeki bir hesaplama asistanısın. Kullanıcının matematiksel, finansal, mantıksal veya genel kültür sorularını Türkçe olarak yanıtla. Cevabın kısa, net ve anlaşılır olsun."); const formatted = answer.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>').replace(/\n/g, '<br>'); showRes('ai_asistan', formatted); } catch (e) { showRes('ai_asistan', 'Bağlantı Hatası: ' + (e.message || 'Bilinmeyen hata'), 'API Anahtarınızı kontrol edip tekrar deneyin.'); } }
async function calc_ai_diyet() { const w = getVal('ai_diyet', 'w'), h = getVal('ai_diyet', 'h'); const gIdx = getVal('ai_diyet', 'goal'); const goals = ['Kilo Vermek', 'Kilo Almak', 'Formu Korumak', 'Kas Yapmak']; if(!w || !h) return; showRes('ai_diyet', '<i class="fa-solid fa-spinner fa-spin"></i> Plan hazırlanıyor...', ''); const prompt = `Kilo: ${w}kg, Boy: ${h}cm, Hedef: ${goals[gIdx]}. Bana 1 günlük örnek bir beslenme planı oluştur.`; const sys = "Sen uzman bir diyetisyensin. Türkçe liste formatında yanıt ver."; try { const answer = await callGemini(prompt, sys); const formatted = answer.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>').replace(/\n/g, '<br>'); showRes('ai_diyet', formatted); } catch (e) { showRes('ai_diyet', 'Plan oluşturulamadı: ' + (e.message || 'Hata')); } }
function calc_yuzde() { const m = parseInt(getVal('yuzde', 'mode')); const a = getNum('yuzde', 'a'); const b = getNum('yuzde', 'b'); let res = 0; let desc = ""; if (m === 0) { res = (a * b) / 100; desc = `${a} sayısının %${b}'si`; } else if (m === 1) { if(b === 0) { showRes('yuzde', 'Tanımsız'); return; } res = (a / b) * 100; desc = `${a}, ${b} sayısının %${res.toFixed(2)}'sidir`; } else if (m === 2) { if(a === 0) { showRes('yuzde', 'Tanımsız'); return; } res = ((b - a) / a) * 100; const direction = res > 0 ? 'Artış' : 'Azalış'; desc = `${a} -> ${b} değişim: %${Math.abs(res).toFixed(2)} ${direction}`; } else if (m === 3) { res = a * (1 + b / 100); desc = `${a} + %${b}`; } else if (m === 4) { res = a * (1 - b / 100); desc = `${a} - %${b}`; } showRes('yuzde', res.toLocaleString('tr-TR', {maximumFractionDigits: 2}), desc); }
function calc_bmi() { const h=getNum('bmi','h')/100, w=getNum('bmi','w'), b=w/(h*h); showRes('bmi', b.toFixed(2), b<25?'Normal':b<30?'Fazla Kilo':'Obez'); }
function calc_yas() { const d=new Date(getVal('yas','date')), n=new Date(); let a=n.getFullYear()-d.getFullYear(), m=n.getMonth()-d.getMonth(); if(m<0||(m===0&&n.getDate()<d.getDate()))a--; showRes('yas', a+' Yaş'); }
function calc_zam() { const s=getNum('zam','curr'), r=getNum('zam','rate'); showRes('zam', (s*(1+r/100)).toFixed(2)+' TL'); }
function calc_indirim() { const p=getNum('indirim','price'), r=getNum('indirim','rate'); showRes('indirim', (p*(1-r/100)).toFixed(2)+' TL'); }
function calc_net_brut() { showRes('net_brut', (getNum('net_brut','net')/0.7149).toFixed(2)+' TL', 'Tahmini Hesap (2026 Ocak)'); }

function calc_brut_net() {
    // --- 2026 PARAMETERS (EDIT HERE) ---
    const MIN_WAGE_GROSS = 33030; // 2026 Tahmini Brüt Asgari Ücret
    const SGK_RATE = 0.14;
    const UNEMP_RATE = 0.01;
    const DAMGA_RATE = 0.00759;

    // 2026 Gelir Vergisi Dilimleri (Tahmini)
    const TAX_BRACKETS = [
        { limit: 158000, rate: 0.15 },
        { limit: 380000, rate: 0.20 },
        { limit: 870000, rate: 0.27 },
        { limit: 4300000, rate: 0.35 },
        { limit: Infinity, rate: 0.40 }
    ];
    // ------------------------------------

    const inputGross = getNum('brut_net', 'brut');
    const selectedMonth = parseInt(getVal('brut_net', 'month')) || 1; // 1-12
    const selectedYear = getVal('brut_net', 'year') || '2026';

    if (inputGross <= 0) {
        showRes('brut_net', '0,00 TL', 'Lütfen geçerli bir brüt maaş giriniz.');
        return;
    }

    let cumMatrahUser = 0;
    let cumMatrahMin = 0;

    let results = [];
    let targetResult = null;

    // Helper: Calculate Tax for a specific base amount given the cumulative progress
    const calcTax = (matrah, cumulative) => {
        let remaining = matrah;
        let currentCum = cumulative;
        let tax = 0;

        for (let i = 0; i < TAX_BRACKETS.length; i++) {
            if (remaining <= 0) break;

            const bracket = TAX_BRACKETS[i];
            const prevLimit = i === 0 ? 0 : TAX_BRACKETS[i - 1].limit;
            const limit = bracket.limit;
            const rate = bracket.rate;

            // Available space in this bracket
            const space = limit - currentCum; // How much room left in this bracket from cumulative start

            if (space > 0) {
                // If we have space, tax as much of 'remaining' as fits
                const amountInBracket = Math.min(remaining, space);
                tax += amountInBracket * rate;
                remaining -= amountInBracket;
                currentCum += amountInBracket;
            } else {
                // We are already past this bracket, continue to next higher bracket
                continue;
            }
        }
        return tax;
    };

    // Iterate 12 Months
    for (let m = 1; m <= 12; m++) {
        // 1. User Calculation
        const sgkUser = inputGross * SGK_RATE;
        const unempUser = inputGross * UNEMP_RATE;
        const matrahUser = inputGross - sgkUser - unempUser;

        const taxUser = calcTax(matrahUser, cumMatrahUser);
        cumMatrahUser += matrahUser;

        // 2. Min Wage Calculation (Exemption Base)
        const sgkMin = MIN_WAGE_GROSS * SGK_RATE;
        const unempMin = MIN_WAGE_GROSS * UNEMP_RATE;
        const matrahMin = MIN_WAGE_GROSS - sgkMin - unempMin;

        const taxMin = calcTax(matrahMin, cumMatrahMin);
        cumMatrahMin += matrahMin; // Important: Min wage cumulative base also grows

        // 3. Exemption Application
        // The exemption is the TAX calculated on the Min Wage
        const exemptTax = taxMin;
        const exemptDamga = MIN_WAGE_GROSS * DAMGA_RATE;

        // 4. Final Payables
        const finalTax = Math.max(0, taxUser - exemptTax);
        const calcDamga = inputGross * DAMGA_RATE;
        const finalDamga = Math.max(0, calcDamga - exemptDamga);

        const totalDeductions = sgkUser + unempUser + finalTax + finalDamga;
        const netSalary = inputGross - totalDeductions;

        const monthData = {
            month: m,
            gross: inputGross,
            sgk: sgkUser,
            unemp: unempUser,
            tax: finalTax,
            damga: finalDamga,
            net: netSalary,
            totalDed: totalDeductions
        };

        results.push(monthData);
        if (m === selectedMonth) targetResult = monthData;
    }

    // Display Main Result (Card)
    const f = (n) => n.toLocaleString('tr-TR', { minimumFractionDigits: 2, maximumFractionDigits: 2 }) + ' TL';

    // Update Result Card
    document.getElementById('val-brut_net').innerText = f(targetResult.net);
    document.getElementById('detail-brut_net').innerHTML = `
        <div class="grid grid-cols-2 gap-2 text-xs">
            <span>SGK Primi:</span> <span class="font-bold">${f(targetResult.sgk)}</span>
            <span>İşsizlik Sig.:</span> <span class="font-bold">${f(targetResult.unemp)}</span>
            <span>Gelir Vergisi:</span> <span class="font-bold">${f(targetResult.tax)}</span>
            <span>Damga Vergisi:</span> <span class="font-bold">${f(targetResult.damga)}</span>
            <span class="text-indigo-600 font-bold mt-1">Toplam Kesinti:</span> <span class="font-bold mt-1 text-indigo-600">${f(targetResult.totalDed)}</span>
        </div>
    `;

    // Render Table
    const tableContainer = document.getElementById('table-brut_net_container');
    if(tableContainer) {
        let html = `
        <div class="overflow-x-auto mt-6 border border-slate-200 rounded-xl">
            <table class="w-full text-xs text-left text-slate-600">
                <thead class="bg-slate-50 text-slate-700 font-bold border-b border-slate-200">
                    <tr>
                        <th class="p-3">Ay</th>
                        <th class="p-3">Brüt</th>
                        <th class="p-3">SGK + İşsizlik</th>
                        <th class="p-3">G. Vergisi</th>
                        <th class="p-3">Damga</th>
                        <th class="p-3 text-indigo-700">NET MAAŞ</th>
                    </tr>
                </thead>
                <tbody class="divide-y divide-slate-100">
        `;

        const monthNames = ["Ocak", "Şubat", "Mart", "Nisan", "Mayıs", "Haziran", "Temmuz", "Ağustos", "Eylül", "Ekim", "Kasım", "Aralık"];

        results.forEach(r => {
            const isSelected = r.month === selectedMonth;
            const rowClass = isSelected ? "bg-indigo-50 font-semibold" : "hover:bg-slate-50";
            const sgkTotal = r.sgk + r.unemp;

            html += `
                <tr class="${rowClass} transition">
                    <td class="p-3">${monthNames[r.month-1]}</td>
                    <td class="p-3">${f(r.gross)}</td>
                    <td class="p-3">${f(sgkTotal)}</td>
                    <td class="p-3">${f(r.tax)}</td>
                    <td class="p-3">${f(r.damga)}</td>
                    <td class="p-3 font-bold text-indigo-700">${f(r.net)}</td>
                </tr>
            `;
        });

        html += `</tbody></table></div>`;
        tableContainer.innerHTML = html;
        tableContainer.classList.remove('hidden');
    }

    const rDiv = document.getElementById('res-brut_net');
    rDiv.classList.remove('hidden');
    rDiv.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
}

function calc_mevduat() { showRes('mevduat', (getNum('mevduat','amt')*getNum('mevduat','rate')*getNum('mevduat','days')/36500*0.95).toFixed(2)+' TL'); }
function calc_iban() { const i=getVal('iban','code'); showRes('iban', i.length===26&&i.startsWith('TR')?'Geçerli':'Geçersiz'); }
function calc_idealkilo() { const h=getNum('idealkilo','h'), k=getVal('idealkilo','g')==0?50+0.9*(h-152):45.5+0.9*(h-152); showRes('idealkilo', Math.round(k)+' kg'); }
function calc_bmr() { const w=getNum('bmr','w'), h=getNum('bmr','h'), a=getNum('bmr','a'), g=getVal('bmr','g'); showRes('bmr', Math.round(g==0?10*w+6.25*h-5*a+5:10*w+6.25*h-5*a-161)+' kcal'); }
function calc_makro() { const c=getNum('makro','cal'); showRes('makro', `P:${Math.round(c*0.3/4)}g K:${Math.round(c*0.4/4)}g Y:${Math.round(c*0.3/9)}g`); }
function calc_nabiz() { showRes('nabiz', (220-getNum('nabiz','age'))+' bpm'); }
function calc_su() { showRes('su', (getNum('su','w')*0.033).toFixed(1)+' Lt'); }
function calc_gebelik() { const d=new Date(getVal('gebelik','date')); d.setDate(d.getDate()+280); showRes('gebelik', d.toLocaleDateString('tr-TR')); }
function calc_sinav() { const r=getNum('sinav','v')*0.4+getNum('sinav','f')*0.6; showRes('sinav', r.toFixed(1), r>=50?'Geçti':'Kaldı'); }
function calc_takdir() { const a=getNum('takdir','avg'); showRes('takdir', a>=85?'Takdir':a>=70?'Teşekkür':'Boş'); }
function calc_dikdortgen() { showRes('dikdortgen', (getNum('dikdortgen','w')*getNum('dikdortgen','h'))+' m²'); }
function calc_kelime() { showRes('kelime', getVal('kelime','txt').trim().split(/\s+/).filter(x=>x).length+' Kelime'); }
function calc_internet() { showRes('internet', ((getNum('internet','size')*8192)/getNum('internet','spd')/60).toFixed(1)+' Dk'); }
function calc_gun() { const d1=new Date(getVal('gun','d1')), d2=new Date(getVal('gun','d2')); showRes('gun', Math.floor(Math.abs((d2-d1)/864e5))+' Gün'); }
function calc_hiz() { showRes('hiz', (getNum('hiz','km')/getNum('hiz','hr')).toFixed(1)+' km/s'); }
function calc_karzarar() { const c=getNum('karzarar','cost'), s=getNum('karzarar','sell'); showRes('karzarar', '%'+((s-c)/c*100).toFixed(1)); }
function calc_bilesik() { const p=getNum('bilesik','p'), r=getNum('bilesik','r'), t=getNum('bilesik','t'); showRes('bilesik', (p*Math.pow(1+r/100,t)).toFixed(2)+' TL'); }
function calc_kk_asgari() { const l=getNum('kk_asgari','lim'), d=getNum('kk_asgari','debt'); showRes('kk_asgari', (d*(l>25000?0.4:0.2)).toFixed(2)+' TL'); }
function calc_komisyon() { showRes('komisyon', (getNum('komisyon','price')*0.02*1.2).toFixed(2)+' TL'); }
function calc_day() { const d = new Date(getVal('day', 'date')); if(isNaN(d)) return; showRes('day', d.toLocaleDateString('tr-TR', { weekday: 'long' }), d.toLocaleDateString('tr-TR', { day: 'numeric', month: 'long', year: 'numeric' })); }
function calc_date_add() { const d = new Date(getVal('add', 'date')); const days = getNum('add', 'days'); if(isNaN(d)) return; d.setDate(d.getDate() + days); showRes('date-add', d.toLocaleDateString('tr-TR', { day: 'numeric', month: 'long', year: 'numeric', weekday: 'long' }), (days>0?'+':'') + days + ' gün sonrası'); }
function calc_vf() { const v = getNum('vf', 'vize'); const f = getNum('vf', 'final'); const r = parseFloat(getVal('vf', 'ratio')); const avg = (v * r) + (f * (1 - r)); const status = avg >= 50 ? 'GEÇTİ' : 'KALDI'; const color = avg >= 50 ? 'text-green-600' : 'text-red-600'; showRes('vf', `<span class="${color}">${avg.toFixed(1)}</span>`, `Durum: <strong>${status}</strong> (Vize: %${r*100}, Final: %${(1-r)*100})`); }
function addGpaRow() { const container = document.getElementById('gpa-rows'); const div = document.createElement('div'); div.className = 'grid grid-cols-12 gap-2 items-center gpa-row'; div.innerHTML = `<div class="col-span-6 md:col-span-5"><input type="text" placeholder="Ders" class="w-full p-3 border border-slate-200 rounded-lg bg-slate-50 text-sm"></div><div class="col-span-3 md:col-span-3"><input type="number" placeholder="Kr" value="3" class="w-full p-3 border border-slate-200 rounded-lg bg-slate-50 text-sm gpa-credit"></div><div class="col-span-3 md:col-span-3"><select class="w-full p-3 border border-slate-200 rounded-lg bg-slate-50 text-sm gpa-grade"><option value="4.0">AA (4.0)</option><option value="3.5">BA (3.5)</option><option value="3.0">BB (3.0)</option><option value="2.5">CB (2.5)</option><option value="2.0">CC (2.0)</option><option value="1.5">DC (1.5)</option><option value="1.0">DD (1.0)</option><option value="0.5">FD (0.5)</option><option value="0.0">FF (0.0)</option></select></div><div class="col-span-1 text-center"><button onclick="this.closest('.gpa-row').remove()" class="text-red-400 hover:text-red-600"><i class="fa-solid fa-trash"></i></button></div>`; container.appendChild(div); }
function calc_gpa() { const credits = document.querySelectorAll('.gpa-credit'); const grades = document.querySelectorAll('.gpa-grade'); let totalC = 0, totalP = 0; credits.forEach((c, i) => { const cr = parseFloat(c.value) || 0; const gr = parseFloat(grades[i].value) || 0; totalC += cr; totalP += cr * gr; }); if(totalC === 0) return; const gpa = totalP / totalC; showRes('gpa', gpa.toFixed(2), `Toplam Kredi: ${totalC} | Başarı Notu: ${gpa.toFixed(2)}/4.00`); }
function calc_asgari() { const p = getVal('asgari', 'period'); const t = getVal('asgari', 'type'); let net = 28500; let gross = 33530; if(p === '2025-2') { net = 20002; gross = 23532; } if(t === 'bn') { showRes('asgari', `${net.toLocaleString()} TL (Net)`, `Tahmini Brüt: ${gross.toLocaleString()} TL`); } else { showRes('asgari', `${gross.toLocaleString()} TL (Brüt)`, `Tahmini Net: ${net.toLocaleString()} TL`); } }
function calc_memur() { const curr = getNum('memur', 'curr'); const rate = getNum('memur', 'rate'); const newVal = curr * (1 + rate / 100); showRes('memur', `${newVal.toLocaleString('tr-TR', {maximumFractionDigits: 0})} TL`, `Artış Oranı: %${rate} | Fark: ${(newVal-curr).toLocaleString('tr-TR', {maximumFractionDigits:0})} TL`); }

function calc_commission() {
    const sell = getNum('comm', 'sell');
    const buy = getNum('comm', 'buy');
    const rate = getNum('comm', 'rate');
    const kdv = getNum('comm', 'kdv');
    const cargo = getNum('comm', 'cargo');
    const service = document.getElementById('comm-service') ? getNum('comm', 'service') : 0;
    const trans = document.getElementById('comm-trans') ? getNum('comm', 'trans') : 0;
    const listing = document.getElementById('comm-listing') ? getNum('comm', 'listing') : 0;
    const ad = document.getElementById('comm-ad') ? getNum('comm', 'ad') : 0;
    const stopajRate = document.getElementById('comm-stopaj') ? getNum('comm', 'stopaj') : 0;

    const serviceVatRate = 0.20;
    const productVatRate = kdv / 100;

    const netSell = sell / (1 + productVatRate);
    const outputVat = sell - netSell;

    const grossCommission = sell * (rate / 100);
    const netCommission = grossCommission / (1 + serviceVatRate);
    const vatCommission = grossCommission - netCommission;

    const netBuy = buy / (1 + productVatRate);
    const inputVatProduct = buy - netBuy;

    const netCargo = cargo / (1 + serviceVatRate);
    const vatCargo = cargo - netCargo;

    const netService = service / (1 + serviceVatRate);
    const vatService = service - netService;

    const netTrans = trans / (1 + serviceVatRate);
    const vatTrans = trans - netTrans;

    const netListing = listing / (1 + serviceVatRate);
    const vatListing = listing - netListing;

    const netAd = ad / (1 + serviceVatRate);
    const vatAd = ad - netAd;

    // Stopaj Calculation: Applied to platform fees (Commission, Service, Listing, Transaction, Ad)
    // Excluding Cargo from Stopaj base as it's often a pass-through or separate logic, but including others.
    const stopajBase = grossCommission + service + listing + trans + ad;
    const stopajAmount = stopajBase * (stopajRate / 100);

    const totalGrossExpenses = buy + grossCommission + cargo + service + trans + listing + ad + stopajAmount;
    const totalInputVat = inputVatProduct + vatCommission + vatCargo + vatService + vatTrans + vatListing + vatAd;
    const payableVat = Math.max(0, outputVat - totalInputVat);
    const netProfit = sell - totalGrossExpenses - payableVat;
    const margin = sell > 0 ? (netProfit / sell) * 100 : 0;

    const f = (n) => n.toLocaleString('tr-TR', { minimumFractionDigits: 2, maximumFractionDigits: 2 });

    if(document.getElementById('res-comm-profit')) document.getElementById('res-comm-profit').innerText = f(netProfit) + ' TL';
    if(document.getElementById('res-comm-margin')) document.getElementById('res-comm-margin').innerText = '%' + f(margin);
    if(document.getElementById('res-comm-vat')) document.getElementById('res-comm-vat').innerText = f(payableVat) + ' TL';
    if(document.getElementById('res-comm-comm')) document.getElementById('res-comm-comm').innerText = f(grossCommission) + ' TL';
    if(document.getElementById('res-comm-stopaj')) document.getElementById('res-comm-stopaj').innerText = f(stopajAmount) + ' TL';

    // Total Expenses (Excluding Buying Price as per label "Alış Hariç")
    // Total Gross Expenses includes 'buy'. We subtract it.
    // We also add Payable VAT as an expense.
    const totalOpExpenses = (totalGrossExpenses - buy) + payableVat;
    if(document.getElementById('res-comm-total')) document.getElementById('res-comm-total').innerText = f(totalOpExpenses) + ' TL';

    const resDiv = document.getElementById('res-commission');
    if(resDiv) {
        resDiv.classList.remove('hidden');
        resDiv.scrollIntoView({behavior:'smooth', block:'nearest'});
    }
}

// Run Init

function populateInflationDropdowns() {
    const start = document.getElementById('enflasyon-start');
    const end = document.getElementById('enflasyon-end');
    if(!start || !end) return;

    start.innerHTML = '';
    end.innerHTML = '';

    const years = Object.keys(window.cpi_data).sort();

    years.forEach(y => {
        const opt1 = document.createElement('option'); opt1.value=y; opt1.text=y;
        const opt2 = document.createElement('option'); opt2.value=y; opt2.text=y;
        start.appendChild(opt1);
        end.appendChild(opt2);
    });

    // Defaults
    start.value = "2020";
    end.value = "2026";
}

window.addEventListener('load', () => {
    checkCookies();
    initDrawer();
    renderSidebar();
    populateInflationDropdowns();

    // Remove legacy conflicting handlers if present on current page inputs
    const msInput = document.getElementById('mobile-tool-search');
    if(msInput) msInput.removeAttribute('onkeyup'); // Remove static HTML binding to prefer JS binding below

    // Mobile Search Suggestions Logic
    const ms = document.getElementById('mobile-tool-search');
    const sg = document.getElementById('search-suggestions');
    const msl = document.getElementById('mobile-search-results-list');
    const msh = document.getElementById('mobile-search-header');

    if(ms && sg && msl) {
        const renderMobileResults = (query) => {
            msl.innerHTML = '';
            let filtered = [];

            if (!query) {
                if(msh) msh.innerText = "POPÜLER ARAÇLAR";
                filtered = tools.filter(t => ['kdv', 'kredi', 'tevkifat', 'net_brut', 'bmi'].includes(t.id));
            } else {
                if(msh) msh.innerText = "ARAMA SONUÇLARI";
                filtered = tools.filter(t =>
                    t.name.toLowerCase().includes(query) ||
                    t.cat.toLowerCase().includes(query)
                );
            }

            if(filtered.length === 0) {
                msl.innerHTML = '<div class="p-3 text-xs text-slate-500 text-center">Sonuç bulunamadı.</div>';
                return;
            }

            filtered.forEach(t => {
                const a = document.createElement('a');
                a.href = t.link;
                a.className = 'block px-3 py-2 text-sm text-slate-600 hover:bg-blue-50 hover:text-blue-600 rounded flex items-center gap-2 mb-1';

                let iconClass = 'fa-calculator';
                if(t.cat === 'Finans') iconClass = 'fa-coins';
                if(t.cat === 'Sağlık') iconClass = 'fa-heart-pulse';
                if(t.cat === 'Eğitim') iconClass = 'fa-graduation-cap';
                if(t.cat === 'Yapay Zeka') iconClass = 'fa-wand-magic-sparkles';
                if(t.cat === 'E-Ticaret') iconClass = 'fa-shop';

                a.innerHTML = `<i class="fa-solid ${iconClass} text-blue-400 w-4 text-center"></i> ${t.name}`;
                msl.appendChild(a);
            });
        };

        ms.addEventListener('focus', () => { sg.classList.remove('hidden'); if(ms.value === '') renderMobileResults(''); });
        ms.addEventListener('input', () => { sg.classList.remove('hidden'); renderMobileResults(ms.value.toLowerCase()); });
        ms.addEventListener('blur', () => { setTimeout(() => sg.classList.add('hidden'), 200); });
    }

    // Desktop Search Suggestions Logic
    const ds = document.getElementById('desktop-tool-search');
    const dsg = document.getElementById('desktop-search-suggestions');
    const dsl = document.getElementById('desktop-search-results-list');
    const dsh = document.getElementById('desktop-search-header');

    if(ds && dsg && dsl) {
        const renderDesktopResults = (query) => {
            dsl.innerHTML = '';
            let filtered = [];

            if (!query) {
                if(dsh) dsh.innerText = "POPÜLER ARAÇLAR";
                filtered = tools.filter(t => ['kdv', 'kredi', 'tevkifat', 'net_brut', 'bmi'].includes(t.id));
            } else {
                if(dsh) dsh.innerText = "ARAMA SONUÇLARI";
                filtered = tools.filter(t =>
                    t.name.toLowerCase().includes(query) ||
                    t.cat.toLowerCase().includes(query)
                );
            }

            if(filtered.length === 0) {
                dsl.innerHTML = '<div class="p-4 text-xs text-slate-500 text-center">Sonuç bulunamadı.</div>';
                return;
            }

            filtered.forEach(t => {
                const a = document.createElement('a');
                a.href = t.link;
                a.className = 'block px-4 py-3 text-xs font-medium text-slate-600 hover:bg-blue-50 hover:text-blue-600 transition flex items-center gap-3 border-b border-slate-50 last:border-0';

                let iconClass = 'fa-calculator';
                if(t.cat === 'Finans') iconClass = 'fa-coins';
                if(t.cat === 'Sağlık') iconClass = 'fa-heart-pulse';
                if(t.cat === 'Eğitim') iconClass = 'fa-graduation-cap';
                if(t.cat === 'Yapay Zeka') iconClass = 'fa-wand-magic-sparkles';
                if(t.cat === 'E-Ticaret') iconClass = 'fa-shop';

                a.innerHTML = `<i class="fa-solid ${iconClass} text-blue-400 w-4 text-center"></i> ${t.name}`;
                dsl.appendChild(a);
            });
        };

        ds.addEventListener('focus', () => { dsg.classList.remove('hidden'); if(ds.value === '') renderDesktopResults(''); });
        ds.addEventListener('input', () => { dsg.classList.remove('hidden'); renderDesktopResults(ds.value.toLowerCase()); });
        ds.addEventListener('blur', () => { setTimeout(() => dsg.classList.add('hidden'), 200); });
    }

    const urlParams = new URLSearchParams(window.location.search);
    const q = urlParams.get('q');
    if (q) {
        const input = document.getElementById('ai_asistan-q');
        if (input) { input.value = q; setTimeout(() => { calc_ai_asistan(); }, 500); }
    }
});
