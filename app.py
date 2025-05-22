from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/', methods=['POST'])
def main():
    req = request.get_json()

    res = {
        "response": {
            "text": "",
            "tts": "<speaker audio=\"dialogs-upload/e8946e14-7a9f-4d28-b210-43e493267ff2/7c639f4f-345d-4201-b486-bbf9f46f327e.opus\"/>",
            "end_session": True
        },
        "version": req.get("version", "1.0")
    }

    return jsonify(res)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
