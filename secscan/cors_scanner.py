from .header_scanner import fetch_headers


def scan_cors(url: str) -> bool:
    """Return True if CORS policy appears misconfigured."""
    headers = fetch_headers(url)
    origin = headers.get("Access-Control-Allow-Origin")
    if origin == "*":
        return True
    return False
