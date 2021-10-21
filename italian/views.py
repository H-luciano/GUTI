# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import ModeSelectItForm
import random
from . table_it import *


class Italian(TemplateView):


    def __init__(self):
        self.params = {
            'title': 'GUTI! Italiano',
            'result': "",
            'answer': "",
            'subject':'italian/images/none_subject.png',
            'tense': 'italian/images/none_tense.png',
            'mode': "",
            'form': ModeSelectItForm(),
            }

    def get(self, request):
        return render (request, 'italian/main_it.html', self.params)

    def post (self, request):

        global answer, mode_fnl, tense_img_chcd, subject_image, word_fnl, mode_tense_cnddt, words_cnddt

        if "button_question" in request.POST:

            #チェックボタンから候補(mode)選択のリストを作る
            indicativo_chcd = request.POST.getlist('INDICATIVO')
            congiuntivo_chcd = request.POST.getlist('CONGIUNTIVO')
            condizionale_chcd = request.POST.getlist('CONDIZIONALE')
            imperativo_chcd = request.POST.getlist('IMPERATIVO')

            #上記リストを結合
            mode_tense_cnddt = indicativo_chcd + congiuntivo_chcd + condizionale_chcd + imperativo_chcd

            #チェックボタンから候補(word)選択のリストを作る
            are_chcd = request.POST.getlist('ARE')
            ire_chcd = request.POST.getlist('IRE')
            ere_chcd = request.POST.getlist('ERE')
            rre_chcd = request.POST.getlist('ALTRI')
            particolari_chcd = request.POST.getlist('PARTICOLARI')

            #上記リストを結合
            words_cnddt = are_chcd + ire_chcd + ere_chcd + rre_chcd + particolari_chcd

            #選ばれた単語のタイプから単語リストを作る
            #eval関数でwords_cnddt要素の文字列を変数名に変更
            #random.choiceで最終1単語を選ぶ
            words_fnl = []
            for i in words_cnddt:
                words_fnl.extend(eval(i))
            word_fnl = random.choice(words_fnl)

            #最終modeを選ぶ
            mode_tense_fnl = []
            mode_tense_fnl = random.choice(mode_tense_cnddt)

            #tenseの画像を選択
            tense_img_chcd = tense_dict[mode_tense_fnl]

            #modeで必要な文章を作る
            if "congiuntivo" in mode_tense_fnl:
                mode_fnl = "Penso "
            elif "condizionale" in mode_tense_fnl:
                mode_fnl = "In queste condizioni, "
            elif "imperativo" in mode_tense_fnl:
                mode_fnl = " ! "
            else:
                mode_fnl = ""

            #最終subjectを作る
            subject_fnl = random.choice(subject)
            subject_image = subject_dict[subject_fnl]

            #Answerを作る
            answer_list = table[word_fnl , subject_fnl]
            answer_dict = dict(zip(mode, answer_list))
            answer = answer_dict.get(mode_tense_fnl)

            #表示
            self.params['subject'] = subject_image
            self.params['result'] = word_fnl
            self.params['mode'] = mode_fnl
            self.params['tense'] = tense_img_chcd
            self.params['form'] = ModeSelectItForm(request.POST)


        if "button_answer" in request.POST:

            self.params['answer'] = answer
            self.params['mode'] = mode_fnl
            self.params['tense'] = tense_img_chcd
            self.params['subject'] = subject_image
            self.params['result'] = word_fnl
            self.params['form'] = ModeSelectItForm(request.POST)

        return render(request,'italian/main_it.html', self.params)






class ItalianList(Italian):

    def __init__(self):
        self.params = {
            'title': 'GUTI! Italiano/List',
        }

    def get(self, request):
        return render (request, 'italian/list_it.html', self.params)
