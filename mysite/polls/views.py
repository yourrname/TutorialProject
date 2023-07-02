from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index")


def detail(request, pk):
    return HttpResponse(f"You're looking at question {pk}")


def results(request, question_id):
    response = "You're looking at the results of question"
    return HttpResponse(f"{response} {question_id}")


def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}")
