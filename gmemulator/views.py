from django.shortcuts import render
from .forms import FateQuestionForm
from .fate_chart import fate_chart
from .roll import roll_d100


def fate_question(request):
    form = FateQuestionForm(request.POST or None)
    context = {"form": form}
    if request.method == "POST":
        if form.is_valid():
            # do the game logic
            odd = form.cleaned_data["odds"]
            print(odd)
            print(type(odd))
            print(fate_chart)
            chaos_factor = int(form.cleaned_data["chaos_factor"]) - 1
            mini, threshold, maxi = fate_chart.get(odd)[chaos_factor]
            dice = roll_d100()
            if dice <= mini:
                answer = "Exceptional Yes!"
            elif dice <= threshold:
                answer = "Yes"
            elif dice < maxi:
                answer = "No"
            else:
                answer = "Exceptional No!"
            context["roll"] = dice
            context["answer"] = answer

    return render(request, "gmemulator/fate_question.html", context)
