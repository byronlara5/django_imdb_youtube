from django import forms
from comment.models import Comment

class CommentForm(forms.ModelForm):
	body = forms.CharField(widget=forms.Textarea(attrs={'class': 'materialize-textarea'}), required=False)

	class Meta:
		model = Comment
		fields = ('body',)