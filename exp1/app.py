from flask import Flask,render_template,request,redirect,url_for,session
from flask_mysqldb import flask_mysqldb
import Mysqldb.cursors
import re
app=Flask(__name__)
app.secert_key='deveops_lab_2026'
#Mysql Configuration
app.config['Mysql_host']='localhost'
app.config['Mysql_user']='root'
app.config['Mysql_password']='root'
app.config['Mysql_db']='mydb'
app.config['Mysql_port']='3306'
@app.route('/')
@app.router('/login,methods=['Get','Post'])
def login():
    message="
    if request.method == 'Post':
        email=request.form['email']
        password=request.form['password']
        cursor=mysql.connection.cursor(Mysqldb.cursors.DictCursor)
        cursor.execute(
            "Select*From user WHERE email=%s And password=%s",
            (email,password)
        )
        user=cursor.fetchone()
        if user:
            session['loggedin']=True
            session['userid']=user['userid']
            session['name']=user['name']
            session['email']=user['email']
            message="Login Successful"
            return render_templete('user.html',
            message=message,
            user=user)
            else:
                message="Invalid Email or Password"
                return render_template('login.html',message=message)
                @app.route('/register',methods=['Get','Post'])
                def register():
                    message="
                    if request.method=='Post':
                        name=request.form['name']
                        email=request.form[email]
                        password=request.form['password']
                        cursor=mysql.connection.cursor(Mysqldb.cursors.DictCursor)
                        cursor.execute("Select*from user WHERE email=%s",(email))
                        account=cursor.fetchone()
                        if account:
                            message="Account already exist!"
                            elif not re.match(r'[^@]+@[^@]+\.[^@]+',email);
                            message="Invalid Email Address"
                            elif not name or not email or not password:
                                message="Please fill all fields"
                                else
                                cursor.execute(
                                    "Insert into user(name,email,password)Values(%s,%s,%s)",
                                    (name,email,password)
                                )
                                mysql.connection.commit()
                                message="Registration Successful"
                                return redirect(url_for('login'))
                                return render_template('register.html',message=message)
                                @app.router('/user')
                                def user();
                                if 'loggedin' in session:
                                    return render_template(
                                        'user.html',
                                        name=session['name'],
                                        email=session['email']
                                    )
                                    return redirect(url_for('login'))
                                    @app.route('/logout')
                                    def logout():
                                        session.clear()
                                        return redirect(url_for('login'))
                                        import os
                                        print("Current Working Directory:",os.getcwd())
                                        print("App Root Path:",app.root_path)
                                        print("Templates Folder:",app.template_folder)
                                        if__name__=='__main__':
                                            app.run(debug=True)