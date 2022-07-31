from django.contrib import admin
from django.urls import re_path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import about_us
from news.views import PostListView

urlpatterns = [
    re_path('^admin/', admin.site.urls),
    re_path(r'^$', PostListView.as_view(), name='news'),
    re_path(r'^accounts/', include('accounts.urls')),
    re_path('^products/', include('products.urls')),
    re_path('^basket/', include('basket.urls')),
    re_path('^about_us/', about_us)]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                        document_root=settings.MEDIA_ROOT)

