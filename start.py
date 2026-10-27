#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Chạy ứng dụng Web học 360 Động Từ Bất Quy Tắc Tiếng Anh
"""
import http.server
import socketserver
import webbrowser
import os
import sys

PORT = 8000
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

def run():
    os.chdir(DIRECTORY)
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        url = f"http://localhost:{PORT}/index.html"
        print("=" * 60)
        print("✨ ỨNG DỤNG HỌC 360 ĐỘNG TỪ BẤT QUY TẮC TIẾNG ANH ĐANG CHẠY ✨")
        print(f"👉 Mở trình duyệt tại: {url}")
        print("👉 Nhấn Ctrl + C để dừng máy chủ")
        print("=" * 60)
        try:
            webbrowser.open(url)
        except Exception:
            pass
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nĐã dừng máy chủ. Tạm biệt!")
            sys.exit(0)

if __name__ == "__main__":
    run()
