from .roll import roll_d100

EVENT_FOCUS = {
    5: "Remote Event",
    10: "Ambiguous Event",
    20: "New NPC",
    40: "NPC Action",
    45: "NPC Negative",
    50: "NPC Positive",
    55: "Move Toward A Thread",
    65: "Move Away From A Thread",
    70: "Close A Thread",
    80: "PC Negative",
    85: "PC Positive",
    100: "Current Context",
}


def get_event_focus():
    dice = roll_d100()
    for k in range(dice, 101):
        if k in EVENT_FOCUS:
            return EVENT_FOCUS[k]
