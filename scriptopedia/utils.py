from django.contrib import messages

def info_msg( request, message ):
    return messages.add_message( request, messages.INFO, message )

def error_msg( request, message ):
    return messages.add_message( request, messages.ERROR, message )

def warn_msg( request, message ):
    return messages.add_message( request, messages.WARNING, message )
