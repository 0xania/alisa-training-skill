from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/', methods=['POST'])
def main():
    req = request.get_json()

    res = {
        "response": {
            "text": "Воспроизвожу тренировку",
            "tts": (
                "<speaker audio=\"dialogs-upload/e8946e14-7a9f-4d28-b210-43e493267ff2/7a68b042-694a-4dc8-9658-d09068ec991d.opus\"/> "
                "<speaker audio=\"dialogs-upload/e8946e14-7a9f-4d28-b210-43e493267ff2/b94113bf-6344-428b-b9a1-174db2485fab.opus\"/> "
                "<speaker audio=\"dialogs-upload/e8946e14-7a9f-4d28-b210-43e493267ff2/17485194-bb1b-4e0b-a81a-039a856f4e98.opus\"/> "
                "<speaker audio=\"dialogs-upload/e8946e14-7a9f-4d28-b210-43e493267ff2/b94113bf-6344-428b-b9a1-174db2485fab.opus\"/> "
                "<speaker audio=\"dialogs-upload/e8946e14-7a9f-4d28-b210-43e493267ff2/7b875d35-a8ed-4982-a719-ad76bd406e62.opus\"/> "
                "<speaker audio=\"dialogs-upload/e8946e14-7a9f-4d28-b210-43e493267ff2/b94113bf-6344-428b-b9a1-174db2485fab.opus\"/> "
                "<speaker audio=\"dialogs-upload/e8946e14-7a9f-4d28-b210-43e493267ff2/3068f85d-54b0-4dee-840b-99a96e988505.opus\"/> "
                "<speaker audio=\"dialogs-upload/e8946e14-7a9f-4d28-b210-43e493267ff2/b94113bf-6344-428b-b9a1-174db2485fab.opus\"/> "
                "<speaker audio=\"dialogs-upload/e8946e14-7a9f-4d28-b210-43e493267ff2/ef361eda-e4e4-4533-8948-ed06f5147295.opus\"/> "
            ),
            "end_session": True
        },
        "version": req.get("version", "1.0")
    }

    return jsonify(res)

@app.route('/', methods=['GET'])
def ping():
    return "OK", 200
    
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
