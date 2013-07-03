$(document).ready(function(){
	// 
	// CONFIRMATION DIALOG - create the appropriate content in HTML code
	// 
	$( '.confirm-delete' ).click(function(e){
		e.preventDefault();
		var targetUrl = $(this).attr('href');

		$( "#dialog-confirm" ).dialog({
			resizable: false,
			modal: true,
			buttons: {
				Confirmer: function() {
					$( this ).dialog( "close" );
					window.location.href = targetUrl;
				},
				Annuler: function() {
					$( this ).dialog( "close" );
				}
			}
		});

		$( "#dialog-confirm" ).dialog('open');
	});
	
	
	//
   	// SCRIPT NEW
	//
	$('.delete_param').click(function(){
		$(this).parent('li').parent('ul').hide();
		$(this).prev('input[type="checkbox"]').attr('checked','checked');
		return false;
	});
	
	$('#add_more').click(function() {
       	addMore('.parameter:last', 'param');
   	});
   	
	function addMore(selector, type){
	    var newElement = $(selector).clone(true);
	    var total = $('#id_' + type + '-TOTAL_FORMS').val();
	    
	    newElement.find(':input').not('button').each(function() {
	        var name = $(this).attr('name').replace('-' + (total-1) + '-','-' + total + '-');
	        var id = 'id_' + name;
	        $(this).attr({'name': name, 'id': id}).val('').removeAttr('checked');
	    });
	    
	    newElement.find('label').each(function() {
	        var newFor = $(this).attr('for').replace('-' + (total-1) + '-','-' + total + '-');
	        $(this).attr('for', newFor);
	    });
	    total++;
	    
	    $('#id_' + type + '-TOTAL_FORMS').val(total);
	    newElement.show();
	    $('#add_more').before(newElement);
	}
});
