import http.server
import socketserver
import threading
import unittest

from secscan.header_scanner import scan_exposed_headers, fetch_headers


class TestHandler(http.server.BaseHTTPRequestHandler):
    server_version = "Apache/2.2.0"
    sys_version = ""

    def do_GET(self):
        self.send_response(200)
        self.send_header("X-Powered-By", "PHP/5.6")
        self.end_headers()
        self.wfile.write(b"ok")

    def log_message(self, *args, **kwargs):
        pass


class HeaderScannerTest(unittest.TestCase):
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

    def test_fetch_headers(self):
        headers = fetch_headers(self.url)
        self.assertIn("Server", headers)

    def test_scan_exposed_headers(self):
        exposed = scan_exposed_headers(self.url)
        self.assertIn("Server", exposed)
        self.assertIn("X-Powered-By", exposed)


if __name__ == "__main__":
    unittest.main()
