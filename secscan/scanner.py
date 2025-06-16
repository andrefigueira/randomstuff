import json
from typing import Iterable, Dict, Any

from .port_scanner import scan_ports
from .header_scanner import scan_exposed_headers
from .software_version_scanner import scan_outdated_software
from .cors_scanner import scan_cors


def run_scan(url: str, ports: Iterable[int]) -> Dict[str, Any]:
    host = url.split('://')[-1].split('/')[0]
    results = {
        "open_ports": scan_ports(host, ports),
        "exposed_headers": scan_exposed_headers(url),
        "outdated_software": scan_outdated_software(url),
        "cors_misconfigured": scan_cors(url),
    }
    return results


def scan_to_json(url: str, ports: Iterable[int]) -> str:
    return json.dumps(run_scan(url, ports), indent=2)


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python -m secscan.scanner <url> [ports]")
        sys.exit(1)
    target_url = sys.argv[1]
    ports = [80, 443]
    if len(sys.argv) > 2:
        ports = [int(p) for p in sys.argv[2].split(',')]
    print(scan_to_json(target_url, ports))
