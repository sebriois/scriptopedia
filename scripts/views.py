from django.shortcuts   import render, redirect
from django.http        import HttpResponse
from django.template    import RequestContext

from scripts.models         import Script, Parameter, Option
from scripts.forms          import ScriptForm, ParamForm
from django.forms.formsets  import formset_factory

def script_new(request):
    ParamFormset = formset_factory(ParamForm)
    if request.method == 'POST':
        form          = ScriptForm( request.POST )
        param_formset = ParamFormset( request.POST, prefix='param' )
        if form.is_valid():
            script = form.save()            
            
            return redirect('script_list')          
    else:
        form          = ScriptForm()
        param_formset = ParamFormset( prefix='param' )
        
    return render(request, 'script_new.html', {
        'form'   : form,
        'param_formset': param_formset,
    }, context_instance=RequestContext(request))

def script_list(request):
    return render(request, 'script_list.html', {
        'scripts': Script.objects.all()
    })

# def get_parameter_form(request, formset_prefix):
#     if not request.is_ajax():
#         raise 'Not ajax'
#     
#     
#     
#     