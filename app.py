from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/', methods=['POST'])
def main():
    req = request.get_json()
    audio_url = "https://drive.google.com/uc?export=download&id=1nIsjdQZX333HK7zlkn2NEoRfje8EOYgd"

    # SSML-ответ с тегом <speaker>
    ssml = f"<speak>Начинаю тренировку! " \
           f"<speaker audio='{audio_url}'/>" \
           f" Удачной тренировировки!</speak>"

    response = {
        "version": req.get("version", "1.0"),
        "session": req.get("session"),
        "response": {
            "text": "Начинаю тренировку! Воспроизводится аудио.",
            "tts": ssml,
            "end_session": True
        }
    }
    return jsonify(response)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
