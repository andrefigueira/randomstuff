import http.server
import socketserver
import threading
import unittest

from secscan.software_version_scanner import scan_outdated_software


class TestHandler(http.server.BaseHTTPRequestHandler):
    server_version = "Apache/2.2.0"
    sys_version = ""

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"ok")

    def log_message(self, *args, **kwargs):
        pass


class VersionScannerTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.httpd = socketserver.TCPServer(("localhost", 0), TestHandler)
        cls.port = cls.httpd.server_address[1]
        cls.thread = threading.Thread(target=cls.httpd.serve_forever)
        cls.thread.daemon = True
        cls.thread.start()
        cls.url = f"http://localhost:{cls.port}/"

    @classmethod
    def tearDownClass(cls):
        cls.httpd.shutdown()
        cls.httpd.server_close()
        cls.thread.join()

    def test_outdated(self):
        result = scan_outdated_software(self.url)
        self.assertIn("Apache", result)


if __name__ == "__main__":
    unittest.main()
