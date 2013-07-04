from django.conf.urls import patterns, url
from scripts.views import script_new, script_list, script_delete, section_new
 
urlpatterns = patterns('',
    url(r'^new-section/$', section_new, name = "section_new"),
    url(r'^new/$', script_new, name = "script_new"),
    url(r'^(?P<script_id>\d+)/delete/$', script_delete, name="script_delete"),
    url(r'^$', script_list, name = "script_list"),    
)