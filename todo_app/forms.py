from django import forms


class CreateTodoForm(forms.Form):
    text = forms.CharField(
        max_length=30,
    )
    description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'rows': 3,
                'cols': 40,
            }
        ),
    )
    is_done = forms.BooleanField(
        required=False
    )

    bots_catcher = forms.CharField(
        widget=forms.HiddenInput(),
        required=False
    )

    def clean_bots_catcher(self):
        value = self.cleaned_data['bots_catcher']
        if value:
            raise forms.ValidationError('You are a bot')
