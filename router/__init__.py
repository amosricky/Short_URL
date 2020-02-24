from flask import Flask, request, jsonify, redirect
from router import helper

app = Flask(__name__)
conn = helper.getConnection()


@app.route("/shortURL", methods=['POST'])
def shortUrl_request():
    result = {"code": 200, "result": "", "message": ""}

    body = request.json
    if "url" not in body.keys():
        result["code"] = 400
        result["message"] = "[url] not found."
        return jsonify(result), 400

    chkRes = helper.checkUrl(body["url"])
    if chkRes["code"] != 200:
        return jsonify(chkRes), chkRes["code"]

    genSUrlRes = helper.genShortUrl(body["url"], conn)
    return jsonify(genSUrlRes), genSUrlRes["code"]


@app.route('/<path:path>', methods=['GET'])
def shortUrl_redirect(path):
    chkUrlRes = helper.getFullUrl(path, conn)
    if chkUrlRes["code"] != 200:
        return jsonify(chkUrlRes), chkUrlRes["code"]
    else:
        return redirect(chkUrlRes["result"], code=302)


@app.route('/', methods=['GET'])
def default():
    return 'None'