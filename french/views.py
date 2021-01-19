# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import ModeSelectFrForm
import random
from . table import *

global candidate_dict, mode_cnddt, words_cnddt, tense_dict, tense_img_chcd, mode_fnl, subject, table, mode

mode_tense_cnddt = []
words_cnddt = []

class FrenchSetView(TemplateView):

    def __init__(self):
        self.params = {
            'title': 'GUTI! Français/Set',
            'form': ModeSelectFrForm(),
            'result': None,
            'word': None,
        }

    def get(self, request):
        return render (request, 'french/set_fr.html', self.params)

    def post (self, request):

        global cnadidate_mode, mode_tense_cnddt, words_cnddt

        #チェックボタンから候補(mode)選択のリストを作る
        indicatif_chcd = request.POST.getlist('INDICATIF')
        subjontif_chcd = request.POST.getlist('SUBJONCTIF')
        conditionel_chcd = request.POST.getlist('CONDITIONNEL')

        #上記リストを結合
        mode_tense_cnddt = indicatif_chcd + subjontif_chcd + conditionel_chcd

        #チェックボタンから候補(word)選択のリストを作る
        er_chcd = request.POST.getlist('ER')
        ir_chcd = request.POST.getlist('IR')
        re_chcd = request.POST.getlist('RE')
        Illég_chcd = request.POST.getlist('Illéguliers')

        #上記リストを結合
        words_cnddt = er_chcd + ir_chcd + re_chcd + Illég_chcd


        #フォームとしてhtmlで表示させる
        self.params['result'] = mode_tense_cnddt
        self.params['word'] = words_cnddt
        self.params['form'] = ModeSelectFrForm(request.POST)

        return render(request,'french/set_fr.html', self.params)



class FrenchQuestion(FrenchSetView):

    def __init__(self):
        self.params = {
            'title': 'GUTI! Français/Practice',
            'result': "",
            'answer': "",
            'subject':'french/images/none_subject.png',
            'tense': 'french/images/none_tense.png',
            'mode': "",
        }

    def get(self, request):
        return render (request, 'french/main_fr.html', self.params)

    def post(self, request):

        global question_fr, answer_fr, mode_tense_cnddt, words_cnddt, tense_dict, tense_img_chcd, mode_fnl, subject_dict, subject_image, answer, answer_list, answer_dict, mode, word_fnl


        if "button_question" in request.POST:

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
            if "Subjonctif" in mode_tense_fnl:
                mode_fnl = "Il faut "
            elif "Conditionel" in mode_tense_fnl:
                mode_fnl = "Si c'était ça, "
            elif "Impératif" in mode_tense_fnl:
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


        if "button_answer" in request.POST:

            self.params['answer'] = answer
            self.params['mode'] = mode_fnl
            self.params['tense'] = tense_img_chcd
            self.params['subject'] = subject_image
            self.params['result'] = word_fnl

        return render(request,'french/main_fr.html', self.params)


class FrenchList(FrenchSetView):

    def __init__(self):
        self.params = {
            'title': 'GUTI! Français/List',
        }

    def get(self, request):
        return render (request, 'french/list_fr.html', self.params)
