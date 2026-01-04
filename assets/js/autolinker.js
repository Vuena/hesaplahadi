
document.addEventListener('DOMContentLoaded', async () => {
    // Only run on pages under the /blog/ path
    if (!window.location.pathname.includes('/blog/')) {
        return;
    }

    try {
        // From a /blog/ page, the path to the project root is one level up (../)
        const response = await fetch('../tools_data.json');
        if (!response.ok) {
            throw new Error(`Failed to fetch tools_data.json: ${response.statusText}`);
        }
        const tools = await response.json();
        const article = document.querySelector('article');
        if (!article) return;

        const keywordMap = new Map();
        tools.forEach(tool => {
            if (!tool.fileName) return;
            // Keywords for matching include the tool's name and its related keywords
            const keywords = [tool.name, ...(tool.related_keywords || [])];
            
            keywords.forEach(kw => {
                // Clean the keyword for better matching
                const kwClean = kw.replace(/Hesaplama|Aracı/gi, "").trim().toLowerCase();
                if (kwClean.length > 3 && !keywordMap.has(kwClean)) {
                    // Map the clean keyword to the tool's data
                    keywordMap.set(kwClean, { 
                        // Use root-relative URLs for robustness
                        url: `/${tool.fileName}`, 
                        title: tool.name 
                    });
                }
            });
        });

        // Sort keywords from longest to shortest to prevent partial matches (e.g., "KDV" vs "KDV Tevkifatı")
        const sortedKeywords = [...keywordMap.keys()].sort((a, b) => b.length - a.length);
        const linkedKeywordsOnPage = new Set();
        
        const textNodes = [];
        // Walk the DOM to find all text nodes within the main article
        const treeWalker = document.createTreeWalker(article, NodeFilter.SHOW_TEXT, null, false);
        let currentNode;
        while (currentNode = treeWalker.nextNode()) {
            // Exclude nodes within tags that should not contain links
            if (!currentNode.parentElement.closest('a, h1, h2, h3, h4, script, style')) {
                textNodes.push(currentNode);
            }
        }
        
        textNodes.forEach(node => {
            let nodeContent = node.textContent;
            let hasBeenReplaced = false;

            for (const keyword of sortedKeywords) {
                if (hasBeenReplaced) break; // Create only one link per text node
                if (linkedKeywordsOnPage.has(keyword)) continue; // Link each keyword only once per page

                const regex = new RegExp(`\b(${keyword.replace(/[-\/\\^$*+?.()|[\]{}]/g, '\\$&')})\b`, 'i');
                
                if (regex.test(nodeContent)) {
                    const tool = keywordMap.get(keyword);
                    // Create a link with styling
                    const newHtml = nodeContent.replace(regex, `<a href="..${tool.url}" title="${tool.title}" class="font-bold text-blue-600 hover:underline">$&</a>`);
                    
                    const newFragment = document.createRange().createContextualFragment(newHtml);
                    node.parentNode.replaceChild(newFragment, node);
                    
                    linkedKeywordsOnPage.add(keyword); // Mark keyword as used for this page
                    hasBeenReplaced = true; // Mark this text node as processed
                }
            }
        });
    } catch (error) {
        console.error('Auto-linking script failed:', error);
    }
});
