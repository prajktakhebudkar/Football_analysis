from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Wait until the table is visible
try:
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CLASS_NAME, "league-table__tbody"))
    )
    print("Table loaded successfully")
except:
    print("Error: Unable to locate the table after waiting.")
