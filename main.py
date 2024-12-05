import requests 
from flask import Flask,render_template,url_for,redirect,request,jsonify 

app = Flask(__name__)


@app.route("/")
def index():

      return render_template("index.html")
@app.route("/assistant_chat",methods=['POST','GET'])
def chat_mmai():
       requestdat = request.get_json(force=True)
       email = requestdat.get("email")
       command = requestdat.get("command") 
       reqdat = requests.post("http://192.168.50.4:7795/components_request",json={"email":email,"command":command}).json()
       return jsonify(reqdat)
if __name__ == "__main__":

      app.run(debug=True,threaded=True,host="0.0.0.0",port=5794)
