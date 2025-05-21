from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/', methods=['POST'])
def main():
    req = request.get_json()

    audio_url = "https://raw.githubusercontent.com/0xania/alisa-training-skill/99ee2e84f6878b53b06f1219a29458ca245590a8/trenirovka.mp3"

    response = {
        "version": req.get("version", "1.0"),
        "session": req.get("session"),
        "response": {
            "text": "Starting training. Playing audio.",
            "tts": "Starting training. Playing audio.",
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
