from django import forms


class ContactForm(forms.Form):
    title = forms.CharField()
    full_name = forms.CharField()
    email = forms.EmailField()
    description = forms.CharField(widget=forms.Textarea)


class RegisterForm(forms.Form):
    reg_choice = [("id_options_0", " Patient"), ("id_options_1", " Doctor")]
    fname = forms.CharField()
    lname = forms.CharField()
    uname = forms.CharField()
    email = forms.EmailField()
    pw = forms.PasswordInput()
    cpw = forms.PasswordInput()
    options = forms.ChoiceField(choices=reg_choice, widget=forms.RadioSelect)
