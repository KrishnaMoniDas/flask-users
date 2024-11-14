from flask import Flask,render_template, request, redirect, flash, url_for, session
from flaskext.mysql import MySQL
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)




app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='MyNewPass'
app.config['MYSQL_DB']='user'


mysql=MySQL(app)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/signup',methods=['POST','GET'])
def signup():
    if request.method=='POST':
        username = request.form['username']
        email = request.form['email']
        mobile = request.form['mobile']
        password = request.form['password']
        hashed_password =  generate_password_hash(password, method='sha256')

        cur = mysql.connection.curson()
        cur.execute('insert into users (username, email, mobile, password) values (%s, %s, %s, %s)',(username, email, mobile, hashed_password))

        mysql.connection.commit()
        cur.close()

        flash('signup success')

        return redirect(url_for('login'))


if __name__ == ('__main__'):
    app.run(debug=True)