import requests
import time

TIMEOUT = 3

def get(url):
    start = time.time()

    try:
        # Désactive l'utilisation des proxies d'environnement
        session = requests.Session()
        session.trust_env = False

        response = session.get(url, timeout=TIMEOUT)

        latency_ms = (time.time() - start) * 1000

        return {
            "status_code": response.status_code,
            "latency_ms": latency_ms,
            "json": response.json(),
            "headers": response.headers
        }

    except Exception:
        return {
            "status_code": "ERROR",
            "latency_ms": TIMEOUT * 1000,
            "json": None,
            "headers": {}
        }
