from django.conf import settings
from products.models import Product

class Cart(object):

    def __init__(self, request):
        """
        Init cart
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self,product,quantity=1,update_quantity=False):
        """
        Add product in cart or update his quantity.
        """
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity':0,
                                    'price':str(product.get_price()),
                                    }
        if self.cart[product_id]['price'] != product.get_price():
            self.cart[product_id]['price'] = product.get_price()
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def sub(self,product,quantity=1,update_quantity=False):
        """
        Add product in cart or update his quantity.
        """
        product_id = str(product.id)

        if self.cart[product_id]['price'] != product.get_price():
            self.cart[product_id]['price'] = product.get_price()
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] -= quantity
        self.save()
        
    def save(self):
        #Update session cart
        self.session[settings.CART_SESSION_ID] = self.cart
        #Mark session as modified to make sure it is saved
        self.session.modified = True
    
    def remove(self, product):
        """
        Remove product from the cart
        """
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()
    
    def __iter__(self):
        """
        Sorting through items in the cart and getting products
        from DB
        """
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        
        for product in products:
            self.cart[str(product.id)]['product'] = product
        
        for item in self.cart.values():
            item['total_price'] = int(item['price']) * int(item['quantity'])
            yield item
    
    def __len__(self):
        """
        Counting all the items in the cart
        """
        return sum(item['quantity'] for item in self.cart.values())
    
    def get_total_price(self):
        """
        Calculation of the cost of goods in the cart.
        """
        return sum(int(item['price']) * int(item['quantity'])
                        for item in self.cart.values())
    
    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True

    