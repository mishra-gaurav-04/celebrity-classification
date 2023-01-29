from flask import request,jsonify,Flask
import util

app = Flask(__name__)

@app.route('/classify-image',methods=['GET','POST'])
def classifyImage():
    return "hi"

if __name__ == "__main__":
    app.run(port=5000)