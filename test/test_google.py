from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
# Desactivar mensajes emergentes de cookies
prefs = {"profile.default_content_setting_values.cookies": 2}  # Bloquear cookies
options.add_experimental_option("prefs", prefs)

# Configurar el navegador con las opciones
driver = webdriver.Chrome(options=options)

driver.maximize_window()
driver.get("https://marca.com")
print("Navegador abierto sin ventanas emergentes de cookies.")

inicio_sesion_xpath = "//a[text()='Suscríbete']"

try:
    elemento = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, inicio_sesion_xpath))
    )
    elemento.click()
    print("Elemento localizado y clickeado.")
except Exception as e:
    print(f"Error al localizar el elemento: {e}")

# Continuar con el test
driver.quit()