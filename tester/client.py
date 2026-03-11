
import requests
import time

TIMEOUT = 3

def get(url):
    start = time.time()

    try:
        response = requests.get(url, timeout=TIMEOUT)
        latency_ms = (time.time() - start) * 1000

        return {
            "status_code": response.status_code,
            "latency_ms": latency_ms,
            "json": response.json(),
            "headers": response.headers
        }

    except requests.exceptions.Timeout:
        return {
            "status_code": "TIMEOUT",
            "latency_ms": TIMEOUT * 1000,
            "json": None,
            "headers": {}
        }
