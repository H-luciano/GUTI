# -*- coding: utf-8 -*-


from django import forms

class ModeSelectItForm(forms.Form):

    INDICATIVO = forms.MultipleChoiceField (
        label = 'INDICATIVO',
        choices = [
            ("presente","Presente"),
            ("passato_pr","Passato prossimo"),
            ("imperfetto","Imperfetto"),
            ("tranpassato","Tranpassato prossimo"),
            ("futuro_semp","Futuro semplice"),
            ("futuro_ant","Futuro anterio"),
            ],
        widget = forms.CheckboxSelectMultiple(),
        required=False,
        )

    CONGIUNTIVO = forms.MultipleChoiceField (
        label = 'CONGIUNTIVO',
        choices = [
            ("congiuntivo","Presente"),
            ("congiuntivo_pas","Passato"),
            ("congiuntivo_imp","Imperfetto"),
            ("congiuntivo_trap","Tranpassato prossimo"),
            ],
        widget = forms.CheckboxSelectMultiple(),
        required=False,
        )

    CONDIZIONALE = forms.MultipleChoiceField (
        label = 'CONDIZIONALE',
        choices = [
            ("condizionale","Presente"),
            ("condizionale_pas","Passato"),
            ],
        widget = forms.CheckboxSelectMultiple(),
        required=False
        )

    IMPERATIVO = forms.MultipleChoiceField (
        label = 'IMPERATIVO',
        choices = [
            ("imperativo","Presente"),
            ],
        widget = forms.CheckboxSelectMultiple(),
        required=False
        )

    ARE = forms.MultipleChoiceField (
        label = '',
        choices = [
            ("are_1", "-ARE (1)"),
            ("are_2", "-ARE (2)"),
            ("are_3", "-ARE (3)"),
            ],
        widget = forms.CheckboxSelectMultiple(),
        required=False
        )

    IRE = forms.MultipleChoiceField (
        label = '',
        choices = [
            ("ire_1", "-IRE (1)"),
            ("ire_2", "-IRE (2)"),
            ("ire_3", "-IRE (3)"),
            ],
        widget = forms.CheckboxSelectMultiple(),
        required=False
        )

    ERE = forms.MultipleChoiceField (
        label = '',
        choices = [
            ("ere_1", "-ERE (1)"),
            ("ere_2", "-ERE (2)"),
            ("ere_3", "-ERE (3)"),
            ],
        widget = forms.CheckboxSelectMultiple(),
        required=False
        )

    ALTRI = forms.MultipleChoiceField (
        label = '',
        choices = [
            ("particolari_1", "Particolari (1)"),
            ("particolari_2", "Particolari (2)"),
            ("rre", "-RRE"),
            ("si", "-SI"),
            ],
        widget = forms.CheckboxSelectMultiple(),
        required=False
        )

    PARTICOLARI = forms.MultipleChoiceField (
        label = 'Particolari',
        choices = [
            ("particolari_1", "particolari (1)"),
            ("particolari_2", "particolari (2)"),
            ],
        widget = forms.CheckboxSelectMultiple(),
        required=False
        )
