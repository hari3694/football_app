from flask import Flask, request
from apis import api_blueprint
app = Flask("__name__")


@app.route("/api/v1/index", methods=['GET'])
def index():
    """
    API to show the index
    :return: json of available functions
    """
    return {"available_functions": ["Get_PL_Teams", "Get_Competetions", "Get_Areas"]}


app.register_blueprint(api_blueprint)


if __name__ == "__main__":
    app.run(debug=True)

"""

flask with selenium


"""