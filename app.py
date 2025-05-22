from flask import Flask, request, jsonify

app = Flask(__name__)

# Список аудиофайлов
audio_files = [
    "https://drive.google.com/uc?export=download&id=1o7c-Z2GEBdeD1jus8BLnEgi3_NU336r6",
    "https://drive.google.com/uc?export=download&id=1nzQJzL_WaXQrovpdKguEfoILlHRArjR5",
    "https://drive.google.com/uc?export=download&id=1o3c5ecJsetjT0OpkEoJSORip98MRvLNV",
    "https://drive.google.com/uc?export=download&id=1o8g744KOih2S02Ss7xAeH7ukwKyKXpht"
]

@app.route('/', methods=['POST'])
def main():
    req = request.get_json()
    req_type = req['request']['type']

    # Запуск навыка
    if req_type == 'SimpleUtterance':
        return jsonify({
            "response": {
                "text": "Начинаю тренировку",
                "tts": "Начинаю тренировку",
                "end_session": True
            },
            "version": "1.0",
            "response_directives": [
                {
                    "type": "AudioPlayer.Play",
                    "audio_item": {
                        "stream": {
                            "url": audio_files[0],
                            "offset_in_milliseconds": 0
                        }
                    }
                }
            ]
        })

    # Когда заканчивается один из аудиофайлов
    elif req_type == 'AudioPlayer.PlaybackFinished':
        current_url = req['request']['payload']['audio_item']['stream']['url']
        try:
            next_index = audio_files.index(current_url) + 1
            next_url = audio_files[next_index]
        except (ValueError, IndexError):
            # Все части проиграны
            return jsonify({
                "response": {
                    "text": "Тренировка завершена. Отличная работа!",
                    "tts": "Тренировка завершена. Отличная работа!",
                    "end_session": True
                },
                "version": "1.0"
            })

        return jsonify({
            "response": {
                "text": "",
                "tts": "",
                "end_session": True
            },
            "version": "1.0",
            "response_directives": [
                {
                    "type": "AudioPlayer.Play",
                    "audio_item": {
                        "stream": {
                            "url": next_url,
                            "offset_in_milliseconds": 0
                        }
                    }
                }
            ]
        })

    # По умолчанию — просто завершить
    return jsonify({
        "response": {
            "text": "Навык завершён.",
            "end_session": True
        },
        "version": "1.0"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
