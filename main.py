from youtube_transcript_api import YouTubeTranscriptApi
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/transcript', methods=['POST'])
def get_transcript():
    data = request.json
    video_url = data.get("url")

    if "v=" in video_url:
        video_id = video_url.split("v=")[1].split("&")[0]
    else:
        return jsonify({"error": "Invalid URL"}), 400

    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        full_text = " ".join([line['text'] for line in transcript])
        return jsonify({"transcript": full_text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)