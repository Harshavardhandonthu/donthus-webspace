from flask import Flask, render_template
from data.projects import projects  # ← Add this

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", projects=projects)

if __name__ == '__main__':
    app.run(debug=True)
