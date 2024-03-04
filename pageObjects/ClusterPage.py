from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Cluster:

    def __init__(self, driver):
        self.driver = driver

    # Cluster Locators
    CLUSTER_LINK = By.XPATH, "//a[contains(@href,'cluster?sid')]",
    CLUSTER_TITLE = By.XPATH, "//h5[@class='title' and contains(text(), 'Clusters')]",
    CLUSTER_CREATE_BUTTON = By.XPATH, " //div[@class='mb-2 create-btn col-md-3']//button",
    CLUSTER_NAME_FIELD = By.XPATH, "//input[@placeholder='Enter cluster name']",
    CLUSTER_CATALOG_SELECT = By.XPATH, "//div[contains(@class,'react-select__in-valid react-select')]",
    CLUSTER_TABLE_ROW = By.XPATH, "//table//tbody//tr",
    CLUSTER_COLUMN_NAME = By.XPATH, "./td[1]",
    CLUSTER_COLUMN_CREATED_BY = By.XPATH, "CLUSTER_TABLE_ROW.td[5]",
    CLUSTER_COLUMN_STATUS = By.XPATH, "./td[6]",



    def get_cluster_page(self):
        self.driver.find_element(*Cluster.CLUSTER_LINK).click()

    def get_title(self):
        self.driver.find_element(*Cluster.CLUSTER_TITLE).text

    def create_cluster(self):
        self.driver.find_element(*Cluster.CLUSTER_CREATE_BUTTON).click()
        self.driver.find_element(*Cluster.CLUSTER_NAME_FIELD).send_keys("test12")
        self.driver.find_element(*Cluster.CLUSTER_CATALOG_SELECT).click()

    def get_cluster_records(self):
        self.driver.find_element(*Cluster.CLUSTER_LINK).click()
        rows = self.driver.find_elements(*Cluster.CLUSTER_TABLE_ROW)

        records = []

        for row in rows:
            name = row.find_element(*Cluster.CLUSTER_COLUMN_NAME).text
            created_by = row.find_element(*Cluster.CLUSTER_COLUMN_CREATED_BY).text
            status = row.find_element(*Cluster.CLUSTER_COLUMN_STATUS).text

            records.append({"Name": name, "Created By": created_by, "Status": status})
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//table//tbody//tr//td")))

        assert records, "No records were printed!"

        # Display total records
        print("Total Records:")
        for record in records:
            print(record)

