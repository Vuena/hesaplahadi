
from playwright.sync_api import sync_playwright

def verify_mobile_header():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        # Use iPhone 13 Pro viewport for mobile simulation
        context = browser.new_context(viewport={"width": 390, "height": 844})
        page = context.new_page()

        # Load index.html
        # Since I'm in a container, I'll use file:// protocol.
        # I need absolute path. Assuming /app is repo root.
        import os
        cwd = os.getcwd()
        page.goto(f"file://{cwd}/index.html")

        # 1. Verify AI Placeholder
        ai_input = page.locator('input[name="q"]')
        placeholder = ai_input.get_attribute("placeholder")
        print(f"AI Input Placeholder: {placeholder}")
        assert placeholder == "Ne hesaplayalım?"

        # 2. Verify Mobile Burger Button in Header (Top Left)
        # The simple one
        header_burger = page.locator('header button.md\\:hidden').first
        print(f"Header Burger visible: {header_burger.is_visible()}")

        # 3. Verify New Button below Search
        # Button text "Tüm Hesaplama Araçları"
        new_btn = page.locator('button:has-text("Tüm Hesaplama Araçları")')
        print(f"New 'Tüm Hesaplama Araçları' button visible: {new_btn.is_visible()}")

        # 4. Verify Search Suggestions
        search_input = page.locator('#mobile-tool-search')
        suggestions = page.locator('#search-suggestions')

        print(f"Suggestions visible initially: {suggestions.is_visible()}") # Should be False

        # Click/Focus search
        search_input.click()
        # Wait a bit
        page.wait_for_timeout(500)
        print(f"Suggestions visible after focus: {suggestions.is_visible()}") # Should be True

        # Take Screenshot
        page.screenshot(path="verification/verify_mobile_ux_new.png")
        print("Screenshot saved to verification/verify_mobile_ux_new.png")

        browser.close()

if __name__ == "__main__":
    verify_mobile_header()
