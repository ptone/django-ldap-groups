from django.contrib import admin
from ldap_groups.models import LDAPGroup

admin.site.register(LDAPGroup)