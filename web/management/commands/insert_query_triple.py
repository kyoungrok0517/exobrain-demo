from django.core.management.base import BaseCommand, CommandError
from web.models import *
import codecs
import ast, json

class Command(BaseCommand):
    help = 'Insert bulk data'

    def handle(self, *args, **options):
        pass

        # list = GoldAnswer.objects.all()
        # for a in list:
        #     a.delete()
        #     self.stdout.write(self.style.SUCCESS('delte candidate {}'.format(a.pk)))
        for i in list(range(0,2032)):
            question = Question.objects.get(id=i+1)
            with codecs.open('./web/temp_data/version4/{0}/one_hop_triples'.format(i), 'r', 'utf-8') as f:
                bulk_list = []
                for line in f:
                    if line == '':
                        break
                    try:
                        e1_id, relation, e2_id, e1_text, e2_text = line.split('\t')
                        if e1_id == e1_text or e2_id == e2_text.strip():
                            continue
                        e1 = '{0} ({1})'.format(e1_text,e1_id)
                        e2 = '{0} ({1})'.format(e2_text,e2_id)
                        candidate = GraphEdge(question=question,entity1=e1,relation=relation, entity2=e2)
                        bulk_list.append(candidate)
                    except:
                        pass

                if len(bulk_list) > 0:
                    GraphEdge.objects.bulk_create(bulk_list)
                    # self.stdout.write(self.style.SUCCESS('Successfully insert candiate {}'.format(question.pk)))
                else:
                    pass
                    # self.stdout.write(self.style.SUCCESS('Already insert candiate {}'.format(question.pk)))
        # for i in list(range(0,2032)):
        #     question = Question.objects.get(id=i+1)
        #     with codecs.open('./web/temp_data/outputs/{0}/weighted_query_triples'.format(i), 'r', 'utf-8') as f:
        #         bulk_list = []
        #         for line in f:
        #             if line == '':
        #                 break
        #             try:
        #                 _, fid, text, relation, score = line.split('\t')
        #                 candidate = AnswerTriple(question=question,fid=fid,text=text, relation=relation, score=score)
        #                 bulk_list.append(candidate)
        #             except:
        #                 pass
        #
        #         if len(bulk_list) > 0:
        #             AnswerTriple.objects.bulk_create(bulk_list)
        #             self.stdout.write(self.style.SUCCESS('Successfully insert candiate {}'.format(question.pk)))
        #         else:
        #             self.stdout.write(self.style.SUCCESS('Already insert candiate {}'.format(question.pk)))
        #     with codecs.open('./web/temp_data/version4/{0}/psm.cut.candidates'.format(i), 'r', 'utf-8') as f:
        #         bulk_list = []
        #         for line in f:
        #             if line == '':
        #                 break
        #             try:
        #                 _, fid, text, _ = line.split('\t')
        #                 candidate = AnswerCandidate(question=question,fid=fid,text=text)
        #                 bulk_list.append(candidate)
        #             except:
        #                 pass
        #
        #         if len(bulk_list) > 0:
        #             AnswerCandidate.objects.bulk_create(bulk_list)
        #             # self.stdout.write(self.style.SUCCESS('Successfully insert candiate {}'.format(1)))
        #         else:
        #             pass
        #             # self.stdout.write(self.style.SUCCESS('Already insert candiate {}'.format(1)))

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