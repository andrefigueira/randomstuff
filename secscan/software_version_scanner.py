from typing import Dict, Tuple
from .header_scanner import fetch_headers

# Minimal version map for demonstration purposes
MIN_VERSIONS = {
    "Apache": (2, 4),  # require >= 2.4
    "nginx": (1, 18),
}


def parse_version(value: str) -> Tuple[int, ...]:
    numbers = []
    for part in value.split('.'):
        if part.isdigit():
            numbers.append(int(part))
        else:
            break
    return tuple(numbers)


def scan_outdated_software(url: str) -> Dict[str, str]:
    headers = fetch_headers(url)
    server = headers.get("Server")
    result = {}
    if server:
        for name, min_ver in MIN_VERSIONS.items():
            if server.startswith(name):
                version_part = server.split('/')[-1].split()[0]
                version = parse_version(version_part)
                if version and version < min_ver:
                    result[name] = version_part
                break
    return result
