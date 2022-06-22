import pytest, time
from selenium import webdriver
import sqlite3


@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Chrome(executable_path="./chromedriver")
    yield driver
    driver.quit()
    
@pytest.fixture(scope="module")
def browser_reg():
    driver = webdriver.Chrome(executable_path="./chromedriver")
    driver.get('http://127.0.0.1:8000')
    login = driver.find_element_by_id('id_username_login')
    login.send_keys('test1')
    passw = driver.find_element_by_id('id_password_login')
    passw.send_keys('1q1w1e1R')
    button = driver.find_element_by_xpath('//*[@id="header"]/header/div/form/input[2]').click()
    greeting = driver.find_element_by_css_selector('.profile-info > p').text
    yield driver
    driver.find_element_by_xpath('/html/body/div/div/header/div/a[2]').click()
    driver.quit()

@pytest.fixture(scope="session")
def db():
    try:
        sqlite_connection = sqlite3.connect('F:\\Django_shop\\shop_project\\db.sqlite3')
        cursor = sqlite_connection.cursor()
        
        sqlite_select_query = "SELECT * from products_product"
        table = cursor.execute(sqlite_select_query)
        name_cols = [name[0] for name in cursor.description]
        products = ()
        for product in table.fetchall():
            products += (dict([(name_col,product[name_cols.index(name_col)]) for name_col in name_cols]),)
        cursor.close()
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
    return products

try:
    pytest.skip()
except BaseException as e:
    Skipped = type(e)

try:
    pytest.xfail()
except BaseException as e:
    XFailed = type(e)

def pytest_runtest_makereport(item, call):
    if "incremental" in item.keywords:
        if call.excinfo is not None:
            if call.excinfo.type in {Skipped, XFailed}:
                return

            parent = item.parent
            parent._previousfailed = item

def pytest_runtest_setup(item):
    previousfailed = getattr(item.parent, "_previousfailed", None)
    if previousfailed is not None:
        pytest.xfail("previous test failed (%s)" % previousfailed.name)