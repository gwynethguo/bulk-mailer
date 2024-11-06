from flask import Flask, send_file, jsonify, request
from dotenv import load_dotenv
from pydantic import ValidationError
from api.models import (
    EmailHistoryPostRequest,
    EmailHistoryGetResponse,
    EmailHistoryGetResponseList,
    EmailCountGetResponse,
    EmailCountGetResponseList,
    TrackingCounterGetResponse,
    TrackingCounterGetResponseList,
)
import os

app = Flask(__name__)

load_dotenv()

import os
from supabase import create_client, Client

url: str = os.getenv("SUPABASE_URL")
key: str = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(url, key)


@app.route("/tracking/pixel", methods=["GET"])
def get_tracking_pixel():
    gif_path = os.path.join(app.root_path, "static", "images", "pixel.gif")
    email_id = request.args.get("email_id")
    recipient_email = request.args.get("recipient_email")

    max_created_at = (
        supabase.table("email_history")
        .select("created_at.max()")
        .eq("email_id", email_id)
        .eq("recipient_email", recipient_email)
        .execute()
        .data[0]
        .get("max")
    )
    supabase.table("email_history").update({"status": "OPENED"}).eq(
        "email_id", email_id
    ).eq("recipient_email", recipient_email).eq("created_at", max_created_at).execute()
    return send_file(gif_path, mimetype="image/gif"), 200


@app.route("/tracking/counter", methods=["GET"])
def get_tracking_counter():
    response = supabase.table("tracking_view").select("*").execute()
    json_data = response.data

    try:
        response_model = TrackingCounterGetResponseList(
            message="Tracking counter retrieved successfully",
            data=[TrackingCounterGetResponse(**item) for item in json_data],
        )
    except ValidationError as e:
        return jsonify({"error": e.errors()}), 422

    return jsonify(response_model.model_dump()), 200


@app.route("/email-history", methods=["POST"])
def insert_email_history():
    try:
        data = EmailHistoryPostRequest(**request.json)
    except ValidationError as e:
        return jsonify({"error": e.errors()}), 422

    json_data = dict(data)
    json_data["email_id"] = str(json_data["email_id"])
    resp = supabase.table("email_history").insert(json_data).execute()
    return (
        jsonify(
            {
                "message": "Email history entry added successfully",
                "data": resp.data,
            }
        ),
        201,
    )


@app.route("/email-history", methods=["GET"])
def get_email_history():
    resp = supabase.table("history_view").select("*").execute()
    json_data = resp.data

    try:
        response_model = EmailHistoryGetResponseList(
            message="Email history retrieved successfully",
            data=[EmailHistoryGetResponse(**item) for item in json_data],
        )
    except ValidationError as e:
        return jsonify({"error": e.errors()}), 422

    return jsonify(response_model.model_dump()), 200


@app.route("/email-count-by-dept", methods=["GET"])
def get_email_history_count():
    resp = supabase.table("email_history").select("department_code, count()").execute()
    json_data = resp.data

    try:
        response_model = EmailCountGetResponseList(
            message="Email count by department retrieved successfully",
            data=[EmailCountGetResponse(**item) for item in json_data],
        )
    except ValidationError as e:
        return jsonify({"error": e.errors()}), 422

    return jsonify(response_model.model_dump()), 200


if __name__ == "__main__":
    app.run(debug=True)
