import json
import socket
import struct
from crypto_utils import verify_signature, b64d

HOST = "127.0.0.1"
PORT = 65432

def server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen(1)
        print(f"[SERVER] Listening on {HOST}:{PORT}")
        conn, addr = s.accept()
        with conn:
            print(f"[SERVER] Connected by {addr}")
            raw_len = conn.recv(4)
            msg_len = struct.unpack(">I", raw_len)[0]
            data = conn.recv(msg_len)
            payload = json.loads(data.decode())

            print("[SERVER] Payload received keys:", list(payload.keys()))
            pub = b64d(payload["dsa_pub_b64"])
            sig = b64d(payload["dsa_sig_b64"])
            ok = verify_signature(pub, payload["kem_ct_b64"].encode(), sig)
            print(f"[SERVER] Signature valid: {ok}")

            print(f"[SERVER] KEM ciphertext size: {len(b64d(payload['kem_ct_b64']))}")
            print("[SERVER] Received encrypted banking message (base64):", payload["enc_msg_b64"][:50], "...")
            print("[SERVER] --- End of transaction ---")

if __name__ == "__main__":
    server()
