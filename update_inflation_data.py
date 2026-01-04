
import os
import re

# --- DATA ---
# Annual Inflation Rates (Realized & OVP Targets)
# Source: TCMB / TÜİK & OVP (2025-2027)
rates = {
    2000: 39.0, 2001: 68.5, 2002: 29.7,
    2003: 18.4, 2004: 9.32, 2005: 7.72, 2006: 9.65, 2007: 8.39, 2008: 10.06, 2009: 6.53,
    2010: 6.40, 2011: 10.45, 2012: 6.16, 2013: 7.40, 2014: 8.17, 2015: 8.81, 2016: 8.53,
    2017: 11.92, 2018: 20.30, 2019: 11.84, 2020: 14.60, 2021: 36.08, 2022: 64.27, 2023: 64.77,
    2024: 44.38, # Estimating/Realized
    2025: 17.5,  # OVP Forecast
    2026: 9.7    # OVP Forecast
}

# Calculate Indices (Base 2003 = 100)
# Note: This is a simplification. Official indices are monthly.
# We are generating an "Annual Average Index" or "Year End Index" map.
# Given the tool asks for "Start Year" and "End Year", annual indices are appropriate.
indices = {}
current_index = 100.0
indices[2003] = current_index

# Forward (2004-2026)
for y in range(2004, 2027):
    rate = rates.get(y, 0)
    current_index = current_index * (1 + rate / 100)
    indices[y] = round(current_index, 2)

# Backward (2000-2002)
# 2003 value was result of 2003 inflation applied to 2002.
# Index_2003 = Index_2002 * (1 + Rate_2003/100)
# Index_2002 = Index_2003 / (1 + Rate_2003/100)
prev_index = 100.0
for y in range(2003, 1999, -1):
    rate = rates.get(y, 0)
    prev_index = prev_index / (1 + rate / 100)
    indices[y-1] = round(prev_index, 2)

# Format for JS
js_obj_str = "window.cpi_data = {\n"
sorted_keys = sorted(indices.keys())
for k in sorted_keys:
    js_obj_str += f"    {k}: {indices[k]},\n"
js_obj_str += "};"

print("Generated CPI Data:")
print(js_obj_str)

# --- UPDATE CALCULATOR.JS ---
calc_js_path = 'assets/js/calculator.js'
with open(calc_js_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Replace cpi_data
# Regex to find 'const cpi_data = { ... };'
content = re.sub(r'const cpi_data = \{[^}]+\};', js_obj_str, content)

# 2. Add populateInflationDropdowns function
new_func = """
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
"""

# Append this function before 'window.addEventListener' or at the end of helpers
# We can just append it before 'function calc_kdv' for example, or generally in helpers area.
# Let's insert it before 'window.addEventListener' to be safe.
if "function populateInflationDropdowns" not in content:
    content = content.replace("window.addEventListener('load', () => {", new_func + "\nwindow.addEventListener('load', () => {")

# 3. Update calc_enflasyon to use window.cpi_data and handle formatting
# The original function:
# function calc_enflasyon() { const a=getNum('enflasyon','amt'); const s=parseInt(getVal('enflasyon','start')); const e=parseInt(getVal('enflasyon','end')); const i1=cpi_data[s]||100; const i2=cpi_data[e]||100; const r=i2/i1; showRes('enflasyon',(a*r).toLocaleString('tr-TR',{maximumFractionDigits:2})+' TL', `Enflasyon Katsayısı: ${r.toFixed(2)}x`); }

new_calc_enflasyon = """function calc_enflasyon() {
    const a=getNum('enflasyon','amt');
    const s=parseInt(getVal('enflasyon','start'));
    const e=parseInt(getVal('enflasyon','end'));
    const i1=window.cpi_data[s]||100;
    const i2=window.cpi_data[e]||100;
    const r=i2/i1;
    showRes('enflasyon',(a*r).toLocaleString('tr-TR',{maximumFractionDigits:2})+' TL', `Enflasyon Katsayısı: ${r.toFixed(2)}x (${s} -> ${e})`);
}"""

# Regex replace the old one function
content = re.sub(r'function calc_enflasyon\(\) \{[^}]+\}', new_calc_enflasyon, content)

# 4. Add call to populateInflationDropdowns in Init
if "populateInflationDropdowns();" not in content:
    content = content.replace("renderSidebar();", "renderSidebar();\n    populateInflationDropdowns();")

with open(calc_js_path, 'w', encoding='utf-8') as f:
    f.write(content)
print(f"Updated {calc_js_path}")

# --- UPDATE TOOLS.JS (Rent Calculator) ---
tools_js_path = 'assets/js/tools.js'
with open(tools_js_path, 'r', encoding='utf-8') as f:
    t_content = f.read()

# Update calc_kira to use dynamic data
# Old: function calc_kira() { const curr = getNum2('kira-curr'); const rate = 0.45; const next = curr * (1 + rate); showRes('kira', next.toLocaleString('tr-TR') + ' TL', "Yasal Artış Oranı (TÜFE)"); }

new_calc_kira = """function calc_kira() {
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
}"""

# Regex replace
t_content = re.sub(r'function calc_kira\(\) \{[^}]+\}', new_calc_kira, t_content)

with open(tools_js_path, 'w', encoding='utf-8') as f:
    f.write(t_content)
print(f"Updated {tools_js_path}")

# --- UPDATE HTML ---
html_path = 'enflasyon-alim-gucu-hesaplama.html'
with open(html_path, 'r', encoding='utf-8') as f:
    h_content = f.read()

# Remove the hardcoded script block at the end that populates years
# It looks like:
# <script>
#     // Init Years
#     const start = document.getElementById('enflasyon-start');
# ...
# </script>

h_content = re.sub(r'<script>\s+// Init Years[\s\S]*?</script>', '', h_content)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(h_content)
print(f"Updated {html_path}")
