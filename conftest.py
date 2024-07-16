import datetime
import logging
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.options import Options as FireFoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager



def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser to use")
    parser.addoption("--base_url", default="http://192.168.0.3:8081", help="Base URL")
    parser.addoption("--headless", action="store_true", help="Run tests in headless mode")
    parser.addoption("--log_level", action="store", default="INFO", help="Log level")
    parser.addoption("--executor", action="store", default="local", help="Executor address")
    parser.addoption("--mobile", action="store_true", help="Enable mobile emulation")
    parser.addoption("--vnc", action="store_true", help="Enable VNC")
    parser.addoption("--logs", action="store_true", help="Enable logs")
    parser.addoption("--video", action="store_true", help="Enable video")
    parser.addoption("--bv", action="store", default=None, help="Browser version")
    #parser.addoption("--selenium-manager", action="store_true", help="Use Selenium Manager for driver management")

@pytest.fixture()
def browser(request):
    browser = request.config.getoption("--browser")
    executor = request.config.getoption("--executor")
    vnc = request.config.getoption("--vnc")
    version = request.config.getoption("--bv")
    logs = request.config.getoption("--logs")
    video = request.config.getoption("--video")
    log_level = request.config.getoption("--log_level").upper()

    logger = logging.getLogger(request.node.name)
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(message)s'))
    logger.addHandler(handler)

    logger.info("===> Test %s started at %s" % (request.node.name, datetime.datetime.now()))

    options = None
    driver = None

    if executor == "local":
        if browser == "chrome":
            options = ChromeOptions()
            if request.config.getoption("--headless"):
                options.add_argument("--headless")
            service = ChromeService(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service, options=options)
        elif browser == "firefox":
            options = FireFoxOptions()
            if request.config.getoption("--headless"):
                options.add_argument("--headless")
            service = FirefoxService(GeckoDriverManager().install())
            driver = webdriver.Firefox(service=service, options=options)
    else:
        executor_url = f"http://{executor}:4444/wd/hub"
        options = ChromeOptions() if browser == "chrome" else FireFoxOptions()
        capabilities = {
            "browserName": browser,
            "browserVersion": version if version != "latest" else "",
            "selenoid:options": {
                "enableVNC": vnc,
                "name": request.node.name,
                "screenResolution": "1920x1080x24",
                "enableVideo": video,
                "enableLog": logs,
            },
        }

        for k, v in capabilities.items():
            if v:
                options.set_capability(k, v)
        logger.info(f"Connecting to WebDriver at {executor_url}")

        driver = webdriver.Remote(command_executor=executor_url, options=options)

    driver.logger = logger
    driver.base_url = request.config.getoption("--base_url")
    driver.maximize_window()
    yield driver
    if driver is not None:
        driver.quit()
        logger.info("===> Test %s finished at %s", request.node.name, datetime.datetime.now())