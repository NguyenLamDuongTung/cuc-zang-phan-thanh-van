import http.server
import socketserver
import threading
import webbrowser
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
HTML_FILE = BASE_DIR / "index_touch_heart.html"
HOST = "127.0.0.1"
PORT = 8000


class ReusableTCPServer(socketserver.TCPServer):
    allow_reuse_address = True


def open_browser():
    webbrowser.open(f"http://{HOST}:{PORT}/{HTML_FILE.name}")


def main():
    if not HTML_FILE.exists():
        print(f"Không tìm thấy file: {HTML_FILE}")
        print("Hãy đặt index_touch_heart.html cùng thư mục với PythonApplication2.py")
        return

    os.chdir(BASE_DIR)
    handler = http.server.SimpleHTTPRequestHandler

    with ReusableTCPServer((HOST, PORT), handler) as httpd:
        print(f"Đang chạy web tại: http://{HOST}:{PORT}/{HTML_FILE.name}")
        print("Nhấn Ctrl+C để dừng server.")

        threading.Timer(1.0, open_browser).start()

        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nĐã dừng server.")


if __name__ == "__main__":
    main()
