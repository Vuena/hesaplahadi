from playwright.sync_api import sync_playwright
import os

def verify_ai_redirect():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # 1. Test AI Redirect
        query = "Istanbul nufusu"
        url = f"file://{os.getcwd()}/ai-asistan.html?q={query}"
        print(f"Navigating to: {url}")

        page.goto(url)

        # Wait for input to be populated
        page.wait_for_selector("input#ai_asistan-q")

        input_val = page.input_value("input#ai_asistan-q")
        if input_val == query:
             print(f"SUCCESS: Input field populated with '{query}'")
        else:
             print(f"FAILURE: Input field is '{input_val}', expected '{query}'")

        # Wait for "Thinking" or Result
        # It takes a bit for calc_ai_asistan to fire and show spinner or result
        try:
            page.wait_for_selector("#res-ai_asistan", state="visible", timeout=3000)
            print("SUCCESS: Result area is visible (Calculation triggered)")
        except:
             # It might be the spinner inside the result area?
             # Or maybe it failed to trigger?
             print("WARNING: Result area did not become visible within timeout.")

        page.screenshot(path="verification/ai_redirect.png")

        # 2. Verify Crypto Blog is Gone
        crypto_path = f"file://{os.getcwd()}/blog/kripto-para-vergilendirme.html"
        print(f"Checking Crypto Page: {crypto_path}")

        try:
            # File protocol throws error on missing file usually?
            # Or playwright just shows empty/error page.
            if not os.path.exists("blog/kripto-para-vergilendirme.html"):
                 print("SUCCESS: Crypto file does not exist on disk.")
            else:
                 print("FAILURE: Crypto file STILL exists on disk!")

        except Exception as e:
            print(f"Exception checking file: {e}")

        browser.close()

if not os.path.exists("verification"):
    os.makedirs("verification")
verify_ai_redirect()
