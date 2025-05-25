import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright, inn) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://egrul.nalog.ru/index.html")
    page.get_by_role("link", name="Искать по точному соответствию наименования юридического лица или фамилии, имени").click()
    page.locator("#uni_set_1").get_by_role("link").click()
    page.get_by_text("</div></div></div></div>").content_frame.get_by_role("button", name="Выбрать все").click()
    page.get_by_text("</div></div></div></div>").content_frame.get_by_role("button", name="OK").click()
    page.get_by_role("textbox", name="Поисковый запрос:*").click()
    page.get_by_role("textbox", name="Поисковый запрос:*").fill("https://egrul.nalog.ru/index.html")
    page.get_by_role("textbox", name="Поисковый запрос:*").press("Tab")
    page.get_by_role("link", name="Искать по точному соответствию наименования юридического лица или фамилии, имени").press("Tab")
    page.get_by_role("textbox", name="Поисковый запрос:*").click()
    page.get_by_role("textbox", name="Поисковый запрос:*").fill(f'{inn}')
    page.get_by_role("button", name="Найти ").click()
    with page.expect_download() as download_info:
        page.get_by_role("button", name="Получить выписку").click()
    download = download_info.value

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright, "3000015570")
