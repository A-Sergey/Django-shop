
def menu(request):
    #names_menu = {'Main':'/','Products':'/products/',
    #            'About Us':'/about_us/'}
    names_menu = {'/':'News','/products/':'Products',
                '/about_us/':'About Us'}
    return {"names_menu": names_menu}