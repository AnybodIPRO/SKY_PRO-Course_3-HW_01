from flask import Flask

import utils
FILE_DIR = 'candidates.json'
data = utils.load_candidates(FILE_DIR)

app = Flask(__name__)


@app.route("/")
def page_index():
    result = utils.get_all()
    return result


@app.route("/candidates/<int:pk>")
def page_candidates(pk):
    result = utils.et_by_pk(pk)
    return result

@app.route("/candidates/<skill_name>")
def page_candidates_by_skills(skill_name):
    result = utils.get_by_skill(skill_name)
    return result

app.run()

