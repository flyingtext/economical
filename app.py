from flask import Flask, render_template, request, redirect, url_for
import json

from models import FeatureConfig, SessionLocal, init_db

app = Flask(__name__)

# Ensure tables exist
def get_session():
    init_db()
    return SessionLocal()


@app.route("/features", methods=["GET", "POST"])
def features():
    session = get_session()
    if request.method == "POST":
        name = request.form["name"]
        config_raw = request.form["config"]
        config = json.loads(config_raw)
        feature = FeatureConfig(name=name, config=config)
        session.add(feature)
        session.commit()
        return redirect(url_for("features"))

    features = session.query(FeatureConfig).all()
    return render_template("features.html", features=features)


if __name__ == "__main__":
    app.run(debug=True)
