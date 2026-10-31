import data
import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


# no modificar
def retrieve_phone_code(driver) -> str:
    """Este código devuelve un número de confirmación de teléfono y lo devuelve como un string.
    Utilízalo cuando la aplicación espere el código de confirmación para pasarlo a tus pruebas.
    El código de confirmación del teléfono solo se puede obtener después de haberlo solicitado en la aplicación."""

    import json
    import time
    from selenium.common import WebDriverException
    code = None
    for i in range(10):
        try:
            logs = [log["message"] for log in driver.get_log('performance') if log.get("message")
                    and 'api/v1/number?number' in log.get("message")]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody',
                                              {'requestId': message_data["params"]["requestId"]})
                code = ''.join([x for x in body['body'] if x.isdigit()])
        except WebDriverException:
            time.sleep(1)
            continue
        if not code:
            raise Exception("No se encontró el código de confirmación del teléfono.\n"
                            "Utiliza 'retrieve_phone_code' solo después de haber solicitado el código en tu aplicación.")
        return code


class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    taxi_button = (By.XPATH, '//button[@class="button round"]')
    comfort_button = (By.XPATH, '//div[@class="tcard-title" and contains(text(),"Comfort")]')
    phone_number_button = (By.CLASS_NAME, 'np-button')
    phone_number_field = (By.XPATH, '//input[@id="phone"]')
    next_button = (By.XPATH, '(//button[@class="button full"])[1]')
    phone_code_field = (By.XPATH, '//input[@id="code" and @class="input"]')
    confirm_button = (By.XPATH, '//button[@class="button full" and text()="Confirmar"]')
    reserve_button = (By.CLASS_NAME, 'smart-button')
    pay_method_button = (By.XPATH, '//div[@class="pp-text"]')
    card_button = (By.CLASS_NAME, 'pp-plus-container')
    card_number_field = (By.CLASS_NAME, 'card-input')
    card_code_field = (By.XPATH, '//input[@id="code" and @class="card-input"]')
    add_button = (By.XPATH, '(//button[@class="button full"])[4]')
    close_button = (By.XPATH, '(//button[@class="close-button section-close"])[3]')
    comment_field = (By.ID, 'comment')
    blanket_switch = (By.XPATH, "//div[contains(@class,'r-sw-container')][.//div[contains(text(),'Manta y pañuelos')]]//span[contains(@class,'slider')]")
    ice_cream_plus = (By.XPATH,
                      '//div[contains(@class,"r-counter-container")][.//div[text()="Helado"]]//div[contains(@class,"counter-plus")]')


    def __init__(self, driver):
        self.driver = driver

    def wait_for_load_field(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(self.from_field)
        )

    def set_from(self, from_address):
        self.driver.find_element(*self.from_field).send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def set_route(self, from_address, to_address):
        self.set_from(from_address)
        self.set_to(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def select_taxi(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(self.taxi_button)
        ).click()

    def select_comfort(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(self.comfort_button)
        ).click()
    def click_phone_button(self):
        self.driver.find_element(*self.phone_number_button).click()

    def input_phone_number(self):
        self.driver.find_element(*self.phone_number_field).send_keys(data.phone_number)

    def click_next_button(self):
        phone = self.driver.find_element(*self.phone_number_field)
        button = self.driver.find_element(*self.next_button)

        print("Número:", phone.get_attribute("value"))
        print("Campo válido:", phone.get_property("validity")["valid"])
        print("Botón deshabilitado:", button.get_property("disabled"))
        print("Texto de validación:", phone.get_property("validationMessage"))

        button.click()
        time.sleep(3)

    def input_phone_code(self):
        self.driver.find_element(*self.phone_code_field).send_keys(retrieve_phone_code(self.driver))

    def confirm_code_button(self):
        self.driver.find_element(*self.confirm_button).click()

    def get_phone_number(self):
        return self.driver.find_element(*self.phone_number_field).get_property('value')
    def click_pay_method(self):
        self.driver.find_element(*self.pay_method_button).click()

    def click_add_card(self):
        self.driver.find_element(*self.card_button).click()

    def input_card_number(self):
        self.driver.find_element(*self.card_number_field).send_keys(data.card_number)

    def input_card_code(self):
        self.driver.find_element(*self.card_code_field).send_keys(data.card_code)
        self.driver.find_element(*self.card_code_field).send_keys(Keys.TAB)

    def click_add_card_button(self):
        self.driver.find_element(*self.add_button).click()

    def input_message_for_driver(self):
        self.driver.find_element(*self.comment_field).send_keys(data.message_for_driver)

    def select_blanket_and_tissues(self):
        switch = self.driver.find_element(*self.blanket_switch)
        self.driver.execute_script("arguments[0].click();", switch)

    def add_two_ice_creams(self):
        for i in range(2):
            button = self.driver.find_element(*self.ice_cream_plus)
            self.driver.execute_script("arguments[0].click();", button)

    def click_reserve_button(self):
        button = self.driver.find_element(*self.reserve_button)
        self.driver.execute_script("arguments[0].click();", button)


class TestUrbanRoutes:
    driver = None

    @classmethod
    def setup_class(cls):
        options = webdriver.ChromeOptions()
        options.set_capability("goog:loggingPrefs", {"performance": "ALL"})
        cls.driver = webdriver.Chrome(options=options)

    def test_set_route(self):
        self.driver.get(data.urban_routes_url)

        routes_page = UrbanRoutesPage(self.driver)
        routes_page.wait_for_load_field()

        address_from = data.address_from
        address_to = data.address_to

        routes_page.set_route(address_from, address_to)

        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

        routes_page.select_taxi()
        routes_page.select_comfort()
        #routes_page.click_phone_button()
        #routes_page.input_phone_number()
        #routes_page.click_next_button()
        #routes_page.input_phone_code()
        #routes_page.confirm_code_button()

        routes_page.click_pay_method()
        routes_page.click_add_card()
        routes_page.input_card_number()
        routes_page.input_card_code()
        routes_page.click_add_card_button()
        routes_page.input_message_for_driver()
        routes_page.select_blanket_and_tissues()
        routes_page.add_two_ice_creams()
        routes_page.click_reserve_button()


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
