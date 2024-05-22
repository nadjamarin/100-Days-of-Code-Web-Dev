from flask import Flask

app = Flask(__name__)

print(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# This defines what is displayed when user goes to URL/bye
@app.route("/bye")
def say_bye():
    return "Bye"

if __name__ == "__main__":
    app.run()
