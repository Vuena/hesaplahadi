from playwright.sync_api import sync_playwright

def verify_mobile_blog_button():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(
            viewport={"width": 375, "height": 667},
            user_agent="Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 Mobile/15E148 Safari/604.1"
        )

        # Check Tool Page (which we just regenerated)
        print("Navigating to AI Diyetisyen...")
        page.goto(f"file://{os.getcwd()}/ai-diyetisyen.html")
        page.wait_for_selector("header")

        # Verify Mobile Blog Button - Fixed Selector
        # Using a more robust selector or just checking text
        # .md:hidden needs to be escaped or just check class content
        # CSS selector with colons needs escaping, or use text

        # We look for the link with the text "Blog" inside the header
        blog_btn = page.query_selector('header a[href="blog/index.html"] span:text("Blog")')

        # Check if it is visible
        if blog_btn:
             # Check if the parent anchor has the class md:hidden
             parent = blog_btn.evaluate("el => el.parentElement.classList.contains('md:hidden')")
             if parent:
                 print("SUCCESS: Mobile Blog Button found and has correct class.")
                 page.screenshot(path="verification/mobile_tool_page.png")
             else:
                 print("WARNING: Blog button found but might not be mobile-only?")
        else:
            print("FAILURE: Mobile Blog Button NOT found.")

        browser.close()

import os
if not os.path.exists("verification"):
    os.makedirs("verification")
verify_mobile_blog_button()
