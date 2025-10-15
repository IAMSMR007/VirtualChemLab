from flask import Flask, send_from_directory
from api.routes.test_routes import bp as test_bp
import os

def create_app():
    app = Flask(__name__, static_folder="../frontend/dist", static_url_path="/")
    app.register_blueprint(test_bp, url_prefix="/api")
    return app

app = create_app()

# Serve frontend build when deployed
@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def serve(path):
    if path != "" and os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    return send_from_directory(app.static_folder, "index.html")

if __name__ == "__main__":
    app.run(port=5000, debug=True)
