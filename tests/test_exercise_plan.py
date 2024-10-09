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

    def interact_with_element(self, by, value, action="click", input_value=None):
        """Helper method to interact with an element."""
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((by, value))
        )
        if action == "click":
            element.click()
        elif action == "input":
            element.clear()
            element.send_keys(input_value)
            assert element.get_attribute(
                "value") == input_value, f"Expected value '{input_value}', got '{element.get_attribute('value')}'"
        return element

    def test_header(self):
        heading = self.interact_with_element(By.CSS_SELECTOR, "body > h1", action="get")
        assert heading.text == "Exercise Planner", f"Expected 'Exercise Planner', got '{heading.text}'"

    def test_add_name(self):
        self.interact_with_element(By.CSS_SELECTOR, "#name", action="input", input_value="Arnold")

    @pytest.mark.parametrize("exercise_id, series, repetitions", [
        ("Barbell Squats", "3", "12"),
        ("Incline Dumbbell Flyes", "2", "15"),
        ("Dumbbell Rows", "4", "8"),
        ("French Press", "1", "20"),
    ])
    def test_exercises(self, exercise_id, series, repetitions):
        self.interact_with_element(By.ID, exercise_id, action="click")
        self.interact_with_element(By.ID, f"{exercise_id}_series", action="input", input_value=series)
        self.interact_with_element(By.ID, f"{exercise_id}_repetitions", action="input", input_value=repetitions)
