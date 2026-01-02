from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("http://localhost:8080/asgari-ucret-hesaplama.html")

        # Inject custom JS to check if function exists
        exists = page.evaluate("typeof calc_asgari === 'function'")
        print(f"Function exists: {exists}")

        # Try running it manually
        page.evaluate("calc_asgari()")

        # Check result
        val = page.locator("#val-asgari").inner_text()
        print(f"Result after manual call: '{val}'")

        browser.close()

if __name__ == "__main__":
    run()
