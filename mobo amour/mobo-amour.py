from flask import Flask
from flask import render_template,request
from pymongo import MongoClient


app=Flask(__name__)


mongo=MongoClient("mongodb://localhost:27017/")

@app.route('/')
def index():
    return render_template('login.html')
@app.route('/mainpage',methods=['POST'])
def mainpage():
    if(request.method=='POST'):
        log=request.form
        user=log['user']
        passer=log['passer']
        #print(user)
        findpass=mongo.flaskdb.mobologin.find({'usename':user})
        #print(findpass)
        flag=0
        for j in findpass:
            if(j['usename']==user):
                flag=1
                passcheck=j['password']
        if(passcheck==passer):
            return render_template('mainpage.html')
        else:
            return render_template('login.html')
    
@app.route('/sample',methods=['POST'])
def sample():
    return render_template('sample.html')

if __name__=='__main__':
    app.run(debug=True)

