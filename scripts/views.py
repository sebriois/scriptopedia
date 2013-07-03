from django.shortcuts       import get_object_or_404, render, redirect
from django.forms.formsets  import formset_factory
from django.db              import transaction

from scripts.models import Script, Parameter, Option, Section
from scripts.forms  import ScriptForm, ParamForm, SectionForm
from scriptopedia.utils import info_msg, error_msg, warn_msg

@transaction.commit_on_success
def script_new(request):
    ParamFormSet = formset_factory(ParamForm, can_delete = True )
    if request.method == 'POST':
        script_form = ScriptForm( request.POST )
        param_formset = ParamFormSet( data = request.POST, prefix='param')
        
        if script_form.is_valid() and param_formset.is_valid():
            script = script_form.save()
            for parameter_data in param_formset.cleaned_data:
                if parameter_data:
                    parameter = Parameter.objects.create( **parameter_data )
                    script.parameters.add( parameter )
            script.save()
            
            info_msg(request, 'Script added successfully')
            
            if 'save_and_add' in request.POST.keys():
                return redirect('script_new')
            else:            
                return redirect('script_list')
    else:
        script_form = ScriptForm()
        param_formset = ParamFormSet( prefix='param' )
    
    return render(request, 'script_new.html', {
        'form'   : script_form,
        'formset': param_formset,
    })

def script_list(request):
    return render(request, 'script_list.html', {
        'sections': Section.objects.all(),
        'section_form': SectionForm(),
    })

def script_edit(request, script_id):
    script = get_object_or_404(Script, id = script_id)
    
    ParamFormSet = formset_factory(ParamForm)
    if request.method == 'POST':
        script_form = ScriptForm( data = request.POST, initial = script )
        param_formset = ParamFormset( request.POST, prefix='param' )
        if script_form.is_valid() and param_formset.is_valid():
            script = script_form.save()
            
            return redirect('script_list')
    else:
        form = ScriptForm(initial = script)
        param_formset = ParamFormSet( prefix='param' )
    
    return render(request, 'script_new.html', {
        'form'   : form,
        'formset': param_formset,
    })

def script_delete(request, script_id):
    script = get_object_or_404(Script, id = script_id)
    script.delete()
    
    info_msg(request, 'Script deleted successfully.')
    return redirect('script_list')


def section_new(request):
    data = request.POST.copy()
    data.update({
        'name': data['label'].lower().replace(' ', '_')
    })
    form = SectionForm( data = data )
    if form.is_valid():
        info_msg(request, "Category '%s' created successfully" % data['label'])
        form.save()
    return redirect('script_list')
