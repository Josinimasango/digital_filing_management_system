from django.forms import ModelForm
from django.core.files.base import File
from django.db.models.base import Model
from typing import Any, Mapping
from django.forms.utils import ErrorList

from .models import Patient


class QuickPatientForm(ModelForm):
    class Meta:
        model=Patient
        fields = ["name", "age", "gender", "mobile", "detail", "medicine_detail", "next_visit"]
    
    def __init__(self, *args, **kwargs):
        super(QuickPatientForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control'
         
         
class PatientForm(ModelForm):
    class Meta:
        model=Patient
        fields = ["name", "age", "gender", "mobile", "detail", "medicine_detail", "address", "mobile", "next_visit", "note"]
    
    def __init__(self, *args, **kwargs):
        super(PatientForm, self).__init__(*args, **kwargs)
        self.fields['address'].widget.attrs['rows']='5'
        self.fields['note'].widget.attrs['rows']='5'
        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control'            
            