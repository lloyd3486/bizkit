from flask import Blueprint, request
from .data.schedule_data import SCHEDULES

bp = Blueprint("schedule", __name__, url_prefix="/schedule")


@bp.route("<string:user_id>")
def schedule(user_id):
    match = False
    x = {}
    for c, temp_user in enumerate(SCHEDULES):
        if temp_user["user_id"] == user_id:
            match = True
            x = c

    if not match:
        #create user
        SCHEDULES.append({"user_id": user_id, "schedules": []})
        x = len(SCHEDULES) - 1

    #add schedule
    sched = f"{request.form.get('start')} - {request.form.get('end')}"
    SCHEDULES[x]["schedules"].append(sched)

    return SCHEDULES

