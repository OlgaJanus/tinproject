from django import forms

from .models import Post
from .models import Category
from .models import Difficulty

class PostForm(forms.ModelForm):

    category = forms.ModelMultipleChoiceField(queryset=Category.objects.all())
    difficulty = forms.	ModelChoiceField(queryset=Difficulty.objects.all())

    class Meta:
        model = Post
        fields = ('title', 'text','difficulty', 'category',)

class DifficultyForm(forms.ModelForm):
    class Meta:
        model = Difficulty
        fields = ('name',)


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)
