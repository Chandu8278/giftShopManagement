from flask import Flask,redirect,url_for,render_template,request,session
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'admin'
app.config['MYSQL_DB'] = 'flaskdemo'

mysql = MySQL(app)

app.secret_key = "flask123"

@app.route("/index")
def index():
  return render_template("index.html")

@app.route("/page1/<string:uname>")
def page1(uname):
  session['uname']=uname
  return redirect(url_for('page2'))

@app.route("/page2")
def page2():
 
  if "uname" in session:
    return session["uname"]
  else:
    session.pop("uname")
    return "Session Expired"


@app.route("/adduser")
def adduser():
  return render_template("adduser.html")

@app.route("/insertuser",methods=["POST","GET"])
def insertuser():
  if request.method=="POST":
    try:
      name=request.form["name"]
      email=request.form["email"]
      password=request.form["password"]
      location=request.form["location"]
      print(name,email,password,location)
      db_cursor = mysql.connection.cursor()
      db_cursor.execute("INSERT INTO registration(name,email,password,location) VALUES (%s,%s,%s,%s)", [name,email,password,location])
      mysql.connection.commit()
      #msg="User Added Successfully"
      return render_template("display.html",message="User Added Successfully")#message = param name and msg = param value
    except Exception as e:
      print(e)
      #msg="Fail to Add User Record"
      return render_template("display.html",message="Fail to Add User Record")#message = param name and msg = param value




if __name__ == '__main__':
  app.run(debug=True)