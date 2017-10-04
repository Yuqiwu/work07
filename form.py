from flask import Flask, render_template, session, request

my_app = Flask(__name__)

user = "user"
password = "pass"
u = "Sorry, your username is incorrect"
p = "Sorry, your password is incorrect"

@my_app.route('/', methods=["POST", "GET"])
def root():
    return render_template("form.html")

@my_app.route("/welcome", methods=["POST", "GET"])
def welcome():
    if user == request.form['username']:
        if password == request.form['password']:
            return render_template("welcome.html",un = user, pw = password)
        else:
            return render_template("welcome.html",un = user, pw = p)
    else:
        return render_template("welcome.html", un = u, pw = "")

if __name__ == "__main__":
    my_app.debug = True
    my_app.run()
