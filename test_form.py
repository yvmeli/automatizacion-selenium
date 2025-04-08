from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time
import pytest

URL = "file:///G:/ITLA%20TAREAS/PROGRAMACI%C3%93N_3/auto/form.html"

SCREENSHOT_DIR = "screenshots/exitosos"
if not os.path.exists(SCREENSHOT_DIR):
    os.makedirs(SCREENSHOT_DIR)

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.get(URL)
    yield driver
    driver.quit()

def take_screenshot(browser, name):
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    filename = f"{SCREENSHOT_DIR}/{name}_{timestamp}.png"
    browser.save_screenshot(filename)
    return filename

def test_form_submission(browser):
    try:
        take_screenshot(browser, "1_formulario_inicio")
        browser.find_element(By.NAME, "nombre").send_keys("Yameli")
        browser.find_element(By.NAME, "apellido").send_keys("Martínez")
        browser.find_element(By.NAME, "email").send_keys("yameli@example.com")
        browser.find_element(By.NAME, "telefono").send_keys("8291234567")

        take_screenshot(browser, "2_formulario_completo")
        browser.find_element(By.TAG_NAME, "form").submit()
        time.sleep(1)

        mensaje_div = browser.find_element(By.ID, "mensaje")
        assert "Formulario enviado correctamente" in mensaje_div.text

        take_screenshot(browser, "3_test_exitoso_formulario_enviado")
        with open(f"{SCREENSHOT_DIR}/test_form_submission_EXITOSO.txt", "w") as f:
            f.write(f"Test exitoso - {time.strftime('%Y-%m-%d %H:%M:%S')}")

    except Exception as e:
        take_screenshot(browser, "form_submission_ERROR")
        print(f"Test falló: {str(e)}")
        raise

def test_empty_fields_validation(browser):
    try:
        browser.find_element(By.NAME, "nombre").clear()
        browser.find_element(By.NAME, "apellido").send_keys("Martínez")
        browser.find_element(By.NAME, "email").send_keys("yameli@example.com")
        browser.find_element(By.NAME, "telefono").send_keys("8291234567")

        browser.find_element(By.TAG_NAME, "form").submit()
        time.sleep(1)

        mensaje_div = browser.find_element(By.ID, "mensaje")
        assert "Por favor, complete todos los campos" in mensaje_div.text

        take_screenshot(browser, "1_test_exitoso_campos_vacios")
        with open(f"{SCREENSHOT_DIR}/test_empty_fields_validation_EXITOSO.txt", "w") as f:
            f.write(f"Test exitoso - {time.strftime('%Y-%m-%d %H:%M:%S')}")

    except Exception as e:
        take_screenshot(browser, "empty_fields_ERROR")
        print(f"Test falló: {str(e)}")
        raise

def test_invalid_email(browser):
    try:
        browser.find_element(By.NAME, "nombre").send_keys("Yameli")
        browser.find_element(By.NAME, "apellido").send_keys("Martínez")
        browser.find_element(By.NAME, "email").send_keys("email_invalido.com")
        browser.find_element(By.NAME, "telefono").send_keys("8291234567")

        browser.find_element(By.TAG_NAME, "form").submit()
        time.sleep(1)

        mensaje_div = browser.find_element(By.ID, "mensaje")
        assert "Correo electrónico inválido" in mensaje_div.text

        take_screenshot(browser, "1_test_exitoso_email_invalido")
        with open(f"{SCREENSHOT_DIR}/test_invalid_email_EXITOSO.txt", "w") as f:
            f.write(f"Test exitoso - {time.strftime('%Y-%m-%d %H:%M:%S')}")

    except Exception as e:
        take_screenshot(browser, "invalid_email_ERROR")
        print(f"Test falló: {str(e)}")
        raise