from playwright.sync_api import sync_playwright

def verify_enflasyon_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Load the local file
        page.goto("file:///home/jules/repo/enflasyon-alim-gucu-hesaplama.html")

        # Check if blog list container is present
        # The id is 'recent-blog-list'

        # Wait for JS to render (renderRecentBlog)
        # We can wait for the presence of an anchor tag inside the list, which indicates it's populated
        try:
            # We expect 3 items
            page.wait_for_selector("#recent-blog-list a", timeout=5000)

            # Take screenshot
            page.screenshot(path="/home/jules/verification/enflasyon_blog_preview.png")
            print("Screenshot taken: /home/jules/verification/enflasyon_blog_preview.png")

            # Verify we have content
            content = page.inner_html("#recent-blog-list")
            if "blog/" in content and "text-slate-700" in content:
                print("Verification SUCCESS: Blog list populated.")
            else:
                print("Verification FAILURE: Blog list empty or incorrect.")

        except Exception as e:
            print(f"Verification ERROR: {e}")
            page.screenshot(path="/home/jules/verification/enflasyon_error.png")

        browser.close()

if __name__ == "__main__":
    import os
    if not os.path.exists("/home/jules/verification"):
        os.makedirs("/home/jules/verification")
    verify_enflasyon_page()
