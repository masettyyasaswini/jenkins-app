from flask import Flask,render_template,request,session,redirect
from pymongo import MongoClient
import smtplib
app = Flask(__name__)

server = smtplib.SMTP(host='smtp.gmail.com',port=587)
cluster = MongoClient('mongodb+srv://jayasrimandava2:jaya@cluster0.vf0ghjh.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')

app.secret_key = "ejfhjk$%^&*9fvbijh"
db = cluster['ysjk']
appointments = db['ops']

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/dashboard')
def dash():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/login',methods=['post'])
def dologin():
    email = request.form['email']
    session['email']= email
    return redirect('/dashboard')

@app.route('/book',methods=['post'])
def book():
    name= request.form['name']
    email = request.form['email']
    date = request.form['date']
    time = request.form['time']
    slot = request.form['slot']
    msg = request.form['message']
    product = request.form['product']
    service  = request.form['service']
    print(name,email,date,time,slot,msg,product,service)
    appointments.insert_one({'email':email,'name':name,'date':date,'time':time,'slot':slot,'product':product,'service':service})
    messsage='''Subject: Booking confirmation \n
    Hai {0} , Thanks for bookin.
    '''.format(name)
    server.starttls()
    server.login('yasaswini.masetty@gmail.com','gdxndsnudeblnxat' )
    server.sendmail('yasaswini.masetty@gmail.com',email,messsage)
    return render_template('index.html',status="Thank you for contacting us will get back to you soon......")

if __name__ == "__main__":
    app.run()
