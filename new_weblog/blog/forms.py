from django import forms

from blog.models import Comment, Post


class TicketForm(forms.Form):
    SUBJECT_CHOICES = (
        ('پیشنهاد', 'پیشنهاد'),
        ('انتقاد', 'انتقاد'),
        ('گزارش مشکل', 'گزارش'),
    )
    message = forms.CharField(widget=forms.Textarea, required=True)
    name = forms.CharField(max_length=250, required=True)
    email = forms.EmailField(max_length=11, required=True)
    phone = forms.CharField(required=True)
    subject = forms.ChoiceField(choices=SUBJECT_CHOICES, required=True)

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if phone:
            if not phone.isnumeric():
                raise forms.ValidationError("شماره تلفن صحیح وارد نشده است!")
            else:
                return phone


class CommentForm(forms.ModelForm):
    def clean_name(self):
        name = self.cleaned_data['name']
        if name:
            if len(name) < 3:
                raise forms.ValidationError("نام کوتاه است")
            else:
                return name

    class Meta:
        model = Comment
        fields = ['name', 'body']
        widgets = {
            'body': forms.TextInput(attrs={
                'placeholder': 'متن',
                'class': 'form-control'
            }),
            'name': forms.TextInput(attrs={
                'placeholder': 'نام',
                'class': 'form-control'
            }),
        }


class SearchForm(forms.Form):
    query = forms.CharField()


class CreatePostForm(forms.ModelForm):
    image1 = forms.ImageField(label="تصویر اول")
    image2 = forms.ImageField(label="تصویر دوم")
    class Meta:
        model = Post
        fields = ['title', 'content', 'reading_time']