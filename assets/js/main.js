function renderRecentBlog() {
    const container = document.getElementById('recent-blog-list');
    if(!container || typeof blogPosts === 'undefined') return;

    const recent = [...blogPosts].reverse().slice(0, 3);
    container.innerHTML = "";
    recent.forEach(post => {
        const a = document.createElement('a');
        a.href = `blog/${post.slug}.html`;
        a.className = "block group mb-3 last:mb-0";
        a.innerHTML = `
          <div class="flex items-start gap-3">
            <div class="shrink-0 w-6 text-center mt-1"><i class="fa-solid ${post.icon || 'fa-file-lines'} text-blue-300 group-hover:text-blue-500 transition"></i></div>
            <div>
              <p class="text-sm text-slate-700 font-bold group-hover:text-blue-600 transition leading-snug">${post.title}</p>
            </div>
          </div>
        `;
        container.appendChild(a);
    });
}

function toggleDrawer() {
    const d = document.getElementById('drawer');
    const m = document.getElementById('drawer-mask');
    if (!d || !m) return;

    const isOpen = d.classList.contains('drawer-open');
    d.classList.toggle('drawer-open', !isOpen);
    d.classList.toggle('drawer-closed', isOpen);
    m.classList.toggle('mask-visible', !isOpen);
    m.classList.toggle('mask-hidden', isOpen);
}

function filterDrawerTools() {
    const q = document.getElementById('mobile-tool-search').value.toLowerCase();
    const drawerList = document.getElementById('drawer-list');
    if (!drawerList) return;
    const items = drawerList.querySelectorAll('a');
    items.forEach(item => {
        const txt = item.innerText.toLowerCase();
        item.style.display = txt.includes(q) ? 'flex' : 'none';
    });
}

document.addEventListener('DOMContentLoaded', () => {
    if (typeof tools !== 'undefined') {
        renderCalculatorGrid(tools, 'tool-container');
        renderSidebar(tools, 'sidebar-list', 'popular-tools-list');
        renderSidebar(tools, 'drawer-list', null, true);
        setupSearch('desktop-tool-search', 'desktop-search-suggestions', tools);
        
        const mobileSearch = document.getElementById('mobile-tool-search');
        if(mobileSearch) {
            mobileSearch.addEventListener('input', filterDrawerTools);
        }
    }
    
    if (typeof blogPosts !== 'undefined') {
        renderRecentBlog();
    }
});