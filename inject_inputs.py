
import os
import re

# Tool Inputs Configuration
# Format: ID -> List of Input Configs
tool_inputs = {
    "net_brut": [{"id":"net","l":"Net Maaş (TL)","p":"17002"}],
    "brut_net": [{"id":"brut","l":"Brüt Maaş (TL)","p":"20002.50"}],
    "mevduat": [{"id":"amt","l":"Anapara (TL)","p":"100000"}, {"id":"rate","l":"Yıllık Faiz (%)","p":"45"}, {"id":"days","l":"Gün Sayısı","p":"32"}],
    "iban": [{"id":"code","l":"IBAN No","p":"TR..."}],
    "indirim": [{"id":"price","l":"Etiket Fiyatı","p":"1000"}, {"id":"rate","l":"İndirim Oranı (%)","p":"25"}],
    "karzarar": [{"id":"cost","l":"Maliyet","p":"100"}, {"id":"sell","l":"Satış Fiyatı","p":"150"}],
    "bilesik": [{"id":"p","l":"Anapara","p":"10000"}, {"id":"r","l":"Yıllık Getiri (%)","p":"20"}, {"id":"t","l":"Süre (Yıl)","p":"5"}],
    "kk_asgari": [{"id":"lim","l":"Kart Limiti","p":"50000"}, {"id":"debt","l":"Dönem Borcu","p":"15000"}],
    "komisyon": [{"id":"price","l":"Satış Bedeli","p":"3000000"}],
    "zam": [{"id":"curr","l":"Mevcut Maaş","p":"17002"}, {"id":"rate","l":"Zam Oranı (%)","p":"30"}],

    # Health
    "ai_diyet": [{"id":"w","l":"Kilo (kg)","p":"80"}, {"id":"h","l":"Boy (cm)","p":"180"}, {"id":"goal","l":"Hedef","type":"select","opts":["Kilo Vermek","Kilo Almak","Formu Korumak","Kas Yapmak"]}],
    "bmi": [{"id":"h","l":"Boy (cm)","p":"175"}, {"id":"w","l":"Kilo (kg)","p":"75"}],
    "idealkilo": [{"id":"h","l":"Boy (cm)","p":"170"}, {"id":"g","l":"Cinsiyet","type":"select","opts":["Erkek","Kadın"]}],
    "bmr": [{"id":"w","l":"Kilo (kg)","p":"70"}, {"id":"h","l":"Boy (cm)","p":"175"}, {"id":"a","l":"Yaş","p":"30"}, {"id":"g","l":"Cinsiyet","type":"select","opts":["Erkek","Kadın"]}],
    "makro": [{"id":"cal","l":"Günlük Hedef Kalori","p":"2000"}],
    "su": [{"id":"w","l":"Kilo (kg)","p":"70"}],
    "gebelik": [{"id":"date","l":"Son Adet Tarihi","type":"date"}],
    "sigara": [{"id":"price","l":"Paket Fiyatı","p":"60"}, {"id":"daily","l":"Günlük Adet","p":"20"}],
    "nabiz": [{"id":"age","l":"Yaş","p":"30"}],

    # Education
    "yuzde": [
        {"id":"mode","l":"Hesaplama Türü","type":"select","opts":["A sayısının %B'si kaçtır?","A sayısı, B sayısının % kaçıdır?","A'dan B'ye değişim oranı %?","A sayısı %B artırılırsa?","A sayısı %B azaltılırsa?"]},
        {"id":"a","l":"A Değeri (Sayı)","p":"500"},
        {"id":"b","l":"B Değeri (Oran/Sayı)","p":"20"}
    ],
    "sinav": [{"id":"v","l":"Vize Notu","p":"60"}, {"id":"f","l":"Final Notu","p":"80"}],
    "takdir": [{"id":"avg","l":"Dönem Ortalaması","p":"86.50"}],
    "dikdortgen": [{"id":"w","l":"En (m)","p":"5"}, {"id":"h","l":"Boy (m)","p":"10"}],
    "kelime": [{"id":"txt","l":"Metni Yapıştırın","type":"textarea"}],

    # Practical
    "internet": [{"id":"size","l":"Dosya Boyutu (GB)","p":"10"}, {"id":"spd","l":"Hız (Mbps)","p":"35"}],
    "yakit": [{"id":"km","l":"Yol (km)","p":"100"}, {"id":"lit","l":"Ort. Tüketim (Lt/100km)","p":"7"}, {"id":"pr","l":"Litre Fiyatı","p":"42"}],
    "yas": [{"id":"date","l":"Doğum Tarihi","type":"date"}],
    "gun": [{"id":"d1","l":"Başlangıç","type":"date"}, {"id":"d2","l":"Bitiş","type":"date"}],
    "sifre": [{"id":"len","l":"Şifre Uzunluğu","p":"16"}],
    "hiz": [{"id":"km","l":"Mesafe (km)","p":"400"}, {"id":"hr","l":"Süre (Saat)","p":"4"}]
}

# Helper to generate HTML input
def generate_input_html(tool_id, inp):
    label = f'<label class="block text-xs font-bold text-slate-600 uppercase tracking-wide mb-2 ml-1">{inp["l"]}</label>'
    input_html = ""

    if inp.get('type') == 'select':
        opts_html = "".join([f'<option value="{i}">{opt}</option>' for i, opt in enumerate(inp['opts'])])
        input_html = f'''<div class="relative">
            <select id="{tool_id}-{inp["id"]}" class="w-full p-4 border border-slate-200 rounded-xl bg-slate-50 text-sm font-medium appearance-none focus:bg-white transition cursor-pointer input-premium">
                {opts_html}
            </select>
            <i class="fa-solid fa-chevron-down absolute right-4 top-4.5 text-slate-400 text-xs pointer-events-none"></i>
        </div>'''
    elif inp.get('type') == 'textarea':
        input_html = f'<textarea id="{tool_id}-{inp["id"]}" class="w-full p-4 border border-slate-200 rounded-xl bg-slate-50 text-sm focus:bg-white transition input-premium" rows="4" placeholder="{inp.get("p", "")}"></textarea>'
    else:
        itype = inp.get('type', 'number')
        step = 'step="any"' if itype != 'date' else ''
        input_html = f'<input type="{itype}" id="{tool_id}-{inp["id"]}" class="w-full p-4 border border-slate-200 rounded-xl bg-slate-50 text-sm font-medium focus:bg-white transition input-premium" placeholder="{inp.get("p", "")}" {step}>'

    return f'<div>{label}{input_html}</div>'

# Iterate over files in current directory
for filename in os.listdir('.'):
    if filename.endswith('.html') and filename not in ['index.html', 'kdv-hesaplama.html', 'tevkifat-hesaplama.html', 'kidem-tazminati.html', 'kredi-hesaplama.html', 'ai-asistan.html', 'blog/index.html']:

        # Read file
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()

        # Reset any previous injection if running multiple times (revert to placeholder)
        if '<div id="tool-placeholder"></div>' not in content:
             # Basic regex replace to strip out previous injection if it exists
             # But since I don't have a backup, I have to rely on the fact that I am re-generating these pages from `generate_tool_pages.py`?
             # No, `generate_tool_pages.py` rewrites them from scratch. I should run that first!
             # Or I can just continue if I assume I run `generate_tool_pages` before this.
             # But to be safe in this "Fix" plan, I should probably rely on the placeholder.
             # Wait, I didn't re-run `generate_tool_pages` in this plan.
             # If I run `inject_inputs` again on an already injected file, it won't find the placeholder.
             # So I MUST re-run `generate_tool_pages.py` first to get a clean state.
             pass

        # Identify tool ID from content (I embedded it in the HTML comments or ID)
        # Look for <div id="content-{tool_id}">
        match = re.search(r'id="content-([^"]+)"', content)
        if match:
            tool_id = match.group(1)
            if tool_id in tool_inputs:
                print(f"Injecting inputs for {tool_id} into {filename}")

                # Generate Grid HTML
                inputs_list = tool_inputs[tool_id]
                cols = "2" if len(inputs_list) > 1 else "1"

                # Mobile Fix: gap-5 instead of gap-6
                inputs_html = f'<div class="grid grid-cols-1 md:grid-cols-{cols} gap-5 md:gap-6">'
                for inp in inputs_list:
                    inputs_html += generate_input_html(tool_id, inp)
                inputs_html += '</div>'

                # Add Calc Button and Result Card
                # Need to lookup color from calculator.js logic or hardcode?
                # I'll default to blue for simplicity or regex it from file?
                # The file has <div class="p-3 bg-blue-100... text-blue-600"> so I can infer color.
                color = "blue"
                if "bg-indigo-100" in content: color = "indigo"
                elif "bg-green-100" in content: color = "green" # emerald in calc js but green in class? calc.js uses color names that map to classes.
                elif "bg-purple-100" in content: color = "purple" # violet
                elif "bg-orange-100" in content: color = "orange" # amber

                # Map back to Tailwind colors used in calculator.js render logic for consistency
                # calc.js: blue->blue, green->emerald, purple->violet, orange->amber, indigo->indigo
                # But my generated HTML used specific classes? No, I used a template.
                # Actually my generate_tool_pages.py didn't set color logic! It defaulted to blue icons.
                # I should fix colors too if I can, but inputs are priority.

                btn_html = f'''
                <button onclick="calc_{tool_id}()" class="btn-calc w-full mt-8 py-4 rounded-xl font-bold text-white text-sm tracking-wide shadow-lg shadow-{color}-500/20 flex justify-center items-center gap-2 bg-{color}-600 hover:bg-{color}-700 transition">
                    <i class="fa-solid fa-bolt"></i> Hesapla
                </button>

                <div id="res-{tool_id}" class="result-card hidden mt-8 p-6 rounded-2xl relative group bg-{color}-50 border border-{color}-100">
                    <button id="btn-copy-{tool_id}" onclick="copyResult('{tool_id}')" class="absolute top-4 right-4 text-xs bg-white border border-slate-200 px-3 py-1.5 rounded-lg hover:bg-slate-50 transition text-slate-500 flex items-center gap-1 shadow-sm">
                        <i class="fa-regular fa-copy"></i> Kopyala
                    </button>
                    <p class="text-[10px] font-bold text-{color}-600 uppercase tracking-widest mb-2">SONUÇ</p>
                    <div id="val-{tool_id}" class="text-3xl font-black text-slate-900 tracking-tight"></div>
                    <div id="detail-{tool_id}" class="text-sm text-slate-500 mt-3 pt-3 border-t border-slate-200/50 empty:hidden"></div>
                </div>
                '''

                full_injection = inputs_html + btn_html

                # Replace placeholder
                new_content = content.replace('<div id="tool-placeholder"></div>', full_injection)

                # Fix color classes if they were blue by default in template
                if color != 'blue':
                    new_content = new_content.replace('bg-blue-100', f'bg-{color}-100')
                    new_content = new_content.replace('text-blue-600', f'text-{color}-600')

                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(new_content)
