from flask import Blueprint, request, jsonify
from external_api_manager import get_teams, get_competitions, get_areas

api_blueprint = Blueprint('api_blueprint', __name__)


@api_blueprint.route("/api/v1/select", methods=['POST'])
def select_operation():
    """
    Api to select the operation
    :return: json based on the operation
    """
    if request.method == "POST":
        body = request.json
        if "operation" in body:
            operation = body['operation'].casefold()
            if operation == "get_teams":
                if "competition_code" in body:
                    data = get_teams(body["competition_code"].upper())
                else:
                    return {"message": "To get the teams, include the param 'competition_code' in  request"}, 200
            elif operation == "get_competitions":
                data = get_competitions()
            elif operation == "get_areas":
                data = get_areas()
            else:
                return {"message": f"{operation} is not a valid operation"}, 200
            return {"data": data}, 200
        else:
            return {"messgae": "Mandatory param not found in request body"}, 200


@api_blueprint.route("/api/v1/team", methods=['POST'])
def get_team_data():
    """
    API to return a team's data
    :return: json of team's data
    """
    if request.method == "POST":
        body = request.json
        if "team_name" in body and "competition_code" in body:
            team = body.get('team_name')
            teamname = team.replace(" ", "").casefold()

            competition_code = body["competition_code"].upper()
            teams_data = get_teams(competition_code=competition_code)
            for item in teams_data:
                club_name = item.get('name').casefold()
                club_name = club_name.replace(" ", "")
                if teamname in club_name:
                    return {"team_data": item}, 200
            return {"message": f"No team name {team} in the given competition"}, 200
        else:
            return {"messgae": "Mandatory param not found in request body!!"}, 200
