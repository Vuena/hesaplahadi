from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Listen for console logs
        page.on("console", lambda msg: print(f"Console: {msg.text}"))
        page.on("pageerror", lambda err: print(f"Page Error: {err}"))

        page.goto("http://localhost:8080/asgari-ucret-hesaplama.html?v=debug2")

        # Click Calculate
        print("Clicking button...")
        page.locator("button.btn-calc").click()
        page.wait_for_timeout(2000)

        browser.close()

if __name__ == "__main__":
    run()
