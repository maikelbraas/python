from flask import Flask, render_template

app = Flask(__name__)

TASKS = [
  {
    "id" : 1,
    "title" : "Fill in the logboek: 1",
    "content" : "The logboek hasn't been filled yet, fill it."
  },
  {
    "id" : 2,
    "title" : "Fill in the logboek: 2",
    "content" : "The logboek hasn't been filled yet, fill it."
  },
  {
    "id" : 3,
    "title" : "Fill in the logboek: 3",
    "content" : "The logboek hasn't been filled yet, fill it."
  }
]

@app.route("/")
def hello_world():
  return render_template("home.html", tasks=TASKS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)