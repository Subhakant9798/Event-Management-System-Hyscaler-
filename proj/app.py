from flask import Flask, render_template, request, redirect, session, flash
from flask_mysqldb import MySQL
import mysql.connector
import os

app = Flask(__name__)
app.secret_key = os.urandom(20)

conn = mysql.connector.connect(
    host="localhost", user="root", password="", database="eventmanage")
cursor = conn.cursor()


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'eventmanage'


mysql = MySQL(app)


@app.route('/')
def login():
    return render_template('mylogin.html')


@app.route('/home')
def home():
    if 'user_id' in session:
        return render_template('index.html', type=session['user_id'])
    else:
        return redirect('/')


@app.route('/reg')
def regis():
    return render_template('registration.html')


@app.route('/rent_venue')
def rent_venue():
    if 'user_id' in session:
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM create_event")
        event_data = cursor.fetchall()
        return render_template('rent-venue.html', data=event_data, type=session['user_id'])
    else:
        return redirect('/')


@app.route('/about')
def about():
    if 'user_id' in session:
        return render_template('about.html', type=session['user_id'])
    else:
        return redirect('/')


@app.route('/showevents')
def showevents():
    if 'user_id' in session:
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM create_event")
        event_data = cursor.fetchall()
        return render_template("shows-events.html", data=event_data, type=session['user_id'])
    else:
        return redirect('/')


@app.route('/tickets')
def tickets():
    if 'user_id' in session:
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM create_event")
        event_data = cursor.fetchall()
        return render_template('tickets.html', data=event_data, type=session["user_id"])
    else:
        return redirect('/')


@app.route('/ticket_det/<int:id>')
def ticket_det(id):
    if 'user_id' in session:
        cursor = mysql.connection.cursor()
        cursor.execute(f"SELECT * FROM create_event WHERE id = {id}")
        event_data = cursor.fetchall()
        return render_template('ticket-details.html', data=event_data, type=session['user_id'])
    else:
        return redirect('/')


@app.route('/feedback')
def feedback():
    if 'user_id' in session:
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM feedback")
        feedback_data = cursor.fetchall()
        return render_template("feedback.html", data=feedback_data, type=session['user_id'])
    else:
        return redirect('/')


# Fetching Login data and validating
@app.route('/login_accnt', methods=["POST"])
def login_accnt():
    ln_username = request.form["email"]
    ln_password = request.form["password"]
    ln_type = request.form.get('type')

    if (ln_type):
        cursor.execute("SELECT * FROM regis_table WHERE email= %s AND password= %s AND type=%s",
                       (ln_username, ln_password, ln_type))
    else:
        cursor.execute(
            "SELECT * FROM regis_table WHERE email= %s AND password= %s AND type='user'", (ln_username, ln_password))
    exist_user = cursor.fetchall()
    if len(exist_user) > 0:
        session['user_id'] = exist_user[0][3]
        return redirect('/home')
    else:
        return redirect('/')


# Data input to reg_table
@app.route('/register_accnt', methods=["POST"])
def register_accnt():
    if request.method == "POST":
        reg_user = request.form["reg_username"]
        reg_mail = request.form["reg_email"]
        reg_pass = request.form["reg_password"]

        cursor.execute(
            "SELECT * FROM regis_table WHERE EMAIL = %s", (reg_mail,))
        dat = cursor.fetchall()
        if (len(dat) > 0):
            return render_template('exist_email.html')
        else:
            cursor.execute("INSERT INTO regis_table(NAME, EMAIL, PASSWORD) VALUES(%s, %s, %s)",
                           (reg_user, reg_mail, reg_pass))
            conn.commit()
            return redirect("/reg")


# Inserting data to Reservation application
@app.route('/postdata', methods=['POST'])
def submit():
    if 'user_id' in session:
        if request.method == 'POST':
            Title = request.form["event_title"]
            Phone = request.form["phone-number"]
            Datetime = request.form["date_time"]
            Location = request.form["location"]
            Desc = request.form["description"]
            Price = request.form["price"]

            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO create_event(title, phone, datetime, location, description,price) VALUES (%s, %s, %s, %s, %s,%s)",
                        (Title, Phone, Datetime, Location, Desc, Price))
            mysql.connection.commit()

            cursor = mysql.connection.cursor()
            cursor.execute("SELECT * FROM create_event")
            event_data = cursor.fetchall()

            return render_template("shows-events.html", data=event_data, type=session['user_id'])
        else:
            return "Something went wrong"
    else:
        return redirect('/')


@app.route("/deletedata/<int:id>", methods=['GET', 'POST'])
def deletedata(id):
    if 'user_id' in session:
        if (request.method == 'GET'):
            cur = mysql.connection.cursor()
            cur.execute(f"DELETE FROM create_event WHERE id={id}")
            mysql.connection.commit()

            cursor = mysql.connection.cursor()
            cursor.execute("SELECT * FROM create_event")
            event_data = cursor.fetchall()

            return render_template('shows-events.html', data=event_data, type=session['user_id'])
        else:
            return "Failed"
    else:
        return redirect('/')


@app.route("/editdata/<int:id>", methods=['GET', 'POST'])
def editdata(id):
    if 'user_id' in session:
        if (request.method == 'GET'):
            cur = mysql.connection.cursor()
            cur.execute(f"SELECT * FROM create_event WHERE id={id}")
            data = cur.fetchall()

            return render_template('edit_event.html', data=data, type=session['user_id'])
        else:
            return "Failed"
    else:
        return redirect('/')


@app.route("/updatedata/<int:id>", methods=['GET', 'POST'])
def updatedata(id):
    if 'user_id' in session:
        if (request.method == 'POST'):
            Title = request.form["event_title"]
            Phone = request.form["phone-number"]
            Datetime = request.form["date_time"]
            Location = request.form["location"]
            Desc = request.form["description"]
            Price = request.form["price"]

            cur = mysql.connection.cursor()
            cur.execute(f"UPDATE create_event set title = %s, phone = %s, datetime = %s, location = %s, description = %s, price = %s WHERE id = {id}", (
                Title, Phone, Datetime, Location, Desc, Price))
            mysql.connection.commit()

            cursor = mysql.connection.cursor()
            cursor.execute("SELECT * FROM create_event")
            event_data = cursor.fetchall()

            return render_template("shows-events.html", data=event_data, type=session['user_id'])
        else:
            return "Failed"
    else:
        return redirect('/')

# Taking feedbacks


@app.route('/take_feedback', methods=["POST"])
def take_feedback():
    if 'user_id' in session:
        if request.method == "POST":
            f_name = request.form["u_name"]
            f_mail = request.form["u_email"]
            f_msg = request.form["u_feedback"]
            cur = mysql.connection.cursor()
            cur.execute(
                "INSERT INTO feedback(fed_name, fed_email, fed_msg) VALUES (%s, %s, %s)", (f_name, f_mail, f_msg))
            mysql.connection.commit()

            cursor = mysql.connection.cursor()
            cursor.execute("SELECT * FROM feedback")
            feedback_data = cursor.fetchall()

            flash("Feedback rececived!!", 'info')
            return render_template("feedback.html", data=feedback_data, type=session['user_id'])
        else:
            return "Feedback taking failed"
    else:
        return redirect('/')


@app.route("/dashboard")
def dashboard():
    if 'user_id' in session:
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT DISTINCT title FROM create_event")
        event_num = len(cursor.fetchall())

        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM regis_table WHERE type= 'admin'")
        admin_num = len(cursor.fetchall())

        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM regis_table WHERE type= 'user'")
        user_num = len(cursor.fetchall())

        cursor = mysql.connection.cursor()
        cursor.execute("SELECT SUM(no_of_tickets) FROM payment")
        parti_num = cursor.fetchall()

        return render_template('dashboard.html', no_of_events=event_num, no_of_admins=admin_num, no_of_users=user_num, no_of_parti=parti_num, type=session['user_id'])
    else:
        return redirect('/')


@app.route("/transaction", methods=["GET", "POST"])
def transaction():
    if 'user_id' in session:
        if request.method == "POST":
            print("Inside IF")
            Evename = request.form["event_name"]
            Tcount = request.form["ticket_count"]
            Tname = request.form["ticket_name"]
            Tamount = request.form["amount"]

            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO payment(event_name, no_of_tickets, person_name, amount) VALUES (%s, %s, %s, %s)",
                        (Evename, Tcount, Tname, Tamount))
            mysql.connection.commit()

            return render_template('payment.html', type=session['user_id'])
        else:
            return "Something went Wrong"
    else:
        return redirect('/')


@app.route("/retrive_payment/<int:id>", methods=["GET", "POST"])
def retrive_payment(id):
    if 'user_id' in session:
        cur = mysql.connection.cursor()
        cur.execute(f"SELECT * FROM create_event WHERE id = {id}")
        data = cur.fetchall()
        no_of_persons = request.form['quantity']
        amount = int(data[0][6]) * int(no_of_persons)

        return render_template("transaction.html", data=data, qty=no_of_persons, amount=amount, type=session['user_id'])
    else:
        return redirect('/')


# Logging out of the account
@app.route('/logout')
def logout():
    session.pop('user_id')
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
