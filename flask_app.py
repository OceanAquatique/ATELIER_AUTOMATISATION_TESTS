from flask import Flask, render_template
from tester.runner import run_tests
from storage import init_db, save_run, list_runs

app = Flask(__name__)

init_db()


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
