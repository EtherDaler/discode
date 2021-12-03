from django import forms
from .models import Comments
from ckeditor.widgets import CKEditorWidget

class CommentsForm(forms.ModelForm):
    text = forms.Textarea()
    #rating = forms.ChoiceField(choices=(5,4,3,2,1), widget=forms.RadioSelect())
    class Meta:
        model = Comments
        fields = ['text']

    def __init__(self, *args, **kwargs):
        super(CommentsForm, self).__init__(*args, **kwargs)
        self.fields['text'].widget.attrs \
            .update({
            'id': 'text',
            'class': 'input'
        })


