from flask import Flask, render_template
from tester.runner import run_tests
from storage import init_db, save_run, list_runs
DB = "/home/oceaquatique/project/runs.db"
app = Flask(__name__)

init_db()


@app.get("/")
def consignes():
     return render_template('consignes.html')


@app.route("/run")
def run():
    result = run_tests()
    save_run(result)
    return result


@app.route("/dashboard")
def dashboard():
    runs = list_runs()
    return render_template(
        "dashboard.html",
        runs=runs
    )

     
if __name__ == "__main__":
    # utile en local uniquement
    app.run(host="0.0.0.0", port=5000, debug=True)
     


