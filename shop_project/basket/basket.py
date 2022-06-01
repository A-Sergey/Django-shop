from django.conf import settings
from products.models import Product

class Basket(object):

    def __init__(self, request):
        """
        Init basket
        """
        self.session = request.session
        basket = self.session.get(settings.BASKET_SESSION_ID)
        if not basket:
            basket = self.session[settings.BASKET_SESSION_ID] = {}
        self.basket = basket

    def add(self,product,quantity=1,update_quantity=False):
        """
        Add product in basket or update his quantity.
        """
        product_id = str(product.id)
        if product_id not in self.basket:
            self.basket[product_id] = {'quantity':0,
                                    'price':str(product.get_price()),
                                    }
        if self.basket[product_id]['price'] != product.get_price():
            self.basket[product_id]['price'] = product.get_price()
        if update_quantity:
            self.basket[product_id]['quantity'] = quantity
        else:
            self.basket[product_id]['quantity'] += quantity
        self.save()

    def sub(self,product,quantity=1,update_quantity=False):
        """
        Add product in basket or update his quantity.
        """
        product_id = str(product.id)

        if self.basket[product_id]['price'] != product.get_price():
            self.basket[product_id]['price'] = product.get_price()
        if update_quantity:
            self.basket[product_id]['quantity'] = quantity
        else:
            self.basket[product_id]['quantity'] -= quantity
        self.save()
        
    def save(self):
        #Update session basket
        self.session[settings.BASKET_SESSION_ID] = self.basket
        #Mark session as modified to make sure it is saved
        self.session.modified = True
    
    def remove(self, product):
        """
        Remove product from the basket
        """
        product_id = str(product.id)
        print('>',product_id)
        print('>>',self.basket)
        if product_id in self.basket:
            print('>>>',self.basket)
            del self.basket[product_id]
            print('>>>>',self.basket)
            self.save()
    
    def __iter__(self):
        """
        Sorting through items in the basket and getting products
        from DB
        """
        product_ids = self.basket.keys()
        products = Product.objects.filter(id__in=product_ids)
        
        for product in products:
            self.basket[str(product.id)]['product'] = product
        
        for item in self.basket.values():
            item['total_price'] = int(item['price']) * int(item['quantity'])
            yield item
    
    def __len__(self):
        """
        Counting all the items in the basket
        """
        return sum(item['quantity'] for item in self.basket.values())
    
    def get_total_price(self):
        """
        Calculation of the cost of goods in the basket.
        """
        return sum(int(item['price']) * int(item['quantity']) for item in self.basket.values())
    
    def clear(self):
        del self.session[settings.BASKET_SESSION_ID]
        self.session.modified = True

    