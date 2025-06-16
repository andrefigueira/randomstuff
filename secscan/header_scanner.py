from urllib import request
from typing import Dict


def fetch_headers(url: str, timeout: float = 5.0) -> Dict[str, str]:
    """Fetch HTTP response headers for a URL."""
    req = request.Request(url, method="GET")
    with request.urlopen(req, timeout=timeout) as resp:
        headers = dict(resp.headers)
    return headers


def scan_exposed_headers(url: str) -> Dict[str, str]:
    """Check for potentially sensitive headers."""
    headers = fetch_headers(url)
    sensitive = {}
    for name in ["Server", "X-Powered-By"]:
        if name in headers:
            sensitive[name] = headers[name]
    return sensitive
