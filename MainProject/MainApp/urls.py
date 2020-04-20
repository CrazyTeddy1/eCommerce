from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from django.conf.urls import url
from .views import home_page, contact_page, about_page, login_page, register_page
from products.views import ProductListView, ProductDetailtListView


urlpatterns = [
    url(r'^$', home_page),
    url(r'^contact/$', contact_page),
    url(r'^login/$', login_page),
    url(r'^register/$', register_page),
    url(r'^products/$', ProductListView),
    url(r'^products/(?P<pk>\d+)$', ProductDetailtListView),
    path('admin/', admin.site.urls),

]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
