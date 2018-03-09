from django.shortcuts import render
from django.template.response import TemplateResponse
from web.models import *
from exo_web.settings import BASE_DIR
# Create your views here.
import json
import random

def getDis():

    while True:
        x = random.randrange(1,500) - 250
        y = random.randrange(1,500) - 250

        if x*x/1 + y*y/1 <= 250*250:
            break;
    return [x,y]
def demo(req):

    datas = [[0, '---질의---'],
             [214, '무함마드의 출생지이자 이슬람 최고의 성지 [Q214. 정답: 메카, 유형: 추론형-연상추론형]'],
             [738, '1960년대 자메이카의 토속음악이 리듬 앤드 블루스의 영향을 받아 생겨난 음악 [정답: 레게, 유형: 정의형-용어요청형]'],
             [1689, '섀도 캐비닛은 그림자 내각이라는 뜻으로 야당의 최고 지도부를 일컫는 말이다. 이 말이 유래된 국가는 어디일까? [Q1689. 정답: 영국, 유형: 정의형-용어요청형]'],
             [1875, "유럽 4개국 지역협력체인 '비세그라드(Visegrad)' 그룹의 회원국이 아닌 나라는 어디일까? [정답: 루마니아, 유형: 사실관계형-속성값요청형]"],
             [1855, "신문에서 각 나라의 이름을 한자를 써서 약칭으로 표현할 때가 있다. 프랑스의 경우는 '불'이라 한자를, 네덜란드는 '란'이라는 한자를 사용한다. 그렇다면 한자 '더할 가'로 표현하는 나라는 어디일까? [정답: 캐나다, 유형: 사실관계형-속성값요청형]"],
             [1496, '이곳은 미국 매사추세츠 주의 주도로 하버드, MIT 등 다수의 명문대와 명문 고등학교들이 있는 도시이다. 미국을 대표하는 교육도시인 이곳은 어디일까? [Q1496. 정답: 보스턴, 유형: 사실관계형-속성값요청형]'],
             [1246, 'ABO식 혈액형에서 응집반응이 일어나는 응집원이 없는 혈액형은 무엇일까? [정답: O형, 유형: 사실관계형-속성값요청형]'],]
    """
    <option value="1648">이 열매는 대개는 붉은색이지만 드물게 흰색 품종도 있다. 씨방이 발달해 열매가 되는 다른 열매와 달리 꽃받침이 발달한 것으로 씨가 열매 속에 없고 과실의 표면에 깨와 같이 있는데 코끝이 빨개질 때 '이것' 코라고도 부르는 이 열매는 무엇일까? [Q1648. 정답: 딸기, 유형: 정의형-용어요청형]</option>
    <option value="334">조선 후기 명필 김정희의 독특한 서체 [정답: 추사체, 유형: 추론형-연상추론형]</option>
    <option value="3">흰 사슴이 물을 마시던 연못이라는 뜻을 가진 한라산 정상의 화구호 이름 [정답: 백록담, 유형: 정의형-용어요청형]</option>

    """

    qid = req.GET.get('qid', -1)
    questions = Question.objects.all().order_by('id')

    result = {'questions' : questions}
    graph = {"nodes":[], "edges":[]}
    concept_graph = {"nodes":[], "edges":[]}
    if qid != -1:
        question = Question.objects.get(id=qid)
        result['question'] = question
        result['gold_answers'] = question.gold_answers.all()

        gold_texts = [x.text.strip() for x in question.gold_answers.all()]
        candidates = []

        for can in question.candidates.all():
            candidates.append(["{0}".format(can.text.strip()), can.text.strip() in gold_texts])
            # candidates.append(["{0} ({1})".format(can.text.strip(), can.fid), can.text.strip() in gold_texts])

        result['candidates'] = candidates

        # result['decomposed'] = question.decomposed_list.all()

        result['selected_question_id'] = question.id
        result['selected_question_text'] = question.text

        import random


        graph["nodes"].append({'id':'n0', 'label':'Answer', 'x':-250, 'y':0, 'size':11, 'color':'#ffd700'})
        n = 1
        y = -150
        e = 1
        f = False

        for candidate in question.query_candidates.all():
            if candidate.score < 0.000001 and f:
                continue
            f = True
            nid = 'none'
            for node in graph["nodes"]:
                if node['id'] == candidate.r1:
                    nid = candidate.r1
            if nid == 'none':
                pos = getDis()
                graph["nodes"].append({'id':'{}'.format(candidate.r1), 'label':candidate.r1, 'x':0, 'y':pos[1], 'size':9, 'color':'#f00'})
            graph["edges"].append({'id':'e{}'.format(e), 'source':'n0', 'target':'{}'.format(candidate.r1), 'color':'#aaa', 'size':1})
            e += 1

            nid = 'none'
            for node in graph["nodes"]:
                if node['id'] == candidate.e1:
                    nid = candidate.e1
            if nid == 'none':
                pos = getDis()
                graph["nodes"].append({'id':'{}'.format(candidate.e1), 'label':candidate.e1, 'x':250, 'y':pos[1], 'color':'#00f', 'size': 10})
            graph["edges"].append({'id':'e{}'.format(e), 'source':'{}'.format(candidate.e1), 'target':'{}'.format(candidate.r1), 'color':'#aaa','size':1})
            e += 1

            print(candidate.type)
            if candidate.type == 'ERMRT':
                nid = 'none'
                for node in graph["nodes"]:
                    if node['id'] == candidate.r2:
                        nid = candidate.r2
                if nid == 'none':
                    pos = getDis()
                    graph["nodes"].append(
                        {'id': '{}'.format(candidate.r2), 'label': candidate.r2, 'x': 0, 'y': pos[1], 'size': 9,
                         'color': '#f00'})
                graph["edges"].append(
                    {'id': 'e{}'.format(e), 'source': 'n0', 'target': '{}'.format(candidate.r2), 'color': '#aaa',
                     'size': 1})
                e += 1
                graph["edges"].append(
                    {'id': 'e{}'.format(e), 'source': '{}'.format(candidate.e1), 'target': '{}'.format(candidate.r2),
                     'color': '#aaa', 'size': 1})
                e += 1
            elif candidate.type == 'ERMRERT':
                nid = 'none'
                for node in graph["nodes"]:
                    if node['id'] == candidate.r3:
                        nid = candidate.r3
                if nid == 'none':
                    pos = getDis()
                    graph["nodes"].append(
                        {'id': '{}'.format(candidate.r3), 'label': candidate.r3, 'x': 0, 'y': pos[1], 'size': 9,
                         'color': '#f00'})
                graph["edges"].append(
                    {'id': 'e{}'.format(e), 'source': 'n0', 'target': '{}'.format(candidate.r3), 'color': '#aaa',
                     'size': 1})
                e += 1

                nid = 'none'
                for node in graph["nodes"]:
                    if node['id'] == candidate.e2:
                        nid = candidate.e2
                if nid == 'none':
                    pos = getDis()
                    graph["nodes"].append(
                        {'id': '{}'.format(candidate.e2), 'label': candidate.e2, 'x': 250, 'y': pos[1],
                         'color': '#00f', 'size': 10})
                graph["edges"].append(
                    {'id': 'e{}'.format(e), 'source': '{}'.format(candidate.e2), 'target': '{}'.format(candidate.r3),
                     'color': '#aaa', 'size': 1})
                e += 1

                nid = 'none'
                for node in graph["nodes"]:
                    if node['id'] == candidate.r2:
                        nid = candidate.r2
                if nid == 'none':
                    pos = getDis()
                    graph["nodes"].append(
                        {'id': '{}'.format(candidate.r2), 'label': candidate.r2, 'x': 0, 'y': pos[1], 'size': 9,
                         'color': '#f00'})
                graph["edges"].append(
                    {'id': 'e{}'.format(e), 'source': 'n0', 'target': '{}'.format(candidate.r2), 'color': '#aaa',
                     'size': 1})
                e += 1
                graph["edges"].append(
                    {'id': 'e{}'.format(e), 'source': '{}'.format(candidate.e1), 'target': '{}'.format(candidate.r2),
                     'color': '#aaa', 'size': 1})
                e += 1
                graph["edges"].append(
                    {'id': 'e{}'.format(e), 'source': '{}'.format(candidate.e2), 'target': '{}'.format(candidate.r2),
                     'color': '#aaa', 'size': 1})
                e += 1

        # for tripple in question.answer_triples.all():
        #
        #     nid = 'none'
        #     for node in graph["nodes"]:
        #         if node['id'] == tripple.relation:
        #             nid = tripple.relation
        #     if nid == 'none':
        #         graph["nodes"].append({'id':'{}'.format(tripple.relation), 'label':tripple.relation, 'x':0, 'y':y, 'size':9, 'color':'#f00'})
        #     graph["edges"].append({'id':'e{}'.format(e), 'source':'n0', 'target':'{}'.format(tripple.relation), 'color':'#aaa', 'size':1})
        #     n += 1
        #     e += 1
        #     y += 20
        #
        #     nid = 'none'
        #     for node in graph["nodes"]:
        #         if node['id'] == tripple.fid:
        #             nid = tripple.fid
        #     if nid == 'none':
        #         graph["nodes"].append({'id':'{}'.format(tripple.fid), 'label':tripple.text + '(' + tripple.fid + ')', 'x':250, 'y':y, 'size':10, 'color':'#00f'})
        #     graph["edges"].append({'id':'e{}'.format(e), 'source':'{}'.format(tripple.relation), 'target':'{}'.format(tripple.fid), 'color':'#aaa','size':1})
        #     n += 1
        #     e += 1
        #
        #     y += 20

        e = 10000
        for edge in question.graph_edges.all().order_by('?'):
            if e > 11050:
                break
            e1 = edge.entity1
            rel = edge.relation
            e2 = edge.entity2
            nid = 'none'
            for node in concept_graph["nodes"]:
                if node['id'] == e1:
                    nid = e1
            if nid == 'none':
                pos = getDis()
                concept_graph["nodes"].append({'id':'{}'.format(e1), 'label':e1, 'x':pos[0], 'y':pos[1], 'size':2, 'color':'#00f'})
            nid = 'none'
            for node in concept_graph["nodes"]:
                if node['id'] == e2:
                    nid = e2
            if nid == 'none':
                pos = getDis()
                concept_graph["nodes"].append({'id':'{}'.format(e2), 'label':e2, 'x':pos[0], 'y':pos[1], 'size':2, 'color':'#00f'})

            nid = 'none'
            for node in concept_graph["nodes"]:
                if node['id'] == rel:
                    nid = rel
            if nid == 'none':
                pos = getDis()
                concept_graph["nodes"].append({'id':'{}'.format(rel), 'label':rel, 'x':pos[0], 'y':pos[1], 'size':3, 'color':'#f00'})

            concept_graph["edges"].append({'id':'e{}'.format(e), 'source':'{}'.format(e1), 'target':'{}'.format(rel), 'color':'#aaa', 'size':1})
            concept_graph["edges"].append({'id':'e{}'.format(e+1), 'source':'{}'.format(rel), 'target':'{}'.format(e2), 'color':'#aaa', 'size':1})
            e += 2
    else:
        result['selected_question_id'] = -1
        result['selected_question_text'] = '-- 질의 선택 --'

    with open(BASE_DIR + '/web/statics/graph.json', 'w') as f:
        json.dump(graph, f)
    with open(BASE_DIR + '/web/statics/concept_graph.json', 'w') as f:
        json.dump(concept_graph, f)

    response = TemplateResponse(req, 'demo.html', result)

    # print()
    return response
