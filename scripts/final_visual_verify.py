import asyncio
from playwright.async_api import async_playwright

async def verify():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.set_viewport_size({"width": 1920, "height": 1080})

        print("Opening Sanctum...")
        await page.goto("http://localhost:3000", wait_until="networkidle")

        # Take landing screenshot
        await page.screenshot(path="verification/temple_landing_final.png")
        print("Landing saved.")

        # Check for placeholder via accessibility or role if text matching fails
        print("Finding input...")
        input_field = page.locator('input')
        await input_field.first.fill("What is the essence of devotion?")
        await input_field.first.press("Enter")

        print("Waiting for Revelation...")
        try:
            # Wait for any text containing "Eternal" or the manuscript card
            await page.wait_for_selector('h3', timeout=25000)
            await asyncio.sleep(5) # Let it finish typing/animating
            await page.screenshot(path="verification/temple_revelation_final.png")
            print("Revelation saved.")
        except Exception as e:
            print(f"Revelation timeout: {e}")
            await page.screenshot(path="verification/error_final.png")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(verify())
