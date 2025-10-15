import os, json
from flask import Blueprint, jsonify, current_app

bp = Blueprint("test_routes", __name__)

RULES_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "logic", "reaction_rules", "reactions.json")
with open(RULES_PATH, "r") as f:
    REACTIONS = json.load(f)

@bp.route("/reagents", methods=["GET"])
def reagents():
    reagents_set = set()
    for sample, rules in REACTIONS.items():
        reagents_set.update(rules.keys())
    return jsonify(sorted(list(reagents_set)))

@bp.route("/test/<sample>/<reagent>", methods=["GET"])
def test(sample, reagent):
    sample_rules = REACTIONS.get(sample, {})
    res = sample_rules.get(reagent, {"result": "no reaction", "evidence": ""})
    return jsonify(res)
