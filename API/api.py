from flask import Flask, request, jsonify
import Utilities as utils

app = Flask(__name__)

@app.route('/api/convertkm')
def convertKm():
    try:
        value = float(request.args['value'])
        type = int(request.args['type'])

        if value != None:
            match type:
                case 1:
                    return [int(utils.convertToMeter(value)[0])]
                case 2:
                    return [int(utils.convertToKilogram(value)[0])]
                case 3:
                    return [int(utils.convertToPounds(value)[0])]
    except:
        return 0