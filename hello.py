from flask import Flask

app = Flask(__name__)


@app.route("/")


def home():
    return "<h1> Hej välkommen till min coola hemsida, detta är produktion. </h1> <h2> hur blir detta </h2>"


app.run()
