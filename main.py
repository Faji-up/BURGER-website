from flask import Flask, request
from flask import render_template
import sqlite3
import Products
import Users
from flask import request
from datetime import date,datetime
current_user = 0
isExist = True
categories_img = [
    'https://scontent-xsp1-1.xx.fbcdn.net/v/t39.30808-6/386517405_177931588686758_326795398217709096_n.jpg?stp=cp6_dst-jpg&_nc_cat=108&ccb=1-7&_nc_sid=dd5e9f&_nc_eui2=AeGSC1DsDuKlcw-JQTeQ2UZwTk4S8fgkYy5OThLx-CRjLk2Y9pKqOElsulaOIY93U8f9Awpptkz7IF-tA_2AorE1&_nc_ohc=H42TN-aEMUcAX9YiSj2&_nc_zt=23&_nc_ht=scontent-xsp1-1.xx&oh=00_AfDk4LibuXw_SAhxLcwYZ9Fc93iXbR5_eqG7Avmt2PTU7Q&oe=65D468A9',
    'https://scontent-xsp2-1.xx.fbcdn.net/v/t39.30808-6/391756286_179147561898494_8156046641011433024_n.jpg?stp=cp6_dst-jpg&_nc_cat=111&ccb=1-7&_nc_sid=dd5e9f&_nc_eui2=AeFZSj0WEl1AqFvQMm0-Es_roiUJMqP47ByiJQkyo_jsHCq-3vKhQ8oe-E3Jw0i1UphWeyoEEa-nyoriR-__kvFt&_nc_ohc=2RPuTSoNstUAX_MMzET&_nc_zt=23&_nc_ht=scontent-xsp2-1.xx&oh=00_AfAh2H6mWAHBsBXOZyxEAJ33PoOXDeVYEI0EkAc1bUYRrw&oe=65D3B50B',
    'https://scontent-hkg4-2.xx.fbcdn.net/v/t39.30808-6/393635742_181817514964832_4308394252961311811_n.jpg?_nc_cat=111&ccb=1-7&_nc_sid=dd5e9f&_nc_eui2=AeGpDDbkUubcuFMpHDON6DFHqbqm3hVJ1t6puqbeFUnW3iuqPxpz0YgQd2KaqmYUAat0Z2WonTiNDrgaPZnC6ywP&_nc_ohc=XtwP8oLSNZIAX-1Tpsb&_nc_zt=23&_nc_ht=scontent-hkg4-2.xx&oh=00_AfBmZD9ea3t0JWLpN-axgV3b7NybYqi-NP5eGgXilGAEJg&oe=65D43705',
    'https://scontent-hkg4-2.xx.fbcdn.net/v/t39.30808-6/395289081_186226024523981_91694763671746802_n.jpg?_nc_cat=111&ccb=1-7&_nc_sid=dd5e9f&_nc_eui2=AeGqkobvIp4Zo3jQjTyZNgM_DZ9vjQkEWYoNn2-NCQRZimagUwNzZWW3agMaL01Bi8BN7aV_5DwCAtWI_XZqwWZq&_nc_ohc=pQwuamNhsTEAX-Zb2eB&_nc_zt=23&_nc_ht=scontent-hkg4-2.xx&oh=00_AfDnHdVlB-xnXMhxsiRIbNhnCxL21AomPVHPvfnNDbNPnw&oe=65D5413E',
    'https://scontent.fmnl4-3.fna.fbcdn.net/v/t39.30808-6/399148927_191365937343323_6247063010197874225_n.jpg?_nc_cat=110&ccb=1-7&_nc_sid=3635dc&_nc_eui2=AeFyJrGpNNE5D_F4AfnOxO6XiO7pAad6YSmI7ukBp3phKRgVRqiO3UzkaccqDJDjniJ2EF3nDL4SglZETi4ww9Gi&_nc_ohc=JDgUzW_id_0AX86cNSC&_nc_zt=23&_nc_ht=scontent.fmnl4-3.fna&oh=00_AfC9e5JuIf7k9EnC2voilgt_KVrc3DidL-PgfbBK_FtEnA&oe=65D3BE12',
    'https://scontent.fmnl13-2.fna.fbcdn.net/v/t39.30808-6/399550235_192871480526102_2988463428811633231_n.jpg?_nc_cat=107&ccb=1-7&_nc_sid=dd5e9f&_nc_eui2=AeFM_u5bGVMym5EcVE6r66m3T7lAuFELPVNPuUC4UQs9U6pj-EsUSN9kb8hKR-V7e_4lX1lZPjq__6Rg2E9Vcpwe&_nc_ohc=C1wi_99tK6MAX9lnrIx&_nc_zt=23&_nc_ht=scontent.fmnl13-2.fna&oh=00_AfDQJR950WnadsmP3usXPMIXqSCADr0WAhiMGidAhibVtg&oe=65D496A8'
]

acc = []
app = Flask(__name__)
db = None
date = date.today()
def add_user(name,email,password):
    global db
    db = sqlite3.connect("Users.db")
    c = db.cursor()
    exe = "INSERT INTO users (name,email,password) VALUES (?,?,?)"
    c.execute(exe,(name,email,password))
    db.commit()
    db.close()
    db = None
@app.route('/create/<string:username>/<string:email>/<string:password>', methods=['POST'])
def create_account(username,email,password):
    add_user(username, email, password)
    return '', 204  # No content, account created successfully

def get_users():
    global db
    users = []
    db = sqlite3.connect("Users.db")
    c = db.cursor()
    exe = "SELECT * FROM users"

    c.execute(exe)
    for user in c.fetchall():
        print(user)
        users.append(Users.User(user[0],user[1],user[2],user[3]))
    db.commit()
    db.close()
    return users

@app.route('/buy/<string:prod>/<string:price>', methods=['POST'])
def buy_Item(prod, price):
    try:
        # Assuming current_user is imported and working correctly
          # You need to define the get_current_user function

        if current_user is None:
            return 'User not authenticated', 401

        db = sqlite3.connect("Transactions.db")
        c = db.cursor()
        today = date.today()
        exe = "INSERT INTO transactions(prod, payment, date, buyer_id) VALUES (?, ?, ?, ?)"
        c.execute(exe, (prod, price, today, current_user.get_id()))
        db.commit()
        db.close()
        return '', 204
    except Exception as e:
        return str(e), 500
def get_db():
    global db
    db = sqlite3.connect("Users.db")
    c = db.cursor()
    exe = "SELECT * FROM users"
    c.execute(exe)

    return c.fetchall()
@app.route('/delete_item/<int:buyer_id>', methods=['DELETE'])
def del_item(buyer_id):
    db = sqlite3.connect("Transactions.db")
    c = db.cursor()
    exe = f"DELETE FROM transactions WHERE id={buyer_id}"
    c.execute(exe)
    db.commit()
    db.close()
    return '', 204
def add_tran(id,prod,price,date):
    pass
    #db = sqlite3.connect("Transactions.db")
    #c = db.cursor()
    #exe = "INSERT INTO transactions(prod,payment,date,buyer_id) VALUES (?,?,?,?)"
    #c.execute(exe,(prod,price,date,id))
    #db.commit()
    #db.close()
def get_trans():
    db = sqlite3.connect("Transactions.db")
    c = db.cursor()
    exe = "SELECT * FROM transactions"

    c.execute(exe)
    tran = c.fetchall()
    db.commit()
    db.close()
    print(tran)
    return tran

def get_user_transactions(user_id):
    db = sqlite3.connect("Transactions.db")
    c = db.cursor()
    exe = "SELECT * FROM transactions WHERE buyer_id = ?"
    c.execute(exe, (user_id,))
    user_transactions = c.fetchall()
    db.close()
    return user_transactions

def close_db():
    if db:
        db.close()

@app.route("/Home")
def home(current_user):  # Accept current_user as parameter
    user_cart = []
    if current_user == 0:
        return render_template("error.html")
    else:
        # Retrieve transactions for the current user from the database
        user_transactions = get_user_transactions(current_user.get_id())

        # Add the purchased items to the user's cart
        for transaction in user_transactions:
            user_cart.append({
                "name": transaction[1],
                "price": transaction[2]
            })

    return render_template('home.html', del_cart=del_item, current_user=current_user, user_cart=user_cart, get_tran=get_trans(), cart=user_cart, items=categories_img, products=Products.products_list)

@app.route("/login",methods=['post'])
def login_():
    global acc,isExist,current_user

    password = request.form['password']
    email = request.form['email']
    db = sqlite3.connect("Users.db")
    c = db.cursor()
    exe = "SELECT * FROM users"
    c.execute(exe)
    for user in c.fetchall():
        if email == user[2] and password == user[3]:
            current_user = Users.User(user[0],user[1],user[2],user[3])
            return home(current_user)  # Pass current_user to home()
        elif email == "admin123@gmail.com" and password == "admin123":
            return admin()
    db.commit()
    db.close()
    return login()

@app.route("/",methods=['post'])
def buy():
    global date
    if current_user == 0:
        return render_template("error.html")
    else:
        name = request.form['name']
        price = request.form['price']
        add_tran(current_user.get_id(),name,price,date)
        return home()


@app.route("/create",methods=['post'])
def create_():
    global acc
    name = request.form['username']
    password = request.form['password']
    confirm_password = request.form['confirm-password']
    email = request.form['email']

    if password == confirm_password:
        add_user(name,email,password)

    return render_template("create.html",acc=acc)


@app.route("/")
def login():
    global current_user
    current_user = Users
    return render_template("login.html", current_user=current_user)

@app.route("/Admin")
def admin():

    return render_template("admin.html",products = Products.products_list)

@app.route("/Admin/Users")
def users_page():
    return render_template("users.html", users = get_users())

@app.route("/Create")
def create():
    return render_template("create.html",acc=acc)

@app.route("/Admin/Transaction")
def tran_page():
    global db
    trans = []
    present_val = 0
    past_val = 0
    total_val = 0
    db = sqlite3.connect("Transactions.db")
    c = db.cursor()
    exe = "SELECT * FROM transactions"
    c.execute(exe)
    for tra in c.fetchall():
        trans.append({
            "name":tra[1],
            "price":tra[2],
            "date":tra[3],
            "buyer_id":tra[4]
        })
        data_date = datetime.strptime(tra[3],'%Y-%m-%d').date()
        if date == data_date:
            present_val += tra[2]
        elif date < data_date:
            past_val += tra[2]
        total_val += tra[2]
    db.commit()
    db.close()
    return render_template("transactions.html",trans = trans,present = present_val,past = past_val,total = total_val)
if __name__ == '__main__':
    app.debug = True

    print(date)
    app.run()
