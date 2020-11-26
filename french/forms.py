from django import forms

class ModeSelectFrForm(forms.Form):

    INDICATIF = forms.MultipleChoiceField (
        label = 'INDICATIF',
        choices = [
            ("Indicatif Présent","Présent"),
            ("Indicatif Passé composé","Passé composé"),
            ("Indicatif Impafait","Impafait"),
            ("Indicatif Plus-que-parfait","Plus-que-parfait"),
            ("Indicatif Futur simple","Futur simple"),
            ],
        widget = forms.CheckboxSelectMultiple(),
        required=False,
        )

    SUBJONCTIF = forms.MultipleChoiceField (
        label = 'SUBJONCTIF',
        choices = [
            ("Subjonctif Présent","Présent"),
            ("Subjonctif Passé","Passé"),
            ],
        widget = forms.CheckboxSelectMultiple(),
        required=False,
        )

    CONDITIONNEL = forms.MultipleChoiceField (
        label = 'CONDITIONNEL',
        choices = [
            ("Conditionel Présent","Présent"),
            ("Conditionel Passé","Passé"),
            ],
        widget = forms.CheckboxSelectMultiple(),
        required=False
        )

    IMPÉRATIF = forms.MultipleChoiceField (
        label = 'IMPÉRATIF',
        choices = [
            ("Impératif","Présent"),
            ],
        widget = forms.CheckboxSelectMultiple(),
        required=False
        )

    ER = forms.MultipleChoiceField (
        label = '-ER',
        choices = [
            ("er_1", "(1)"),
            ("er_2", "(2)"),
            ("er_3", "(3)"),
            ],
        widget = forms.CheckboxSelectMultiple(),
        required=False
        )

    IR = forms.MultipleChoiceField (
        label = '-IR',
        choices = [
            ("ir_1", "(1)"),
            ("ir_2", "(2)"),
            ("ir_3", "(3)"),
            ],
        widget = forms.CheckboxSelectMultiple(),
        required=False
        )

    RE = forms.MultipleChoiceField (
        label = '-RE',
        choices = [
            ("re_1", "(1)"),
            ("re_2", "(2)"),
            ("re_3", "(3)"),
            ],
        widget = forms.CheckboxSelectMultiple(),
        required=False
        )

    Illéguliers = forms.MultipleChoiceField (
        label = 'Illéguliers',
        choices = [
            ("Illéguliers", "(1)"),
            ("Illéguliers_2", "(2)"),
            ("Illéguliers_3", "(3)"),
            ],
        widget = forms.CheckboxSelectMultiple(),
        required=False
        )
