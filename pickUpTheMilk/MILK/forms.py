from django import forms
from django.contrib.auth.models import User
from MILK.models import Item, UserProfile, Group

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    balance = forms.DecimalField(widget=forms.HiddenInput(),initial=0)
    picture = forms.ImageField(required=False)

    class Meta:
        model = UserProfile
        fields = ('balance', 'picture')

# Still in progress. Form to add item to database.
class itemForm(forms.ModelForm):
    itemName = forms.CharField(max_length=128,
                        help_text="Please enter the item name:")

    # Probably want this to be auto generated rather
    # than have the user enter an ID each time...
    ##itemID = forms.IntegerField(widget=forms.HiddenInput(),initial=0)
    class Meta:
        model = Item
        fields = ('itemName',)

class groupForm(forms.ModelForm):
    group = forms.CharField(max_length=128, help_text="Please enter the new group's name:")
    administrator = forms.ModelChoiceField(queryset= UserProfile.objects.all(), widget = forms.HiddenInput(), required = False)

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(groupForm, self).__init__(*args, **kwargs)

    def clean_administrator(self):

        return UserProfile.objects.get(user = self.user)



    class Meta:
        model = Group
        fields = ('group', 'administrator')
