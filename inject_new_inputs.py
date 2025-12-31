
import os
import re

# Dictionary of forms for new tools
forms = {
    "ags-puan-hesapla.html": """
        <div class="grid grid-cols-1 gap-4 mb-4">
            <div>
                <label class="block text-sm font-medium text-slate-700 mb-1">Toplam Net Sayısı</label>
                <input type="number" id="ags-nets" class="w-full rounded-xl border-slate-200 focus:border-purple-500 focus:ring-purple-500" placeholder="Örn: 45">
            </div>
        </div>
        <button onclick="calc_ags()" class="w-full bg-purple-600 hover:bg-purple-700 text-white font-bold py-3 rounded-xl transition shadow-lg shadow-purple-200">
            <i class="fa-solid fa-calculator mr-2"></i> Puan Hesapla
        </button>
        <!-- Result Area -->
        <div id="res-ags" class="hidden mt-6 bg-purple-50 rounded-2xl p-6 border border-purple-100 text-center animate-fade-in">
            <div class="text-xs font-bold text-purple-400 uppercase tracking-wider mb-1">Hesaplanan Puan</div>
            <div id="val-ags" class="text-3xl font-extrabold text-purple-700 mb-2"></div>
            <div id="detail-ags" class="text-sm text-purple-600 font-medium"></div>
        </div>
    """,
    "deger-artisi-hesaplama.html": """
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mb-4">
            <div>
                <label class="block text-sm font-medium text-slate-700 mb-1">Alış Bedeli (TL)</label>
                <input type="number" id="deger_artisi-buy" class="w-full rounded-xl border-slate-200" placeholder="0">
            </div>
            <div>
                <label class="block text-sm font-medium text-slate-700 mb-1">Satış Bedeli (TL)</label>
                <input type="number" id="deger_artisi-sell" class="w-full rounded-xl border-slate-200" placeholder="0">
            </div>
        </div>
        <button onclick="calc_deger_artisi()" class="w-full bg-blue-600 hover:bg-blue-700 text-white font-bold py-3 rounded-xl transition shadow-lg shadow-blue-200">
            <i class="fa-solid fa-money-bill-trend-up mr-2"></i> Vergiyi Hesapla
        </button>
        <div id="res-deger_artisi" class="hidden mt-6 bg-blue-50 rounded-2xl p-6 border border-blue-100 text-center animate-fade-in">
            <div class="text-xs font-bold text-blue-400 uppercase tracking-wider mb-1">Ödenecek Vergi</div>
            <div id="val-deger_artisi" class="text-3xl font-extrabold text-blue-700 mb-2"></div>
            <div id="detail-deger_artisi" class="text-sm text-blue-600 font-medium"></div>
        </div>
    """,
    "ek-ders-hesaplama.html": """
        <div class="mb-4">
            <label class="block text-sm font-medium text-slate-700 mb-1">Toplam Ders Saati (Aylık)</label>
            <input type="number" id="ek_ders-hrs" class="w-full rounded-xl border-slate-200" placeholder="Örn: 40">
        </div>
        <button onclick="calc_ek_ders()" class="w-full bg-blue-600 hover:bg-blue-700 text-white font-bold py-3 rounded-xl transition shadow-lg shadow-blue-200">Hesapla</button>
        <div id="res-ek_ders" class="hidden mt-6 bg-blue-50 rounded-2xl p-6 border border-blue-100 text-center animate-fade-in">
            <div id="val-ek_ders" class="text-3xl font-extrabold text-blue-700 mb-2"></div>
            <div id="detail-ek_ders" class="text-sm text-blue-600"></div>
        </div>
    """,
    "promil-hesaplama.html": """
        <div class="grid grid-cols-1 md:grid-cols-3 gap-4 mb-4">
            <div>
                <label class="block text-sm font-medium text-slate-700 mb-1">İçilen Miktar (ml)</label>
                <input type="number" id="promil-vol" class="w-full rounded-xl border-slate-200" placeholder="Örn: 500 (Bir Büyük Bira)">
            </div>
            <div>
                <label class="block text-sm font-medium text-slate-700 mb-1">Alkol Oranı (%)</label>
                <input type="number" id="promil-alc" class="w-full rounded-xl border-slate-200" placeholder="Örn: 5">
            </div>
            <div>
                <label class="block text-sm font-medium text-slate-700 mb-1">Kilonuz (kg)</label>
                <input type="number" id="promil-kg" class="w-full rounded-xl border-slate-200" placeholder="70">
            </div>
        </div>
        <button onclick="calc_promil()" class="w-full bg-orange-500 hover:bg-orange-600 text-white font-bold py-3 rounded-xl transition shadow-lg shadow-orange-200">Hesapla</button>
        <div id="res-promil" class="hidden mt-6 bg-orange-50 rounded-2xl p-6 border border-orange-100 text-center animate-fade-in">
            <div id="val-promil" class="text-3xl font-extrabold text-orange-700 mb-2"></div>
            <div id="detail-promil" class="text-sm text-orange-600 font-bold"></div>
        </div>
    """,
    "tus-puan-hesaplama.html": """
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mb-4">
            <div>
                <label class="block text-sm font-medium text-slate-700 mb-1">Temel Bilimler Neti</label>
                <input type="number" id="tus-temel" class="w-full rounded-xl border-slate-200" placeholder="0">
            </div>
            <div>
                <label class="block text-sm font-medium text-slate-700 mb-1">Klinik Bilimler Neti</label>
                <input type="number" id="tus-klinik" class="w-full rounded-xl border-slate-200" placeholder="0">
            </div>
        </div>
        <button onclick="calc_tus()" class="w-full bg-purple-600 hover:bg-purple-700 text-white font-bold py-3 rounded-xl transition shadow-lg shadow-purple-200">Hesapla</button>
        <div id="res-tus" class="hidden mt-6 bg-purple-50 rounded-2xl p-6 border border-purple-100 text-center animate-fade-in">
            <div id="val-tus" class="text-3xl font-extrabold text-purple-700 mb-2"></div>
            <div id="detail-tus" class="text-sm text-purple-600"></div>
        </div>
    """,
    "lgs-puan-hesaplama.html": """
        <div class="grid grid-cols-2 md:grid-cols-3 gap-3 mb-4 text-sm">
            <div><label>Türkçe D/Y</label><input id="lgs-tr" type="number" class="w-full rounded-lg border-slate-200" placeholder="Net"></div>
            <div><label>Matematik D/Y</label><input id="lgs-mat" type="number" class="w-full rounded-lg border-slate-200" placeholder="Net"></div>
            <div><label>Fen D/Y</label><input id="lgs-fen" type="number" class="w-full rounded-lg border-slate-200" placeholder="Net"></div>
            <div><label>İnkılap D/Y</label><input id="lgs-ink" type="number" class="w-full rounded-lg border-slate-200" placeholder="Net"></div>
            <div><label>Din K. D/Y</label><input id="lgs-din" type="number" class="w-full rounded-lg border-slate-200" placeholder="Net"></div>
            <div><label>Yabancı Dil D/Y</label><input id="lgs-dil" type="number" class="w-full rounded-lg border-slate-200" placeholder="Net"></div>
        </div>
        <button onclick="calc_lgs()" class="w-full bg-purple-600 hover:bg-purple-700 text-white font-bold py-3 rounded-xl transition shadow-lg shadow-purple-200">Puan Hesapla</button>
        <div id="res-lgs" class="hidden mt-6 bg-purple-50 rounded-2xl p-6 border border-purple-100 text-center animate-fade-in">
            <div id="val-lgs" class="text-3xl font-extrabold text-purple-700 mb-2"></div>
            <div id="detail-lgs" class="text-sm text-purple-600"></div>
        </div>
    """,
    "islah-harci-hesaplama.html": """
        <div class="mb-4">
            <label class="block text-sm font-medium text-slate-700 mb-1">Islah Edilen Tutar (TL)</label>
            <input type="number" id="islah-val" class="w-full rounded-xl border-slate-200" placeholder="Örn: 100000">
        </div>
        <button onclick="calc_islah()" class="w-full bg-blue-600 hover:bg-blue-700 text-white font-bold py-3 rounded-xl transition shadow-lg shadow-blue-200">Hesapla</button>
        <div id="res-islah" class="hidden mt-6 bg-blue-50 rounded-2xl p-6 border border-blue-100 text-center animate-fade-in">
            <div id="val-islah" class="text-3xl font-extrabold text-blue-700 mb-2"></div>
            <div id="detail-islah" class="text-sm text-blue-600"></div>
        </div>
    """,
    "taksimetre-hesaplama.html": """
        <div class="mb-4">
            <label class="block text-sm font-medium text-slate-700 mb-1">Gidilecek Mesafe (KM)</label>
            <input type="number" id="taksimetre-km" class="w-full rounded-xl border-slate-200" placeholder="Örn: 15">
        </div>
        <button onclick="calc_taksimetre()" class="w-full bg-orange-500 hover:bg-orange-600 text-white font-bold py-3 rounded-xl transition shadow-lg shadow-orange-200">Hesapla</button>
        <div id="res-taksimetre" class="hidden mt-6 bg-orange-50 rounded-2xl p-6 border border-orange-100 text-center animate-fade-in">
            <div id="val-taksimetre" class="text-3xl font-extrabold text-orange-700 mb-2"></div>
            <div id="detail-taksimetre" class="text-sm text-orange-600"></div>
        </div>
    """,
    "safak-hesaplama.html": """
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mb-4">
            <div>
                <label class="block text-sm font-medium text-slate-700 mb-1">Sülüs Tarihi</label>
                <input type="date" id="safak-date" class="w-full rounded-xl border-slate-200">
            </div>
            <div>
                <label class="block text-sm font-medium text-slate-700 mb-1">Hizmet Türü</label>
                <select id="safak-type" class="w-full rounded-xl border-slate-200">
                    <option value="6">Er / Erbaş (6 Ay)</option>
                    <option value="12">Yedek Subay/Astsubay (12 Ay)</option>
                </select>
            </div>
        </div>
        <button onclick="calc_safak()" class="w-full bg-orange-500 hover:bg-orange-600 text-white font-bold py-3 rounded-xl transition shadow-lg shadow-orange-200">Şafak Say</button>
        <div id="res-safak" class="hidden mt-6 bg-orange-50 rounded-2xl p-6 border border-orange-100 text-center animate-fade-in">
            <div id="val-safak" class="text-3xl font-extrabold text-orange-700 mb-2"></div>
            <div id="detail-safak" class="text-sm text-orange-600"></div>
        </div>
    """,
    "yks-net-hesaplama.html": """
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mb-4">
            <div>
                <label class="block text-sm font-medium text-slate-700 mb-1">TYT Toplam Net</label>
                <input type="number" id="yks-tyt" class="w-full rounded-xl border-slate-200" placeholder="0">
            </div>
            <div>
                <label class="block text-sm font-medium text-slate-700 mb-1">AYT Toplam Net</label>
                <input type="number" id="yks-ayt" class="w-full rounded-xl border-slate-200" placeholder="0">
            </div>
        </div>
        <button onclick="calc_yks()" class="w-full bg-purple-600 hover:bg-purple-700 text-white font-bold py-3 rounded-xl transition shadow-lg shadow-purple-200">Hesapla</button>
        <div id="res-yks" class="hidden mt-6 bg-purple-50 rounded-2xl p-6 border border-purple-100 text-center animate-fade-in">
            <div id="val-yks" class="text-3xl font-extrabold text-purple-700 mb-2"></div>
            <div id="detail-yks" class="text-sm text-purple-600"></div>
        </div>
    """,
    "kira-artis-hesaplama.html": """
        <div class="mb-4">
            <label class="block text-sm font-medium text-slate-700 mb-1">Mevcut Kira Bedeli</label>
            <input type="number" id="kira-cur" class="w-full rounded-xl border-slate-200" placeholder="Örn: 10000">
        </div>
        <button onclick="calc_kira()" class="w-full bg-blue-600 hover:bg-blue-700 text-white font-bold py-3 rounded-xl transition shadow-lg shadow-blue-200">Hesapla</button>
        <div id="res-kira" class="hidden mt-6 bg-blue-50 rounded-2xl p-6 border border-blue-100 text-center animate-fade-in">
            <div id="val-kira" class="text-3xl font-extrabold text-blue-700 mb-2"></div>
            <div id="detail-kira" class="text-sm text-blue-600"></div>
        </div>
    """,
    "vekalet-ucreti-hesaplama.html": """
        <div class="mb-4">
            <label class="block text-sm font-medium text-slate-700 mb-1">Dava / İcra Değeri (TL)</label>
            <input type="number" id="vekalet-val" class="w-full rounded-xl border-slate-200" placeholder="0">
        </div>
        <button onclick="calc_vekalet()" class="w-full bg-blue-600 hover:bg-blue-700 text-white font-bold py-3 rounded-xl transition shadow-lg shadow-blue-200">Hesapla</button>
        <div id="res-vekalet" class="hidden mt-6 bg-blue-50 rounded-2xl p-6 border border-blue-100 text-center animate-fade-in">
            <div id="val-vekalet" class="text-3xl font-extrabold text-blue-700 mb-2"></div>
            <div id="detail-vekalet" class="text-sm text-blue-600"></div>
        </div>
    """,
    "gano-hesaplama.html": """
        <div class="grid grid-cols-2 gap-4 mb-4">
            <div><input type="number" id="gano-c1" class="w-full border-slate-200 rounded-lg" placeholder="Ders 1 Kredi"></div>
            <div><input type="number" id="gano-g1" class="w-full border-slate-200 rounded-lg" placeholder="Ders 1 Not"></div>
            <div><input type="number" id="gano-c2" class="w-full border-slate-200 rounded-lg" placeholder="Ders 2 Kredi"></div>
            <div><input type="number" id="gano-g2" class="w-full border-slate-200 rounded-lg" placeholder="Ders 2 Not"></div>
        </div>
        <button onclick="calc_gano()" class="w-full bg-purple-600 hover:bg-purple-700 text-white font-bold py-3 rounded-xl transition shadow-lg shadow-purple-200">Ortalama Hesapla</button>
        <div id="res-gano" class="hidden mt-6 bg-purple-50 rounded-2xl p-6 border border-purple-100 text-center animate-fade-in">
            <div id="val-gano" class="text-3xl font-extrabold text-purple-700 mb-2"></div>
            <div id="detail-gano" class="text-sm text-purple-600"></div>
        </div>
    """
}

# Regex to find the tool placeholder div
placeholder_regex = re.compile(r'<div id="tool-placeholder">.*?</div>', re.DOTALL)

for filename, html_content in forms.items():
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()

        if placeholder_regex.search(content):
            new_content = placeholder_regex.sub(html_content, content)
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Injected inputs into {filename}")
        else:
            print(f"Placeholder not found in {filename}")
    else:
        print(f"File {filename} does not exist.")
