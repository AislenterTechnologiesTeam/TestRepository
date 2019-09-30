from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from model import *

app =Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

#//////////public////////////////

@app.route('/pindex')
def pindex():
    return render_template("p_index.html")


@app.route('/')
def layout():
    return render_template("p_layout.html")    

#/////////////////////staff//////////////////


@app.route('/cusform', methods=['POST', 'GET'])
def cusform():
    if request.method == 'POST':
        print("Hello....")
        customer_name = request.form['name']
        customer_adhar = request.form['adhar']
        customer_dob = stringtodate(request.form['dob'])
        customer_mobile = request.form['mobile']
        customer_policyname = request.form['policyname']
        customer_amount = request.form['amount']
        customer_policydate = stringtodate(request.form['policydate'])
        customer_policyduration = stringtodate(request.form['policyduration'])
        customer_agencycode = request.form['agencycode']
        customer_gender = request.form['gender']
        customer_address = request.form['address']
        new_customer = Customer(name=customer_name,adhar=customer_adhar,dob=customer_dob,mobile=customer_mobile,policy_name=customer_policyname,amount=customer_amount,policydate=customer_policydate,policyduration=customer_policyduration,agencycode=customer_agencycode,gender=customer_gender,address=customer_address)
        try:
            db.session.add(new_customer)
            db.session.commit()
            return redirect('/scusview')
        except Exception as e:
            print(e)
            return 'There was an issue adding your task'  
    else:
        return render_template('s_addcustomer.html')


@app.route('/smeetview')
def smeetview():
    return render_template("s_meetingview.html")    
    

@app.route('/details')
def staff():
    return render_template("s_layout.html")


@app.route('/sindex')
def sindex():
    return render_template("s_index.html")


@app.route('/meet')
def schedule():
    return render_template("s_meeting.html")


@app.route('/policy')
def policy():
    return render_template("s_addpolicy.html")


@app.route('/attend')
def attendance():
    return render_template("s_attendance.html")


@app.route('/comp')
def comp():
    return render_template("s_competition.html")


@app.route('/spolicyview')
def spolicyview():
    return render_template("s_policyview.html")


@app.route('/scusview')
def scusview():
    customers = Customer.query.all()
    return render_template("s_cusview.html", customers=customers)

#//////////////////////agent////////////////////

@app.route('/alay')
def alay():
    return render_template("a_layout.html")

@app.route('/aindex')
def aindex():
    return render_template("a_index.html")  

@app.route('/totalp')
def ptotal():
    return render_template("a_totalp.html")


@app.route('/acusv')
def acusv():
    return render_template("a_customerview.html")  


@app.route('/meetview')
def ameetview():
    return render_template("a_meetview.html")  


#////////////////////////admin////////////////////////////////////

@app.route('/admin')
def admin():
    return render_template("admin_layout.html")    

@app.route('/admindex')
def admindex():
    return render_template("admin_index.html")    

@app.route('/admagent')
def admagent():
    return render_template("admin_addagent.html")    
     
@app.route('/group')
def group():
    return render_template("admin_addgroup.html")     

@app.route('/login')
def login():
    return render_template("login.html")    


@app.route('/admaview')
def agentview():
    return render_template("admin_agentview.html")  


def stringtodate(strdate):
    return datetime.strptime(strdate, '%Y-%m-%d')

if __name__ == '__main__':
    app.run(debug=True)    