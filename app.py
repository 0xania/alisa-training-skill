from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/', methods=['POST'])
def main():
    req = request.get_json()

    res = {
        "response": {
            "text": "Начинаю тренировку. Включаю ваш аудиофайл.",
            "tts": "Начинаю тренировку. Включаю ваш аудиофайл.",
            "end_session": False,
            "buttons": [
                {
                    "title": "Слушать тренировку",
                    "url": "https://drive.google.com/uc?export=download&id=1nIsjdQZX333HK7zlkn2NEoRfje8EOYgd",
                    "hide": False
                }
            ]
        },
        "version": req.get("version", "1.0")
    }

    return jsonify(res)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
