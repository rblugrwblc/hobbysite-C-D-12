from django import forms
from .models import Comment, Article, ArticleGallery

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['entry']

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'category', 'entry', 'header_image']

ArticleGalleryFormSet = forms.inlineformset_factory(Article, 
                                                    ArticleGallery, 
                                                    fields=('article_gallery',), 
                                                    extra=3,
                                                    can_delete=False
                                                    )

