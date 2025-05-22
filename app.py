from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/', methods=['POST'])
def main():
    req = request.get_json()

    res = {
        "response": {
            "text": "Начинаем тренировку.",
            "tts": ("<speak>Начинаем тренировку."
                    "<speaker audio=\"dialogs-upload/e8946e14-7a9f-4d28-b210-43e493267ff2/7c639f4f-345d-4201-b486-bbf9f46f327e.opus\"/>"
                    "<break time=\"1s\"/>"
                    "<speaker audio=\"dialogs-upload/e8946e14-7a9f-4d28-b210-43e493267ff2/0e4c93f1-019d-4c8f-9195-e0f709b6d51f.opus\"/>"
                    "<break time=\"1s\"/>"
                    "<speaker audio=\"dialogs-upload/e8946e14-7a9f-4d28-b210-43e493267ff2/a0acbef5-5562-49cc-966d-0f9bc35eba43.opus\"/>"
                    "<break time=\"1s\"/>"
                    "<speaker audio=\"dialogs-upload/e8946e14-7a9f-4d28-b210-43e493267ff2/ac484922-1130-45e1-9ede-a8a13d8c6e11.opus\"/>"
                    "</speak>"),
            "end_session": True
        },
        "version": req.get("version", "1.0")
    }

    return jsonify(res)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
