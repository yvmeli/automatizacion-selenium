from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
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
    """Toma una captura de pantalla con el nombre especificado"""
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    filename = f"{SCREENSHOT_DIR}/{name}_{timestamp}.png"
    browser.save_screenshot(filename)
    return filename

def test_form_submission(browser):
    """Test para validar el envío exitoso del formulario"""
    try:
        take_screenshot(browser, "1_formulario_inicio")
        
        browser.find_element(By.NAME, "nombre").send_keys("Yameli")
        browser.find_element(By.NAME, "apellido").send_keys("Martínez")
        browser.find_element(By.NAME, "email").send_keys("yameli@example.com")
        browser.find_element(By.NAME, "telefono").send_keys("8291234567")
        
        take_screenshot(browser, "2_formulario_completo")
        
        browser.find_element(By.TAG_NAME, "form").submit()
        time.sleep(1)
        
        alert = Alert(browser)
        alert_text = alert.text
        
        alert.accept()
        time.sleep(0.5)
        
        assert "Formulario enviado correctamente" in alert_text
        
        take_screenshot(browser, "3_test_exitoso_formulario_enviado")
        
        with open(f"{SCREENSHOT_DIR}/test_form_submission_EXITOSO.txt", "w") as f:
            f.write(f"Test exitoso - {time.strftime('%Y-%m-%d %H:%M:%S')}")
        
    except Exception as e:
        print(f"Test falló: {str(e)}")
        raise

def test_empty_fields_validation(browser):
    """Test para validar que no se puedan enviar campos vacíos"""
    try:
        browser.find_element(By.NAME, "nombre").clear()
        browser.find_element(By.NAME, "apellido").send_keys("Martínez")
        browser.find_element(By.NAME, "email").send_keys("yameli@example.com")
        browser.find_element(By.NAME, "telefono").send_keys("8291234567")
        
        browser.find_element(By.TAG_NAME, "form").submit()
        time.sleep(1)
        
        alert = Alert(browser)
        alert_text = alert.text
        
        alert.accept()
        time.sleep(0.5)
        
        assert "Por favor, complete todos los campos" in alert_text
        
        take_screenshot(browser, "1_test_exitoso_campos_vacios")
        
        with open(f"{SCREENSHOT_DIR}/test_empty_fields_validation_EXITOSO.txt", "w") as f:
            f.write(f"Test exitoso - {time.strftime('%Y-%m-%d %H:%M:%S')}")
        
    except Exception as e:
        print(f"Test falló: {str(e)}")
        raise

def test_invalid_email(browser):
    """Test para validar el rechazo de emails inválidos"""
    try:
        browser.find_element(By.NAME, "nombre").send_keys("Yameli")
        browser.find_element(By.NAME, "apellido").send_keys("Martínez")
        browser.find_element(By.NAME, "email").send_keys("email_invalido.com")
        browser.find_element(By.NAME, "telefono").send_keys("8291234567")
        
        browser.find_element(By.TAG_NAME, "form").submit()
        time.sleep(1)
        
        alert = Alert(browser)
        alert_text = alert.text
        
        alert.accept()
        time.sleep(0.5)
        
        assert "Correo electrónico inválido" in alert_text
        
        take_screenshot(browser, "1_test_exitoso_email_invalido")
        
        with open(f"{SCREENSHOT_DIR}/test_invalid_email_EXITOSO.txt", "w") as f:
            f.write(f"Test exitoso - {time.strftime('%Y-%m-%d %H:%M:%S')}")
        
    except Exception as e:
        print(f"Test falló: {str(e)}")
        raise

if __name__ == "__main__":
    print("Generando resumen de tests exitosos...")
    
    test_resultados = []
    for archivo in os.listdir(SCREENSHOT_DIR):
        if archivo.endswith("_EXITOSO.txt"):
            nombre_test = archivo.replace("_EXITOSO.txt", "")
            with open(os.path.join(SCREENSHOT_DIR, archivo), "r") as f:
                tiempo = f.read()
            test_resultados.append((nombre_test, tiempo))
    
    if test_resultados:
        print("\n=== TESTS EXITOSOS ===")
        for test, tiempo in test_resultados:
            print(f"✅ {test}: {tiempo}")
        print(f"\nTotal tests exitosos: {len(test_resultados)}")
        print(f"Capturas guardadas en: {os.path.abspath(SCREENSHOT_DIR)}")
    else:
        print("No se encontraron tests exitosos.")