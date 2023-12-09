from django.shortcuts import render
from .forms import FateQuestionForm

# Create your views here.


def fate_question(request):
    form = FateQuestionForm(request.POST or None)
    context = {"form": form}
    if request.method == "POST":
        if form.is_valid():
            # do the game logic
            pass

    return render(request, "gmemulator/fate_question.html", context)
