QUANTUM-SAFE BANKING DEMO FRAMEWORK
-----------------------------------

This demo shows hybrid encryption using PQC + AES in a client-server model.

Dependencies:
-------------
pip install pqcrypto cryptography

File structure:
---------------
crypto_utils.py  -> Shared PQC/AES utilities
server.py        -> Bank server receiving encrypted message
client.py        -> Client encrypting and signing message
demo_run.py      -> Runs both together for demonstration

How to Run:
-----------
Option 1: Run combined demo
> python demo_run.py

Option 2: Run manually
Terminal 1:
> python server.py

Terminal 2:
> python client.py

Expected Output:
----------------
[SERVER] Listening on 127.0.0.1:65432
[CLIENT] Public key length: 64
[CLIENT] Payload sent successfully.
[SERVER] Connected by ('127.0.0.1', port)
[SERVER] Signature valid: True
[SERVER] --- End of transaction ---

You can safely replace the mock encrypt/sign logic inside crypto_utils.py
once pqcrypto provides the full functions in your environment.
