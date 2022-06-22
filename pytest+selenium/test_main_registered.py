from selenium.common.exceptions import NoSuchElementException
import pytest, requests,time

objects_in_page = ('id_find_product',)
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
    def test_correct_responce(self,browser_reg):
        response = requests.get('http://127.0.0.1:8000').status_code
        assert response == 200
    
    #@pytest.mark.skip()
    def test_correct_name_shop(self,browser_reg):
        browser_reg.get(home_page)
        shop_name = browser_reg.find_element_by_class_name('myshop').text
        assert shop_name == 'My shop'
    
    
    #@pytest.mark.skip()
    @pytest.mark.parametrize('var', objects_in_page, ids=objects_in_page)
    def test_availability_find(self,browser_reg,var):
        browser_reg.get(home_page)
        try:
            browser_reg.find_element_by_id(var)
        except NoSuchElementException as u:
            assert False, u.msg
            
    #@pytest.mark.skip()
    def test_availability_top_menu(self,browser_reg):
        browser_reg.get(home_page)
        elements = browser_reg.find_element_by_class_name('top-menu').find_elements_by_tag_name('li')
        list_all = [element.text for element in elements]
        assert list_all == ['News', 'Products', 'About Us']
    
    #@pytest.mark.skip()
    def test_find_2_product(self,browser_reg,db):
        browser_reg.get(home_page)
        for x,y in db_name_pairs(db):
            if x.startswith(y[:3]):
                print('>>>>>>', x,y)
                similar_name = x
                break
        browser_reg.find_element_by_css_selector('#id_find_product').send_keys(similar_name[:3])
        browser_reg.find_element_by_css_selector('#header > nav:nth-child(2) > form:nth-child(2) > input:nth-child(4)').click()
        finded_names=[x.text for x in browser_reg.find_elements_by_css_selector('.product-test > a')]
        assert len(finded_names) == 2
        
        
    #@pytest.mark.skip()
    def test_find_1_product(self,browser_reg,db):
        browser_reg.get(home_page)
        products_visible = [product['name'] for product in db if product['visible_in_shop'] != 0]
        for i in products_visible:
            count = 0
            for j in products_visible:
                if i in j: count += 1
            if count == 1:
                product_name = i
                break
        browser_reg.find_element_by_css_selector('#id_find_product').send_keys(product_name)
        browser_reg.find_element_by_css_selector('#header > nav:nth-child(2) > form:nth-child(2) > input:nth-child(4)').click()
        finded_name = browser_reg.find_element_by_css_selector('.name > p').text
        assert finded_name == product_name