from django.conf.urls.defaults import *
from ldap_groups.views import ldap_search

urlpatterns = patterns('',
    (r'^ldap_search/$', ldap_search),
)
