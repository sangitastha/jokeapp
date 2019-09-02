import os
from flask import Flask, request, render_template
import random

app = Flask(__name__)


@app.route('/')
@app.route('/home/')
@app.route("/tellmeajoke/")
def tellmeajoke():
    array_of_jokes = [
        "I used to think the brain was the most important organ. Then I thought, look what's telling me that.",
        "How does NASA organize their company parties? They planet.",
        "Today at the bank, an old lady asked me to help check her balance. So I pushed her over.",
        "I'm so good at sleeping. I can do it with my eyes closed.",
        "My boss told me to have a good day.. so I went home."
    ]

    index_of_array = random.randint(0, len(array_of_jokes)-1)
    random_joke = array_of_jokes[index_of_array]

    return random_joke

if  __name__ == "__main__":
    try:
        pirt = int(os.getenv("PORT"))
        app.run(host='0.0.0.0', port=port)
    except Exception:
        app.run(host= 'localhost', port=8080)
     