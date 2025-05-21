from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/', methods=['POST'])
def main():
    req = request.get_json()
    audio_url = "https://drive.google.com/uc?export=download&id=1nIsjdQZX333HK7zlkn2NEoRfje8EOYgd"

    response = {
        "version": req.get("version", "1.0"),
        "session": req.get("session"),
        "response": {
            "text": "Начинаю тренировку. Воспроизводится аудио.",
            "tts": "Начинаю тренировку. Воспроизводится аудио.",
            "end_session": True,
            "directives": [
                {
                    "type": "AudioPlayer.Play",
                    "audio_item": {
                        "stream": {
                            "url": audio_url,
                            "offset_ms": 0,
                            "token": "training-audio-token"
                        }
                    }
                }
            ]
        }
    }
    return jsonify(response)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
