
from playwright.sync_api import sync_playwright

def verify_changes():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        # Mobile Context
        context = browser.new_context(
            viewport={'width': 375, 'height': 667},
            user_agent='Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 Mobile/15E148 Safari/604.1'
        )
        page = context.new_page()

        # Load local index.html
        import os
        page.goto(f"file://{os.path.abspath('index.html')}")

        # Verify Mobile Header: Logo should be visible
        # It's an 'a' tag with href="index.html" containing h1
        # Selector: header a[href='index.html']

        # Take Screenshot of Mobile Header
        page.screenshot(path="verification/mobile_header.png")
        print("Mobile header screenshot taken.")

        # Desktop Context
        context_desktop = browser.new_context(viewport={'width': 1280, 'height': 800})
        page_desktop = context_desktop.new_page()
        page_desktop.goto(f"file://{os.path.abspath('index.html')}")

        # Verify Sidebar: #sidebar-list should have flex-col
        sidebar = page_desktop.locator('#sidebar-list')
        classes = sidebar.get_attribute('class')
        print(f"Sidebar classes: {classes}")

        if 'flex-col' in classes:
            print("SUCCESS: Sidebar has flex-col.")
        else:
            print("FAILURE: Sidebar missing flex-col.")

        # Take screenshot of desktop sidebar
        page_desktop.screenshot(path="verification/desktop_sidebar.png")

        browser.close()

if __name__ == "__main__":
    verify_changes()
