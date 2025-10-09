from django.forms import ModelForm, Form, IntegerField
from .models import Video

class CreateVideoForm(ModelForm):
    class Meta:
        model = Video
        fields = ['MovieID','MovieTitle','Actor1Name','Actor2Name','DirectorName','MovieGenre','ReleaseYear']

class FindByIDForm(Form):
    MovieID = IntegerField()