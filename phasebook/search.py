from flask import Blueprint, request

from .data.search_data import USERS


bp = Blueprint("search", __name__, url_prefix="/search")


@bp.route("")
def search():
    return search_users(request.args.to_dict()), 200


def search_users(args):
    """Search users database

    Parameters:
        args: a dictionary containing the following search parameters:
            id: string
            name: string
            age: string
            occupation: string

    Returns:
        a list of users that match the search parameters
    """

    # Implement search here!
    temp_users = []   

    if not args:
        return USERS

    # Place matches in a temporary list if keys exist
    temp_users.extend([x for x in USERS if "id" in args if x.get("id") == args["id"]])
    temp_users.extend([x for x in USERS if "name" in args if args["name"].lower() in x.get("name").lower()])
    temp_users.extend([x for x in USERS if "age" in args if
                       int(args["age"]) + 1 >= int(x.get("age")) >= int(args["age"]) - 1])
    temp_users.extend([x for x in USERS if "occupation" in args if
                       args["occupation"].lower() in x.get("occupation").lower()])

    # Remove duplicates from the temporary list
    unique_users = []
    [unique_users.append(x) for x in temp_users if x not in unique_users]

    return unique_users
