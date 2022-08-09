#learning python this is my first flask sever dont be too critical please.
#going to pair this with sqlite and react to create a cool blog app.
from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route("/")
def home():
  return render_template("login.html")


@app.route("/confirm-login", methods=['POST', 'GET'])
def confirm_login():
    password = request.form['password']
    username = request.form['username']
    accounts = os.listdir()
    if username in accounts:
      file = open(f"{username}", "r")
      passwrdline = file.readlines()[0:1]
      passwrd = ''.join(passwrdline)
      file.close()
      if password == passwrd:
        return "Logged in!"
      else:
        return "Failed to login!"
    else:
      return "Failed to login!"



if __name__ == '__main__':
    app.run(debug=True)
