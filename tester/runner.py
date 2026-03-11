from tester.tests import *

import time
import statistics


def run_tests():

    tests = [
        ("status_code", test_status_code),
        ("content_type", test_content_type),
        ("json_valid", test_json_valid),
        ("file_field", test_file_field),
        ("file_type", test_file_type),
        ("file_url", test_file_url),
    ]

    results = []
    latencies = []

    for name, test in tests:
        start = time.time()

        try:
            test()
            status = "PASS"

        except Exception as e:
            status = "FAIL"

        latency = (time.time() - start) * 1000
        latencies.append(latency)

        results.append({
            "name": name,
            "status": status,
            "latency_ms": latency
        })

    passed = len([r for r in results if r["status"] == "PASS"])
    failed = len([r for r in results if r["status"] == "FAIL"])

    avg = statistics.mean(latencies)
    p95 = statistics.quantiles(latencies, n=20)[18]

    return {
        "summary": {
            "passed": passed,
            "failed": failed,
            "error_rate": failed / len(results),
            "latency_ms_avg": avg,
            "latency_ms_p95": p95
        },
        "tests": results
    }
