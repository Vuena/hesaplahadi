// API Key Obfuscation
const _k = "QUl6YVN5Qzh6SGxSTkZvck1peW5tM01qUnFNc3RvWjRNczBwQVdR";
const apiKey = atob(_k);

// --- TOOL CONFIGURATION (Central Source of Truth) ---
const tools = [
    // 1. YAPAY ZEKA
    { id: 'ai_asistan', cat: 'Yapay Zeka', name: 'AI Hesaplama Asistanı', link: 'ai-asistan.html', color:'indigo' },

    // 2. FİNANS & VERGİ
    { id: 'kdv', cat: 'Finans', name: 'KDV Hesaplama', link: 'kdv-hesaplama.html', color:'blue', inputs: [{}, {opts:['%1','%10','%20']}] },
    { id: 'tevkifat', cat: 'Finans', name: 'KDV Tevkifat Hesaplama', link: 'tevkifat-hesaplama.html', color:'blue' },
    { id: 'kidem', cat: 'Finans', name: 'Kıdem Tazminatı', link: 'kidem-tazminati.html', color:'blue' },
    { id: 'kredi', cat: 'Finans', name: 'Kredi Hesaplama', link: 'kredi-hesaplama.html', color:'blue' },
    { id: 'net_brut', cat: 'Finans', name: 'Netten Brüte Maaş', link: 'netten-brute-maas-hesaplama-2026.html', color:'blue' },
    { id: 'brut_net', cat: 'Finans', name: 'Brütten Nete Maaş', link: 'brutten-nete-maas-hesaplama-2026.html', color:'blue' },
    { id: 'mevduat', cat: 'Finans', name: 'Mevduat Getirisi', link: 'mevduat-faizi-hesaplama.html', color:'blue' },
    { id: 'iban', cat: 'Finans', name: 'IBAN Doğrulama', link: 'iban-dogrulama-ve-cozumleme-araci.html', color:'blue' },
    { id: 'indirim', cat: 'Finans', name: 'İndirim Hesaplama', link: 'i̇ndirim-hesaplama.html', color:'blue' },
    { id: 'karzarar', cat: 'Finans', name: 'Kâr Marjı', link: 'kâr-marji-ve-zarar-hesaplama.html', color:'blue' },
    { id: 'bilesik', cat: 'Finans', name: 'Bileşik Faiz', link: 'bilesik-faiz-hesaplama.html', color:'blue' },
    { id: 'kk_asgari', cat: 'Finans', name: 'K.K. Asgari Ödeme', link: 'kredi-karti-asgari-odeme-hesaplama.html', color:'blue' },
    { id: 'komisyon', cat: 'Finans', name: 'Emlak Komisyonu', link: 'emlakci-komisyonu-hesaplama.html', color:'blue' },
    { id: 'zam', cat: 'Finans', name: 'Maaş Zam', link: 'maas-zam-orani-hesaplama.html', color:'blue' },

    // 3. SAĞLIK
    { id: 'ai_diyet', cat: 'Sağlık', name: 'AI Diyetisyen', link: 'ai-diyetisyen.html', color:'indigo' },
    { id: 'bmi', cat: 'Sağlık', name: 'Vücut Kitle İndeksi', link: 'vucut-kitle-i̇ndeksi-bmi-hesaplama.html', color:'green' },
    { id: 'idealkilo', cat: 'Sağlık', name: 'İdeal Kilo', link: 'i̇deal-kilo-hesaplama.html', color:'green' },
    { id: 'bmr', cat: 'Sağlık', name: 'Bazal Metabolizma', link: 'bazal-metabolizma-hizi-bmr-hesaplama.html', color:'green' },
    { id: 'makro', cat: 'Sağlık', name: 'Günlük Makro İhtiyacı', link: 'gunluk-makro-protein,-karbonhidrat,-yag-hesaplama.html', color:'green' },
    { id: 'su', cat: 'Sağlık', name: 'Su Tüketimi', link: 'gunluk-su-i̇htiyaci-hesaplama.html', color:'green' },
    { id: 'gebelik', cat: 'Sağlık', name: 'Doğum Tarihi (SAT)', link: 'gebelik-hesaplama-ve-dogum-tarihi.html', color:'green' },
    { id: 'sigara', cat: 'Sağlık', name: 'Sigara Maliyeti', link: 'sigara-maliyeti-hesaplama.html', color:'green' },
    { id: 'nabiz', cat: 'Sağlık', name: 'Spor Nabız Aralığı', link: 'spor-nabiz-araligi-hesaplama.html', color:'green' },

    // 4. EĞİTİM & MATEMATİK
    { id: 'yuzde', cat: 'Eğitim', name: 'Yüzde Hesaplama', link: 'yuzde-hesaplama-araci.html', color:'purple' },
    { id: 'sinav', cat: 'Eğitim', name: 'Üniversite Not Ort.', link: 'universite-not-ortalamasi-vize-final-hesaplama.html', color:'purple' },
    { id: 'takdir', cat: 'Eğitim', name: 'Takdir / Teşekkür', link: 'takdir-tesekkur-hesaplama-e-okul.html', color:'purple' },
    { id: 'dikdortgen', cat: 'Eğitim', name: 'Alan Hesaplama', link: 'dikdortgen-alan-ve-cevre-hesaplama.html', color:'purple' },
    { id: 'kelime', cat: 'Eğitim', name: 'Kelime Sayacı', link: 'kelime-ve-karakter-sayaci.html', color:'purple' },
    { id: 'vf', cat: 'Eğitim', name: 'Vize Final Hesaplama', link: 'vize-final-hesaplama.html', color:'purple' },
    { id: 'gpa', cat: 'Eğitim', name: 'Not Ortalaması (GNO)', link: 'universite-not-ortalamasi-hesaplama.html', color:'purple' },

    // 5. PRATİK & ARAÇLAR
    { id: 'day', cat: 'Pratik', name: 'Hangi Gün?', link: 'hangi-gun-hesaplama.html', color:'orange' },
    { id: 'date_add', cat: 'Pratik', name: 'Tarihe Gün Ekle', link: 'tarihe-gun-ekleme-hesaplama.html', color:'orange' },
    { id: 'asgari', cat: 'Finans', name: '2026 Asgari Ücret', link: 'asgari-ucret-hesaplama.html', color:'blue' },
    { id: 'memur', cat: 'Finans', name: '2026 Memur Zammı', link: 'memur-maas-zammi-hesaplama.html', color:'blue' },
    { id: 'internet', cat: 'Pratik', name: 'İndirme Süresi', link: 'i̇nternet-hizi-i̇ndirme-suresi-hesaplama.html', color:'orange' },
    { id: 'yakit', cat: 'Pratik', name: 'Yakıt Tüketimi', link: 'yakit-tuketimi-hesaplama.html', color:'orange' },
    { id: 'yas', cat: 'Pratik', name: 'Tam Yaş Hesaplama', link: 'tam-yas-hesaplama.html', color:'orange' },
    { id: 'gun', cat: 'Pratik', name: 'İki Tarih Arası', link: 'i̇ki-tarih-arasi-gun-sayaci.html', color:'orange' },
    { id: 'sifre', cat: 'Pratik', name: 'Güçlü Şifre Üret', link: 'guclu-sifre-olusturucu.html', color:'orange' },
    { id: 'hiz', cat: 'Pratik', name: 'Hız / Zaman', link: 'hiz,-yol-ve-zaman-hesaplama.html', color:'orange' }
];

// --- RENDER SIDEBAR ---
function renderSidebar() {
    const cats = [...new Set(tools.map(t => t.cat))];
    const currentPath = window.location.pathname.split('/').pop() || 'index.html';

    // Target both desktop sidebar and mobile drawer
    const containers = ['sidebar-list', 'drawer-list'];

    containers.forEach(id => {
        const container = document.getElementById(id);
        if(!container) return;
        container.innerHTML = ''; // Clear

        // Note: "All Tools" link explicitly removed for Mobile Drawer per request

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

                const icon = t.cat === 'Yapay Zeka' ? '<i class="fa-solid fa-wand-magic-sparkles text-indigo-500"></i>' : '<span class="w-1.5 h-1.5 rounded-full bg-slate-300"></span>';
                a.innerHTML = `${icon} ${t.name}`;
                container.appendChild(a);
            });
        });

        // Strict Cleanup: Remove any "Tüm Hesaplamalar" link if present
        const links = container.querySelectorAll('a');
        links.forEach(link => {
            const txt = link.innerText.toLowerCase();
            if(txt.includes('tüm hesaplama') || txt.includes('tum hesaplama')) {
                link.remove();
            }
        });
    });
}

// --- GEMINI API HELPER ---
async function callGemini(userPrompt, systemPrompt) {
    // Rate Limiting (50 requests per day)
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

            // Increment count on success
            localStorage.setItem('ai_daily_count', (count + 1).toString());
            return data.candidates[0].content.parts[0].text;
        } catch (error) {
            if (i === 2) throw error;
            await new Promise(r => setTimeout(r, 1000));
        }
    }
}

// --- COOKIE & UTILS ---
function checkCookies() { if(!localStorage.getItem('cookiesAccepted')) setTimeout(()=>document.getElementById('cookie-banner').classList.remove('translate-y-full'), 1000); }
function acceptCookies() { localStorage.setItem('cookiesAccepted','true'); document.getElementById('cookie-banner').classList.add('translate-y-full'); }

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

    // AI Help Link Injection
    const existingHelp = r.querySelector('.ai-help-link');
    if(existingHelp) existingHelp.remove();

    const tool = tools.find(t => t.id === id);
    if(tool && tool.cat !== 'Yapay Zeka' && !tool.id.startsWith('ai_')) {
        const div = document.createElement('div');
        div.className = 'mt-4 p-4 bg-indigo-50 border border-indigo-100 rounded-xl text-center shadow-sm ai-help-link block'; // Ensure display:block
        div.style.display = 'block';
        div.innerHTML = '<a href="ai-asistan.html" class="block text-xs font-bold text-indigo-600 hover:text-indigo-800 transition"><i class="fa-solid fa-wand-magic-sparkles mb-1 text-lg block"></i> Bir hata olduğunu mu düşünüyorsunuz? Ai Asistanımıza sormayı deneyin!</a>';
        r.appendChild(div);
    }

    r.classList.remove('hidden');
    r.scrollIntoView({behavior:'smooth', block:'nearest'});
}

// --- DRAWER FUNCTIONS (Global) ---
function toggleDrawer() {
    const d = document.getElementById('drawer');
    const m = document.getElementById('drawer-mask');
    if(!d || !m) return;

    if(d.classList.contains('drawer-closed')) {
        d.classList.remove('drawer-closed');
        d.classList.add('drawer-open');
        m.classList.remove('mask-hidden');
        m.classList.add('mask-visible');
    } else {
        d.classList.remove('drawer-open');
        d.classList.add('drawer-closed');
        m.classList.remove('mask-visible');
        m.classList.add('mask-hidden');
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
        const drawerHTML = `
    <div id="drawer-mask" class="fixed inset-0 bg-black/50 z-[90] transition-opacity duration-300 mask-hidden" onclick="toggleDrawer()"></div>
    <aside id="drawer" class="fixed top-0 left-0 w-64 h-full bg-white z-[100] shadow-2xl transition-transform duration-300 drawer-closed overflow-y-auto">
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
function calc_kdv() {
    const a=getNum('kdv','amt');
    const rIdx = getVal('kdv','rate');
    const rates = [0.01, 0.10, 0.20];
    const r = rates[rIdx];
    const t=getVal('kdv','type');
    let n,x,tot;
    if(t==0){n=a/(1+r);x=a-n;tot=a;}else{n=a;x=a*r;tot=a+x;}
    showRes('kdv', tot.toLocaleString('tr-TR',{minimumFractionDigits:2})+' TL', `Net: <strong>${n.toLocaleString('tr-TR',{minimumFractionDigits:2})}</strong> | KDV: <strong>${x.toLocaleString('tr-TR',{minimumFractionDigits:2})}</strong>`);
}

function calc_tevkifat() {
    const a=getNum('tevkifat','amt');
    const r=[0.01,0.1,0.2][getVal('tevkifat','rate')];
    const tn=[2,3,4,5,7,9][getVal('tevkifat','tev')];
    const t=getVal('tevkifat','type');
    let m,ft;
    if(t==1){m=a/(1+r);ft=a-m;}else{m=a;ft=a*r;}
    const w=ft*tn/10, d=ft-w, p=m+d;
    showRes('tevkifat', p.toLocaleString('tr-TR',{minimumFractionDigits:2})+' TL', `KDV: ${ft.toFixed(2)} | Tevkifat (${tn}/10): -${w.toFixed(2)} | Beyan: ${d.toFixed(2)}`);
}

function calc_kredi() {
    const p=getNum('kredi','amt'), t=getNum('kredi','term'), r=getNum('kredi','rate')/100;
    const x=Math.pow(1+r,t), pay=p*(r*x)/(x-1);
    showRes('kredi', pay.toLocaleString('tr-TR',{maximumFractionDigits:2})+' TL/Ay', `Toplam Geri Ödeme: ${(pay*t).toLocaleString('tr-TR')} TL`);
}

function calc_kidem() {
    const s = new Date(getVal('kidem','start')); const e = new Date(getVal('kidem','end')); let sal = getNum('kidem','salary');
    if (isNaN(s)||isNaN(e)||!sal) return;

    // 2026 Cap Estimate
    if (sal > 55000) sal = 55000; // Updated logic: If salary > cap, use cap. 55000 is approx estimate.

    const diffTime = Math.abs(e - s);
    const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));
    const tenureYears = diffDays / 365;

    let years = e.getFullYear() - s.getFullYear();
    let months = e.getMonth() - s.getMonth();
    let days = e.getDate() - s.getDate();
    if (days < 0) { months--; days += new Date(e.getFullYear(), e.getMonth(), 0).getDate(); }
    if (months < 0) { years--; months += 12; }

    const gross = sal * tenureYears;
    const net = gross * 0.99241;
    showRes('kidem', `${net.toLocaleString('tr-TR', {maximumFractionDigits: 2})} TL`, `${years} Yıl ${months} Ay ${days} Gün`);
}

async function calc_ai_asistan() {
    const q = getVal('ai_asistan', 'q');
    if(!q) return;
    showRes('ai_asistan', '<i class="fa-solid fa-spinner fa-spin"></i> Düşünüyorum...', '');
    try {
        const answer = await callGemini(q, "Sen yardımsever ve zeki bir hesaplama asistanısın. Kullanıcının matematiksel, finansal, mantıksal veya genel kültür sorularını Türkçe olarak yanıtla. Cevabın kısa, net ve anlaşılır olsun.");
        const formatted = answer.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>').replace(/\n/g, '<br>');
        showRes('ai_asistan', formatted);
    } catch (e) {
        showRes('ai_asistan', 'Bağlantı Hatası: ' + (e.message || 'Bilinmeyen hata'), 'API Anahtarınızı kontrol edip tekrar deneyin.');
    }
}

async function calc_ai_diyet() {
    const w = getVal('ai_diyet', 'w'), h = getVal('ai_diyet', 'h');
    const gIdx = getVal('ai_diyet', 'goal');
    const goals = ['Kilo Vermek', 'Kilo Almak', 'Formu Korumak', 'Kas Yapmak'];
    if(!w || !h) return;
    showRes('ai_diyet', '<i class="fa-solid fa-spinner fa-spin"></i> Plan hazırlanıyor...', '');
    const prompt = `Kilo: ${w}kg, Boy: ${h}cm, Hedef: ${goals[gIdx]}. Bana 1 günlük örnek bir beslenme planı oluştur.`;
    const sys = "Sen uzman bir diyetisyensin. Türkçe liste formatında yanıt ver.";
    try {
        const answer = await callGemini(prompt, sys);
        const formatted = answer.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>').replace(/\n/g, '<br>');
        showRes('ai_diyet', formatted);
    } catch (e) {
        showRes('ai_diyet', 'Plan oluşturulamadı: ' + (e.message || 'Hata'));
    }
}

// Updated Yuzde Calculation with 5 Modes
function calc_yuzde() {
    const m = parseInt(getVal('yuzde', 'mode'));
    const a = getNum('yuzde', 'a');
    const b = getNum('yuzde', 'b');
    let res = 0;
    let desc = "";

    // 0: A'nın %B'si
    // 1: A, B'nin % kaçı
    // 2: A->B Değişim
    // 3: A'yı %B Artır
    // 4: A'yı %B Azalt

    if (m === 0) {
        res = (a * b) / 100;
        desc = `${a} sayısının %${b}'si`;
    } else if (m === 1) {
        if(b === 0) { showRes('yuzde', 'Tanımsız'); return; }
        res = (a / b) * 100;
        desc = `${a}, ${b} sayısının %${res.toFixed(2)}'sidir`;
    } else if (m === 2) {
        if(a === 0) { showRes('yuzde', 'Tanımsız'); return; }
        res = ((b - a) / a) * 100;
        const direction = res > 0 ? 'Artış' : 'Azalış';
        desc = `${a} -> ${b} değişim: %${Math.abs(res).toFixed(2)} ${direction}`;
    } else if (m === 3) {
        res = a * (1 + b / 100);
        desc = `${a} + %${b}`;
    } else if (m === 4) {
        res = a * (1 - b / 100);
        desc = `${a} - %${b}`;
    }

    showRes('yuzde', res.toLocaleString('tr-TR', {maximumFractionDigits: 2}), desc);
}

// Others
function calc_bmi() { const h=getNum('bmi','h')/100, w=getNum('bmi','w'), b=w/(h*h); showRes('bmi', b.toFixed(2), b<25?'Normal':b<30?'Fazla Kilo':'Obez'); }
function calc_yas() { const d=new Date(getVal('yas','date')), n=new Date(); let a=n.getFullYear()-d.getFullYear(), m=n.getMonth()-d.getMonth(); if(m<0||(m===0&&n.getDate()<d.getDate()))a--; showRes('yas', a+' Yaş'); }
function calc_sifre() {
    const l=getNum('sifre','len');
    const charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+";
    let r = "";
    const values = new Uint32Array(l);
    crypto.getRandomValues(values);
    for(let i=0; i<l; i++) r += charset[values[i] % charset.length];
    showRes('sifre', r);
}
// Placeholder for others to ensure no errors if called
function calc_zam() { const s=getNum('zam','curr'), r=getNum('zam','rate'); showRes('zam', (s*(1+r/100)).toFixed(2)+' TL'); }
function calc_indirim() { const p=getNum('indirim','price'), r=getNum('indirim','rate'); showRes('indirim', (p*(1-r/100)).toFixed(2)+' TL'); }
function calc_net_brut() { showRes('net_brut', (getNum('net_brut','net')/0.7149).toFixed(2)+' TL', 'Tahmini Hesap (2026 Ocak)'); }
function calc_brut_net() { showRes('brut_net', (getNum('brut_net','brut')*0.7149).toFixed(2)+' TL', 'Tahmini Hesap (2026 Ocak)'); }
function calc_mevduat() { showRes('mevduat', (getNum('mevduat','amt')*getNum('mevduat','rate')*getNum('mevduat','days')/36500*0.95).toFixed(2)+' TL'); }
function calc_iban() { const i=getVal('iban','code'); showRes('iban', i.length===26&&i.startsWith('TR')?'Geçerli':'Geçersiz'); }
function calc_idealkilo() { const h=getNum('idealkilo','h'), k=getVal('idealkilo','g')==0?50+0.9*(h-152):45.5+0.9*(h-152); showRes('idealkilo', Math.round(k)+' kg'); }
function calc_bmr() { const w=getNum('bmr','w'), h=getNum('bmr','h'), a=getNum('bmr','a'), g=getVal('bmr','g'); showRes('bmr', Math.round(g==0?10*w+6.25*h-5*a+5:10*w+6.25*h-5*a-161)+' kcal'); }
function calc_makro() { const c=getNum('makro','cal'); showRes('makro', `P:${Math.round(c*0.3/4)}g K:${Math.round(c*0.4/4)}g Y:${Math.round(c*0.3/9)}g`); }
function calc_nabiz() { showRes('nabiz', (220-getNum('nabiz','age'))+' bpm'); }
function calc_su() { showRes('su', (getNum('su','w')*0.033).toFixed(1)+' Lt'); }
function calc_gebelik() { const d=new Date(getVal('gebelik','date')); d.setDate(d.getDate()+280); showRes('gebelik', d.toLocaleDateString('tr-TR')); }
function calc_sigara() { showRes('sigara', (getNum('sigara','price')*getNum('sigara','daily')*365).toLocaleString()+' TL/Yıl'); }
function calc_sinav() { const r=getNum('sinav','v')*0.4+getNum('sinav','f')*0.6; showRes('sinav', r.toFixed(1), r>=50?'Geçti':'Kaldı'); }
function calc_takdir() { const a=getNum('takdir','avg'); showRes('takdir', a>=85?'Takdir':a>=70?'Teşekkür':'Boş'); }
function calc_dikdortgen() { showRes('dikdortgen', (getNum('dikdortgen','w')*getNum('dikdortgen','h'))+' m²'); }
function calc_kelime() { showRes('kelime', getVal('kelime','txt').trim().split(/\s+/).filter(x=>x).length+' Kelime'); }
function calc_internet() { showRes('internet', ((getNum('internet','size')*8192)/getNum('internet','spd')/60).toFixed(1)+' Dk'); }
function calc_yakit() { showRes('yakit', ((getNum('yakit','km')/100)*getNum('yakit','lit')*getNum('yakit','pr')).toFixed(2)+' TL'); }
function calc_gun() { const d1=new Date(getVal('gun','d1')), d2=new Date(getVal('gun','d2')); showRes('gun', Math.floor(Math.abs((d2-d1)/864e5))+' Gün'); }
function calc_hiz() { showRes('hiz', (getNum('hiz','km')/getNum('hiz','hr')).toFixed(1)+' km/s'); }
function calc_karzarar() { const c=getNum('karzarar','cost'), s=getNum('karzarar','sell'); showRes('karzarar', '%'+((s-c)/c*100).toFixed(1)); }
function calc_bilesik() { const p=getNum('bilesik','p'), r=getNum('bilesik','r'), t=getNum('bilesik','t'); showRes('bilesik', (p*Math.pow(1+r/100,t)).toFixed(2)+' TL'); }
function calc_kk_asgari() { const l=getNum('kk_asgari','lim'), d=getNum('kk_asgari','debt'); showRes('kk_asgari', (d*(l>25000?0.4:0.2)).toFixed(2)+' TL'); }
function calc_komisyon() { showRes('komisyon', (getNum('komisyon','price')*0.02*1.2).toFixed(2)+' TL'); }

// New Tools Logic
function calc_day() {
    const d = new Date(getVal('day', 'date'));
    if(isNaN(d)) return;
    showRes('day', d.toLocaleDateString('tr-TR', { weekday: 'long' }), d.toLocaleDateString('tr-TR', { day: 'numeric', month: 'long', year: 'numeric' }));
}

function calc_date_add() {
    const d = new Date(getVal('add', 'date'));
    const days = getNum('add', 'days');
    if(isNaN(d)) return;
    d.setDate(d.getDate() + days);
    showRes('date-add', d.toLocaleDateString('tr-TR', { day: 'numeric', month: 'long', year: 'numeric', weekday: 'long' }), (days>0?'+':'') + days + ' gün sonrası');
}

function calc_vf() {
    const v = getNum('vf', 'vize');
    const f = getNum('vf', 'final');
    const r = parseFloat(getVal('vf', 'ratio'));
    const avg = (v * r) + (f * (1 - r));
    const status = avg >= 50 ? 'GEÇTİ' : 'KALDI'; // Simple assumption
    const color = avg >= 50 ? 'text-green-600' : 'text-red-600';
    showRes('vf', `<span class="${color}">${avg.toFixed(1)}</span>`, `Durum: <strong>${status}</strong> (Vize: %${r*100}, Final: %${(1-r)*100})`);
}

function addGpaRow() {
    const container = document.getElementById('gpa-rows');
    const div = document.createElement('div');
    div.className = 'grid grid-cols-12 gap-2 items-center gpa-row';
    div.innerHTML = `
        <div class="col-span-6 md:col-span-5"><input type="text" placeholder="Ders" class="w-full p-3 border border-slate-200 rounded-lg bg-slate-50 text-sm"></div>
        <div class="col-span-3 md:col-span-3"><input type="number" placeholder="Kr" value="3" class="w-full p-3 border border-slate-200 rounded-lg bg-slate-50 text-sm gpa-credit"></div>
        <div class="col-span-3 md:col-span-3">
            <select class="w-full p-3 border border-slate-200 rounded-lg bg-slate-50 text-sm gpa-grade">
                <option value="4.0">AA (4.0)</option><option value="3.5">BA (3.5)</option><option value="3.0">BB (3.0)</option>
                <option value="2.5">CB (2.5)</option><option value="2.0">CC (2.0)</option><option value="1.5">DC (1.5)</option>
                <option value="1.0">DD (1.0)</option><option value="0.5">FD (0.5)</option><option value="0.0">FF (0.0)</option>
            </select>
        </div>
        <div class="col-span-1 text-center"><button onclick="this.closest('.gpa-row').remove()" class="text-red-400 hover:text-red-600"><i class="fa-solid fa-trash"></i></button></div>
    `;
    container.appendChild(div);
}

function calc_gpa() {
    const credits = document.querySelectorAll('.gpa-credit');
    const grades = document.querySelectorAll('.gpa-grade');
    let totalC = 0, totalP = 0;
    credits.forEach((c, i) => {
        const cr = parseFloat(c.value) || 0;
        const gr = parseFloat(grades[i].value) || 0;
        totalC += cr;
        totalP += cr * gr;
    });
    if(totalC === 0) return;
    const gpa = totalP / totalC;
    showRes('gpa', gpa.toFixed(2), `Toplam Kredi: ${totalC} | Başarı Notu: ${gpa.toFixed(2)}/4.00`);
}

function calc_asgari() {
    const p = getVal('asgari', 'period');
    const t = getVal('asgari', 'type');

    // 2026 Estimates (Hypothetical)
    // 2025 July Estimate: ~20000 Net
    // 2026 Jan Estimate: ~25000 Net (Assumed 25% increase)
    let net = 25000;
    let gross = 30000; // Approx

    if(p === '2025-2') { net = 20002; gross = 23532; } // Approx values for late 2025

    if(t === 'bn') {
        showRes('asgari', `${net.toLocaleString()} TL (Net)`, `Tahmini Brüt: ${gross.toLocaleString()} TL`);
    } else {
        showRes('asgari', `${gross.toLocaleString()} TL (Brüt)`, `Tahmini Net: ${net.toLocaleString()} TL`);
    }
}

function calc_memur() {
    const curr = getNum('memur', 'curr');
    const rate = getNum('memur', 'rate');
    const newVal = curr * (1 + rate / 100);
    showRes('memur', `${newVal.toLocaleString('tr-TR', {maximumFractionDigits: 0})} TL`, `Artış Oranı: %${rate} | Fark: ${(newVal-curr).toLocaleString('tr-TR', {maximumFractionDigits:0})} TL`);
}

// Run Init
window.addEventListener('load', () => {
    checkCookies();
    initDrawer();
    renderSidebar();

    // Mobile Search Suggestions Logic
    const ms = document.getElementById('mobile-tool-search');
    const sg = document.getElementById('search-suggestions');
    if(ms && sg) {
        ms.addEventListener('focus', () => { if(ms.value === '') sg.classList.remove('hidden'); });
        ms.addEventListener('input', () => { if(ms.value !== '') sg.classList.add('hidden'); else sg.classList.remove('hidden'); });
        ms.addEventListener('blur', () => { setTimeout(() => sg.classList.add('hidden'), 200); });
    }

    // Check for AI Asistan query param
    const urlParams = new URLSearchParams(window.location.search);
    const q = urlParams.get('q');
    if (q) {
        // If we are on the ai-asistan page and have a query, auto-calc
        const input = document.getElementById('ai_asistan-q');
        if (input) {
            input.value = q;
            // Add a small delay for UI rendering before triggering
            setTimeout(() => {
               calc_ai_asistan();
            }, 500);
        }
    }
});
