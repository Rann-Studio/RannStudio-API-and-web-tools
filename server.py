import flask
import json
import api.bmkg as bmkg

app = flask.Flask(__name__)
app.config["JSONIFY_PRETTYPRINT_REGULAR"] = True
app.config["JSON_SORT_KEYS"] = False


###############################################################################
#                                   INDEX API                                 #
###############################################################################
@app.route(rule='/', methods=['GET'])
def index():
    with open('index.json', 'r') as data:
        return flask.jsonify(json.load(data)), 200


###############################################################################
#                              API BMKG [ GEMPA ]                             #
###############################################################################
@app.route(rule='/bmkg/gempa/terbaru/', methods=['GET'])
def gempa_terbaru():
    data = bmkg.BMKG().gempaTerbaru()
    return flask.jsonify(data), 200

@app.route(rule='/bmkg/gempa/15-terbaru/', methods=['GET'])
def gempa_terbaru_15():
    data = bmkg.BMKG().gempaTerbaru15()
    return flask.jsonify(data), 200

@app.route(rule='/bmkg/gempa/15-terbaru-5-magnitude/', methods=['GET'])
def gempa_terbaru_15_m5():
    data = bmkg.BMKG().gempaTerbaru15_M5()
    return flask.jsonify(data), 200

@app.route(rule='/bmkg/gempa/shakemap/<name>/', methods=['GET'])
def shakemap(name):
    data = bmkg.BMKG().getShakemap(name)
    return flask.Response(data, mimetype='image/png')


###############################################################################
#                              API BMKG [ CUACA ]                             #
###############################################################################
@app.route(rule='/bmkg/cuaca/<provinsi>/', methods=['GET'])
def cuaca(provinsi):
    status, data = bmkg.BMKG().cuaca(provinsi)
    if status == 200:
        return flask.Response(data, mimetype='text/xml')
    else:
        provinsi = ["Aceh", "Bali", "BangkaBelitung", "Banten", "Bengkulu", "DIYogyakarta", "DKIJakarta", "Gorontalo", "Jambi", "JawaBarat", "JawaTengah", "JawaTimur", "KalimantanBarat", "KalimantanSelatan", "KalimantanTengah", "KalimantanTimur", "KalimantanUtara", "KepulauanRiau", "Lampung", "Maluku", "MalukuUtara", "NusaTenggaraBarat","NusaTenggaraTimur", "Papua", "PapuaBarat", "Riau", "SulawesiBarat", "SulawesiSelatan", "SulawesiTengah", "SulawesiTenggara", "SulawesiUtara", "SumateraBarat", "SumateraSelatan", "SumateraUtara", "Indonesia"]
        return flask.jsonify({
            "status": "error",
            "message": "Provinsi tidak ditemukan",
            "provinsi": provinsi
        }), 404
        

###############################################################################
#                                API BOT TULIS                                #
###############################################################################
@app.route(rule='/tulis/', methods=['GET'])
def tulis():
    return flask.jsonify({
        "status": "error",
        "message": "Sedang dalam pengembangan"
    }), 410


###############################################################################
#                                MENJALANKAN API                              #
###############################################################################
if __name__ == "__main__":
    app.run(host="localhost", port=5000)