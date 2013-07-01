from django.conf.urls import patterns, url
from scripts.views import script_new, script_list
 
 
urlpatterns = patterns('',
    url(r'^new/$', script_new, name = "new_script"),
    url(r'^$', script_list, name = "script_list"),    
)