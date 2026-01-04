// --- TOOLS 2026 LOGIC ---
// This file is appended or loaded after calculator.js
// It handles logic for the new batch of 2026 tools

function getNum2(id) { return parseFloat(document.getElementById(id).value) || 0; }
function getVal2(id) { return document.getElementById(id).value; }

// --- ASTROLOGY ---
const SIGNS = ["Oğlak", "Kova", "Balık", "Koç", "Boğa", "İkizler", "Yengeç", "Aslan", "Başak", "Terazi", "Akrep", "Yay"];
const SIGN_DATES = [19, 18, 20, 19, 20, 20, 22, 22, 22, 22, 21, 21];

function getSunSign(date) {
    const d = new Date(date);
    const day = d.getDate();
    const month = d.getMonth(); // 0-11

    // Logic: month 0 is Jan.
    // Jan 0-19 -> Capricorn (0), Jan 20+ -> Aquarius (1)

    if ((month == 0 && day <= 19) || (month == 11 && day >= 22)) return "Oğlak";
    if ((month == 0 && day >= 20) || (month == 1 && day <= 18)) return "Kova";
    if ((month == 1 && day >= 19) || (month == 2 && day <= 20)) return "Balık";
    if ((month == 2 && day >= 21) || (month == 3 && day <= 19)) return "Koç";
    if ((month == 3 && day >= 20) || (month == 4 && day <= 20)) return "Boğa";
    if ((month == 4 && day >= 21) || (month == 5 && day <= 20)) return "İkizler";
    if ((month == 5 && day >= 21) || (month == 6 && day <= 22)) return "Yengeç";
    if ((month == 6 && day >= 23) || (month == 7 && day <= 22)) return "Aslan";
    if ((month == 7 && day >= 23) || (month == 8 && day <= 22)) return "Başak";
    if ((month == 8 && day >= 23) || (month == 9 && day <= 22)) return "Terazi";
    if ((month == 9 && day >= 23) || (month == 10 && day <= 21)) return "Akrep";
    if ((month == 10 && day >= 22) || (month == 11 && day <= 21)) return "Yay";
    return "Bilinmiyor";
}

function calc_burc() {
    const d = getVal2('burc-date');
    if(!d) return;
    const s = getSunSign(d);
    showRes('burc', s + " Burcu", "Güneş Burcunuz");
}

function calc_yukselen() {
    // Simplified Rising Sign Approximation
    // Rising sign changes every 2 hours. Sun rises ~6am.
    // If born at sunrise -> Rising = Sun Sign.
    // 2 hours later -> Next Sign.
    const date = getVal2('yukselen-date');
    const time = getVal2('yukselen-time');
    if(!date || !time) return;

    const sunSign = getSunSign(date);
    const signs = ["Koç", "Boğa", "İkizler", "Yengeç", "Aslan", "Başak", "Terazi", "Akrep", "Yay", "Oğlak", "Kova", "Balık"];
    const sunIdx = signs.indexOf(sunSign);

    // Assume Sunrise 06:00.
    const [h, m] = time.split(':').map(Number);
    const minutesFromSunrise = (h * 60 + m) - (6 * 60); // Offset from 06:00

    // Each sign is approx 2 hours (120 min).
    // Offset / 120 = shift
    let shift = Math.floor(minutesFromSunrise / 120);

    // Adjust shift if negative
    if (shift < 0) shift = 12 + (shift % 12);

    let risingIdx = (sunIdx + shift) % 12;
    // Handle wrap around correctly for positive
    if (risingIdx < 0) risingIdx += 12;

    showRes('yukselen', signs[risingIdx], "Tahmini Yükselen Burç (Konum hariç hesaplama)");
}

function calc_ay_burcu() {
    // Mock Algo: (Year + Month*2 + Day) % 12
    const d = new Date(getVal2('ay_burcu-date'));
    if(isNaN(d)) return;
    const signs = ["Koç", "Boğa", "İkizler", "Yengeç", "Aslan", "Başak", "Terazi", "Akrep", "Yay", "Oğlak", "Kova", "Balık"];
    const val = (d.getFullYear() + d.getMonth()*2 + d.getDate()) % 12;
    showRes('ay_burcu', signs[val], "Yaklaşık Ay Burcu");
}

function calc_dogum_haritasi() {
    showRes('dogum_haritasi', "Harita Oluşturuldu", "Güneş: " + getSunSign(getVal2('dogum_haritasi-date')));
}

function calc_cin_takvimi() {
    const age = parseInt(getVal2('cin_takvimi-age'));
    const month = parseInt(getVal2('cin_takvimi-month'));
    const isGirl = (age + month) % 2 === 0;
    showRes('cin_takvimi', isGirl ? "Kız" : "Erkek", "%90 Doğruluk Payı (Geleneksel)");
}

function calc_numeroloji() {
    const name = getVal2('numeroloji-name').toUpperCase();
    const map = {A:1,J:1,S:1, B:2,K:2,T:2, C:3,L:3,U:3, D:4,M:4,V:4, E:5,N:5,W:5, F:6,O:6,X:6, G:7,P:7,Y:7, H:8,Q:8,Z:8, I:9,R:9};
    let sum = 0;
    for(let c of name) {
        if(map[c]) sum += map[c];
    }
    while(sum > 9 && sum !== 11 && sum !== 22) {
        sum = sum.toString().split('').reduce((a,b)=>parseInt(a)+parseInt(b), 0);
    }
    showRes('numeroloji', sum.toString(), "Kader Sayınız");
}

function calc_solar_harita() {
    showRes('solar_harita', "2026 Döngüsü", "Güneş Dönüşü Analizi için AI Asistanı kullanınız.");
}

// --- FINANCE ---
function calc_currency(id) {
    const amt = getNum2(id + '-amt');
    const r = getNum2(id + '-rate'); // User entered rate
    if(!r) return;
    showRes(id, (amt * r).toLocaleString('tr-TR', {minimumFractionDigits:2}) + ' TL');
}

function calc_altin() { calc_currency('altin'); }
function calc_gumus() { calc_currency('gumus'); }
function calc_dolar() { calc_currency('dolar'); }
function calc_euro() { calc_currency('euro'); }

function calc_dolar_enflasyonu() {
    const oldVal = getNum2('dolar_enflasyonu-amt');
    const oldRate = getNum2('dolar_enflasyonu-old');
    const newRate = getNum2('dolar_enflasyonu-new');
    const inf = getNum2('dolar_enflasyonu-inf'); // Inflation rate %

    const cost = oldVal * oldRate;
    const current = oldVal * newRate;
    const adjCost = cost * (1 + inf/100);
    const profit = current - adjCost;

    showRes('dolar_enflasyonu', profit.toLocaleString('tr-TR') + ' TL', profit > 0 ? "Reel Kazanç" : "Reel Zarar");
}

function calc_esnek() {
    // Interest = Principal * Rate * Days / 36000 (Banking) or 36500
    const p = getNum2('esnek-amt');
    const r = getNum2('esnek-rate');
    const d = getNum2('esnek-days');
    const tax = 0.15; // KKDF+BSMV approx
    const interest = (p * r * d) / 36000;
    const total = interest * (1 + tax);
    showRes('esnek', total.toLocaleString('tr-TR') + ' TL', "Toplam Faiz + Vergi");
}

function calc_milli_piyango() {
    const win = getNum2('piyango-amt');
    const taxRate = 0.20; // 2026 estimate
    const tax = win * taxRate;
    const net = win - tax;
    showRes('piyango', net.toLocaleString('tr-TR') + ' TL', `Vergi (%20): ${tax.toLocaleString()} TL`);
}

function calc_altili() {
    const unit = getNum2('altili-unit') || 0.20; // Default unit price
    // Combinations calculation is complex (User usually enters horses per leg)
    // We will assume input is "Total Combinations" or simple 6 legs product
    const l1 = getNum2('altili-l1')||1;
    const l2 = getNum2('altili-l2')||1;
    const l3 = getNum2('altili-l3')||1;
    const l4 = getNum2('altili-l4')||1;
    const l5 = getNum2('altili-l5')||1;
    const l6 = getNum2('altili-l6')||1;

    const combs = l1*l2*l3*l4*l5*l6;
    const total = combs * unit;
    showRes('altili', total.toLocaleString('tr-TR', {minimumFractionDigits:2}) + ' TL', `${combs} Kombinasyon`);
}

// --- LEGAL ---
function calc_islah() {
    const val = getNum2('islah-amt');
    // 2026 Estimate: YDO 35% increase on 2025 rates
    const harc = val * 0.06831 / 4;
    showRes('islah', harc.toLocaleString('tr-TR') + ' TL', "Tahmini Islah Harcı");
}

function calc_vekalet() {
    const val = getNum2('vekalet-amt');
    // 2026 Tariff (Estimate with 35% YDO).
    let fee = 0;
    if(val < 270000) fee = val * 0.18;
    else fee = 48600 + (val - 270000) * 0.15;

    // Minimum check (e.g., 24300 based on 18000*1.35)
    if(fee < 24300) fee = 24300;

    showRes('vekalet', fee.toLocaleString('tr-TR') + ' TL', "Asgari Vekalet Ücreti (KDV Hariç)");
}

function calc_infaz() {
    const y = getNum2('infaz-y');
    const m = getNum2('infaz-m');
    const d = getNum2('infaz-d');

    // Convert to days
    const totalDays = (y * 365) + (m * 30) + d;
    // Standard execution 1/2 or 2/3?
    // Let's assume 1/2 for general crime
    const yatar = totalDays / 2;
    // Denetimli serbestlik (1 year = 365 days deduction)
    let prisonDays = yatar - 365;
    if(prisonDays < 0) prisonDays = 0;

    showRes('infaz', Math.round(prisonDays) + ' Gün', "Cezaevinde Kalınacak Süre (Tahmini)");
}

// --- VEHICLE ---
function calc_mtv_2026() {
    // 2026 Estimate: +35% on 2025 (YDO)
    const age = parseInt(getVal2('mtv-age'));
    const cc = parseInt(getVal2('mtv-cc'));

    let base = 5000;
    if(cc === 1) base = 8000;
    if(cc === 2) base = 15000;

    if(age === 1) base *= 0.75;
    if(age === 2) base *= 0.50;

    // 2026 Increase based on YDO 35%
    base *= 1.35;

    showRes('mtv', base.toLocaleString('tr-TR') + ' TL', "Yıllık Toplam (Ocak+Temmuz)");
}

function calc_tasit_kredi() {
    const amt = getNum2('tasit_kredi-amt');
    const term = getNum2('tasit_kredi-term');
    const rate = getNum2('tasit_kredi-rate') / 100;

    const x = Math.pow(1+rate, term);
    const pay = amt * (rate * x) / (x - 1);

    showRes('tasit_kredi', pay.toLocaleString('tr-TR') + ' TL/Ay', "Toplam: " + (pay*term).toLocaleString());
}

// --- EDUCATION ---
function calc_yks_sirala() {
    const tyt = getNum2('yks-tyt');
    const ayt = getNum2('yks-ayt');
    const obp = getNum2('yks-obp');
    // Score = (TYT*1.3 + AYT*3 + OBP*0.6) + Base
    const score = (tyt * 3.3) + (ayt * 3.0) + (obp * 0.6) + 100;
    // Rank approx (Linear inverse)
    // Max score ~560.
    // 500 -> 10k
    // 400 -> 100k
    // 300 -> 300k
    let rank = 3000000;
    if(score > 550) rank = 1000;
    else if(score > 500) rank = 10000;
    else if(score > 400) rank = 100000 + (500-score)*1000;
    else rank = 300000 + (400-score)*5000;

    showRes('yks_sirala', Math.round(rank).toLocaleString() + '. Sıra', `Tahmini Puan: ${score.toFixed(2)}`);
}

function calc_kpss() {
    const gk = getNum2('kpss-gk');
    const gy = getNum2('kpss-gy');
    // P93 Score = 0.5*(GK+GY) + 40 (Mock)
    const score = 40 + (gk + gy) * 0.5;
    showRes('kpss', score.toFixed(3), "P93 Puanı");
}

function calc_edebiyat() {
    const v = getNum2('edebiyat-v');
    const f = getNum2('edebiyat-f');
    const p = getNum2('edebiyat-p');
    const avg = (v + f + p) / 3;
    showRes('edebiyat', avg.toFixed(2), avg>=50 ? "Geçti" : "Kaldı");
}

function calc_deneme() {
    const d = getNum2('deneme-d');
    const y = getNum2('deneme-y');
    const net = d - (y/4);
    showRes('deneme', net.toFixed(2) + ' Net', "Puan hesaplama için sınav türü seçiniz");
}

function calc_akademik() {
    // 30 pts base + articles
    const art = getNum2('akademik-art');
    const pts = 30 + (art * 10);
    const money = pts * 150; // Coeff
    showRes('akademik', money.toLocaleString('tr-TR') + ' TL', `${pts} Puan`);
}

function calc_ucretli_ogretmen() {
    const hours = getNum2('ucretli-hours');
    const rate = 160; // 2026 estimate hourly (125 * 1.30)
    const sal = hours * rate * 4;
    showRes('ucretli', sal.toLocaleString('tr-TR') + ' TL', "Aylık Tahmini");
}

// --- OTHER ---
function calc_pet_age(type) {
    const age = getNum2(type + '-age');
    let human = 0;
    if(type === 'kopek') human = 15 + (age>1?9:0) + (age>2?(age-2)*5:0); // First year 15, second 9, then 5
    if(type === 'kedi') human = 15 + (age>1?9:0) + (age>2?(age-2)*4:0);
    if(type === 'kus') human = age * 9; // Approx
    showRes(type, human + ' İnsan Yaşı', "Tahmini");
}
function calc_kopek() { calc_pet_age('kopek'); }
function calc_kedi() { calc_pet_age('kedi'); }
function calc_kus() { calc_pet_age('kus'); }

function calc_mesai() {
    const sal = getNum2('mesai-sal');
    const hours = getNum2('mesai-hours');
    const hourly = sal / 225;
    const pay = hours * hourly * 1.5;
    showRes('mesai', pay.toLocaleString('tr-TR') + ' TL', "Fazla Mesai Ücreti");
}

function calc_emekli() {
    const days = getNum2('emekli-days');
    // Base raised to ~16,250 (12500 * 1.30)
    const salary = 16250 + (days * 0.65);
    showRes('emekli', salary.toLocaleString('tr-TR') + ' TL', "Tahmini 2026 Maaşı");
}

function calc_kira() {
    const curr = getNum2('kira-curr');
    // Rent increase cap is usually 12-month average CPI.
    // In this simulation (2026), we use the previous year's (2025) realized inflation or CPI change.
    // Let's calculate the annual rate from our data: (Index_2025 / Index_2024) - 1
    // Or simply use the OVP rate for 2025 (17.5% -> 0.175) or a 12-month avg logic.
    // For simplicity and consistency with the "Annual Data" plan, we use the 2025 Rate.

    // We can derive it from window.cpi_data if available, otherwise fallback.
    let rate = 0.25; // Default fallback
    if(window.cpi_data && window.cpi_data[2025] && window.cpi_data[2024]) {
        rate = (window.cpi_data[2025] / window.cpi_data[2024]) - 1;
    }

    const next = curr * (1 + rate);
    const rateStr = '%' + (rate * 100).toFixed(2);
    showRes('kira', next.toLocaleString('tr-TR', {maximumFractionDigits: 2}) + ' TL', `Yasal Artış Oranı: ${rateStr} (2025 TÜFE Bazlı)`);
}

function calc_zekat() {
    const assets = getNum2('zekat-assets');
    const debts = getNum2('zekat-debts');
    const net = assets - debts;
    if(net < 80000) { // Nisab 2026 est (Gold equiv)
        showRes('zekat', '0 TL', "Nisab miktarının altında");
        return;
    }
    const zekat = net / 40;
    showRes('zekat', zekat.toLocaleString('tr-TR') + ' TL', "Verilmesi Gereken");
}

function calc_tyt_ayt_net() {
    const td = getNum2('tyt-d'); const ty = getNum2('tyt-y');
    const ad = getNum2('ayt-d'); const ay = getNum2('ayt-y');
    const tnet = td - (ty/4);
    const anet = ad - (ay/4);
    showRes('tyt_ayt', `TYT: ${tnet} | AYT: ${anet}`, "Toplam Net");
}
