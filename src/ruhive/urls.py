from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
import profiles.urls
import accounts.urls
from . import views

urlpatterns = [
    url(r'^$', views.HomePage.as_view(), name='home'),
    url(r'^about/$', views.AboutPage.as_view(), name='about'),
    url(r'^services/$', views.ServicesPage.as_view(), name='services'),
    url(r'^blog/$', views.BlogPage.as_view(), name='blog'),
    url(r'^iot/$', views.IOTPage.as_view(), name='iot'),
    url(r'^dc/$', views.DCPage.as_view(), name='dc'),
    url(r'^products/$', views.HadoopPage.as_view(), name='products'),
    url(r'^hadoop/$', views.HadoopPage.as_view(), name='hadoop'),
    url(r'^contact/$', views.ContactPage.as_view(), name='contact'),
    url(r'^users/', include(profiles.urls, namespace='profiles')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(accounts.urls, namespace='accounts')),

]

# User-uploaded files like profile pics need to be served in development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
