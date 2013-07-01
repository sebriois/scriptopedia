$(document).ready(function addMore(selector, type){
//	alert('ok');
	
	var newParam = $(selector).clone(true);
	var total = $('#id_' + type + '-TOTAL_FORMS').val();
	
	newParam.find(':input').each(function(){
		var name = $(this).attr('name').replace('-'+(total-1)+'-','-' + total + '-');
		var id = 'id_' + name;
	    $(this).attr({'name': name, 'id': id}).val('').removeAttr('checked');
	});
	newParam.find('label').each(function() {
        var newFor = $(this).attr('for').replace('-' + (total-1) + '-','-' + total + '-');
        $(this).attr('for', newFor);
    });
    total++;
    $('#id_' + type + '-TOTAL_FORMS').val(total);
    $(selector).after(newParam);
    
});
