from selenium import webdriver
from configuration import Config
import chromedriver_autoinstaller
from datetime import datetime
import os
import re

def before_all(context):
    chromedriver_autoinstaller.install()
    context.driver = webdriver.Chrome()
    context.driver.implicitly_wait(Config.IMPLICIT_WAIT)
    #context.driver.maximize_window()
    context.driver.set_window_size(1920, 1080)


def before_scenario(context, scenario):
    context.driver.get(Config.BASE_URL)


def after_scenario(context, scenario):
    timestamp_report = datetime.now().strftime("%Y-%m-%d_%H-%M")
    timestamp_screenshot = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    scenario_name = re.sub(r'[^\w\-_]', '_', scenario.name)
    report_address = os.path.join(os.getcwd(), "reports", timestamp_report)
    screenshot_address = os.path.join(os.getcwd(), "screenshots")

    os.makedirs(report_address, exist_ok=True)
    os.makedirs(screenshot_address, exist_ok=True)

    # Create or update the report
    with open(os.path.join(report_address, "custom_report.txt"), "a") as reporte:
        if scenario.status == "passed":
            reporte.write(f"Scenario '{scenario.name}' PASSED\n")
        else:
            reporte.write(f"Scenario '{scenario.name}' FAILED\n")
            try:
                screenshot_filename = os.path.join(screenshot_address, f"{scenario_name}_{timestamp_screenshot}.png")
                context.driver.save_screenshot(screenshot_filename)
            except Exception as e:
                print(f"Error al guardar captura de pantalla: {e}")


def after_all(context):
    context.driver.quit()