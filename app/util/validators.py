from wtforms.validators import ValidationError


class Unique(object):
    def __init__(self, programMemory, field, message=u'This element already exists.'):
        self.programMemory = programMemory
        self.field = field

    def __call__(self, form, field):
        if self.field.data in self.programMemory.keys():
            raise ValidationError(self.message)
