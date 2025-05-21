from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['POST'])
def main():
    req = request.get_json()

    # Формируем простой ответ
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
        "version": req["version"]
    }

    return jsonify(res)

if __name__ == '__main__':
    app.run()
