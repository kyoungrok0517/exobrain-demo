from django.contrib import admin
from web.models import *
# Register your models here.

admin.site.register(Question)
admin.site.register(GoldAnswer)
admin.site.register(PredAnswer)
admin.site.register(AnswerCandidate)
admin.site.register(AnswerTriple)
admin.site.register(GraphEdge)
admin.site.register(DecomposedQuestion)
admin.site.register(Tripple)
admin.site.register(QueryCandidate)