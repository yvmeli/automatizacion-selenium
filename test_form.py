from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time
import pytest

URL = "file:///G:/ITLA%20TAREAS/PROGRAMACI%C3%93N_3/auto/form.html"

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.get(URL)
    yield driver
    driver.quit()

def test_form_submission(browser):
    browser.find_element(By.NAME, "nombre").send_keys("Yameli")
    browser.find_element(By.NAME, "apellido").send_keys("Martínez")
    browser.find_element(By.NAME, "email").send_keys("yameli@example.com")
    browser.find_element(By.NAME, "telefono").send_keys("8291234567")
    browser.find_element(By.TAG_NAME, "form").submit()
    time.sleep(1)

    alert = Alert(browser)
    assert "Formulario enviado correctamente" in alert.text
    alert.accept()

def test_empty_fields_validation(browser):
    browser.find_element(By.NAME, "nombre").send_keys("")
    browser.find_element(By.NAME, "apellido").send_keys("Martínez")
    browser.find_element(By.NAME, "email").send_keys("yameli@example.com")
    browser.find_element(By.NAME, "telefono").send_keys("8291234567")
    browser.find_element(By.TAG_NAME, "form").submit()
    time.sleep(1)

    alert = Alert(browser)
    assert "Por favor, complete todos los campos" in alert.text
    alert.accept()

def test_invalid_email(browser):
    browser.find_element(By.NAME, "nombre").send_keys("Yameli")
    browser.find_element(By.NAME, "apellido").send_keys("Martínez")
    browser.find_element(By.NAME, "email").send_keys("email_invalido.com")
    browser.find_element(By.NAME, "telefono").send_keys("8291234567")
    browser.find_element(By.TAG_NAME, "form").submit()
    time.sleep(1)

    alert = Alert(browser)
    assert "Correo electrónico inválido" in alert.text
    alert.accept()