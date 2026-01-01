import json
import os

# Read the mapping
with open('tools_data.json', 'r') as f:
    tools = json.load(f)

# HTML Template (Based on kdv-hesaplama.html)
TEMPLATE = """<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="{seo_desc_short}">
    <meta name="keywords" content="{keywords}">
    <meta name="author" content="HesaplaHadi">
    <meta name="robots" content="index, follow">
    <title>{title} | HesaplaHadi</title>
    <link rel="canonical" href="https://hesaplahadi.com/{filename}">
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "Calculator",
      "name": "{title}",
      "url": "https://hesaplahadi.com/{filename}",
      "description": "{seo_desc_short}",
      "applicationCategory": "{schema_cat}",
      "offers": {{ "@type": "Offer", "price": "0", "priceCurrency": "TRY" }}
    }}
    </script>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <link href="assets/css/style.css" rel="stylesheet">
</head>
<body class="flex flex-col min-h-screen text-slate-800">
    <!-- Header -->
    <header class="bg-white/90 backdrop-blur-md shadow-sm sticky top-0 z-50 border-b border-slate-100">
        <div class="container mx-auto px-4 py-3">
            <div class="flex justify-between items-center">
                <div class="flex items-center gap-3">
                     <a href="index.html" class="flex items-center space-x-2 group">
                        <div class="flex items-center justify-center bg-gradient-to-br from-blue-600 to-indigo-700 text-white p-2.5 rounded-xl group-hover:shadow-lg group-hover:shadow-blue-500/30 transition duration-300 flex-shrink-0">
                            <i class="fa-solid fa-calculator text-lg"></i>
                        </div>
                        <div class="leading-tight">
                            <h1 class="text-xl md:text-2xl font-extrabold tracking-tight text-slate-900">Hesapla<span class="text-blue-600">Hadi</span></h1>
                        </div>
                    </a>
                </div>
                <div class="flex items-center gap-3">
                    <div class="hidden md:block relative">
                         <i class="fa-solid fa-search absolute left-3 top-1/2 -translate-y-1/2 text-slate-400 text-xs"></i>
                         <input type="text" placeholder="Araç ara..." class="pl-8 pr-4 py-2 bg-slate-50 border border-slate-200 rounded-lg text-xs font-bold focus:bg-white focus:border-blue-500 transition outline-none w-48">
                    </div>
                    <div class="hidden md:flex items-center space-x-3 text-xs font-bold text-slate-600">
                        <a href="index.html" class="hover:text-blue-600 transition">Araçlar</a>
                        <a href="blog/index.html" class="hover:text-blue-600 transition">Blog</a>
                        <a href="ai-asistan.html" class="flex items-center gap-2 bg-indigo-50 hover:bg-indigo-100 text-indigo-700 px-4 py-2 rounded-xl border border-indigo-100 transition duration-300">
                            <i class="fa-solid fa-wand-magic-sparkles"></i>
                            <span>AI Asistan</span>
                        </a>
                    </div>
                </div>
            </div>
            <div class="md:hidden mt-3 relative group z-40">
                 <i class="fa-solid fa-search absolute left-3 top-3 text-slate-400 text-sm z-10"></i>
                 <input type="text" id="mobile-tool-search" onkeyup="filterDrawerTools()" placeholder="Hesaplama aracı ara..." class="w-full pl-9 pr-4 py-2 bg-slate-50 border border-slate-200 rounded-lg text-sm focus:bg-white focus:border-blue-500 transition outline-none relative z-0">
                 <div id="search-suggestions" class="hidden absolute top-full left-0 w-full bg-white border border-slate-200 rounded-lg shadow-lg mt-1 z-20">
                    <div class="p-2 text-xs font-bold text-slate-400 uppercase tracking-wider">Popüler Araçlar</div>
                    <a href="kdv-hesaplama.html" class="block px-3 py-2 text-sm text-slate-600 hover:bg-blue-50 hover:text-blue-600 rounded flex items-center gap-2">
                        <i class="fa-solid fa-percent text-blue-400"></i> KDV Hesaplama
                    </a>
                    <a href="kredi-hesaplama.html" class="block px-3 py-2 text-sm text-slate-600 hover:bg-blue-50 hover:text-blue-600 rounded flex items-center gap-2">
                        <i class="fa-solid fa-coins text-blue-400"></i> Kredi Hesaplama
                    </a>
                    <a href="tevkifat-hesaplama.html" class="block px-3 py-2 text-sm text-slate-600 hover:bg-blue-50 hover:text-blue-600 rounded flex items-center gap-2">
                        <i class="fa-solid fa-file-invoice-dollar text-blue-400"></i> Tevkifat Hesapla
                    </a>
                 </div>
            </div>
            <button class="md:hidden w-full mt-3 flex items-center justify-center gap-2 bg-gradient-to-r from-indigo-600 to-purple-700 text-white px-4 py-2.5 rounded-lg font-bold text-sm hover:from-indigo-700 hover:to-purple-800 transition shadow-sm relative z-40 cursor-pointer" onclick="toggleDrawer()">
                <i class="fa-solid fa-bars"></i>
                <span>Tüm Hesaplama Araçları</span>
            </button>
        </div>
    </header>

    <div class="container mx-auto px-4 py-8 grid grid-cols-1 lg:grid-cols-12 gap-8 flex-grow">
        <!-- Sidebar -->
        <nav class="hidden lg:block lg:col-span-3 space-y-4">
            <div class="bg-white/80 backdrop-blur glass-panel rounded-2xl overflow-hidden flex flex-col sticky top-24">
                <div class="bg-slate-50/50 px-5 py-4 border-b border-slate-100 flex justify-between items-center shrink-0">
                    <h3 class="font-bold text-slate-700 text-sm uppercase tracking-wide">Hesaplama Araçları</h3>
                </div>
                <div id="sidebar-list" class="overflow-y-auto p-2 space-y-1">
                    <!-- Populated via JS -->
                </div>
            </div>
        </nav>

        <!-- Main Content -->
        <main class="col-span-1 lg:col-span-6 space-y-6">
            <div class="bg-white/90 backdrop-blur rounded-2xl shadow-sm border border-slate-200 p-6 md:p-8 animate-slide-up relative">
                <div class="flex items-center gap-4 mb-6 pb-6 border-b border-slate-100">
                    <div class="p-3 bg-blue-100 rounded-2xl text-blue-600 shadow-sm">
                        <i class="fa-solid fa-calculator text-xl"></i>
                    </div>
                    <div>
                        <h1 class="text-2xl font-bold text-slate-900 tracking-tight">{title}</h1>
                        <p class="text-xs text-slate-500 mt-1">{seo_desc_short}</p>
                    </div>
                </div>

                <!-- DYNAMIC FORM CONTENT -->
                {form_content}

                <div id="res-{func_id}" class="result-card hidden mt-8 p-6 rounded-2xl relative group">
                    <button id="btn-copy-{func_id}" onclick="copyResult('{func_id}')" class="absolute top-4 right-4 text-xs bg-white border border-slate-200 px-3 py-1.5 rounded-lg hover:bg-slate-50 transition text-slate-500 flex items-center gap-1 shadow-sm">
                        <i class="fa-regular fa-copy"></i> Kopyala
                    </button>
                    <p class="text-[10px] font-bold text-blue-600 uppercase tracking-widest mb-2">HESAPLAMA SONUCU</p>
                    <div id="val-{func_id}" class="text-3xl md:text-4xl font-black text-slate-900 tracking-tight"></div>
                    <div id="detail-{func_id}" class="text-sm text-slate-500 mt-3 pt-3 border-t border-slate-200/50 empty:hidden"></div>
                </div>

            </div>

            <!-- SEO Content -->
            {seo_content}

        </main>

        <!-- Right Sidebar -->
        <aside class="col-span-1 lg:col-span-3 space-y-6">
             <div class="bg-white p-6 rounded-2xl shadow-sm border border-slate-200">
                <h4 class="font-bold text-xs text-slate-500 mb-4 uppercase tracking-wider border-b border-slate-100 pb-2 flex items-center gap-2">
                    <i class="fa-solid fa-fire text-orange-500"></i> Popüler Araçlar
                </h4>
                <ul class="text-sm space-y-2 text-slate-600 font-medium">
                    <li class="cursor-pointer hover:text-blue-600 hover:bg-blue-50 p-2.5 rounded-lg transition flex items-center justify-between group" onclick="window.location.href='kdv-hesaplama.html'">
                        <span>KDV Hesaplama</span> <i class="fa-solid fa-chevron-right text-xs opacity-30"></i>
                    </li>
                    <li class="cursor-pointer hover:text-blue-600 hover:bg-blue-50 p-2.5 rounded-lg transition flex items-center justify-between group" onclick="window.location.href='kredi-hesaplama.html'">
                        <span>Kredi Hesaplama</span> <i class="fa-solid fa-chevron-right text-xs opacity-30"></i>
                    </li>
                    <li class="cursor-pointer hover:text-blue-600 hover:bg-blue-50 p-2.5 rounded-lg transition flex items-center justify-between group" onclick="window.location.href='netten-brute-maas-hesaplama-2026.html'">
                        <span>Netten Brüte Maaş</span> <i class="fa-solid fa-chevron-right text-xs opacity-30"></i>
                    </li>
                     <li class="cursor-pointer hover:text-blue-600 hover:bg-blue-50 p-2.5 rounded-lg transition flex items-center justify-between group" onclick="window.location.href='mtv-hesaplama-2026.html'">
                        <span>MTV Hesaplama</span> <i class="fa-solid fa-chevron-right text-xs opacity-30"></i>
                    </li>
                </ul>
            </div>
        </aside>
    </div>

    <footer class="bg-slate-900 text-slate-400 py-12 mt-auto border-t border-slate-800">
        <div class="container mx-auto px-4 text-center">
            <span class="text-2xl font-bold text-white tracking-tight">Hesapla<span class="text-blue-500">Hadi</span></span>
            <div class="flex justify-center flex-wrap gap-6 text-sm font-medium mt-6 text-slate-300">
                <a href="index.html" class="hover:text-white transition">Ana Sayfa</a>
                <a href="blog/index.html" class="hover:text-white transition">Blog</a>
            </div>
            <div class="text-xs text-slate-600 mt-6">&copy; 2026 HesaplaHadi.</div>
        </div>
    </footer>
    <div id="cookie-banner" class="fixed bottom-0 left-0 right-0 bg-white/95 backdrop-blur shadow-[0_-5px_20px_rgba(0,0,0,0.05)] border-t border-slate-200 p-4 z-50 transform translate-y-full">
        <div class="container mx-auto flex flex-col md:flex-row items-center justify-between gap-4">
            <div class="text-sm text-slate-600 text-center md:text-left">Çerezler deneyiminizi iyileştirmek için kullanılır.</div>
            <button onclick="acceptCookies()" class="bg-slate-900 hover:bg-slate-800 text-white text-sm font-bold py-2.5 px-6 rounded-xl transition">Tamam</button>
        </div>
    </div>
    <script src="assets/js/calculator.js?v=3"></script>
    <script src="assets/js/tools-2026.js?v=1"></script>
</body>
</html>
"""

# Import the SEO generator function
from map_tools import generate_seo_text

def get_input_html(tool, func_id):
    itype = tool.get("input_type", "text")

    if itype == "birth_time":
        return f"""
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div>
                <label class="block text-xs font-bold text-slate-600 uppercase tracking-wide mb-2 ml-1">Doğum Tarihi</label>
                <input type="date" id="{func_id}-date" class="w-full p-4 border border-slate-200 rounded-xl bg-slate-50 text-sm font-medium focus:bg-white transition input-premium">
            </div>
            <div>
                <label class="block text-xs font-bold text-slate-600 uppercase tracking-wide mb-2 ml-1">Doğum Saati</label>
                <input type="time" id="{func_id}-time" class="w-full p-4 border border-slate-200 rounded-xl bg-slate-50 text-sm font-medium focus:bg-white transition input-premium">
            </div>
        </div>
        <button onclick="calc_{func_id.replace('-','_')}()" class="btn-calc w-full mt-8 py-4 rounded-xl font-bold text-white text-sm tracking-wide shadow-lg shadow-blue-500/20 flex justify-center items-center gap-2">
            <i class="fa-solid fa-star"></i> Hesapla
        </button>
        """
    elif itype == "date":
        return f"""
        <div>
            <label class="block text-xs font-bold text-slate-600 uppercase tracking-wide mb-2 ml-1">Tarih Seçiniz</label>
            <input type="date" id="{func_id}-date" class="w-full p-4 border border-slate-200 rounded-xl bg-slate-50 text-sm font-medium focus:bg-white transition input-premium">
        </div>
        <button onclick="calc_{func_id.replace('-','_')}()" class="btn-calc w-full mt-8 py-4 rounded-xl font-bold text-white text-sm tracking-wide shadow-lg shadow-blue-500/20 flex justify-center items-center gap-2">
            <i class="fa-solid fa-calendar"></i> Hesapla
        </button>
        """
    elif itype == "currency":
        return f"""
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div>
                <label class="block text-xs font-bold text-slate-600 uppercase tracking-wide mb-2 ml-1">Miktar</label>
                <input type="number" id="{func_id}-amt" class="w-full p-4 border border-slate-200 rounded-xl bg-slate-50 text-sm font-medium focus:bg-white transition input-premium" placeholder="1">
            </div>
            <div>
                <label class="block text-xs font-bold text-slate-600 uppercase tracking-wide mb-2 ml-1">Kur / Fiyat (TL)</label>
                <input type="number" id="{func_id}-rate" class="w-full p-4 border border-slate-200 rounded-xl bg-slate-50 text-sm font-medium focus:bg-white transition input-premium" placeholder="35.50">
            </div>
        </div>
        <button onclick="calc_{func_id.replace('-','_')}()" class="btn-calc w-full mt-8 py-4 rounded-xl font-bold text-white text-sm tracking-wide shadow-lg shadow-blue-500/20 flex justify-center items-center gap-2">
            <i class="fa-solid fa-calculator"></i> Hesapla
        </button>
        """
    elif itype == "inflation":
        return f"""
        <div class="grid grid-cols-1 gap-6">
            <div>
                <label class="block text-xs font-bold text-slate-600 uppercase tracking-wide mb-2 ml-1">Yatırım Tutarı ($)</label>
                <input type="number" id="{func_id}-amt" class="w-full p-4 border border-slate-200 rounded-xl bg-slate-50 text-sm font-medium focus:bg-white transition input-premium" placeholder="1000">
            </div>
            <div class="grid grid-cols-2 gap-4">
                <div>
                    <label class="block text-xs font-bold text-slate-600 uppercase tracking-wide mb-2 ml-1">Alış Kuru</label>
                    <input type="number" id="{func_id}-old" class="w-full p-4 border border-slate-200 rounded-xl bg-slate-50 text-sm font-medium focus:bg-white transition input-premium" placeholder="18.50">
                </div>
                <div>
                    <label class="block text-xs font-bold text-slate-600 uppercase tracking-wide mb-2 ml-1">Satış Kuru</label>
                    <input type="number" id="{func_id}-new" class="w-full p-4 border border-slate-200 rounded-xl bg-slate-50 text-sm font-medium focus:bg-white transition input-premium" placeholder="35.00">
                </div>
            </div>
            <div>
                <label class="block text-xs font-bold text-slate-600 uppercase tracking-wide mb-2 ml-1">Dönem Enflasyonu (%)</label>
                <input type="number" id="{func_id}-inf" class="w-full p-4 border border-slate-200 rounded-xl bg-slate-50 text-sm font-medium focus:bg-white transition input-premium" placeholder="65">
            </div>
        </div>
        <button onclick="calc_{func_id.replace('-','_')}()" class="btn-calc w-full mt-8 py-4 rounded-xl font-bold text-white text-sm tracking-wide shadow-lg shadow-blue-500/20 flex justify-center items-center gap-2">
            <i class="fa-solid fa-chart-line"></i> Hesapla
        </button>
        """
    elif itype == "mtv":
        return f"""
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
             <div>
                <label class="block text-xs font-bold text-slate-600 uppercase tracking-wide mb-2 ml-1">Araç Yaşı</label>
                <select id="{func_id}-age" class="w-full p-4 border border-slate-200 rounded-xl bg-slate-50 text-sm font-medium focus:bg-white transition input-premium">
                    <option value="0">1-3 Yaş</option>
                    <option value="1">4-6 Yaş</option>
                    <option value="2">7-11 Yaş</option>
                    <option value="3">12+ Yaş</option>
                </select>
            </div>
            <div>
                <label class="block text-xs font-bold text-slate-600 uppercase tracking-wide mb-2 ml-1">Motor Hacmi (cc)</label>
                <select id="{func_id}-cc" class="w-full p-4 border border-slate-200 rounded-xl bg-slate-50 text-sm font-medium focus:bg-white transition input-premium">
                    <option value="0">0 - 1300 cc</option>
                    <option value="1">1301 - 1600 cc</option>
                    <option value="2">1601 - 2000 cc</option>
                    <option value="3">2001+ cc</option>
                </select>
            </div>
        </div>
        <button onclick="calc_mtv_2026()" class="btn-calc w-full mt-8 py-4 rounded-xl font-bold text-white text-sm tracking-wide shadow-lg shadow-blue-500/20 flex justify-center items-center gap-2">
            <i class="fa-solid fa-car"></i> Hesapla
        </button>
        """
    elif itype == "text":
        return f"""
         <div>
            <label class="block text-xs font-bold text-slate-600 uppercase tracking-wide mb-2 ml-1">İsim Giriniz</label>
            <input type="text" id="{func_id}-name" class="w-full p-4 border border-slate-200 rounded-xl bg-slate-50 text-sm font-medium focus:bg-white transition input-premium" placeholder="Ad Soyad">
        </div>
        <button onclick="calc_{func_id.replace('-','_')}()" class="btn-calc w-full mt-8 py-4 rounded-xl font-bold text-white text-sm tracking-wide shadow-lg shadow-blue-500/20 flex justify-center items-center gap-2">
            <i class="fa-solid fa-magnifying-glass"></i> Hesapla
        </button>
        """
    elif itype == "date_age":
         return f"""
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div>
                <label class="block text-xs font-bold text-slate-600 uppercase tracking-wide mb-2 ml-1">Anne Yaşı (Gebe Kalınan)</label>
                <input type="number" id="{func_id}-age" class="w-full p-4 border border-slate-200 rounded-xl bg-slate-50 text-sm font-medium focus:bg-white transition input-premium" placeholder="25">
            </div>
            <div>
                <label class="block text-xs font-bold text-slate-600 uppercase tracking-wide mb-2 ml-1">Gebe Kalınan Ay</label>
                <select id="{func_id}-month" class="w-full p-4 border border-slate-200 rounded-xl bg-slate-50 text-sm font-medium focus:bg-white transition input-premium">
                    <option value="1">Ocak</option>
                    <option value="2">Şubat</option>
                    <option value="3">Mart</option>
                    <option value="4">Nisan</option>
                    <option value="5">Mayıs</option>
                    <option value="6">Haziran</option>
                    <option value="7">Temmuz</option>
                    <option value="8">Ağustos</option>
                    <option value="9">Eylül</option>
                    <option value="10">Ekim</option>
                    <option value="11">Kasım</option>
                    <option value="12">Aralık</option>
                </select>
            </div>
        </div>
        <button onclick="calc_{func_id.replace('-','_')}()" class="btn-calc w-full mt-8 py-4 rounded-xl font-bold text-white text-sm tracking-wide shadow-lg shadow-blue-500/20 flex justify-center items-center gap-2">
            <i class="fa-solid fa-venus-mars"></i> Hesapla
        </button>
        """
    # Default fallback
    return f"""
        <div>
            <label class="block text-xs font-bold text-slate-600 uppercase tracking-wide mb-2 ml-1">Değer</label>
            <input type="number" id="{func_id}-val" class="w-full p-4 border border-slate-200 rounded-xl bg-slate-50 text-sm font-medium focus:bg-white transition input-premium">
        </div>
        <button onclick="calc_{func_id.replace('-','_')}()" class="btn-calc w-full mt-8 py-4 rounded-xl font-bold text-white text-sm tracking-wide shadow-lg shadow-blue-500/20 flex justify-center items-center gap-2">
            <i class="fa-solid fa-calculator"></i> Hesapla
        </button>
    """

# Process tools
for tool in tools:
    # Skip existing file updates in this script, handled separately or manually?
    # Actually, I should check if file exists. If so, I might need to update CONTENT, but user said "don't delete".
    # But for "New" tools, I create.
    # The tools list has "new_filename" for rename, but also completely new tools.

    filename = tool.get("new_filename", tool["filename"])

    # If it is a brand new tool (doesn't exist in repo), generate it.
    if not os.path.exists(tool["filename"]) and "new_filename" not in tool:
        # It's a new tool
        func_id = filename.replace('.html','').replace('i̇','i').replace('ı','i').replace('-','_') # Basic sanitization

        # Override func_ids for known logic in JS
        if "altin" in filename: func_id = "altin"
        if "dolar-hesaplama" in filename: func_id = "dolar"
        if "euro" in filename: func_id = "euro"
        if "gumus" in filename: func_id = "gumus"
        if "mtv" in filename: func_id = "mtv"
        if "tasit" in filename: func_id = "tasit_kredi"
        if "piyango" in filename: func_id = "piyango"

        # ... logic map for func_ids based on tools-2026.js ...
        # I need to ensure the HTML IDs match the JS `getNum2` calls.

        # Custom tweaks for specific forms that are not standard "input_type"
        if tool["input_type"] == "pet_age":
             type_pet = "kopek" if "kopek" in filename else "kedi" if "kedi" in filename else "kus"
             form = f"""
                <div>
                    <label class="block text-xs font-bold text-slate-600 uppercase tracking-wide mb-2 ml-1">{type_pet.capitalize()} Yaşı</label>
                    <input type="number" id="{type_pet}-age" class="w-full p-4 border border-slate-200 rounded-xl bg-slate-50 text-sm font-medium focus:bg-white transition input-premium">
                </div>
                <button onclick="calc_{type_pet}()" class="btn-calc w-full mt-8 py-4 rounded-xl font-bold text-white text-sm tracking-wide shadow-lg shadow-blue-500/20 flex justify-center items-center gap-2">
                    <i class="fa-solid fa-paw"></i> Hesapla
                </button>
             """
             func_id = type_pet # for result id

        elif tool["input_type"] == "loan":
            form = f"""
            <div class="grid grid-cols-1 gap-6">
                <div>
                    <label class="block text-xs font-bold text-slate-600 uppercase tracking-wide mb-2 ml-1">Kredi Tutarı</label>
                    <input type="number" id="tasit_kredi-amt" class="w-full p-4 border border-slate-200 rounded-xl bg-slate-50 text-sm font-medium focus:bg-white transition input-premium">
                </div>
                <div class="grid grid-cols-2 gap-4">
                    <div>
                        <label class="block text-xs font-bold text-slate-600 uppercase tracking-wide mb-2 ml-1">Vade (Ay)</label>
                        <input type="number" id="tasit_kredi-term" class="w-full p-4 border border-slate-200 rounded-xl bg-slate-50 text-sm font-medium focus:bg-white transition input-premium">
                    </div>
                    <div>
                        <label class="block text-xs font-bold text-slate-600 uppercase tracking-wide mb-2 ml-1">Faiz Oranı</label>
                        <input type="number" id="tasit_kredi-rate" class="w-full p-4 border border-slate-200 rounded-xl bg-slate-50 text-sm font-medium focus:bg-white transition input-premium" placeholder="3.99">
                    </div>
                </div>
            </div>
            <button onclick="calc_tasit_kredi()" class="btn-calc w-full mt-8 py-4 rounded-xl font-bold text-white text-sm tracking-wide shadow-lg shadow-blue-500/20 flex justify-center items-center gap-2">
                <i class="fa-solid fa-coins"></i> Hesapla
            </button>
            """
            func_id = "tasit_kredi"

        elif tool["input_type"] == "interest":
             form = f"""
            <div class="grid grid-cols-1 gap-6">
                <div>
                    <label class="block text-xs font-bold text-slate-600 uppercase tracking-wide mb-2 ml-1">Kullanılan Tutar</label>
                    <input type="number" id="esnek-amt" class="w-full p-4 border border-slate-200 rounded-xl bg-slate-50 text-sm font-medium focus:bg-white transition input-premium">
                </div>
                <div class="grid grid-cols-2 gap-4">
                    <div>
                        <label class="block text-xs font-bold text-slate-600 uppercase tracking-wide mb-2 ml-1">Gün Sayısı</label>
                        <input type="number" id="esnek-days" class="w-full p-4 border border-slate-200 rounded-xl bg-slate-50 text-sm font-medium focus:bg-white transition input-premium">
                    </div>
                    <div>
                        <label class="block text-xs font-bold text-slate-600 uppercase tracking-wide mb-2 ml-1">Faiz Oranı</label>
                        <input type="number" id="esnek-rate" class="w-full p-4 border border-slate-200 rounded-xl bg-slate-50 text-sm font-medium focus:bg-white transition input-premium" placeholder="5.00">
                    </div>
                </div>
            </div>
            <button onclick="calc_esnek()" class="btn-calc w-full mt-8 py-4 rounded-xl font-bold text-white text-sm tracking-wide shadow-lg shadow-blue-500/20 flex justify-center items-center gap-2">
                <i class="fa-solid fa-percent"></i> Hesapla
            </button>
            """
             func_id = "esnek"

        elif tool["input_type"] == "betting":
             form = f"""
            <div class="grid grid-cols-3 md:grid-cols-6 gap-2">
                <input type="number" id="altili-l1" class="p-2 border rounded" placeholder="Ayak 1">
                <input type="number" id="altili-l2" class="p-2 border rounded" placeholder="Ayak 2">
                <input type="number" id="altili-l3" class="p-2 border rounded" placeholder="Ayak 3">
                <input type="number" id="altili-l4" class="p-2 border rounded" placeholder="Ayak 4">
                <input type="number" id="altili-l5" class="p-2 border rounded" placeholder="Ayak 5">
                <input type="number" id="altili-l6" class="p-2 border rounded" placeholder="Ayak 6">
            </div>
             <div class="mt-4">
                <label class="block text-xs font-bold text-slate-600 uppercase tracking-wide mb-2 ml-1">Birim Fiyat (TL)</label>
                <input type="number" id="altili-unit" class="w-full p-4 border border-slate-200 rounded-xl bg-slate-50 text-sm font-medium focus:bg-white transition input-premium" value="0.50">
            </div>
            <button onclick="calc_altili()" class="btn-calc w-full mt-8 py-4 rounded-xl font-bold text-white text-sm tracking-wide shadow-lg shadow-blue-500/20 flex justify-center items-center gap-2">
                <i class="fa-solid fa-horse-head"></i> Hesapla
            </button>
            """
             func_id = "altili"

        elif tool["input_type"] == "legal_fee":
             fid = "vekalet" if "vekalet" in filename else "islah"
             form = f"""
            <div>
                <label class="block text-xs font-bold text-slate-600 uppercase tracking-wide mb-2 ml-1">Dava Değeri / Tutar</label>
                <input type="number" id="{fid}-amt" class="w-full p-4 border border-slate-200 rounded-xl bg-slate-50 text-sm font-medium focus:bg-white transition input-premium">
            </div>
            <button onclick="calc_{fid}()" class="btn-calc w-full mt-8 py-4 rounded-xl font-bold text-white text-sm tracking-wide shadow-lg shadow-blue-500/20 flex justify-center items-center gap-2">
                <i class="fa-solid fa-gavel"></i> Hesapla
            </button>
            """
             func_id = fid

        elif tool["input_type"] == "legal_time":
             form = f"""
            <div class="grid grid-cols-3 gap-4">
                <input type="number" id="infaz-y" class="p-3 border rounded" placeholder="Yıl">
                <input type="number" id="infaz-m" class="p-3 border rounded" placeholder="Ay">
                <input type="number" id="infaz-d" class="p-3 border rounded" placeholder="Gün">
            </div>
            <button onclick="calc_infaz()" class="btn-calc w-full mt-8 py-4 rounded-xl font-bold text-white text-sm tracking-wide shadow-lg shadow-blue-500/20 flex justify-center items-center gap-2">
                <i class="fa-solid fa-clock"></i> Hesapla
            </button>
            """
             func_id = "infaz"

        elif tool["input_type"] == "exam_score":
             if "yks" in filename:
                form = f"""
                <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
                    <input type="number" id="yks-tyt" class="p-3 border rounded" placeholder="TYT Net">
                    <input type="number" id="yks-ayt" class="p-3 border rounded" placeholder="AYT Net">
                    <input type="number" id="yks-obp" class="p-3 border rounded" placeholder="OBP">
                </div>
                <button onclick="calc_yks_sirala()" class="btn-calc w-full mt-8 py-4 rounded-xl font-bold text-white text-sm tracking-wide shadow-lg shadow-blue-500/20 flex justify-center items-center gap-2">
                    <i class="fa-solid fa-graduation-cap"></i> Hesapla
                </button>
                """
                func_id = "yks_sirala"
             elif "kpss" in filename:
                form = f"""
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <input type="number" id="kpss-gk" class="p-3 border rounded" placeholder="Genel Kültür Net">
                    <input type="number" id="kpss-gy" class="p-3 border rounded" placeholder="Genel Yetenek Net">
                </div>
                <button onclick="calc_kpss()" class="btn-calc w-full mt-8 py-4 rounded-xl font-bold text-white text-sm tracking-wide shadow-lg shadow-blue-500/20 flex justify-center items-center gap-2">
                    <i class="fa-solid fa-book"></i> Hesapla
                </button>
                """
                func_id = "kpss"
             elif "deneme" in filename:
                form = f"""
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <input type="number" id="deneme-d" class="p-3 border rounded" placeholder="Doğru Sayısı">
                    <input type="number" id="deneme-y" class="p-3 border rounded" placeholder="Yanlış Sayısı">
                </div>
                <button onclick="calc_deneme()" class="btn-calc w-full mt-8 py-4 rounded-xl font-bold text-white text-sm tracking-wide shadow-lg shadow-blue-500/20 flex justify-center items-center gap-2">
                    <i class="fa-solid fa-pen"></i> Hesapla
                </button>
                """
                func_id = "deneme"
             else:
                form = get_input_html(tool, func_id) # fallback

        elif tool["input_type"] == "exam_net":
             form = f"""
             <div class="mb-4"><h3 class="font-bold">TYT</h3>
             <div class="grid grid-cols-2 gap-2">
                <input type="number" id="tyt-d" class="p-2 border rounded" placeholder="D">
                <input type="number" id="tyt-y" class="p-2 border rounded" placeholder="Y">
             </div></div>
             <div class="mb-4"><h3 class="font-bold">AYT</h3>
             <div class="grid grid-cols-2 gap-2">
                <input type="number" id="ayt-d" class="p-2 border rounded" placeholder="D">
                <input type="number" id="ayt-y" class="p-2 border rounded" placeholder="Y">
             </div></div>
             <button onclick="calc_tyt_ayt_net()" class="btn-calc w-full mt-8 py-4 rounded-xl font-bold text-white text-sm tracking-wide shadow-lg shadow-blue-500/20 flex justify-center items-center gap-2">
                <i class="fa-solid fa-list-check"></i> Hesapla
            </button>
             """
             func_id = "tyt_ayt"

        elif tool["input_type"] == "grade":
             form = f"""
             <div class="grid grid-cols-3 gap-2">
                <input type="number" id="edebiyat-v" class="p-2 border rounded" placeholder="Vize/Sınav 1">
                <input type="number" id="edebiyat-f" class="p-2 border rounded" placeholder="Final/Sınav 2">
                <input type="number" id="edebiyat-p" class="p-2 border rounded" placeholder="Performans">
             </div>
             <button onclick="calc_edebiyat()" class="btn-calc w-full mt-8 py-4 rounded-xl font-bold text-white text-sm tracking-wide shadow-lg shadow-blue-500/20 flex justify-center items-center gap-2">
                <i class="fa-solid fa-marker"></i> Hesapla
            </button>
             """
             func_id = "edebiyat"

        elif tool["input_type"] == "salary":
             fid = "ucretli" if "ucretli" in filename else "mesai" if "mesai" in filename else "emekli"
             if fid == "ucretli":
                form = f"""<input type="number" id="ucretli-hours" class="w-full p-4 border rounded-xl" placeholder="Aylık Ders Saati"><button onclick="calc_ucretli_ogretmen()" class="btn-calc w-full mt-4 py-3 rounded-xl bg-blue-600 text-white">Hesapla</button>"""
             elif fid == "mesai":
                 form = f"""<input type="number" id="mesai-sal" class="w-full p-3 border rounded mb-2" placeholder="Net Maaş"><input type="number" id="mesai-hours" class="w-full p-3 border rounded" placeholder="Fazla Mesai Saati"><button onclick="calc_mesai()" class="btn-calc w-full mt-4 py-3 rounded-xl bg-blue-600 text-white">Hesapla</button>"""
             else: # emekli
                 form = f"""<input type="number" id="emekli-days" class="w-full p-4 border rounded-xl" placeholder="Prim Gün Sayısı"><button onclick="calc_emekli()" class="btn-calc w-full mt-4 py-3 rounded-xl bg-blue-600 text-white">Hesapla</button>"""
             func_id = fid

        elif tool["input_type"] == "religious":
             form = f"""<div class="grid grid-cols-1 gap-4"><input type="number" id="zekat-assets" class="p-4 border rounded" placeholder="Toplam Varlık (TL/Altın)"><input type="number" id="zekat-debts" class="p-4 border rounded" placeholder="Borçlar"></div><button onclick="calc_zekat()" class="btn-calc w-full mt-4 py-3 rounded-xl bg-blue-600 text-white">Hesapla</button>"""
             func_id = "zekat"

        elif tool["input_type"] == "rent":
             form = f"""<input type="number" id="kira-curr" class="w-full p-4 border rounded-xl" placeholder="Mevcut Kira"><button onclick="calc_kira()" class="btn-calc w-full mt-4 py-3 rounded-xl bg-blue-600 text-white">Hesapla</button>"""
             func_id = "kira"

        elif tool["input_type"] == "real_estate":
             # Placeholder for Değer Artış
             form = f"""<div class="p-4 bg-yellow-50 text-yellow-700 rounded">Bu araç yapım aşamasında. AI Asistanı kullanınız.</div>"""
             func_id = "deger_artis"

        else:
             form = get_input_html(tool, func_id)

        # Generate Content
        seo_text = generate_seo_text(tool)

        # Fill Template
        html = TEMPLATE.format(
            title=tool["title"],
            seo_desc_short=tool["title"] + " aracı ile güncel 2026 verileriyle hesaplama yapın.",
            keywords=", ".join(tool["keywords"]),
            filename=filename,
            schema_cat=tool.get("category", "Application"),
            form_content=form,
            seo_content=seo_text,
            func_id=func_id
        )

        # Write
        with open(filename, 'w') as f:
            f.write(html)
        print(f"Created {filename}")
