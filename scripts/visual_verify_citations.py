import asyncio
from playwright.async_api import async_playwright

async def verify():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.set_viewport_size({"width": 1280, "height": 1080})

        print("Opening Sanctum...")
        # Assuming frontend is running on 3000
        await page.goto("http://localhost:3000", wait_until="networkidle")

        print("Finding input...")
        input_field = page.locator('input')
        await input_field.first.fill("Why did Rama accept exile?")
        await input_field.first.press("Enter")

        print("Waiting for Revelation...")
        try:
            # Increased timeout and wait for Source Chips
            await page.wait_for_selector('div.bg-sacred-gold\/5', timeout=30000)
            await asyncio.sleep(2)
            await page.screenshot(path="verification/citations_verify.png")
            print("Citations verified and screenshot saved.")
        except Exception as e:
            print(f"Verification timeout or error: {e}")
            await page.screenshot(path="verification/error_citations.png")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(verify())
