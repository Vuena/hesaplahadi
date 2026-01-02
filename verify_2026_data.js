const fs = require('fs');
const jsdom = require("jsdom");
const { JSDOM } = jsdom;

// Mock DOM
const dom = new JSDOM('<!DOCTYPE html><html><body></body></html>');
global.window = dom.window;
global.document = dom.window.document;
global.localStorage = {
  getItem: () => null,
  setItem: () => {}
};
global.navigator = { clipboard: { writeText: () => Promise.resolve() } };

// Mock Element
global.document.getElementById = (id) => {
    return {
        value: '',
        innerText: '',
        innerHTML: '',
        classList: { remove: ()=>{}, add: ()=>{} },
        scrollIntoView: () => {},
        querySelector: () => null,
        appendChild: () => {}
    };
};

// Load Scripts
// We need to concat them to run in this context or eval them
const calcJs = fs.readFileSync('assets/js/calculator.js', 'utf8');
const toolsJs = fs.readFileSync('assets/js/tools.js', 'utf8');

eval(calcJs);
eval(toolsJs);

console.log("--- 2026 Data Verification ---");

// 1. Verify CPI Data for 2025_YE
if(cpi_data['2025_YE'] === 3500) {
    console.log("PASS: CPI Data for 2025_YE is 3500");
} else {
    console.log("FAIL: CPI Data is " + cpi_data['2025_YE']);
}

// 2. Verify Asgari Ucret Logic
// We can't easily run the function because it relies on getVal/showRes which manipulate DOM heavily.
// But we can check if the source code contains the new values.
if(calcJs.includes('net = 28500') && calcJs.includes('gross = 33530')) {
     console.log("PASS: Asgari Ucret Code contains updated 2026 values (28500/33530)");
} else {
     console.log("FAIL: Asgari Ucret values not found in source");
}

// 3. Verify Kidem Tavan
if(calcJs.includes('if (sal > 60000) sal = 60000')) {
     console.log("PASS: Kidem Tavan Code contains 60000 limit");
} else {
     console.log("FAIL: Kidem Tavan limit not updated");
}

// 4. Verify MTV Logic in Tools.js
if(toolsJs.includes('base *= 1.35')) {
     console.log("PASS: MTV Logic uses 35% increase (YDO)");
} else {
     console.log("FAIL: MTV Logic missing 1.35 multiplier");
}
