from django import forms
from .models import insightsAnalyticsModel 

class insightsAnalyticsForm(forms.ModelForm):
    class Meta:
        model = insightsAnalyticsModel
        fields = '__all__'
        widgets={"report_files":forms.FileInput(attrs={'id':'report_files','required':True,'multiple':True})}