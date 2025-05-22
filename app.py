from flask import Flask, request, jsonify
import os

app = Flask(__name__)

tracks = [
    "dialogs-upload/e8946e14-7a9f-4d28-b210-43e493267ff2/7c639f4f-345d-4201-b486-bbf9f46f327e.opus",
    "dialogs-upload/e8946e14-7a9f-4d28-b210-43e493267ff2/0e4c93f1-019d-4c8f-9195-e0f709b6d51f.opus",
    "dialogs-upload/e8946e14-7a9f-4d28-b210-43e493267ff2/a0acbef5-5562-49cc-966d-0f9bc35eba43.opus",
    "dialogs-upload/e8946e14-7a9f-4d28-b210-43e493267ff2/ac484922-1130-45e1-9ede-a8a13d8c6e11.opus"
]

prompts = [
    "Отличный старт. Хочешь продолжить?",
    "Продолжим тренировку?",
    "Ты почти у цели. Продолжаем?"
]

def make_response(text, tts, end_session=False):
    return {
        "response": {
            "text": text,
            "tts": tts,
            "end_session": end_session
        },
        "version": "1.0"
    }

@app.route('/', methods=['POST'])
def main():
    req = request.get_json()
    session = req.get("session")
    user_input = req["request"].get("original_utterance", "").lower()
    state = session.get("state", {})
    step = state.get("step", 0)

    if session.get("new", False):
        step = 0
        tts = f"Запускаю тренировку. <speaker audio=\"{tracks[0]}\"/>"
        text = "Запускаю тренировку"
        step += 1
        state["step"] = step
        return jsonify(make_response(text, tts, end_session=False))

    if step == 1:
        if user_input in ["да", "конечно", "ага", "хочу", "дальше", "продолжить"]:
            tts = f"<speaker audio=\"{tracks[1]}\"/> {prompts[1]}"
            text = prompts[1]
            step += 1
        else:
            tts = "Хорошо, тренировка завершена."
            text = "Тренировка завершена"
            return jsonify(make_response(text, tts, end_session=True))

    elif step == 2:
        if user_input in ["да", "конечно", "ага", "хочу", "дальше", "продолжить"]:
            tts = f"<speaker audio=\"{tracks[2]}\"/> {prompts[2]}"
            text = prompts[2]
            step += 1
        else:
            tts = "Хорошо, тренировка завершена."
            text = "Тренировка завершена"
            return jsonify(make_response(text, tts, end_session=True))

    elif step == 3:
        if user_input in ["да", "конечно", "ага", "хочу", "дальше", "продолжить"]:
            tts = f"<speaker audio=\"{tracks[3]}\"/>"
            text = "Последний трек"
            step += 1
            return jsonify(make_response(text, tts, end_session=True))
        else:
            tts = "Хорошо, тренировка завершена."
            text = "Тренировка завершена"
            return jsonify(make_response(text, tts, end_session=True))
    else:
        tts = "Тренировка завершена."
        text = "Тренировка завершена"
        return jsonify(make_response(text, tts, end_session=True))

    state["step"] = step
    session["state"] = state
    return jsonify(make_response(text, tts, end_session=False))

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
