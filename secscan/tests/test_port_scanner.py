import socketserver
import threading
import unittest

from secscan.port_scanner import scan_ports


class DummyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        self.request.close()


class PortScannerTest(unittest.TestCase):
    def setUp(self):
        self.server = socketserver.TCPServer(("localhost", 0), DummyTCPHandler)
        self.port = self.server.server_address[1]
        self.thread = threading.Thread(target=self.server.serve_forever)
        self.thread.daemon = True
        self.thread.start()

    def tearDown(self):
        self.server.shutdown()
        self.server.server_close()
        self.thread.join()

    def test_scan_open_port(self):
        result = scan_ports("localhost", [self.port])
        self.assertTrue(result[self.port])

    def test_scan_closed_port(self):
        closed = self.port + 1
        result = scan_ports("localhost", [closed])
        self.assertFalse(result[closed])


if __name__ == "__main__":
    unittest.main()
