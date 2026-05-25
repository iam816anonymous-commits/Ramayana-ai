import asyncio
from playwright.async_api import async_playwright

async def verify():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={'width': 1280, 'height': 800})
        await page.goto('http://localhost:3000')
        await page.fill('input', 'Explain the significance of Hanuman')
        await page.press('input', 'Enter')
        await page.wait_for_selector('h3:has-text("Reflection")', timeout=15000)
        await asyncio.sleep(3) # Wait for animations
        await page.screenshot(path='/home/jules/verification/final_sanctum_verify.png')
        await browser.close()

if __name__ == "__main__":
    asyncio.run(verify())
