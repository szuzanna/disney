from django import forms

# iterable
COLOUR_CHOICES = (
    ("pink", "pink"),
    ("blue", "blue"),
    ("yellow", "yellow"),
    ("green", "green"),
)

PET_CHOICES = (
    ("frog", "frog"),
    ("tiger", "tiger"),
    ("mouse", "mouse"),
    ("horse", "horse"),
)

VALUES_CHOICES = (
    ("love", "love"),
    ("family", "family"),
    ("friends", "friends"),
    ("freedom", "freedom"),
)

FEATURE_CHOICES = (
    ("kind", "kind"),
    ("brave", "brave"),
    ("caring", "caring"),
    ("loyal", "loyal"),
)

FRIEND_CHOICES = (
    ("angus", "Angus"),
    ("chip", "Chip"),
    ("flounder", "Flounder"),
    ("rajah", "Rajah"),
)


# creating a form
class GeeksForm(forms.Form):
    colour_field = forms.ChoiceField(choices=COLOUR_CHOICES,widget=forms.RadioSelect, label="What's your favourite colour?")
    pet_field = forms.ChoiceField(choices=PET_CHOICES, widget=forms.RadioSelect,
                                     label="What's your favourite pet?")
    values_field = forms.ChoiceField(choices=VALUES_CHOICES, widget=forms.RadioSelect,
                                     label="What's the most important for you?")
    feature_field = forms.ChoiceField(choices=FEATURE_CHOICES, widget=forms.RadioSelect,
                                  label="Which best describe you?")
    friends_field = forms.ChoiceField(choices=FRIEND_CHOICES, widget=forms.RadioSelect,
                                      label="With whom you would most like to be friends?")