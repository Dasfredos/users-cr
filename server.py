from flask import Flask, render_template, request, redirect
# import the class from friend.py
from users import Users
app = Flask(__name__)
app.secret_key="rootroot"

@app.route("/add")
def add_user():
    
    return render_template("create.html")

@app.route("/")
def index():
    # call the get all classmethod to get all friends
    user = Users.get_all()
    print(user)
    return render_template("index.html" , user = user)

@app.route('/add_users', methods = ['POST'])
def input():
    user_data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"]
            }
    Users.save(user_data)
    return redirect("/")




if __name__ == "__main__":
    app.run(debug=True)

