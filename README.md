# Proyecto de Automatización con Selenium y Behave

Este proyecto implementa pruebas automatizadas utilizando Selenium, Behave (BDD), y Python, siguiendo el modelo Page Object Model (POM). Está diseñado para ser fácilmente extensible y organizado para manejar pruebas en diferentes secciones de una aplicación web.

## 🚀 Características

- Implementación del modelo Page Object Model (POM).
- Uso de Behave para escribir pruebas en un formato legible y estructurado (Gherkin).
- Ejecución de pruebas con Selenium en navegadores como Chrome.
- Configuración centralizada para facilitar cambios (tiempos de espera, URL base, etc.).
- Organización modular de pasos (steps) según el tipo de elementos (botones, entradas de texto, etc.).
- Soporte para hooks (before_all y after_all) para inicialización y limpieza de recursos.

## 📂 Estructura del Proyecto
```plaintext
project/
├── features/
│   ├── steps/
│   │   ├── button.py         # Pasos relacionados con botones
│   │   ├── input.py          # Pasos relacionados con campos de entrada
│   │   └── dropdown.py       # Pasos relacionados con menús desplegables
│   ├── environment.py        # Hooks (before_all, after_all)
│   ├── configuration.py      # Configuración del proyecto
│   ├── home.feature          # Pruebas relacionadas con la página de inicio
│   └── login.feature         # Pruebas relacionadas con el inicio de sesión
└── README.md                 # Documentación del proyecto
```

## 🛠️ Instalación y Configuración

# Prerrequisitos

- Python 3.8 o superior
- Google Chrome (o cualquier navegador compatible con Selenium).
- Chromedriver (asegúrate de que la versión coincida con tu navegador).

# Configuración del entorno virtual

Crea y activa un entorno virtual:

python -m venv venv
source venv/bin/activate   # En macOS/Linux
venv\Scripts\activate      # En Windows

Instala las dependencias:

pip install -r requirements.txt

# Configuración de variables de entorno (opcional)

Si necesitas configuraciones específicas, puedes usar un archivo .env para almacenar variables como la URL base o credenciales.

## 🧪 Ejecución de las Pruebas

# Ejecutar todas las pruebas
Para ejecutar todas las pruebas, usa:

behave

# Ejecutar un archivo .feature específico

behave features/home.feature

# Ejecutar un escenario específico

behave -n "Nombre del Escenario"

## ⚙️ Configuración

Todas las configuraciones del proyecto (como URL base, tiempos de espera, etc.) están centralizadas en el archivo configuration.py. Aquí hay un ejemplo:

BASE_URL = "http://uitestingplayground.com/home"
IMPLICIT_WAIT = 10
EXPLICIT_WAIT = 15

## 🖥️ Ejemplo de Uso
# Escenario de ejemplo: Navegar a la página de inicio y verificar un botón

Archivo: home.feature

Feature: Home Page Verification
  Scenario: Verify button interaction on home page
    When I click the button with id "homeButton"
    Then I should see the text "Welcome to the Playground" on the page

Archivo: steps/button.py

from behave import when, then

@when('I click the button with id "{button_id}"')
def click_button(context, button_id):
    button = context.driver.find_element(By.ID, button_id)
    button.click()

@then('I should see the text "{expected_text}" on the page')
def verify_text_on_page(context, expected_text):
    assert expected_text in context.driver.page_source, f"'{expected_text}' not found on page"


## 📄 Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.

## 💡 Contribuciones

Las contribuciones son bienvenidas. Si deseas colaborar, abre un issue o crea un pull request con tus mejoras.

1. Crea un fork del repositorio.
2. Crea una rama para tu funcionalidad: git checkout -b feature/nueva-funcionalidad.
3. Realiza tus cambios y commits.
4. Abre un pull request.

## 🔗 Recursos Adicionales

- Behave Documentation
- Selenium Documentation
- Python Official Site
