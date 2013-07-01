from django.db import models


IS_INPUT_OR_OUTPUT_CHOICES = (
    ( 0, 'input' ),
    ( 1, 'output' )
)

TYPE_CHOICES = (
    ( 0, 'string' ),
    ( 1, 'integer' ),
    ( 2, 'float' ),
    ( 3, 'boolean' ),
    ( 4, 'select' ),
    ( 5, 'file' ),
)
    
class Option( models.Model ):
    label = models.CharField( u"choice display to user", max_length = 100 )
    value = models.CharField( u"value send to command line", max_length = 100 )
    def __unicode__( self ):
        return u'%s %s' %( self.label, self.value )
       
class FileType( models.Model ):
    label       = models.CharField( u"File type label", max_length = 100 )
    extension   = models.CharField( u"File extension", max_length = 30, unique = True )
    def __unicode__( self ):
        return u'%s' %( self.extension )

class Parameter( models.Model ):
    name        = models.CharField( u"parameter name", max_length = 100 )
    label       = models.TextField( u"Parameter label", blank = True, null = True )
    param_io    = models.IntegerField( u"input or output", choices = IS_INPUT_OR_OUTPUT_CHOICES )
    is_required = models.BooleanField( u"parameter required or not", default = True )
    param_type  = models.IntegerField( u"parameter type", choices = TYPE_CHOICES )
    file_type   = models.ForeignKey( FileType, verbose_name = u"File format")
    options     = models.ManyToManyField( Option, verbose_name = u"Select options" )
    def __unicode__( self ):
        return u'%s' %( self.name )

class Script( models.Model ):
    name        = models.CharField( u"Script Name", max_length = 50 )
    command     = models.TextField( u"Command line" )
    abs_path    = models.CharField( u"server@abs_path", max_length = 100 )
    author      = models.CharField( u"Author", max_length = 50 )
    description = models.TextField( u"description of the script", blank = True, null = True )
    help        = models.TextField( u"Help of the script", blank = True, null = True )
    parameters  = models.ManyToManyField( Parameter, verbose_name = u"Parameters" )
    def __unicode__(self):
        return u'%s' % (self.name)