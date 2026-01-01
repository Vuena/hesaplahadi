
import os
import re

# Template path
TEMPLATE_FILE = 'kdv-hesaplama.html'

# Common SEO Content (Placeholder - will be refined later or injected)
SEO_TEXT_TEMPLATE = """
            <article class="bg-white rounded-2xl shadow-sm border border-slate-200 p-8 info-panel">
                <h2 class="text-xl font-bold text-slate-800 mb-4">{title} Nedir?</h2>
                <p class="mb-4">{desc_long}</p>
                <h3 class="text-lg font-bold text-slate-800 mb-3">Nasıl Hesaplanır?</h3>
                <p class="mb-4">{how_to}</p>
                <div class="p-4 bg-blue-50 rounded-xl border border-blue-100">
                    <p class="text-sm text-blue-800 font-medium"><i class="fa-solid fa-circle-info mr-2"></i>Bu araç 2026 güncel verileri ve tahminleri kullanılarak hazırlanmıştır.</p>
                </div>
            </article>
"""

TOOLS_CONFIG = [
    {
        'filename': 'hangi-gun-hesaplama.html',
        'title': 'Hangi Gün Hesaplama',
        'desc': 'Girdiğiniz tarihin haftanın hangi gününe denk geldiğini öğrenin.',
        'keywords': 'hangi gün, tarih gün bulma, haftanın günü hesaplama',
        'icon': 'fa-calendar-day',
        'form_html': """
                <div class="grid grid-cols-1 gap-6">
                    <div>
                        <label class="block text-xs font-bold text-slate-600 uppercase tracking-wide mb-2 ml-1">Tarih Seçin</label>
                        <input type="date" id="day-date" class="w-full p-4 border border-slate-200 rounded-xl bg-slate-50 text-sm font-medium focus:bg-white transition input-premium">
                    </div>
                </div>
                <button onclick="calc_day()" class="btn-calc w-full mt-8 py-4 rounded-xl font-bold text-white text-sm tracking-wide shadow-lg shadow-blue-500/20 flex justify-center items-center gap-2">
                    <i class="fa-solid fa-search"></i> Günü Bul
                </button>
                <div id="res-day" class="result-card hidden mt-8 p-6 rounded-2xl relative group">
                    <p class="text-[10px] font-bold text-blue-600 uppercase tracking-widest mb-2">BU TARİH</p>
                    <div id="val-day" class="text-3xl md:text-4xl font-black text-slate-900 tracking-tight"></div>
                    <div id="detail-day" class="text-sm text-slate-500 mt-3 pt-3 border-t border-slate-200/50"></div>
                </div>
        """,
        'seo_data': {
            'title': 'Hangi Gün',
            'desc_long': 'Bu araç, seçtiğiniz tarihin haftanın hangi gününe (Pazartesi, Salı vb.) denk geldiğini anında hesaplar. Geçmişteki doğum gününüzün veya gelecekteki bir planın hangi gün olduğunu öğrenmek için idealdir.',
            'how_to': 'Tarih seçiciyi kullanarak günü, ayı ve yılı belirleyin. Hesapla butonuna bastığınızda sistem otomatik olarak o tarihin haftanın hangi günü olduğunu ekrana yansıtacaktır.'
        }
    },
    {
        'filename': 'tarihe-gun-ekleme-hesaplama.html',
        'title': 'Tarihe Gün Ekleme Hesaplama',
        'desc': 'Bir tarihe belirli bir gün sayısı ekleyin veya çıkarın.',
        'keywords': 'tarihe gün ekleme, tarih hesaplama, gün çıkarma',
        'icon': 'fa-calendar-plus',
        'form_html': """
                <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                    <div>
                        <label class="block text-xs font-bold text-slate-600 uppercase tracking-wide mb-2 ml-1">Başlangıç Tarihi</label>
                        <input type="date" id="add-date" class="w-full p-4 border border-slate-200 rounded-xl bg-slate-50 text-sm font-medium focus:bg-white transition input-premium">
                    </div>
                    <div>
                        <label class="block text-xs font-bold text-slate-600 uppercase tracking-wide mb-2 ml-1">Eklenecek Gün (Çıkarmak için -)</label>
                        <input type="number" id="add-days" placeholder="Örn: 90 veya -30" class="w-full p-4 border border-slate-200 rounded-xl bg-slate-50 text-sm font-medium focus:bg-white transition input-premium">
                    </div>
                </div>
                <button onclick="calc_date_add()" class="btn-calc w-full mt-8 py-4 rounded-xl font-bold text-white text-sm tracking-wide shadow-lg shadow-blue-500/20 flex justify-center items-center gap-2">
                    <i class="fa-solid fa-calculator"></i> Yeni Tarihi Hesapla
                </button>
                <div id="res-date-add" class="result-card hidden mt-8 p-6 rounded-2xl relative group">
                    <p class="text-[10px] font-bold text-blue-600 uppercase tracking-widest mb-2">HESAPLANAN TARİH</p>
                    <div id="val-date-add" class="text-3xl md:text-4xl font-black text-slate-900 tracking-tight"></div>
                    <div id="detail-date-add" class="text-sm text-slate-500 mt-3 pt-3 border-t border-slate-200/50"></div>
                </div>
        """,
        'seo_data': {
            'title': 'Tarihe Gün Ekleme',
            'desc_long': 'Seçtiğiniz bir tarihe belirli bir gün sayısı ekleyerek veya çıkararak yeni tarihi bulmanızı sağlar. Vade hesaplama, teslim tarihi belirleme veya 90 gün sonrası gibi hesaplamalar için kullanılır.',
            'how_to': 'Başlangıç tarihini seçin ve eklenecek gün sayısını girin. Geriye gitmek isterseniz gün sayısını eksi (örneğin -10) olarak girebilirsiniz.'
        }
    },
    {
        'filename': 'vize-final-hesaplama.html',
        'title': 'Vize Final Ortalaması Hesaplama',
        'desc': 'Vize ve final notlarınızla ders ortalamanızı ve geçme durumunuzu hesaplayın.',
        'keywords': 'vize final hesaplama, not ortalaması, ders geçme notu',
        'icon': 'fa-graduation-cap',
        'form_html': """
                <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
                    <div>
                        <label class="block text-xs font-bold text-slate-600 uppercase tracking-wide mb-2 ml-1">Vize Notu</label>
                        <input type="number" id="vf-vize" placeholder="0-100" class="w-full p-4 border border-slate-200 rounded-xl bg-slate-50 text-sm font-medium focus:bg-white transition input-premium">
                    </div>
                    <div>
                        <label class="block text-xs font-bold text-slate-600 uppercase tracking-wide mb-2 ml-1">Final Notu</label>
                        <input type="number" id="vf-final" placeholder="0-100" class="w-full p-4 border border-slate-200 rounded-xl bg-slate-50 text-sm font-medium focus:bg-white transition input-premium">
                    </div>
                     <div>
                        <label class="block text-xs font-bold text-slate-600 uppercase tracking-wide mb-2 ml-1">Vize Etkisi (%)</label>
                        <select id="vf-ratio" class="w-full p-4 border border-slate-200 rounded-xl bg-slate-50 text-sm font-medium focus:bg-white transition input-premium">
                            <option value="0.3">%30</option>
                            <option value="0.4" selected>%40 (Standart)</option>
                            <option value="0.5">%50</option>
                        </select>
                    </div>
                </div>
                <button onclick="calc_vf()" class="btn-calc w-full mt-8 py-4 rounded-xl font-bold text-white text-sm tracking-wide shadow-lg shadow-blue-500/20 flex justify-center items-center gap-2">
                    <i class="fa-solid fa-calculator"></i> Ortalamayı Hesapla
                </button>
                <div id="res-vf" class="result-card hidden mt-8 p-6 rounded-2xl relative group">
                    <p class="text-[10px] font-bold text-blue-600 uppercase tracking-widest mb-2">DERS NOTU</p>
                    <div id="val-vf" class="text-3xl md:text-4xl font-black text-slate-900 tracking-tight"></div>
                    <div id="detail-vf" class="text-sm text-slate-500 mt-3 pt-3 border-t border-slate-200/50"></div>
                </div>
        """,
        'seo_data': {
            'title': 'Vize Final Ortalaması',
            'desc_long': 'Üniversite öğrencileri için vize ve final notlarını girerek ders başarı notunu hesaplayan pratik bir araçtır. Genellikle %40 vize ve %60 final etkisi baz alınır ancak oranları değiştirebilirsiniz.',
            'how_to': 'Vize ve final notlarınızı ilgili kutucuklara girin. Eğer okulunuzda vize etki oranı farklıysa (örneğin %30), seçeneklerden ilgili oranı belirleyin ve hesapla butonuna basın.'
        }
    },
    {
        'filename': 'universite-not-ortalamasi-hesaplama.html',
        'title': 'Üniversite Not Ortalaması Hesaplama (GNO)',
        'desc': 'Dönemlik not ortalamanızı (GNO/ANO) ders kredilerine göre hesaplayın.',
        'keywords': 'gno hesaplama, ano hesaplama, üniversite ortalama, gpa',
        'icon': 'fa-scroll',
        'form_html': """
                <div id="gpa-container" class="space-y-4">
                    <div class="grid grid-cols-12 gap-2 text-xs font-bold text-slate-500 uppercase tracking-wide ml-1">
                        <div class="col-span-6 md:col-span-5">Ders Adı</div>
                        <div class="col-span-3 md:col-span-3">Kredi/AKTS</div>
                        <div class="col-span-3 md:col-span-3">Not</div>
                        <div class="col-span-1"></div>
                    </div>
                    <div id="gpa-rows" class="space-y-3">
                        <!-- Dynamic Rows -->
                         <div class="grid grid-cols-12 gap-2 items-center gpa-row">
                            <div class="col-span-6 md:col-span-5">
                                <input type="text" placeholder="Ders 1" class="w-full p-3 border border-slate-200 rounded-lg bg-slate-50 text-sm">
                            </div>
                            <div class="col-span-3 md:col-span-3">
                                <input type="number" placeholder="Kr" value="3" class="w-full p-3 border border-slate-200 rounded-lg bg-slate-50 text-sm gpa-credit">
                            </div>
                            <div class="col-span-3 md:col-span-3">
                                <select class="w-full p-3 border border-slate-200 rounded-lg bg-slate-50 text-sm gpa-grade">
                                    <option value="4.0">AA (4.0)</option>
                                    <option value="3.5">BA (3.5)</option>
                                    <option value="3.0">BB (3.0)</option>
                                    <option value="2.5">CB (2.5)</option>
                                    <option value="2.0">CC (2.0)</option>
                                    <option value="1.5">DC (1.5)</option>
                                    <option value="1.0">DD (1.0)</option>
                                    <option value="0.5">FD (0.5)</option>
                                    <option value="0.0">FF (0.0)</option>
                                </select>
                            </div>
                             <div class="col-span-1 text-center">
                                <button onclick="this.closest('.gpa-row').remove()" class="text-red-400 hover:text-red-600"><i class="fa-solid fa-trash"></i></button>
                            </div>
                        </div>
                         <div class="grid grid-cols-12 gap-2 items-center gpa-row">
                            <div class="col-span-6 md:col-span-5">
                                <input type="text" placeholder="Ders 2" class="w-full p-3 border border-slate-200 rounded-lg bg-slate-50 text-sm">
                            </div>
                            <div class="col-span-3 md:col-span-3">
                                <input type="number" placeholder="Kr" value="3" class="w-full p-3 border border-slate-200 rounded-lg bg-slate-50 text-sm gpa-credit">
                            </div>
                            <div class="col-span-3 md:col-span-3">
                                <select class="w-full p-3 border border-slate-200 rounded-lg bg-slate-50 text-sm gpa-grade">
                                    <option value="4.0">AA (4.0)</option>
                                    <option value="3.5" selected>BA (3.5)</option>
                                    <option value="3.0">BB (3.0)</option>
                                    <option value="2.5">CB (2.5)</option>
                                    <option value="2.0">CC (2.0)</option>
                                    <option value="1.5">DC (1.5)</option>
                                    <option value="1.0">DD (1.0)</option>
                                    <option value="0.0">FF (0.0)</option>
                                </select>
                            </div>
                             <div class="col-span-1 text-center">
                                <button onclick="this.closest('.gpa-row').remove()" class="text-red-400 hover:text-red-600"><i class="fa-solid fa-trash"></i></button>
                            </div>
                        </div>
                    </div>
                     <button onclick="addGpaRow()" class="text-sm text-blue-600 font-bold hover:underline flex items-center gap-1 mt-2">
                        <i class="fa-solid fa-plus-circle"></i> Ders Ekle
                    </button>
                </div>

                <button onclick="calc_gpa()" class="btn-calc w-full mt-8 py-4 rounded-xl font-bold text-white text-sm tracking-wide shadow-lg shadow-blue-500/20 flex justify-center items-center gap-2">
                    <i class="fa-solid fa-calculator"></i> Ortalamayı Hesapla
                </button>
                <div id="res-gpa" class="result-card hidden mt-8 p-6 rounded-2xl relative group">
                    <p class="text-[10px] font-bold text-blue-600 uppercase tracking-widest mb-2">GENEL ORTALAMA</p>
                    <div id="val-gpa" class="text-3xl md:text-4xl font-black text-slate-900 tracking-tight"></div>
                    <div id="detail-gpa" class="text-sm text-slate-500 mt-3 pt-3 border-t border-slate-200/50"></div>
                </div>
        """,
        'seo_data': {
            'title': 'Üniversite Not Ortalaması',
            'desc_long': 'Dönem sonu not ortalamanızı (GNO/ANO) hesaplamak için derslerinizi, kredilerini ve harf notlarını girin. Bu araç, üniversitelerde kullanılan standart 4.00 üzerinden hesaplama sistemine (AA, BA, BB...) göre çalışır.',
            'how_to': 'Her ders için kredi sayısını ve aldığınız harf notunu girin. "Ders Ekle" butonunu kullanarak dönemdeki tüm dersleri listeye ekleyin ve hesapla butonuna basarak kümülatif veya dönemlik ortalamanızı görün.'
        }
    },
    {
        'filename': 'asgari-ucret-hesaplama.html',
        'title': '2026 Asgari Ücret Hesaplama',
        'desc': '2026 yılı tahmini asgari ücret verileriyle brüt ve net maaş hesaplaması.',
        'keywords': '2026 asgari ücret, asgari ücret ne kadar, brüt net asgari ücret',
        'icon': 'fa-money-bill-wave',
        'form_html': """
                <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                    <div>
                         <label class="block text-xs font-bold text-slate-600 uppercase tracking-wide mb-2 ml-1">Dönem Seçimi</label>
                        <select id="asgari-period" class="w-full p-4 border border-slate-200 rounded-xl bg-slate-50 text-sm font-medium focus:bg-white transition input-premium">
                            <option value="2026-1" selected>2026 Ocak - Haziran (Tahmini)</option>
                            <option value="2025-2">2025 Temmuz - Aralık</option>
                        </select>
                    </div>
                     <div>
                        <label class="block text-xs font-bold text-slate-600 uppercase tracking-wide mb-2 ml-1">Hesaplama Yönü</label>
                         <select id="asgari-type" class="w-full p-4 border border-slate-200 rounded-xl bg-slate-50 text-sm font-medium focus:bg-white transition input-premium">
                            <option value="bn" selected>Brütten Nete</option>
                            <option value="nb">Netten Brüte</option>
                        </select>
                    </div>
                </div>

                 <div class="mt-4 p-4 bg-yellow-50 rounded-xl border border-yellow-100 text-sm text-yellow-800">
                    <i class="fa-solid fa-triangle-exclamation mr-2"></i> 2026 verileri resmi açıklamalara ve enflasyon beklentilerine (%25-%35) dayalı tahminlerdir.
                </div>

                <button onclick="calc_asgari()" class="btn-calc w-full mt-8 py-4 rounded-xl font-bold text-white text-sm tracking-wide shadow-lg shadow-blue-500/20 flex justify-center items-center gap-2">
                    <i class="fa-solid fa-coins"></i> Hesapla
                </button>
                <div id="res-asgari" class="result-card hidden mt-8 p-6 rounded-2xl relative group">
                    <p class="text-[10px] font-bold text-blue-600 uppercase tracking-widest mb-2">MAAŞ DETAYI</p>
                    <div id="val-asgari" class="text-3xl md:text-4xl font-black text-slate-900 tracking-tight"></div>
                    <div id="detail-asgari" class="text-sm text-slate-500 mt-3 pt-3 border-t border-slate-200/50"></div>
                </div>
        """,
        'seo_data': {
            'title': '2026 Asgari Ücret',
            'desc_long': '2026 yılı için beklenen asgari ücret zammı senaryolarına göre brüt ve net maaşınızı hesaplayın. Bu araç, resmi enflasyon hedefleri ve piyasa beklentilerini dikkate alarak tahmini sonuçlar sunar.',
            'how_to': 'Hesaplamak istediğiniz dönemi (2026 Ocak) seçin. Brütten nete veya netten brüte seçeneklerinden birini belirleyerek hesaplamayı başlatın. Sonuçlar tahmini yasal kesintiler düşüldükten sonra gösterilir.'
        }
    },
    {
        'filename': 'memur-maas-zammi-hesaplama.html',
        'title': 'Memur Maaş Zammı Hesaplama 2026',
        'desc': '2026 Ocak dönemi memur ve memur emeklisi maaş zammı hesaplama.',
        'keywords': 'memur zammı 2026, memur maaş hesaplama, enflasyon farkı',
        'icon': 'fa-user-tie',
        'form_html': """
                <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                    <div>
                        <label class="block text-xs font-bold text-slate-600 uppercase tracking-wide mb-2 ml-1">Mevcut Maaşınız (2025 Temmuz)</label>
                        <input type="number" id="memur-curr" class="w-full p-4 border border-slate-200 rounded-xl bg-slate-50 text-sm font-medium focus:bg-white transition input-premium" placeholder="Örn: 45000">
                    </div>
                    <div>
                        <label class="block text-xs font-bold text-slate-600 uppercase tracking-wide mb-2 ml-1">Beklenen Zam Oranı (%)</label>
                        <div class="relative">
                            <input type="number" id="memur-rate" value="11.25" class="w-full p-4 border border-slate-200 rounded-xl bg-slate-50 text-sm font-medium focus:bg-white transition input-premium">
                             <div class="absolute right-4 top-4 text-xs text-slate-400 font-bold">%</div>
                        </div>
                    </div>
                </div>

                 <div class="mt-2 text-xs text-slate-500">
                    * 2026 Ocak için Toplu Sözleşme (%6) + Enflasyon Farkı tahmini (~%5-7) baz alınmıştır.
                </div>

                <button onclick="calc_memur()" class="btn-calc w-full mt-8 py-4 rounded-xl font-bold text-white text-sm tracking-wide shadow-lg shadow-blue-500/20 flex justify-center items-center gap-2">
                    <i class="fa-solid fa-chart-line"></i> Zamlı Maaşı Hesapla
                </button>
                <div id="res-memur" class="result-card hidden mt-8 p-6 rounded-2xl relative group">
                    <p class="text-[10px] font-bold text-blue-600 uppercase tracking-widest mb-2">2026 OCAK TAHMİNİ MAAŞ</p>
                    <div id="val-memur" class="text-3xl md:text-4xl font-black text-slate-900 tracking-tight"></div>
                    <div id="detail-memur" class="text-sm text-slate-500 mt-3 pt-3 border-t border-slate-200/50"></div>
                </div>
        """,
         'seo_data': {
            'title': 'Memur Maaş Zammı 2026',
            'desc_long': '2026 Ocak ayında memurlara yapılacak toplu sözleşme zammı ve enflasyon farkı oranlarını kullanarak yeni maaşınızı hesaplayın. Enflasyon verilerine göre güncellenen dinamik bir hesaplama aracıdır.',
            'how_to': 'Şu anki net maaşınızı girin. Sistem otomatik olarak beklenen zam oranını (veya sizin girdiğiniz oranı) uygulayarak 2026 Ocak ayında elinize geçecek tahmini tutarı hesaplar.'
        }
    }
]

def create_tools():
    # Read template
    with open(TEMPLATE_FILE, 'r', encoding='utf-8') as f:
        template = f.read()

    for tool in TOOLS_CONFIG:
        print(f"Creating {tool['filename']}...")
        new_content = template

        # 1. Replace Title
        new_content = re.sub(r'<title>.*?</title>', f"<title>{tool['title']} | HesaplaHadi</title>", new_content)

        # 2. Replace Meta Description
        new_content = re.sub(r'<meta name="description" content=".*?">', f'<meta name="description" content="{tool["desc"]}">', new_content)

        # 3. Replace Keywords
        new_content = re.sub(r'<meta name="keywords" content=".*?">', f'<meta name="keywords" content="{tool["keywords"]}">', new_content)

        # 4. Replace Canonical
        new_content = re.sub(r'<link rel="canonical" href=".*?">', f'<link rel="canonical" href="https://hesaplahadi.com/{tool["filename"]}">', new_content)

        # 5. Replace H1 and Icon
        # Look for the header block
        header_regex = r'<div class="flex items-center gap-4 mb-6 pb-6 border-b border-slate-100">.*?</div>'
        new_header = f"""<div class="flex items-center gap-4 mb-6 pb-6 border-b border-slate-100">
                    <div class="p-3 bg-blue-100 rounded-2xl text-blue-600 shadow-sm">
                        <i class="fa-solid {tool['icon']} text-xl"></i>
                    </div>
                    <div>
                        <h1 class="text-2xl font-bold text-slate-900 tracking-tight">{tool['title']}</h1>
                        <p class="text-xs text-slate-500 mt-1">{tool['desc']}</p>
                    </div>
                </div>"""

        # Use simple string replacement for the header if regex is tricky due to newlines
        # Or locate the specific block
        start_marker = '<div class="flex items-center gap-4 mb-6 pb-6 border-b border-slate-100">'
        end_marker = '<!-- Static Form for KDV -->'

        # Finding the main content area to replace form
        # The template has <!-- Static Form for KDV --> ... <div id="res-kdv" ... </div>

        # We'll replace everything from <!-- Static Form for KDV --> down to the end of the form area
        # Easier: Find the <main> tag and replace the inner content carefully

        # Construct the new main content block
        new_main_content = f"""
            <div class="bg-white/90 backdrop-blur rounded-2xl shadow-sm border border-slate-200 p-6 md:p-8 animate-slide-up relative">

                {new_header}

                {tool['form_html']}

            </div>

            {SEO_TEXT_TEMPLATE.format(title=tool['seo_data']['title'], desc_long=tool['seo_data']['desc_long'], how_to=tool['seo_data']['how_to'])}
        """

        # Replace the entire <main> block content is risky if we lose sidebar.
        # We want to replace content INSIDE <main ...> ... </main>

        main_match = re.search(r'(<main class="col-span-1 lg:col-span-6 space-y-6">)(.*?)(</main>)', new_content, re.DOTALL)
        if main_match:
            new_content = new_content.replace(main_match.group(2), new_main_content)
        else:
            print(f"Error: Could not find main block in {tool['filename']}")
            continue

        # Write file
        with open(tool['filename'], 'w', encoding='utf-8') as f:
            f.write(new_content)

if __name__ == '__main__':
    create_tools()
