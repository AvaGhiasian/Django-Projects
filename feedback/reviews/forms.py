from django import forms
from .models import Review


# class ReviewForm(forms.Form):
#     user_name = forms.CharField(label="Your Name", max_length=100, error_messages={
#         "required": "Your name must not be empty!",
#         "max_length": "Please enter a shorter name!"
#     })
#     review_text = forms.CharField(
#         label="Your Feedback", widget=forms.Textarea, max_length=500)
#     rating = forms.IntegerField(label="Your Rating", min_value=1, max_value=5)

""" here is a better approach:
instead of inheriting from forms.Form
there is a connection bcs it is a data that we fetch, will end up in the database.
So, django can create a model based on our Model.
so here is a better form:
django will automatically takes all model fields & infer proper HTML inputs for those fields
and gives us preconfigured form based on our model
"""


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review  # pointing at Review, This connects Review Form to Review Model
        # fields = ['user_name', 'review_text', 'rating'] : which fields from models should be part of the form
        fields = "__all__"
        exclude = ['owner_comment'] # fields that wants not to be included
        labels = {
            "user_name" : "Your Name",
            "review_text" : "Your Feedback",
            "rating": "Your Rating"
        }
        error_messages = {
            "user_name": {
                "required": "Your name must not be empty!",
                "max_length": "Please enter a shorter name!"
            }
        }