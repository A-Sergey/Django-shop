from products.models import Product

def menu(request):
    names_menu = {'/':'News','/products/':'Products',
                '/about_us/':'About Us'}
    return {"names_menu": names_menu}