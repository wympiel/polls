from django.http import HttpResponse


def index(request):
    return HttpResponse("Cześć! Jesteś na stronie głównej aplikacji ankiety.")

def detail(request, question_id):
    return HttpResponse('Szukasz pytania %s.' % question_id)


