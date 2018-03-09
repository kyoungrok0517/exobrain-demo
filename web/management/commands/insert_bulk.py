from django.core.management.base import BaseCommand, CommandError
from web.models import *
import ast, json

class Command(BaseCommand):
    help = 'Insert bulk data'

    def handle(self, *args, **options):
        pass
        # gold answers
        # with open('./web/temp_data/webquestions-predictions-gold.txt') as f:
        #     for line in f:
        #         question_text, answer_list = line.split('\t')
        #
        #         if not Question.objects.filter(text=question_text).exists():
        #             question = Question.objects.create(text=question_text)
        #         else:
        #             continue # if not first
        #             question = Question.objects.get(text=question_text)
        #
        #         answer_texts = [answer.text for answer in question.gold_answers.all()]
        #         answer_list = ast.literal_eval(answer_list)
        #
        #         for answer_text in answer_list:
        #             if answer_text not in answer_texts:
        #                 GoldAnswer.objects.create(text=answer_text, question=question)
        #
        #         self.stdout.write(self.style.SUCCESS('Successfully insert question {}'.format(question.pk)))
        #
        # # pred answers
        # with open('./web/temp_data/joint_inference.predicted.final') as f:
        #     for line in f:
        #         question_text, answer_list = line.split('\t')
        #
        #         if not Question.objects.filter(text=question_text).exists():
        #             question = Question.objects.create(text=question_text)
        #         else:
        #             continue # if not first
        #             question = Question.objects.get(text=question_text)
        #
        #         answer_texts = [answer.text for answer in question.pred_answers.all()]
        #         answer_list = ast.literal_eval(answer_list)
        #
        #         for answer_text in answer_list:
        #             if answer_text not in answer_texts:
        #                 PredAnswer.objects.create(text=answer_text, question=question)
        #
        #         self.stdout.write(self.style.SUCCESS('Successfully insert predicted answer {}'.format(question.pk)))
        #
        # # decomposed
        # with open('./web/temp_data/test.questions.decomposed') as f:
        #     for line in f:
        #
        #         data = json.loads(line)
        #
        #         question_text = data['question']
        #         decomposed_list = data['decomposed']
        #
        #         if not Question.objects.filter(text=question_text).exists():
        #             question = Question.objects.create(text=question_text)
        #         else:
        #             continue # if not first
        #             question = Question.objects.get(text=question_text)
        #
        #         decomposed_text_list = [answer.text for answer in question.decomposed_list.all()]
        #
        #         for decomposed_text in decomposed_list:
        #             if decomposed_text not in decomposed_text_list:
        #                 DecomposedQuestion.objects.create(text=decomposed_text, question=question)
        #
        #         self.stdout.write(self.style.SUCCESS('Successfully insert Decomposed Question {}'.format(question.pk)))
        #
        # # pos tagging
        # with open('./web/temp_data/pos.test.questions.decomposed.txt') as f:
        #     for line in f:
        #
        #         data = json.loads(line)
        #
        #         question_text = data['question']
        #         decomposed_list = data['decomposed']
        #
        #         if not Question.objects.filter(text=question_text).exists():
        #             question = Question.objects.create(text=question_text)
        #         else:
        #             question = Question.objects.get(text=question_text)
        #
        #         idx = 0
        #         for decomposed_question in question.decomposed_list.all():
        #             decomposed_question.pos_tagging = decomposed_list[idx]
        #             decomposed_question.save()
        #             idx = idx + 1
        #
        #         self.stdout.write(self.style.SUCCESS('Successfully insert Decomposed Question {}'.format(question.pk)))

        # # tripple
        # with open('./web/temp_data/jointInference.result') as f:
        #     for line in f:
        #
        #         data = json.loads(line)
        #
        #         question_text = data['question']
        #         # decomposed_list = data['decomposed']
        #
        #         if not Question.objects.filter(text=question_text).exists():
        #             question = Question.objects.create(text=question_text)
        #         else:
        #             question = Question.objects.get(text=question_text)
        #
        #         Tripple.objects.create(question=question, relation=data['pred'], subject_text=data['subjSurface'], subject_id=data['subj'])
        #
        #         self.stdout.write(self.style.SUCCESS('Successfully insert Tripple {}'.format(question.pk)))