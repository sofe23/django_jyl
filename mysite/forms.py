from .models import Comment, MainContent
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)


class ImageCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content', 'image']  # 'image' 필드를 추가

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['content'].widget.attrs['placeholder'] = '내용을 입력해주세요.'


class MainContentForm(forms.ModelForm):
    class Meta:
        model = MainContent
        fields = ['title', 'content', 'main_image']
