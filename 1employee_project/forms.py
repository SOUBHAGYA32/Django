from django import forms
from .models import Employee


#  we're creating a form and inheret it from ModelForm.then since we already have a model for employee in models lets import and use the same fields. 
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        # if you want all the fields same as its in models use all but if want to delete some of them then use the other one
        # fields = '__all__'

        # just in case of you want to remove some of the field you can simply write the following code: we creata a tuple for that like below.
        fields = ('fullname','mobile','emp_code','position')
        # we create label object cuz we want to update some labels in our forms
        labels = {
            'fullname':'Full Name',
            'emp_code':'EMP. Code'
        }


        # we define this class to put the select option instead of ----- in the dropdown
    def __init__(self, *args, **kwargs):
        super(EmployeeForm,self).__init__(*args, **kwargs)
        self.fields['position'].empty_label  = "select"