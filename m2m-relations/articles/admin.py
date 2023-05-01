from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, Scope, Tag

class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        counter = 0
        for form in self.forms:
            if form.cleaned_data.get('is_main'):
                counter += 1
        if counter > 1:    
            raise ValidationError('Укажите один основной раздел')
        elif counter == 0:
            raise ValidationError('Основной раздел не указан')
        return super().clean()

class ScopeInLine(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset
    extra = 3

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'text', 'published_at', 'image']
    inlines = [ScopeInLine,]

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']




