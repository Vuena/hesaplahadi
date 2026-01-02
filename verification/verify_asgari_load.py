from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        # Force a hard reload logic or timestamp to bypass any weird cache
        page.goto("http://localhost:8080/asgari-ucret-hesaplama.html?t=1")

        # Check if calculator.js is loaded
        # Look for console errors
        page.on("console", lambda msg: print(f"Console: {msg.text}"))
        page.on("pageerror", lambda err: print(f"Page Error: {err}"))

        page.wait_for_timeout(2000)

        exists = page.evaluate("typeof calc_asgari")
        print(f"Function type: {exists}")

        browser.close()

if __name__ == "__main__":
    run()
