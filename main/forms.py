from django import forms

class YesNoForm(forms.Form):
    def __init__(self, questions, *args, **kwargs):
        super(YesNoForm, self).__init__(*args, **kwargs)

        for idx, question in enumerate(questions):
            self.fields[f"question_{idx}"] = forms.ChoiceField(
                label=question,
                choices=[("yes", "Yes"), ("no", "No")],
                widget=forms.RadioSelect(),
            )
