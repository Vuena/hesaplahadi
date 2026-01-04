
import datetime

all_files = ["ai-asistan.html","ai-diyetisyen.html","akademik-tesvik-hesaplama.html","altili-ne-verir-hesaplama.html","altin-hesaplama.html","amazon-komisyon-hesaplama.html","apply_fixes.py","aralikli-oruc-hesaplama.html","asgari-ucret-hesaplama.html","audit_site.py","ay-burcu-hesaplama.html","bazal-metabolizma-hizi-bmr-hesaplama.html","bilesik-faiz-hesaplama.html","brutten-nete-maas-hesaplama.html","burc-hesaplama.html","calculator_fix.js","cekilis-araci.html","check_remaining.py","ciceksepeti-komisyon-hesaplama.html","cin-takvimi-cinsiyet-hesaplama.html","create_blog_content.py","create_new_tools.py","deger-artis-kazanci-hesaplama.html","deneme-puan-hesaplama.html","dikdortgen-alan-ve-cevre-hesaplama.html","dogum-haritasi-hesaplama.html","dolar-enflasyonu-hesaplama.html","dolar-hesaplama.html","edebiyat-not-hesaplama.html","elektrik-faturasi-hesaplama.html","elektrikli-arac-sarj-hesaplama.html","emekli-maas-hesaplama.html","emlakci-komisyonu-hesaplama.html","enflasyon-alim-gucu-hesaplama.html","esnek-hesap-faiz-hesaplama.html","euro-hesaplama.html","fix_headers_regression.py","fix_ids_and_js.py","fix_ids_and_js_batched.py","fix_ids_and_js_batched_micro.py","fix_ids_and_js_batched_small.py","fix_logos.py","fix_syntax.py","freelancer-gelir-vergisi-hesaplama.html","gebelik-hesaplama-ve-dogum-tarihi.html","generate_blog.py","generate_blogs.py","generate_more_blogs.py","generate_new_blogs.py","generate_pages.py","generate_sitemap.py","generate_tool_pages.py","gizlilik-politikasi.html","guclu-sifre-olusturucu.html","gumus-hesaplama.html","gunes-paneli-amortisman-hesaplama.html","gunluk-makro-protein,-karbonhidrat,-yag-hesaplama.html","gunluk-su-i̇htiyaci-hesaplama.html","hakkimizda.html","hangi-gun-hesaplama.html","hepsiburada-komisyon-hesaplama.html","hiz,-yol-ve-zaman-hesaplama.html","iban-dogrulama-ve-cozumleme-araci.html","ikinci-el-tasit-kredisi-hesaplama.html","iletisim.html","index.html","infaz-hesaplama.html","inject_inputs.py","inject_missing_seo.py","inject_static_sidebar.py","instagram-etkilesim-orani-hesaplama.html","islah-harci-hesaplama.html","i̇deal-kilo-hesaplama.html","i̇ki-tarih-arasi-gun-sayaci.html","i̇ndirim-hesaplama.html","i̇nternet-hizi-i̇ndirme-suresi-hesaplama.html","kahve-tolerans-hesaplama.html","karbon-ayak-izi-hesaplama.html","kdv-hesaplama.html","kdv_redesign.html","kedi-yasi-hesaplama.html","kelime-ve-karakter-sayaci.html","kidem-tazminati-hesaplama.html","kira-zammi-hesaplama.html","kopek-yasi-hesaplama.html","kpss-onlisans-puan-hesaplama.html","kredi-hesaplama.html","kredi-karti-asgari-odeme-hesaplama.html","kus-yasi-hesaplama.html","kâr-marji-ve-zarar-hesaplama.html","layout_generator.py","link_blog_to_tools.py","maas-zam-orani-hesaplama.html","map_tools.py","memur-maas-zammi-hesaplama.html","mesai-hesaplama.html","mevduat-faizi-hesaplama.html","milli-piyango-hesaplama.html","mtv-hesaplama.html","n11-komisyon-hesaplama.html","netten-brute-maas-hesaplama.html","numeroloji-hesaplama.html","outdated_files.txt","qr-kod-olusturucu.html","rebuild_blogs.py","remove_subtitle.py","robots.txt","sigara-maliyeti-hesaplama.html","sinav-geri-sayim-sayaci.html","sitemap.xml","solar-harita-hesaplama.html","sosyal-medya-en-iyi-saat-hesaplama.html","spor-nabiz-araligi-hesaplama.html","takdir-tesekkur-hesaplama-e-okul.html","tam-yas-hesaplama.html","tarihe-gun-ekleme-hesaplama.html","tevkifat-hesaplama.html","tiktok-youtube-gelir-hesaplama.html","tools_data.json","trendyol-komisyon-hesaplama.html","tyt-ayt-net-hesaplama.html","ucretli-ogretmen-maas-hesaplama.html","universite-not-ortalamasi-hesaplama.html","universite-not-ortalamasi-vize-final-hesaplama.html","update_footers_batched.py","update_headers_safely.py","update_inflation_data.py","update_layout.py","update_site_fixes.py","update_site_layout.py","update_tool_headers.py","update_ui_fixes.py","updated_files.txt","uyku-dongusu-hesaplama.html","vekalet-ucreti-hesaplama.html","verify_2026_data.js","verify_calculations.js","verify_enflasyon_ui.py","verify_fixes.py","verify_header.py","verify_mobile_ux.py","verify_tools.py","verify_updates.py","vize-final-hesaplama.html","vucut-kitle-i̇ndeksi-bmi-hesaplama.html","yakit-tuketimi-hesaplama.html","yapay-zeka-token-maliyet-hesaplama.html","yks-siralama-hesaplama.html","yukselen-burc-hesaplama.html","yumurta-haslama-suresi-hesaplama.html","yuzde-hesaplama-araci.html","zekat-hesaplama.html","__pycache__/layout_generator.cpython-312.pyc","__pycache__/map_tools.cpython-311.pyc",".idx/dev.nix","blog/2026-altin-fiyatlari-ve-yatirim-tavsiyeleri.html","blog/2026-altin-piyasasi-yorum.html","blog/2026-asgari-ucret-tahminleri.html","blog/2026-gelir-vergisi-dilimleri-ve-maas-etkisi.html","blog/2026-kidem-tazminati-tavani-ve-hesaplama.html","blog/2026-memur-ve-emekli-zammi.html","blog/2026-mtv-motorlu-tasitlar-vergisi-zamlari.html","blog/2026-vekalet-ucreti-ve-mahkeme-harclari.html","blog/akademik-tesvik-odenegi-hesaplama-ve-sartlari.html","blog/altili-ganyan-birim-fiyat-ve-ikramiye-hesaplama.html","blog/altin-yatirimi-fiziki-mi-banka-mi.html","blog/arac-deger-kaybi-hesaplama-nasil-yapilir.html","blog/arac-kasko-degeri-nedir-nasil-hesaplanir.html","blog/ay-burcu-nedir-ve-nasil-hesaplanir.html","blog/bazal-metabolizma-hizi-bmr-ve-diyet.html","blog/bireysel-emeklilik-sistemi-bes-nedir.html","blog/brutten-nete-maas-hesaplama-rehberi.html","blog/burc-uyumu-ve-ask-hesaplama.html","blog/cin-takvimi-cinsiyet-hesaplama-dogruluk-payi.html","blog/cocuklar-icin-kodlama-egitimi.html","blog/denetimli-serbestlik-ve-yatar-hesaplama-2026.html","blog/dengeli-beslenme-tabagi.html","blog/ders-calisma-teknikleri-pomodoro.html","blog/dolar-enflasyonu-ve-reel-getiri-hesaplama.html","blog/doviz-yatirimi-mantikli-mi.html","blog/emekli-maasi-2026-ocak-zammi-hesaplama.html","blog/enflasyon-nedir-nasil-hesaplanir.html","blog/enflasyonun-alim-gucune-etkisi-rehberi.html","blog/esnek-hesap-kmh-faizi-hesaplama-rehberi.html","blog/ev-almak-mi-kiralamak-mi.html","blog/evde-spor-yaparak-zayiflama.html","blog/gecikme-faizi-hesaplama-rehberi.html","blog/gumus-yatirimi-mantikli-mi-2026.html","blog/gunluk-su-tuketimi-ne-kadar-olmali.html","blog/gunluk-yuruyusun-faydalari.html","blog/hizli-okuma-teknikleri.html","blog/ideal-kilo-nasil-hesaplanir-formulu-nedir.html","blog/ihbar-tazminati-hesaplama-rehberi.html","blog/index.html","blog/intermittent-fasting-aralikli-oruc-nedir.html","blog/internet-hizi-ve-indirme-suresi-hesaplama.html","blog/is-gorusmesinde-maas-pazarligi.html","blog/islah-harci-hesaplama-ve-dava-sureci.html","blog/kalori-acigi-ile-zayiflama.html","blog/kdv-tevkifati-nedir-kimler-yapar.html","blog/kelime-sayaci-ve-seo-uyumlu-makale-yazimi.html","blog/kilonuza-gore-gunluk-su-ihtiyaci-hesaplama.html","blog/kisisel-finans-yonetimi.html","blog/konut-kredisi-cekerken-dikkat-edilmesi-gerekenler.html","blog/kopek-ve-kedi-yasi-hesaplama-insan-yili.html","blog/kpss-onlisans-puan-hesaplama-ve-net-dagilimi.html","blog/kredi-karti-puanlari-nasil-kullanilir.html","blog/kredi-notu-nasil-yukseltilir.html","blog/lgs-hazirlik-rehberi.html","blog/metabolizma-hizlandirma-yollari.html","blog/milli-piyango-vergi-kesintisi-hesaplama.html","blog/muhabbet-kusu-yasi-nasil-anlasilir.html","blog/numeroloji-isim-analizi-ve-kader-sayisi.html","blog/python-ile-yazilima-baslamak.html","blog/solar-return-gunes-donusu-haritasi-nedir.html","blog/su-icmenin-cilde-faydalari.html","blog/takdir-tesekkur-almak-icin-kac-puan-gerekir.html","blog/tasarruf-yapmanin-yollari.html","blog/template.html","blog/vucut-kitle-indeksi-bmi-gercegi.html","blog/vucut-kitle-indeksi-bmi-nedir.html","blog/yapay-zeka-gelecegi.html","blog/yks-2026-hazirlik-rehberi.html","blog/yks-2026-siralama-ve-puan-hesaplama-taktikleri.html","blog/yukselen-burc-hesaplama-rehberi.html","blog/yuzde-hesaplama-formulu-ve-ornekleri.html","tests/test_kdv_math.py","verification/blog_verification.png","verification/brut_net_result.png","verification/sidebar_check.png","verification/verify_blog.py","verification/verify_brut_net.py","verification/verify_sidebar.py","assets/css/style.css","assets/img/favicon.svg","assets/js/autolinker.js","assets/js/blog-data.js","assets/js/calculator.js","assets/js/tools.js","tests/__pycache__/test_kdv_math.cpython-312.pyc"]


def generate_sitemap():
    base_url = "https://hesaplahadi.com/"
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    sitemap_content = '<?xml version="1.0" encoding="UTF-8"?>\n'
    sitemap_content += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'

    # List of files to exclude
    excluded_files = [
        "kdv_redesign.html",
        "yuzde-hesaplama-araci.html", # Incorrect name
        "enflasyon-alim-gucu-hesaplama.html", # Replaced with new guide
        "blog/template.html",
        "blog/2026-mtv-oranlari.html", # Deleted
        
    ]

    # Filter for HTML files only
    html_files = [f for f in all_files if f.endswith('.html') and f not in excluded_files]

    # Prioritize main pages
    main_pages = ["index.html", "hakkimizda.html", "iletisim.html", "gizlilik-politikasi.html", "ai-asistan.html"]

    for page in main_pages:
         if page in html_files:
            sitemap_content += f'  <url>\n'
            sitemap_content += f'    <loc>{base_url}{page}</loc>\n'
            sitemap_content += f'    <lastmod>{today}</lastmod>\n'
            sitemap_content += f'    <priority>1.0</priority>\n' if page == "index.html" else f'    <priority>0.8</priority>\n'
            sitemap_content += f'  </url>\n'

    # Process other root-level pages (tools)
    tool_pages = [f for f in html_files if f not in main_pages and "/" not in f]
    for page in tool_pages:
        sitemap_content += f'  <url>\n'
        sitemap_content += f'    <loc>{base_url}{page}</loc>\n'
        sitemap_content += f'    <lastmod>{today}</lastmod>\n'
        sitemap_content += f'    <priority>0.8</priority>\n'
        sitemap_content += f'  </url>\n'

    # Process blog pages
    blog_pages = [f for f in html_files if f.startswith('blog/')]
    for page in blog_pages:
        sitemap_content += f'  <url>\n'
        sitemap_content += f'    <loc>{base_url}{page}</loc>\n'
        sitemap_content += f'    <lastmod>{today}</lastmod>\n'
        sitemap_content += f'    <priority>0.7</priority>\n'
        sitemap_content += f'  </url>\n'

    sitemap_content += '</urlset>'

    return sitemap_content


new_sitemap = generate_sitemap()

