# send_dummy_transactions.py
import json
import socket
import struct
import time

HOST = "127.0.0.1"
PORT = 65432

def send_payload(payload: dict):
    data = json.dumps(payload).encode()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(struct.pack(">I", len(data)))  # 4-byte length prefix
        s.sendall(data)

def run_sender(json_path="dummy_transactions.json", pause_s=0.5):
    with open(json_path, "r") as f:
        txs = json.load(f)
    for i, payload in enumerate(txs, 1):
        print(f"[SENDER] Sending transaction #{i}")
        try:
            send_payload(payload)
            print(f"[SENDER] Sent #{i}")
        except Exception as e:
            print(f"[SENDER] Failed to send #{i}: {e}")
        time.sleep(pause_s)

if __name__ == "__main__":
    run_sender()
