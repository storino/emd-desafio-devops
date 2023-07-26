# -*- coding: utf-8 -*-
"""
Just a simple hello-world app :)
"""
import os

import pyfiglet
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def hello_world():
    name = os.environ.get("NAME", "World")
    return render_template("hello.html", name=name)


@app.route("/word", methods=["GET", "POST"])
def word_art():
    if request.method == "POST":
        text = request.form["text"]
        font = request.form["font"]
        word_art_text = generate_word_art(text, font)
    else:
        word_art_text = ""

    # Get the list of available fonts from pyfiglet
    available_fonts = pyfiglet.Figlet().getFonts()

    return render_template(
        "word_art.html", word_art_text=word_art_text, available_fonts=available_fonts
    )


def generate_word_art(text, font):
    figlet = pyfiglet.Figlet(font=font)
    return figlet.renderText(text)


if __name__ == "__main__":
    app.run(
        debug=os.environ.get("LOCAL", False),
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
    )
