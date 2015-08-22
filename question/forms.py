from __future__ import unicode_literals
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Question
class AnswerFrom(forms.Form):
    content=forms.CharField(widget=forms.Textarea(attrs={'rows': 6}), label='Answer')
    def __init__(self, *args, **kwargs):
        super(AnswerFrom, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'answer'
        self.helper.form_method = 'post'
        self.helper.form_action = 'answer/'
        self.helper.add_input(Submit('submit', 'Submit'))

class QuestionForm(forms.Form):
    title=forms.CharField(required=True, label='Question')
    content=forms.CharField(label='Content', widget=forms.Textarea(), required=False)
    tags=forms.CharField(label='Topics')

    def clean_title(self):
        title=self.cleaned_data['title'].strip()
        if title[len(title)-1]!='?':
            title+='?'
        return title

    def clean_tags(self):
        tags=self.cleaned_data['tags'].strip()
        tags=tags.strip(',')
        tags=tags.split(',')
        for i in range(len(tags)):
            tags[i]=tags[i].lower().title()
        return tags

    def __init__(self, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'question'
        self.helper.form_method = 'post'
        self.helper.form_action = 'question:add'
        self.helper.add_input(Submit('submit', 'Submit'))