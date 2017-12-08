from flask import Flask, send_file

app = Flask(__name__, static_folder='build/static')

@app.route("/")
def index():
    return send_file("build/index.html")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
