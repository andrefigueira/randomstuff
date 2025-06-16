import socket
from typing import Dict, Iterable


def scan_ports(host: str, ports: Iterable[int], timeout: float = 1.0) -> Dict[int, bool]:
    """Check if the given ports are open on the host.

    Args:
        host: Target hostname or IP.
        ports: Iterable of ports to scan.
        timeout: Connection timeout in seconds.

    Returns:
        Mapping of port numbers to booleans indicating if the port is open.
    """
    results = {}
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        try:
            sock.connect((host, port))
            results[port] = True
        except Exception:
            results[port] = False
        finally:
            sock.close()
    return results
