from django.shortcuts import render
from .forms import FateQuestionForm
from .fate_chart import fate_chart
from .roll import roll_d100


def fate_question(request):
    form = FateQuestionForm(request.POST or None)
    context = {"form": form, "event": ""}
    if request.method == "POST":
        if form.is_valid():
            # do the game logic
            odd = form.cleaned_data["odds"]
            chaos_factor = int(form.cleaned_data["chaos_factor"])
            mini, threshold, maxi = fate_chart.get(odd)[chaos_factor - 1]
            dice = roll_d100()
            # just for testing

            if dice <= mini:
                answer = "Exceptional Yes!"
            elif dice <= threshold:
                answer = "Yes"
            elif dice < maxi:
                answer = "No"
            else:
                answer = "Exceptional No!"
            # check for event

            if dice > 10 and len(set(str(dice))) == 1 and dice % 10 <= chaos_factor:
                context["event"] = "Random Event"
            context["roll"] = dice
            context["answer"] = answer

    return render(request, "gmemulator/fate_question.html", context)
