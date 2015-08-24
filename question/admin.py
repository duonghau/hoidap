from django.contrib import admin
from .models import Question, Answer
# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    list_display=('title','author','content_bref','create', 'votes_count','downvotes_count')
    search_fields = ["title"]
    ordering = ["create"]
    prepopulated_fields={'slug':('title',)}
    fields = ('title','slug','content', 'author','tags','is_active')
admin.site.register(Question, QuestionAdmin)

class AnswerAdmin(admin.ModelAdmin):
    list_display=('author','content_bref','create','votes_count','downvotes_count')
    ordering = ["create"]
    fields=('question','author','content','is_active')

admin.site.register(Answer, AnswerAdmin)