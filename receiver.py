import sys
import io
import os
import socket
from pathlib import Path

# Fix lỗi Unicode để in tiếng Việt có dấu chính xác trên CI/CD
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

from aes_socket_utils import (
    LENGTH_HEADER_SIZE,
    decrypt_aes_cbc,
    parse_key_packet,
    parse_length_header,
    recv_exact,
)

HOST = os.getenv("RECEIVER_HOST", "0.0.0.0")
DATA_PORT = int(os.getenv("DATA_PORT", "6000"))
KEY_PORT = int(os.getenv("KEY_PORT", "6001"))
TIMEOUT = float(os.getenv("SOCKET_TIMEOUT", "10"))
OUTPUT_FILE = os.getenv("OUTPUT_FILE", "")
LOG_FILE = os.getenv("RECEIVER_LOG_FILE", "")

def receive_key_packet() -> bytes:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((HOST, KEY_PORT))
        server.listen(1)
        # In thông báo để script test bắt đầu chạy sender.py
        print(f"[*] Receiver đang lắng nghe kênh khóa tại {HOST}:{KEY_PORT}", flush=True)
        conn, _ = server.accept()
        with conn:
            conn.settimeout(TIMEOUT)
            key_len_header = recv_exact(conn, 4)
            key_len = int.from_bytes(key_len_header, "big")
            rest = recv_exact(conn, key_len + 16)
            return key_len_header + rest

def receive_data_packet() -> bytes:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((HOST, DATA_PORT))
        server.listen(1)
        print(f"[*] Receiver đang lắng nghe kênh dữ liệu tại {HOST}:{DATA_PORT}", flush=True)
        conn, _ = server.accept()
        with conn:
            conn.settimeout(TIMEOUT)
            length_header = recv_exact(conn, LENGTH_HEADER_SIZE)
            length = parse_length_header(length_header)
            ciphertext = recv_exact(conn, length)
            return length_header + ciphertext

def main() -> None:
    lines = []

    # Bước 1: Nhận Key
    key_packet = receive_key_packet()
    key, iv = parse_key_packet(key_packet)
    line1 = "[+] Đã nhận AES key và IV."
    print(line1, flush=True)
    lines.append(line1)

    # Bước 2: Nhận Data
    data_packet = receive_data_packet()
    length = parse_length_header(data_packet[:LENGTH_HEADER_SIZE])
    ciphertext = data_packet[LENGTH_HEADER_SIZE:]

    if len(ciphertext) != length:
        raise ValueError("Ciphertext nhận được không khớp length header.")

    line2 = "[+] Đã nhận ciphertext."
    print(line2, flush=True)
    lines.append(line2)

    # Giải mã
    plaintext = decrypt_aes_cbc(key, iv, ciphertext)
    message = plaintext.decode("utf-8", errors="replace")

    success_msg = "[+] Đã giải mã thành công."
    plain_msg = f"[+] Bản tin gốc: {message}"
    print(success_msg, flush=True)
    print(plain_msg, flush=True)

    lines.extend([success_msg, plain_msg])

    if OUTPUT_FILE:
        Path(OUTPUT_FILE).write_bytes(plaintext)

    if LOG_FILE:
        Path(LOG_FILE).parent.mkdir(parents=True, exist_ok=True)
        Path(LOG_FILE).write_text("\n".join(lines) + "\n", encoding="utf-8")

if __name__ == "__main__":
    main()