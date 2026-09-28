from flask import Flask, jsonify, request

app = Flask(__name__)

EVENTS = [
    {"id": "ev_101", "title": "Jazz Ensemble: Fall Concert", "seatsLeft": 42},
    {"id": "ev_102", "title": "Improv Night", "seatsLeft": 0},
    {"id": "ev_103", "title": "Film Society: Friday Screening", "seatsLeft": 15},
]


@app.get("/events")
def list_events():
    events = EVENTS
    if request.args.get("bookable") == "true":
        events = [event for event in events if event["seatsLeft"] > 0]
    return jsonify({"events": events})


@app.get("/events/<event_id>")
def get_event(event_id):
    event = next((item for item in EVENTS if item["id"] == event_id), None)
    if event is None:
        return jsonify({"error": "not_found"}), 404
    return jsonify(event)


if __name__ == "__main__":
    app.run(port=3000)
