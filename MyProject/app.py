from flask import Flask,render_template,redirect,request
import sqlite3
from flask_mysqldb import MySQL


app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'admin'
app.config['MYSQL_DB'] = 'flaskdemo'

mysql = MySQL(app)

@app.route("/")
def main():
	return "My First Flask Web Application"

@app.route("/demo")
def demo1():
	return "Demo page"

@app.route("/admin")
def demo2():
	return "Admin Page"

@app.route("/user")
def demo3():
	return "Hello World"

@app.route("/user/<name>")
def demo4(name):
	return "Hello %s" %name

@app.route("/index")
def index():
	return render_template('index.html')

@app.route("/about")
def about():
	return render_template('about.html')

@app.route("/stockmanager")
def stockmanager():
	return render_template('stockmanagerlogin.html')

@app.route("/shopowner")
def shopowner():
	return render_template('shopownerlogin.html')

@app.route("/customer")
def customer():
	return render_template('customerL&R.html')

@app.route("/customerregister")
def customerregister():
	return render_template('customerR.html')

@app.route("/register")
def register():
  return render_template('register.html')

@app.route("/adduser")
def adduser():
  return render_template('/adduser.html')

@app.route("/userindex")
def userindex():
  return render_template('/userindex.html')

@app.route("/smindex")
def smindex():
  return render_template('/smindex.html')

@app.route("/soindex")
def soindex():
  return render_template('/soindex.html')

@app.route("/changepwd")
def changepwd():
  return render_template('/changepwd.html')

@app.route("/smchangepwd")
def smchangepwd():
  return render_template('/smchangepwd.html')

@app.route("/sochangepwd")
def sochangepwd():
  return render_template('/soupdatepwd.html')

@app.route("/sorequeststock")
def sorequeststock():
  return render_template('/sorequeststock.html')

@app.route("/smaddstock")
def smaddstock():
  return render_template('/smaddstock.html')

@app.route("/logout")
def logout():
  return render_template('index.html',message='You are Logged out Successfully')


@app.route("/updatepwd", methods=["POST","GET"])
def updatepwd():
  
  if request.method=="POST":
    try:
      email=request.form["email"]
      pwd=request.form["pwd"]
      db_cursor = mysql.connection.cursor()
      i = db_cursor.execute("update registration set password = %s where email=%s",(pwd,email,))
      mysql.connection.commit()
      if(i>0):
        return render_template('changepwd.html',message="password is changed")
      else:
        return render_template('changepwd.html',message="password is not changed")
    except Exception as e:
      print(e)
      return e

@app.route("/smupdatepwd", methods=["POST","GET"])
def smupdatepwd():  
  if request.method=="POST":
    try:
      email=request.form["email"]
      pwd=request.form["pwd"]
      db_cursor = mysql.connection.cursor()
      i = db_cursor.execute("update stockmanager set password = %s where email=%s",(pwd,email,))
      mysql.connection.commit()
      if(i>0):
        return render_template('smchangepwd.html',message="password is changed")
      else:
        return render_template('smchangepwd.html',message="password is not changed")
    except Exception as e:
      print(e)
      return e

@app.route("/soupdatepwd", methods=["POST","GET"])
def soupdatepwd():  
  if request.method=="POST":
    try:
      email=request.form["email"]
      pwd=request.form["pwd"]
      db_cursor = mysql.connection.cursor()
      i = db_cursor.execute("update shopowner set password = %s where email=%s",(pwd,email,))
      mysql.connection.commit()
      if(i>0):
        return render_template('soupdatepwd.html',message="password is changed")
      else:
        return render_template('soupdatepwd.html',message="password is not changed")
    except Exception as e:
      print(e)
      return e

@app.route("/insertuser", methods=["POST","GET"])
def insertuser():
  db_connection = sqlite3.connect("flaskprojectdemo.db")
  if request.method=="POST":
    try:
      name=request.form["name"]
      email=request.form["email"]
      password=request.form["password"]
      location=request.form["location"]
      print(name,email,password,location)
      db_cursor = db_connection.cursor()
      db_cursor.execute("insert into registration(name,email,password,location) values(?,?,?,?)", (name,email,password,location))
      db_connection.commit()
      return render_template('display.html',message="User Added Successfully")
    except Exception as e:
      print(e)
      db_connection.rollback()
      return render_template('display.html',message="Fail to add User")

@app.route("/smaddstockit",methods=["POST","GET"])
def smaddstockit():
  if request.method=="POST":
    try:
      stock_id=request.form["sid"]
      gc=request.form["gc"]
      gn=request.form["gn"]
      gd=request.form["gd"]
      cost=request.form["cost"]
      quantity=request.form["quantity"]
      status="accepted"
      db_cursor = mysql.connection.cursor()
      db_cursor.execute("INSERT INTO stock VALUES (%s,%s,%s,%s,%s,%s,%s)", [stock_id,gc,gn,gd,cost,quantity,status])
      mysql.connection.commit()
      #msg="User Added Successfully"
      return render_template("smaddstock.html",message="Stock Added Successfully")#message = param name and msg = param value
    except Exception as e:
      print(e)
      #msg="Fail to Add User Record"
      return e#message = param name and msg = param value

@app.route("/soaddstockit",methods=["POST","GET"])
def soaddstockit():
  if request.method=="POST":
    try:
      stock_id=request.form["sid"]
      gc=request.form["gc"]
      gn=request.form["gn"]
      gd=request.form["gd"]
      cost=request.form["cost"]
      quantity=request.form["quantity"]
      status = "not_accepted"
      db_cursor = mysql.connection.cursor()
      db_cursor.execute("INSERT INTO stock VALUES (%s,%s,%s,%s,%s,%s,%s)", [stock_id,gc,gn,gd,cost,quantity,status])
      mysql.connection.commit()
      #msg="User Added Successfully"
      return render_template("sorequeststock.html",message="Request for Stock sent Successfully")#message = param name and msg = param value
    except Exception as e:
      print(e)
      #msg="Fail to Add User Record"
      return render_template("sorequeststock.html",message="Fail to sent Stock Request")

@app.route("/registeruser", methods=["POST","GET"])
def registeruser():
  if request.method=="POST":
    try:
      name=request.form["uname"]
      gender=request.form["gender"]
      email=request.form["email"]
      mobile=request.form["mob"]
      password=request.form["pwd"]
      
      db_cursor = mysql.connection.cursor()
      db_cursor.execute("INSERT INTO registration(name,gender,email,mobile,password) VALUES (%s,%s,%s,%s,%s)", [name,gender,email,mobile,password])
      mysql.connection.commit()
      #msg="User Added Successfully"
      return render_template("customerL&R.html",message="User Added Successfully")#message = param name and msg = param value
    except Exception as e:
      print(e)
      #msg="Fail to Add User Record"
      return render_template("customerR.html",message="Fail to Add User Record")#message = param name and msg = param value


@app.route("/loginuser", methods=["POST","GET"])
def loginuser():
  if request.method=="POST":
    try:
      email=request.form["email"]
      password=request.form["pwd"]
      db_cursor = mysql.connection.cursor()
      db_cursor.execute("select * from registration where email = %s and password = %s",[email,password])
      data = db_cursor.fetchone()
      if(len(data)>0):
      	#return render_template('customerHome.html',message="Your Login is Successfully")
      	return render_template('userindex.html')
    except Exception as e:
      return "Invalid Login"
      
     #return render_template('customerR.html',message="Fail to add User")

@app.route("/loginsm", methods=["POST","GET"])
def loginsm():
  if request.method=="POST":
    try:
      email=request.form["email"]
      password=request.form["pwd"]
      db_cursor = mysql.connection.cursor()
      db_cursor.execute("select * from stockmanager where email = %s and password = %s",[email,password])
      data = db_cursor.fetchone()
      if(len(data)>0):
      	#return render_template('customerHome.html',message="Your Login is Successfully")
      	return render_template('smindex.html')
    except Exception as e:
      return "Invalid Login"

@app.route("/sologin", methods=["POST","GET"])
def sologin():
  if request.method=="POST":
    try:
      email=request.form["email"]
      password=request.form["pwd"]
      db_cursor = mysql.connection.cursor()
      db_cursor.execute("select * from shopowner where email = %s and password = %s",[email,password])
      data = db_cursor.fetchone()
      if(len(data)>0):
      	#return render_template('customerHome.html',message="Your Login is Successfully")
      	return render_template('soindex.html')
    except Exception as e:
      return "Invalid Login"

@app.route("/viewstocks")
def viewstocks():
	db_cursor = mysql.connection.cursor()
	db_cursor.execute("select * from stock where status='accepted'")
	rows = db_cursor.fetchall()
	return render_template("viewstocks.html",rows=rows)

@app.route("/viewrequests")
def viewrequests():
	db_cursor = mysql.connection.cursor()
	db_cursor.execute("select * from stock where status='not_accepted'")
	rows = db_cursor.fetchall()
	return render_template("smviewrequests.html",rows=rows)

@app.route("/soviewstocks")
def soviewstocks():
	db_cursor = mysql.connection.cursor()
	db_cursor.execute("select * from stock where status='accepted'")
	rows = db_cursor.fetchall()
	return render_template("soviewstocks.html",rows=rows)

@app.route("/deleteuser")
def deleteuser():
	return render_template('/deleteuser.html')


 
@app.route("/deleteuserbyid/<string:uid>")
def deleteuserbyid(uid):
  try:
    db_connection = sqlite3.connect("flaskprojectdemo.db")
    db_cursor = db_connection.cursor()
    db_cursor.execute("delete from registration where id=?",uid)
    db_connection.commit()
    return "Record Deleted"
  except Exception as e:
    return e  

@app.route("/hard/<string:stock_id>")
def hard(stock_id):
	print(stock_id)
	try:
		db_cursor = mysql.connection.cursor()
		i=db_cursor.execute("update stock set status=%s where stock_id=%s",("accepted",stock_id,))
		mysql.connection.commit()
		return "Stock Added Successfully"
	except Exception as e:
		return e

@app.route("/viewusers")
def viewusers():
    db_connection = sqlite3.connect("flaskprojectdemo.db")
    db_connection.row_factory = sqlite3.Row
    db_cursor = db_connection.cursor()
    db_cursor.execute("select * from registration")
    rows = db_cursor.fetchall()
    return render_template("viewrequests.html",rows=rows)

if __name__=='__main__':
	app.run(debug=True)