from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/', methods=['POST'])
def main():
    req = request.get_json()
    audio_url = (
        "https://raw.githubusercontent.com/"
        "0xania/alisa-training-skill/"
        "fc492be8c0e3decbd8d70b9f0517748c292db37a/"
        "Тренировка.mp3"
    )

    response = {
        "version": req.get("version", "1.0"),
        "session": req.get("session"),
        "response": {
            "text": "Начинаю тренировку. Воспроизводится аудио.",
            "tts": (
                "<speak>Начинаю тренировку! "
                f"<speaker audio=\"{audio_url}\"/>"
                " Удачной тренировки!</speak>"
            ),
            "end_session": True,
            "directives": [
                {
                    "type": "AudioPlayer.Play",
                    "audio_item": {
                        "stream": {
                            "url": audio_url,
                            "offset_ms": 0,
                            "token": "training-token"
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
