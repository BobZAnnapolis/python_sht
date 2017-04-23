from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'bookstore.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    
    # url(r'^store/', 'store.views.store', name='store'),
    url(r'^$', 'store.views.index', name='index'),
 
    url(r'^store/', include('store.urls'), name='store'),
    # - bad - url(r'^$', include('store.urls', name='index'),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url('', include('social.apps.django_app.urls', namespace='social')),

]
