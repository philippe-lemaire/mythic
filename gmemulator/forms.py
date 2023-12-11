from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms

odd_labels = (
    (1, "Certain"),
    (2, "Nearly Certain"),
    (3, "Very Likely"),
    (4, "Likely"),
    (5, "50/50"),
    (6, "Unlikely"),
    (7, "Very Unlikely"),
    (8, "Nearly Impossible"),
    (9, "Impossible"),
)


class FateQuestionForm(forms.Form):
    odds = forms.ChoiceField(
        label="What are the odds?", choices=odd_labels, required=True, initial=5
    )
    chaos_factor = forms.IntegerField(
        label="Chaos Factor", min_value=1, max_value=9, initial=5
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.form_action = "gmemulator:fate_question"
        self.helper.add_input(Submit("submit", "Submit"))
        self.helper.form_class = "blueForms"
