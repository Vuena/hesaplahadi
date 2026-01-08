
// API Key Obfuscation
const _k = "QUl6YVN5Qzh6SGxSTkZvck1peW5tM01qUnFNc3RvWjRNczBwQVdR";
const apiKey = atob(_k);

// --- CONFIGURATION (Paths are absolute from the root)
const tools = [
    { id: 'ai_asistan', cat: 'Yapay Zeka', name: 'AI Hesaplama Asistanı', link: '/ai-asistan.html', color:'indigo' },
    { id: 'ai_diyet', cat: 'Yapay Zeka', name: 'AI Diyetisyen', link: '/ai-diyetisyen.html', color:'indigo' },
    { id: 'token', cat: 'Yapay Zeka', name: 'AI Token Maliyet Hesaplama', link: '/yapay-zeka-token-maliyet-hesaplama.html', color:'indigo' },
    { id: 'enflasyon', cat: 'Finans', name: 'Enflasyon ve Alım Gücü', link: '/enflasyon-alim-gucu-hesaplama.html', color:'blue' },
    { id: 'freelancer', cat: 'Finans', name: 'Freelancer Gelir Vergisi', link: '/freelancer-gelir-vergisi-hesaplama.html', color:'blue' },
    { id: 'dolar', cat: 'Finans', name: 'Dolar Kar/Zarar Hesaplama', link: '/dolar-hesaplama.html', color:'blue' },
    { id: 'kdv', cat: 'Finans', name: 'KDV Hesaplama', link: '/kdv-hesaplama.html', color:'blue' },
    { id: 'tevkifat', cat: 'Finans', name: 'KDV Tevkifat Hesaplama', link: '/tevkifat-hesaplama.html', color:'blue' },
    { id: 'kidem', cat: 'Finans', name: 'Kıdem Tazminatı Hesaplama', link: '/kidem-tazminati-hesaplama.html', color:'blue' },
    { id: 'kredi', cat: 'Finans', name: 'Kredi Hesaplama', link: '/kredi-hesaplama.html', color:'blue' },
    { id: 'net_brut', cat: 'Finans', name: 'Netten Brüte Maaş', link: '/netten-brute-maas-hesaplama.html', color:'blue' },
    { id: 'brut_net', cat: 'Finans', name: 'Brütten Nete Maaş', link: '/brutten-nete-maas-hesaplama.html', color:'blue' },
    { id: 'mevduat', cat: 'Finans', name: 'Mevduat Getirisi Hesaplama', link: '/mevduat-faizi-hesaplama.html', color:'blue' },
    { id: 'iban', cat: 'Finans', name: 'IBAN Doğrulama Aracı', link: '/iban-dogrulama-ve-cozumleme-araci.html', color:'blue' }
];

// --- CORE FUNCTIONS ---

function renderSidebar() {
    const cats = [...new Set(tools.map(t => t.cat))];
    const currentPath = window.location.pathname;
    const containers = ['sidebar-list', 'drawer-list'];

    containers.forEach(id => {
        const container = document.getElementById(id);
        if(!container) return;
        if(container.querySelector('.cat-header')) return; // Already rendered
        container.innerHTML = ''; 

        cats.forEach(cat => {
            const header = document.createElement('div');
            header.className = 'cat-header'; header.innerText = cat;
            container.appendChild(header);

            tools.filter(t => t.cat === cat).forEach(t => {
                const a = document.createElement('a');
                a.href = t.link; // Path is now absolute
                a.className = 'w-full text-left px-4 py-3 rounded-xl text-xs font-medium transition flex items-center nav-item gap-3 mb-1 text-slate-500 hover:bg-slate-50 hover:text-blue-600 block';
                if(currentPath === t.link) {
                    a.classList.add('nav-active', 'bg-blue-50', 'text-blue-600');
                }
                let icon = '<i class="fa-solid fa-calculator text-slate-400 w-4 text-center"></i>';
                if(t.cat === 'Yapay Zeka') icon = '<i class="fa-solid fa-wand-magic-sparkles text-indigo-500 w-4 text-center"></i>';
                a.innerHTML = `${icon} ${t.name}`;
                container.appendChild(a);
            });
        });
    });
}

function getIconForCategory(category) {
    const iconMap = {
        'Finans': 'fa-coins', 'Vergi': 'fa-receipt', 'Pratik Bilgiler': 'fa-lightbulb',
        'Sağlık': 'fa-heart-pulse', 'Teknoloji': 'fa-robot', 'Yatırım': 'fa-chart-line',
        'Eğitim': 'fa-graduation-cap', 'Astroloji': 'fa-star'
    };
    return iconMap[category] || 'fa-file-alt';
}

function displayPosts(filter = '') {
    const grid = document.getElementById('blog-grid');
    const noResults = document.getElementById('no-results');
    const featuredContainer = document.getElementById('featured-post');
    if (!grid) return;
    if (typeof blogPosts === 'undefined' || blogPosts.length === 0) {
        console.error("Blog data (blogPosts) is not loaded or is empty.");
        if(featuredContainer) featuredContainer.style.display = 'none';
        grid.style.display = 'none';
        if(noResults) noResults.classList.remove('hidden');
        return;
    }

    grid.innerHTML = '';
    if (featuredContainer) featuredContainer.innerHTML = '';

    const lowerCaseFilter = filter.toLowerCase().trim();
    let posts = [...blogPosts];
    let filteredPosts = posts.filter(post => 
        post.title.toLowerCase().includes(lowerCaseFilter) || 
        post.summary.toLowerCase().includes(lowerCaseFilter) ||
        post.category.toLowerCase().includes(lowerCaseFilter)
    );

    if (filteredPosts.length === 0) {
        if(noResults) noResults.classList.remove('hidden');
        if(featuredContainer) featuredContainer.style.display = 'none';
        grid.style.display = 'none';
        return;
    }

    if(noResults) noResults.classList.add('hidden');
    if(featuredContainer) featuredContainer.style.display = 'block';
    grid.style.display = 'grid';

    if (lowerCaseFilter === '' && filteredPosts.length > 0 && featuredContainer) {
        const featured = filteredPosts.shift();
        const featuredCard = `
            <a href="${featured.slug}" class="block bg-white rounded-2xl shadow-lg hover:shadow-xl transition-shadow duration-300 overflow-hidden group border border-slate-100">
                <div class="md:flex">
                    <div class="md:w-1/2 bg-slate-100 flex items-center justify-center text-slate-300 p-8 min-h-[250px]">
                         <i class="fa-solid ${getIconForCategory(featured.category)} text-8xl ${featured.category === 'Teknoloji' ? 'text-indigo-400' : 'text-blue-400'}"></i>
                    </div>
                    <div class="md:w-1/2 p-6 md:p-8 flex flex-col justify-center">
                        <span class="text-xs font-bold ${featured.category === 'Teknoloji' ? 'text-indigo-600' : 'text-blue-600'} uppercase tracking-wider">${featured.category}</span>
                        <h2 class="text-2xl font-extrabold text-slate-900 mt-2 mb-3 group-hover:text-blue-600 transition-colors">${featured.title}</h2>
                        <p class="text-slate-500 text-sm leading-relaxed">${featured.summary}</p>
                        <div class="mt-4 text-xs font-bold text-blue-600">Devamını Oku &rarr;</div>
                    </div>
                </div>
            </a>`;
        featuredContainer.innerHTML = featuredCard;
    } else if (featuredContainer) {
        featuredContainer.style.display = 'none';
    }

    filteredPosts.forEach(post => {
        const card = `
           <a href="${post.slug}" class="flex flex-col bg-white rounded-2xl shadow-md hover:shadow-lg transition-shadow duration-300 overflow-hidden group border border-slate-100">
                <div class="h-40 bg-slate-100 flex items-center justify-center text-slate-300">
                     <i class="fa-solid ${getIconForCategory(post.category)} text-5xl"></i>
                </div>
                <div class="p-5 flex flex-col flex-grow">
                    <span class="text-xs font-bold ${post.category === 'Teknoloji' ? 'text-indigo-600' : 'text-blue-600'} uppercase tracking-wider">${post.category}</span>
                    <h3 class="text-lg font-bold text-slate-800 mt-2 mb-2 group-hover:text-blue-600 transition-colors flex-grow">${post.title}</h3>
                    <p class="text-xs text-slate-500 h-12 overflow-hidden">${post.summary}</p>
                </div>
            </a>`;
        grid.innerHTML += card;
    });
}

function setupSearch() {
    const inputEl = document.getElementById('desktop-tool-search');
    const suggestionsEl = document.getElementById('desktop-search-suggestions');
    if (!inputEl || !suggestionsEl) return;

    // ... (rest of the search function remains the same) ...

}

function setupBlogSearch() {
    const searchInput = document.getElementById('search-input');
    if(searchInput) {
        searchInput.addEventListener('input', (e) => {
            displayPosts(e.target.value);
        });
    }
}

function setupMobileMenu() {
    const hamburger = document.querySelector('[data-js-hamburger]');
    if (!hamburger) {
        // Create a hamburger if it doesn't exist for some reason
        const headerActions = document.querySelector('.flex.items-center.gap-3');
        if(headerActions) {
             const mobileButton = document.createElement('button');
             mobileButton.className = 'md:hidden flex items-center justify-center w-8 h-8 rounded-full bg-slate-100 text-slate-600 border border-slate-200 hover:bg-slate-200 transition';
             mobileButton.setAttribute('data-js-hamburger','');
             mobileButton.innerHTML = '<i class="fa-solid fa-bars"></i>';
             headerActions.appendChild(mobileButton);
        }
    }

    const drawerHTML = `
    <div id="drawer-mask" class="fixed inset-0 bg-black/50 z-40 transition-opacity duration-300 opacity-0 pointer-events-none" onclick="toggleDrawer()"></div>
    <aside id="drawer" class="fixed top-0 left-0 w-72 h-full bg-white z-50 shadow-xl transition-transform duration-300 -translate-x-full overflow-y-auto">
        <div class="p-4 border-b border-slate-100 flex justify-between items-center">
             <span class="font-bold text-slate-800">Tüm Araçlar</span>
             <button onclick="toggleDrawer()" class="text-slate-400 hover:text-slate-600"><i class="fa-solid fa-times text-xl"></i></button>
        </div>
        <div id="drawer-list" class="p-3"></div>
    </aside>`;
    if(!document.getElementById('drawer')) {
        document.body.insertAdjacentHTML('afterbegin', drawerHTML);
    }
    document.querySelector('[data-js-hamburger]').addEventListener('click', toggleDrawer);
}

function toggleDrawer() {
    const drawer = document.getElementById('drawer');
    const mask = document.getElementById('drawer-mask');
    if (!drawer || !mask) return;
    drawer.classList.toggle('-translate-x-full');
    mask.classList.toggle('opacity-0');
    mask.classList.toggle('pointer-events-none');
}

// --- INITIALIZATION ---
document.addEventListener('DOMContentLoaded', () => {
    if (document.getElementById('sidebar-list') || document.getElementById('drawer-list')) {
        renderSidebar();
    }
    if (document.getElementById('blog-grid')) {
        displayPosts();
        setupBlogSearch();
    }
    
    setupSearch();
    // Check if mobile menu elements exist before setting it up
    if (window.innerWidth < 768) { 
      setupMobileMenu();
    }
});
