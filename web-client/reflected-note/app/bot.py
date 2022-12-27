import asyncio
from pyppeteer import launch
from config import FLAG, URL
from requests.utils import quote


async def main(title,mssg):
    browser = await launch(
        handleSIGINT=False,
        handleSIGTERM=False,
        handleSIGHUP=False,
        headless=True,
        executablePath="/usr/bin/chromium-browser",
        args=["--no-sandbox", "--disable-gpu"],
    )
    try:
        page = await browser.newPage()
        admin_cookie = {"url": URL, "name": "flag", "value": FLAG}
        await page.setCookie(admin_cookie)
        await page.goto(
            URL
            +"home"
            + "?title="
            + quote(title)
            + "&"
            + "message="
            + quote(mssg)
        )

    except Exception as e:
        raise e
    finally:
        await browser.close()


def get_or_create_eventloop():
    try:
        return asyncio.get_event_loop()
    except RuntimeError as ex:
        if "There is no current event loop in thread" in str(ex):
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            return asyncio.get_event_loop()

def admin_check(title,mssg):
    get_or_create_eventloop().run_until_complete(main(title,mssg))

if __name__ == "__main__":
    admin_check("","")