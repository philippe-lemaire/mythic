from django.shortcuts import render

# Create your views here.


def fate_question(request):
    context = {"question": "what time is it?"}
    return render(request, "gmemulator/fate_question.html", context)
