import json
import os
import boto3
from decimal import Decimal

# ---- Config (set these as Lambda environment variables) ----
TABLE_NAME = os.environ.get("TABLE_NAME", "MyResumeViewCount")
REGION = os.environ.get("AWS_REGION", "us-east-1")

# Allow only your site(s). Comma-separated env var recommended.
# Example: https://jonathanlayman.com,https://www.jonathanlayman.com
ALLOWED_ORIGINS = [o.strip() for o in os.environ.get("ALLOWED_ORIGINS", "https://jonathanlayman.com").split(",")]

dynamodb = boto3.resource("dynamodb", region_name=REGION)
table = dynamodb.Table(TABLE_NAME)

def _get_method(event: dict) -> str:
    # REST API: event["httpMethod"]
    # HTTP API / Function URL: event["requestContext"]["http"]["method"]
    return (
        event.get("httpMethod")
        or event.get("requestContext", {}).get("http", {}).get("method")
        or ""
    ).upper()

def _get_origin(event: dict) -> str:
    headers = event.get("headers") or {}
    # header casing varies
    return headers.get("origin") or headers.get("Origin") or ""

def _cors_headers(origin: str) -> dict:
    # Only reflect back an allowed origin (never "*")
    if origin in ALLOWED_ORIGINS:
        return {
            "Access-Control-Allow-Origin": origin,
            "Vary": "Origin",
            "Access-Control-Allow-Methods": "GET,OPTIONS",
            "Access-Control-Allow-Headers": "Content-Type",
        }
    # If no origin (e.g., curl/Postman), you can omit CORS headers
    return {}

def _json(status: int, body: dict, origin: str = "") -> dict:
    headers = {
        "Content-Type": "application/json",
        **_cors_headers(origin),
    }
    return {
        "statusCode": status,
        "headers": headers,
        "body": json.dumps(body, default=lambda x: float(x) if isinstance(x, Decimal) else str(x)),
    }

def lambda_handler(event, context):
    method = _get_method(event)
    origin = _get_origin(event)

    # Handle browser CORS preflight
    if method == "OPTIONS":
        # If origin isn't allowed, you can return 403 to be strict
        if origin and origin not in ALLOWED_ORIGINS:
            return _json(403, {"error": "Origin not allowed"}, origin)
        return {
            "statusCode": 204,
            "headers": _cors_headers(origin) | {"Content-Type": "application/json"},
            "body": "",
        }

    # Only allow GET for the counter
    if method != "GET":
        return _json(405, {"error": "Method not allowed"}, origin)

    # If this request came from a browser, enforce allowed origin
    if origin and origin not in ALLOWED_ORIGINS:
        return _json(403, {"error": "Origin not allowed"}, origin)

    try:
        # Atomic counter increment
        response = table.update_item(
            Key={"id": "views"},
            UpdateExpression="SET #c = if_not_exists(#c, :start) + :inc",
            ExpressionAttributeNames={"#c": "count"},
            ExpressionAttributeValues={":inc": 1, ":start": 0},
            ReturnValues="UPDATED_NEW",
        )

        views_count = response["Attributes"]["count"]
        return _json(200, {"views": views_count}, origin)

    except Exception as e:
        # Avoid leaking internals in production; log server-side instead
        print("ERROR:", str(e))
        return _json(500, {"error": "Internal server error"}, origin)