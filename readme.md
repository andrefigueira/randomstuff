# Security Scanning Tool

This repository contains a simple security scanning library written in Python.
It performs a few basic checks against a given HTTP/HTTPS endpoint:

- **Port scanning** – checks whether specified TCP ports are open.
- **Header exposure** – looks for sensitive HTTP headers like `Server` or `X-Powered-By`.
- **Outdated software** – inspects the `Server` header to detect old web server versions.
- **CORS configuration** – verifies if the endpoint allows any origin (`*`).

Results are returned as a JSON object when using the `secscan.scanner` module
as a script:

```bash
python -m secscan.scanner https://example.com 80,443
```

## Running Tests

The project uses `pytest` for unit tests. Run all tests with:

```bash
python3 -m pytest -q
```
