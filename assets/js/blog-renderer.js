/*
This is a dedicated renderer for the blog page. 
It is kept separate from the main calculator.js to avoid conflicts.
It assumes `blogPosts` variable is defined in the HTML page itself.
*/

function getIconForCategory(category) {
    const iconMap = {
        'Finans': 'fa-coins',
        'Vergi': 'fa-receipt',
        'Pratik Bilgiler': 'fa-lightbulb',
        'Sağlık': 'fa-heart-pulse',
        'Teknoloji': 'fa-robot',
        'Yatırım': 'fa-chart-line',
        'Eğitim': 'fa-graduation-cap',
        'Astroloji': 'fa-star'
    };
    return iconMap[category] || 'fa-file-alt';
}

function displayPosts(filter = '') {
    const grid = document.getElementById('blog-grid');
    const noResults = document.getElementById('no-results');
    const featuredContainer = document.getElementById('featured-post');

    if (!grid) {
        console.error('Core element #blog-grid not found.');
        return;
    }

    if (typeof blogPosts === 'undefined' || blogPosts.length === 0) {
        console.error('Blog data `blogPosts` is not available.');
        if(featuredContainer) featuredContainer.style.display = 'none';
        if(grid) grid.style.display = 'none';
        if(noResults) noResults.classList.remove('hidden');
        return;
    }

    grid.innerHTML = '';
    if (featuredContainer) featuredContainer.innerHTML = '';

    const lowerCaseFilter = filter.toLowerCase().trim();
    let filteredPosts = blogPosts.filter(post => 
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

function setupBlogSearch() {
    const searchInput = document.getElementById('search-input');
    if(searchInput) {
        searchInput.addEventListener('input', (e) => {
            displayPosts(e.target.value);
        });
    }
}

document.addEventListener('DOMContentLoaded', () => {
    if (document.getElementById('blog-grid')) {
        displayPosts();
        setupBlogSearch();
    }
});
