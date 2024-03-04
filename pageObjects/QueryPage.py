from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.by import By


class Query:

    def __init__(self, driver):
        self.driver = driver

    # Query history locators
    QUERY_HISTORY_LINK = By.XPATH, "//a[contains(@href,'query-history')]//parent::li",
    REFRESH_BUTTON = By.XPATH, "//*[local-name()='svg' and @id='refresh']/*[local-name()='path']//ancestor::button",
    CALENDAR_ICON_FILTER = By.XPATH, "//button[@class='btn btn-outline-primary']//parent::div[@class='button-wrapper']"
    FILTER_PICKER = By.XPATH, "//div[contains(text(), 'Last 7 days')]"
    HISTORY_ROWS = By.XPATH, "//table//tbody//tr"
    # HISTORY_COLUMNS = By.XPATH, "//table//tbody//tr//td"
    HISTORY_COLUMNS = By.TAG_NAME, "td[1]"

    def get_query_page(self):
        self.driver.find_element(*Query.QUERY_HISTORY_LINK).click()

    def apply_filter_from_picker(self):
        self.driver.find_element(*Query.REFRESH_BUTTON).click()
        self.driver.find_element(*Query.CALENDAR_ICON_FILTER).click()
        self.driver.find_element(*Query.FILTER_PICKER).click()

    def get_query_history_table(self):
        try:
            rows = self.driver.find_elements(*Query.HISTORY_ROWS)

            all_records = []

            for row in rows:
                cells = row.find_elements(*Query.HISTORY_COLUMNS)
                record = [cell.text for cell in cells]
                all_records.append(record)

        except(StaleElementReferenceException):
            self.driver.refresh()

            # Display all records
            for record in all_records:
                print(record)





























    # self.driver.find_element(By.XPATH, "//a[contains(@href,'query-history')]//parent::li").click()
    # self.driver.find_element(By.XPATH,
    #                          "//*[local-name()='svg' and @id='refresh']/*[local-name()='path']//ancestor::button").click()
    # self.driver.implicitly_wait(3000)
    # ele = self.driver.find_element(By.XPATH,
    #                                "//button[@class='btn btn-outline-primary']//parent::div[@class='button-wrapper']")
    # ele.click()
    # self.driver.find_element(By.XPATH, "//div[contains(text(), 'Last 7 days')]").click()
    # rows = self.driver.find_elements(By.XPATH, "//table//tbody//tr")