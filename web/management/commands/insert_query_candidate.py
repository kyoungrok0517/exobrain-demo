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
            with codecs.open('./web/temp_data/outputs/{0}/query_candidates'.format(i), 'r', 'utf-8') as f:
                bulk_list = []
                for line in f:
                    if line == '':
                        break
                    try:
                        l1 = line.strip().split('\t')
                        question.answer_type = l1[1]
                        question.save()

                        e1,e2,r1,r2,r3 = '','','','',''
                        type = l1[2]

                        e1 = '{0}({1})'.format(l1[4],l1[3])
                        r1 = l1[5]
                        if type == 'ERT':
                            pass
                        elif type == 'ERMRT':
                            r2 = l1[6]
                        elif type == 'ERMRERT':
                            r2 = l1[6]
                            e2 = '{0}({1})'.format(l1[8],l1[7])
                            r3 = l1[9]

                        score = float(l1[-1])

                        candidate = QueryCandidate(question=question,type=type, e1=e1, e2=e2, r1=r1, r2=r2, r3=r3, score=score)
                        bulk_list.append(candidate)
                    except Exception as e:
                        print(e)
                        pass

                if len(bulk_list) > 0:
                    QueryCandidate.objects.bulk_create(bulk_list)
                    self.stdout.write(self.style.SUCCESS('Successfully insert candiate {}'.format(question.pk)))
                else:
                    self.stdout.write(self.style.SUCCESS('Already insert candiate {}'.format(question.pk)))
