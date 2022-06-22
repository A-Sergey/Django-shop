from selenium.common.exceptions import NoSuchElementException
import pytest, requests

objects_in_page = ('id_username_login','id_password_login','id_find_product')
home_page = 'http://127.0.0.1:8000'

def db_name_pairs(name):
    count = 0
    for i in name:
        for j in name:
            if i['name'] == j['name']:
                continue
            yield i['name'],j['name']

class TestMainPage:
    #@pytest.mark.skip()
    @pytest.mark.incremental
    def test_correct_responce(self,db):
        response = requests.get('http://127.0.0.1:8000').status_code
        assert response == 200
    
    #@pytest.mark.skip()
    def test_correct_name_shop(self,browser):
        browser.get(home_page)
        shop_name = browser.find_element_by_class_name('myshop').text
        assert shop_name == 'My shop'
    
    
    #@pytest.mark.skip()
    @pytest.mark.parametrize('var', objects_in_page, ids=objects_in_page)
    def test_availability_find(self,browser,var):
        browser.get(home_page)
        try:
            browser.find_element_by_id(var)
        except NoSuchElementException as u:
            assert False, u.msg
            
    #@pytest.mark.skip()
    def test_availability_top_menu(self,browser):
        browser.get(home_page)
        elements = browser.find_element_by_class_name('top-menu').find_elements_by_tag_name('li')
        list_all = [element.text for element in elements]
        assert list_all == ['News', 'Products', 'About Us']

    #@pytest.mark.skip()
    def test_find_2_product(self,browser,db):
        browser.get(home_page)
        for x,y in db_name_pairs(db):
            if x.startswith(y[:3]):
                print('>>>>>>', x,y)
                similar_name = x
                break
        browser.find_element_by_css_selector('#id_find_product').send_keys(similar_name[:3])
        browser.find_element_by_css_selector('#header > nav:nth-child(2) > form:nth-child(2) > input:nth-child(4)').click()
        finded_names=[x.text for x in browser.find_elements_by_css_selector('.product-test > a')]
        assert len(finded_names) == 2
        
        
    #@pytest.mark.skip()
    def test_find_1_product(self,browser,db):
        browser.get(home_page)
        products_visible = [product['name'] for product in db if product['visible_in_shop'] != 0]
        for i in products_visible:
            count = 0
            for j in products_visible:
                if i in j: count += 1
            if count == 1:
                product_name = i
                break
        browser.find_element_by_css_selector('#id_find_product').send_keys(product_name)
        browser.find_element_by_css_selector('#header > nav:nth-child(2) > form:nth-child(2) > input:nth-child(4)').click()
        finded_name = browser.find_element_by_css_selector('.name > p').text
        assert finded_name == product_name

    #@pytest.mark.skip()
    def test_login(self, browser):
        browser.get(home_page)
        login = browser.find_element_by_id('id_username_login')
        login.send_keys('test1')
        passw = browser.find_element_by_id('id_password_login')
        passw.send_keys('1q1w1e1R')
        button = browser.find_element_by_xpath('//*[@id="header"]/header/div/form/input[2]').click()
        greeting = browser.find_element_by_css_selector('.profile-info > p').text
        try:
            assert greeting == 'Hello, test1!!!'
        finally:
            browser.find_element_by_xpath('/html/body/div/div/header/div/a[2]').click()

    #@pytest.mark.skip()
    def test_link_lost_password(self,browser):
        browser.get(home_page)
        browser.find_element_by_xpath('//*[@id="header"]/header/div/p[1]/a').click()
        assert browser.find_element_by_id('id_email').tag_name == 'input'

    #@pytest.mark.skip()
    def test_link_register(self,browser):
        browser.get(home_page)
        browser.find_element_by_xpath('//*[@id="header"]/header/div/p[2]/a').click()
        assert (browser.find_element_by_id('id_username').tag_name == 'input' and 
                browser.find_element_by_id('id_email').tag_name == 'input' and
                browser.find_element_by_id('id_date_of_birth').tag_name == 'input' and 
                browser.find_element_by_id('id_password1').tag_name == 'input' and
                browser.find_element_by_id('id_password2').tag_name == 'input')