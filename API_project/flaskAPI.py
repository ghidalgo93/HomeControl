from flask import request #, url_for (didnt need this yet for original program)
from flask_api import FlaskAPI #, status, exceptions (didnt need this yet for original program)
import Plants
import Lights

app = FlaskAPI(__name__)



@app.route("/", methods=['GET', 'POST'])
def get_request():
    if request.method == 'POST':
        payload = request.get_json(silent=True)
        if 'plants' in payload:
            plants = Plants.Plants(payload)
            plants.handle_plants()
        if 'lights' in payload:
            lights = Lights.Lights(payload)
            lights.handle_lights()
        else:
            print ('nothing in the payload')

        #print ("Got data: " + str(payload))
        return {'succeeded with query' : str(payload)}

if __name__ == "__main__":
    app.run(debug=True)
