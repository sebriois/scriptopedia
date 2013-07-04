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
    label = models.CharField( u"Option label", max_length = 100 )
    value = models.CharField( u"Option value for command line", max_length = 100 )
    
    def __unicode__( self ):
        return u'%s %s' %( self.label, self.value )
    

class FileType( models.Model ):
    label       = models.CharField( u"File type label", max_length = 100 )
    extension   = models.CharField( u"File extension", max_length = 30, unique = True )
    
    def __unicode__( self ):
        return u'%s' %( self.extension )
    

class Parameter( models.Model ):
    name        = models.CharField( u"Name (in command line)", max_length = 100 )
    label       = models.CharField( u"Label (for display in a form)", max_length = 100, blank = True, null = True )
    param_type  = models.IntegerField( u"Type", choices = TYPE_CHOICES )
    file_type   = models.ForeignKey( FileType, verbose_name = u"File format", null = True, blank = True )
    param_io    = models.IntegerField( u"Input/Output ?", choices = IS_INPUT_OR_OUTPUT_CHOICES )
    is_required = models.BooleanField( u"Required ?", default = True, blank = True )
    options     = models.ManyToManyField( Option, verbose_name = u"Select options" )
    
    def __unicode__( self ):
        return u'-%s <%s>' %( self.name, self.label )

class Section(models.Model):
    name = models.CharField( u"section_name", max_length = 50 )
    label = models.CharField(u"Name", max_length = 50 )
    
    def __unicode__(self):
        return u"%s" % (self.label)
    

class Script( models.Model ):
    section     = models.ForeignKey( Section, verbose_name = "Category" )
    name        = models.CharField( u"Script Name", max_length = 50 )
    command     = models.TextField( u"Command Line" )
    abs_path    = models.CharField( u"Absolute Path to Script", max_length = 100 )
    author      = models.CharField( u"Author(s)", max_length = 50 )
    description = models.TextField( u"Script Description", blank = True, null = True )
    help        = models.TextField( u"Script Help", blank = True, null = True )
    parameters  = models.ManyToManyField( Parameter, verbose_name = u"Parameters" )
    
    def __unicode__(self):
        return u'%s' % (self.name)
