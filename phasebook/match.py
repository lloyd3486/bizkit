import time
from flask import Blueprint

from .data.match_data import MATCHES


bp = Blueprint("match", __name__, url_prefix="/match")


@bp.route("<int:match_id>")
def match(match_id):
    if match_id < 0 or match_id >= len(MATCHES):
        return "Invalid match id", 404

    start = time.time()
    msg = "Match found" if (is_match(*MATCHES[match_id])) else "No match"
    end = time.time()

    return {"message": msg, "elapsedTime": end - start}, 200


def is_match(fave_numbers_1, fave_numbers_2):
    # Removes duplicate from list 2
    fave_numbers_2 = list(set(fave_numbers_2))

    # Returns false if not all numbers in list 2 are in list 1 (size of list 2 != number of matches with list 1)
    if len(fave_numbers_2) != len(set(fave_numbers_1).intersection(fave_numbers_2)):
        return False

    return True
