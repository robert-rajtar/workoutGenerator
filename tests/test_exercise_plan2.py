import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="class")
def driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


class TestExercisePlanner:
    @pytest.fixture(autouse=True)
    def setup_method(self, driver):
        self.driver = driver
        self.driver.get("http://127.0.0.1:5000/")

    def find_element(self, by, value):
        """Helper method to find an element."""
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((by, value))
        )

    def click_element(self, by, value):
        """Helper method to click an element."""
        element = self.find_element(by, value)
        element.click()
        return element

    def enter_value(self, by, value_id, input_value):
        """Helper method to enter a value in an input field."""
        input_field = self.find_element(by, value_id)
        input_field.clear()
        input_field.send_keys(input_value)
        assert input_field.get_attribute(
            "value") == input_value, f"Expected value '{input_value}', got '{input_field.get_attribute('value')}'"

    def test_header(self):
        heading = self.find_element(By.CSS_SELECTOR, "body > h1")
        assert heading.text == "Exercise Planner", f"Expected 'Exercise Planner', got '{heading.text}'"

    def test_add_name(self):
        self.enter_value(By.CSS_SELECTOR, "#name", "Arnold")

    def test_leg_exercise(self):
        self.click_element(By.CSS_SELECTOR, "body > form > label:nth-child(7)")
        barbell_squats_check = self.find_element(By.ID, "Barbell Squats")
        assert barbell_squats_check.is_selected()

        self.enter_value(By.ID, "Barbell Squats_series", "3")
        self.enter_value(By.ID, "Barbell Squats_repetitions", "12")

    def test_chest_exercise(self):
        self.click_element(By.CSS_SELECTOR, "body > form > label:nth-child(141)")
        incline_df_check = self.find_element(By.ID, "Incline Dumbbell Flyes")
        assert incline_df_check.is_selected()

        self.enter_value(By.ID, "Incline Dumbbell Flyes_series", "2")
        self.enter_value(By.ID, "Incline Dumbbell Flyes_repetitions", "15")

    def test_back_exercise(self):
        self.click_element(By.CSS_SELECTOR, "body > form > label:nth-child(184)")
        dumbbell_rows_check = self.find_element(By.ID, "Dumbbell Rows")
        assert dumbbell_rows_check.is_selected()

        self.enter_value(By.ID, "Dumbbell Rows_series", "4")
        self.enter_value(By.ID, "Dumbbell Rows_repetitions", "8")

    def test_arm_exercise(self):
        self.click_element(By.CSS_SELECTOR, "body > form > label:nth-child(234)")
        french_press_check = self.find_element(By.ID, "French Press")
        assert french_press_check.is_selected()

        self.enter_value(By.ID, "French Press_series", "1")
        self.enter_value(By.ID, "French Press_repetitions", "20")
