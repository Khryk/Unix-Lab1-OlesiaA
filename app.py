from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/OlesiaALab1')
def olesia():
    return jsonify({
        "service": "OlesiaALab1",
        "version": "1.0.0",
        "author": "Olesia Ahapova",
        "group": "ІТШІз-23-1",
        "lab": "Containerization of Application",
        "status": "Running",
        "message": "Flask microservice is operating normally"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
