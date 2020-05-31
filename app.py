import sys
import os
import flask
from flask import jsonify
from datetime import datetime

app = flask.Flask(__name__)

@app.route("/")
def entry_point():
    return flask.render_template('index.html')

@app.route("/upload", methods=["POST"])
def upload():
    print("Total Content-Length: " + flask.request.headers['Content-Length'])
    fileFullPath = os.path.join("/home/joao/source/pythonStreamingUpload/files", "teste{}.mp4".format(datetime.now().strftime("%m%d%Y%H%M%S")))
    messagingFullPath = os.path.join("/home/joao/source/pythonStreamingUpload/messaging", "teste{}.txt".format(datetime.now().strftime("%m%d%Y%H%M%S")))

    chunk_size = 4096
    try:
        with open(fileFullPath, "wb") as f:
            reached_end = False
            while not reached_end:
                chunk = flask.request.stream.read(chunk_size)
                if len(chunk) == 0:
                    reached_end = True
                    with open(messagingFullPath, "w+") as msg:
                        msg.write(fileFullPath)
                        msg.flush()    
                else:
                    sys.stdout.write(".")
                    sys.stdout.flush()
                    f.write(chunk)
                    f.flush()
                    print("wrote chunk of {}".format(len(chunk)))
    except OSError as e:
        result = jsonify(success=False)
        result.status_code = 500
        return result

    result = jsonify(success=True)
    result.status_code = 200
    return result

if __name__ == "__main__":
    app.run(port=8000)