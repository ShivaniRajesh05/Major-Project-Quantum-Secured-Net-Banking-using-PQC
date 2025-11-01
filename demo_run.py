import threading
import time
import server
import client

def run_demo():
    srv_thread = threading.Thread(target=server.server, daemon=True)
    srv_thread.start()
    time.sleep(1)
    client.client()
    time.sleep(1)

if __name__ == "__main__":
    run_demo()
