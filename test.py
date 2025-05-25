import pytest
from playwright.sync_api import sync_playwright
import time

@pytest.fixture()
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture()
def page(browser):
    page = browser.new_page()
    yield page
    page.close()


def test_visible(page):
    #Проверка доступности поля ввода ИНН
    page.goto("https://zachestnyibiznes.ru/")
    inn_input = page.get_by_role("searchbox", name="Submit")
    page.screenshot(path=".\\Artefact\\step1.png")
    assert inn_input.is_visible()

def test_validation_positive(page):
    #Проверка доступности поля ввода ИНН
    page.goto("https://zachestnyibiznes.ru/")
    inn_input = page.get_by_role("searchbox", name="Submit")
    inn_input.click()
    inn_input.fill("771706315618")
    time.sleep(2)
    page.screenshot(path=".\\Artefact\\step2.png")
    assert page.get_by_role("option", name="Пашовкина Алевтина Сергеевна ИНН").is_visible(timeout=60000)

def test_validation_negative_1(page):
    #Проверка доступности поля ввода ИНН
    page.goto("https://zachestnyibiznes.ru/")
    inn_input = page.get_by_role("searchbox", name="Submit")
    inn_input.click()
    inn_input.fill("     ")
    time.sleep(2)
    page.screenshot(path=".\\Artefact\\step3.png")
    assert page.get_by_role("option", name="     ").is_visible(timeout=60000) is False

def test_validation_negative_2(page):
    #Проверка доступности поля ввода ИНН
    page.goto("https://zachestnyibiznes.ru/")
    inn_input = page.get_by_role("searchbox", name="Submit")
    inn_input.click()
    inn_input.fill("%*?")
    time.sleep(2)
    page.screenshot(path=".\\Artefact\\step4.png")
    assert page.get_by_role("option", name="%*?").is_visible(timeout=60000) is False

def test_validation_negative_3(page):
    #Проверка доступности поля ввода ИНН
    page.goto("https://zachestnyibiznes.ru/")
    inn_input = page.get_by_role("searchbox", name="Submit")
    inn_input.click()
    inn_input.fill("A")
    time.sleep(2)
    page.screenshot(path=".\\Artefact\\step5.png")
    assert page.get_by_role("option", name="A").is_visible(timeout=60000) is False

def test_validation_negative_4(page):
    #Проверка доступности поля ввода ИНН
    page.goto("https://zachestnyibiznes.ru/")
    inn_input = page.get_by_role("searchbox", name="Submit")
    inn_input.click()
    inn_input.fill("AFDdsxasc.,l''a ecvwvdsddddddddacWSDCWECVQW.RVL,AFDdsxasc.,l''a ecvwvdsddddddddacWSDCWECVQW.RVL"
                   ",AFDdsxasc.,l''a ecvwvdsddddddddacWSDCWECVQW.RVL,AFDdsxasc.,l''a ecvwvdsddddddddacWSDCWECVQW.RVL"
                   ",AFDdsxasc.,l''a ecvwvdsddddddddacWSDCWECVQW.RVL,AFDdsxasc.,l''a ecvwvdsddddddddacWSDCWECVQW.RVL"
                   ",AFDdsxasc.,l''a ecvwvdsddddddddacWSDCWECVQW.RVL,AFDdsxasc.,l''a ecvwvdsddddddddacWSDCWECVQW.RVL"
                   ",AFDdsxasc.,l''a ecvwvdsddddddddacWSDCWECVQW.RVL,AFDdsxasc.,l''a ecvwvdsddddddddacWSDCWECVQW.RVL"
                   ",AFDdsxasc.,l''a ecvwvdsddddddddaf")
    time.sleep(2)
    page.screenshot(path=".\\Artefact\\step5.png")
    assert page.get_by_role("option", name="AFDdsxasc.,l''a ecvwvdsddddddddacWSDCWECVQW.RVL,AFDdsxasc.,l''a ecvwv"
                                           "dsddddddddacWSDCWECVQW.RVL,AFDdsxasc.,l''a ecvwvdsddddddddacWSDCWECVQW.RVL"
                                           ",AFDdsxasc.,l''a ecvwvdsddddddddacWSDCWECVQW.RVL,AFDdsxasc.,l''a ecvwvdsdd"
                                           "ddddddacWSDCWECVQW.RVL,AFDdsxasc.,l''a ecvwvdsddddddddacWSDCWECVQW.RVL,AFD"
                                           "dsxasc.,l''a ecvwvdsddddddddacWSDCWECVQW.RVL,AFDdsxasc.,l''a ecvwvdsdddddd"
                                           "ddacWSDCWECVQW.RVL,AFDdsxasc.,l''a ecvwvdsddddddddacWSDCWECVQW.RVL,AFDdsxa"
                                           "sc.,l''a ecvwvdsddddddddacWSDCWECVQW.RVL,AFDdsxasc.,l''a ecvwvdsddddddd"
                                           "daf").is_visible(timeout=60000) is False

def test_validation_negative_5(page):
    #Проверка доступности поля ввода ИНН
    page.goto("https://zachestnyibiznes.ru/")
    inn_input = page.get_by_role("searchbox", name="Submit")
    inn_input.click()
    inn_input.fill("Мост")
    time.sleep(2)
    page.screenshot(path=".\\Artefact\\step6.png")
    assert page.get_by_role(
        "link", name="ООО \"МОСТ\" Руководители: Мостаков Алексей Евгеньевич Учредители: Мостаков Алексе"
    ).is_visible(timeout=60000)