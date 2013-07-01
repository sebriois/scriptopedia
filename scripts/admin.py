from django.contrib import admin
from models import Script, Parameter, Option, FileType


class ScriptAdmin(admin.ModelAdmin):
    list_display    = ['name', 'command', 'description', 'author' ]  
admin.site.register(Script, ScriptAdmin)


class ParameterAdmin(admin.ModelAdmin):
    list_display = ['name', 'label','get_parameter_type_admin' , 'param_io', 'is_required']  
    
    def get_parameter_type_admin(self, instance):
        return u"%s" % instance.parameter.param_type
    get_parameter_type_admin.short_description = u"Parameter Type"
admin.site.register(Parameter, ParameterAdmin)


class OptionAdmin(admin.ModelAdmin):
    list_display = ['label', 'value']
admin.site.register(Option, OptionAdmin)
 
 
class FiletypeAdmin(admin.ModelAdmin):
    list_display = ['label', 'extension']
admin.site.register(FileType, FiletypeAdmin)
