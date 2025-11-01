import json
import socket
import struct
import os
from crypto_utils import (
    ensure_public_key, derive_key_from_password,
    aes_cbc_encrypt, kem_encrypt_with_fallback,
    dsa_keygen_with_fallback, dsa_sign_with_fallback, b64e
)

HOST = "127.0.0.1"
PORT = 65432

def client():
    recipient_pub = ensure_public_key()
    print(f"[CLIENT] Public key length: {len(recipient_pub)}")

    salt = os.urandom(16)
    sym_key = derive_key_from_password(b"demo-password", salt)
    iv, ciphertext = aes_cbc_encrypt(sym_key, b"Quantum-safe banking transaction")

    kem_ct = kem_encrypt_with_fallback(recipient_pub, sym_key)
    pub, priv = dsa_keygen_with_fallback()
    sig = dsa_sign_with_fallback(priv, b64e(kem_ct).encode())

    payload = {
        "kem_ct_b64": b64e(kem_ct),
        "dsa_pub_b64": b64e(pub),
        "dsa_sig_b64": b64e(sig),
        "enc_msg_b64": b64e(ciphertext),
        "iv_b64": b64e(iv),
        "salt_b64": b64e(salt)
    }
    data = json.dumps(payload).encode()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(struct.pack(">I", len(data)))
        s.sendall(data)
    print("[CLIENT] Payload sent successfully.")

if __name__ == "__main__":
    client()
