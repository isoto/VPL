from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from visorxml.models import Pais,HDI

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'DatosVisorPublico.views.home', name='home'),
    # url(r'^DatosVisorPublico/', include('DatosVisorPublico.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^paises/', 'visorxml.views.leerXML'),
    url(r'^HDI/(.*)', 'visorxml.views.obtenerTodosHDI'),
    url(r'^GDP/(.*)', 'visorxml.views.obtenerTodosGDP'),
    url(r'^CSV/', 'visorxml.views.leerCSV'),
    
    
)
