````markdown
# 🧠 Quantum-Safe Banking Framework

This project demonstrates **hybrid encryption** using **Post-Quantum Cryptography (PQC)** in a simple **client–server model**.

---

## 📦 Dependencies

Install required Python packages:
```bash
pip install pqcrypto cryptography
````

---

## 📁 File Structure

| File              | Description                                            |
| ----------------- | ------------------------------------------------------ |
| `crypto_utils.py` | Shared PQC + AES utility functions                     |
| `server.py`       | Bank server receiving encrypted messages               |
| `client.py`       | Client that encrypts and signs messages                |
| `demo_run.py`     | Runs both client and server together for demonstration |

---

## 🚀 How to Run:

### Option 1: Run the combined demo

```bash
python demo_run.py
```

### Option 2: Run manually

Open two terminals:

**Terminal 1:**

```bash
python server.py
```

**Terminal 2:**

```bash
python client.py
```

---

## 💡 Expected Output

```
[SERVER] Listening on 127.0.0.1:65432
[CLIENT] Public key length: 64
[CLIENT] Payload sent successfully.
[SERVER] Connected by ('127.0.0.1', port)
[SERVER] Signature valid: True
[SERVER] --- End of transaction ---
```

---

## Overview

This demo highlights how **quantum-safe encryption** can be integrated into financial communication systems, ensuring security even in the post-quantum era.

---




