
const dolarContent = `
<script>
    function setDolarMode(m) {
      document.getElementById('dolar-mode').value = m;
      document.querySelectorAll('.dolar-calc-field').forEach(el => el.style.display = m === 'calc' ? 'block' : 'none');
      document.querySelectorAll('.dolar-conv-field').forEach(el => {
        el.classList.remove('hidden');
        el.style.display = m === 'conv' ? 'block' : 'none';
      });

      // Buttons
      const btnCalc = document.getElementById('btn-mode-calc');
      const btnConv = document.getElementById('btn-mode-conv');

      if(m==='calc') {
        btnCalc.className = "flex-1 py-2 rounded-lg text-sm font-bold bg-white shadow-sm text-slate-800 transition";
        btnConv.className = "flex-1 py-2 rounded-lg text-sm font-bold text-slate-500 hover:text-slate-700 transition";
      } else {
        btnConv.className = "flex-1 py-2 rounded-lg text-sm font-bold bg-white shadow-sm text-slate-800 transition";
        btnCalc.className = "flex-1 py-2 rounded-lg text-sm font-bold text-slate-500 hover:text-slate-700 transition";
      }
    }
function calc_dolar() { const m=document.getElementById('dolar-mode').value; const a=parseFloat(document.getElementById('dolar-amt').value)||0; if(m==='conv'){showRes('dolar',(a*parseFloat(document.getElementById('dolar-rate').value)||0).toLocaleString('tr-TR',{maximumFractionDigits:2})+' TL','');}else{const b=parseFloat(document.getElementById('dolar-buy').value)||0,s=parseFloat(document.getElementById('dolar-sell').value)||0,c=a*b,r=a*s,p=r-c;const cl=p>=0?'text-green-600':'text-red-600';showRes('dolar',`<span class="${cl}">${p.toLocaleString('tr-TR',{maximumFractionDigits:2})} TL</span>`,`ROI: %${((p/c)*100).toFixed(2)}`);}}
  </script>
`;

const a = document.createElement('div');
a.innerHTML = dolarContent;
document.body.appendChild(a);
