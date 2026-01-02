const fs = require('fs');
const vm = require('vm');
const jsdom = require("jsdom");
const { JSDOM } = jsdom;

// Mock DOM
const dom = new JSDOM(`<!DOCTYPE html>
<html>
<body>
    <div id="sidebar-list"></div>
    <div id="drawer-list"></div>
    <div id="mobile-tool-search"></div>
    <div id="desktop-tool-search"></div>
    <div id="res-asgari" class="hidden"></div>
    <div id="val-asgari"></div>
    <div id="detail-asgari"></div>

    <div id="res-mtv" class="hidden"></div>
    <div id="val-mtv"></div>
    <div id="detail-mtv"></div>

    <div id="res-kdv" class="hidden"></div>
    <div id="val-kdv"></div>
    <div id="detail-kdv"></div>
    <div id="kdv-res-net"></div>
    <div id="kdv-res-tax"></div>
    <div id="kdv-res-total"></div>
</body>
</html>`, {
    url: "https://example.com/index.html",
    runScripts: "dangerously",
    resources: "usable"
});

const window = dom.window;
const document = window.document;

// Mock LocalStorage
window.localStorage = {
    getItem: (key) => null,
    setItem: (key, val) => {},
    removeItem: (key) => {}
};

// Mock scrollIntoView (missing in JSDOM)
window.HTMLElement.prototype.scrollIntoView = function() {};

// Mock Clipboard
window.navigator.clipboard = {
    writeText: () => Promise.resolve()
};

// Load Calculator Code
const calculatorCode = fs.readFileSync('assets/js/calculator.js', 'utf8');

// Append Test Logic
const testCode = `
    console.log("--- Starting In-Context Verification ---");

    function setInput(id, value) {
        let el = document.getElementById(id);
        if (!el) {
            el = document.createElement('input');
            el.id = id;
            document.body.appendChild(el);
        }
        el.value = value;
    }

    function setSelect(id, value) {
        let el = document.getElementById(id);
        if (!el) {
            el = document.createElement('select');
            el.id = id;
            document.body.appendChild(el);
        }
        el.value = value;
    }

    try {
        // Test Asgari
        setInput('asgari-period', '-1');
        setInput('asgari-type', 'bn');
        calc_asgari();
        // Note: Asgari calc sets innerText/HTML
        // The mock DOM element exists as #val-asgari
        const asgariRes = document.getElementById('val-asgari').innerHTML; // Use innerHTML as showRes sets it
        console.log("Asgari Result: " + asgariRes);

        // Remove formatting for check
        const cleanAsgari = asgariRes.replace(/[^0-9]/g, '');
        // 25.000 TL (Net) -> 25000
        if(!cleanAsgari.includes('25000')) throw new Error("Asgari unexpected result: " + asgariRes);
        console.log("PASS: Asgari");

        // Test KDV
        setInput('kdv-amt', '1000');
        setInput('kdv-rate', '20');
        setSelect('kdv-type', 'exclude');
        calc_kdv();
        const kdvTotal = document.getElementById('kdv-res-total').innerText;
        console.log("KDV Total: " + kdvTotal);
        if(!kdvTotal.includes('1.200')) throw new Error("KDV unexpected result");
        console.log("PASS: KDV");

    } catch(e) {
        console.error("VERIFICATION FAILED: " + e.message);
        // We cannot call process.exit(1) here easily if we want to bubble up, but we can throw
        throw e;
    }

    console.log("--- All Tests Passed ---");
`;

try {
    const script = new vm.Script(calculatorCode + "\n" + testCode);
    const context = vm.createContext(window);
    script.runInContext(context);
} catch (e) {
    console.error("Script Execution Failed:", e);
    process.exit(1);
}
