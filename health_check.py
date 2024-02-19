import yaml
import requests
import time
from collections import defaultdict
import signal
import sys


def fetch_health_check(config_file_path):
    with open(config_file_path, 'r') as config_file:
        endpoints = yaml.safe_load(config_file)

    domain_stats = defaultdict(lambda: {'total': 0, 'up': 0})

    def signal_handler(signal, frame):
        print("\nProgram interrupted by user.")
        print("Final availability percentages:")
        print_availability_percentage(domain_stats)
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)

    while True:
        print("Starting test cycle...")
        for endpoint in endpoints:
            name = endpoint['name']
            url = endpoint['url']
            method = endpoint.get('method', 'GET')
            headers = endpoint.get('headers', {})
            body = endpoint.get('body')

            try:
                start_time = time.time()
                response = requests.request(method, url, headers=headers, json=body)
                latency = int((time.time() - start_time) * 1000)  # Convert to milliseconds
                status = response.status_code
            except requests.RequestException:
                status = -1
                latency = -1

            outcome = "UP" if 200 <= status < 300 and latency < 500 else "DOWN"

            domain = url.split('/')[2]
            domain_stats[domain]['total'] += 1
            if outcome == "UP":
                domain_stats[domain]['up'] += 1

            print(f"Endpoint '{name}' is {outcome}. Response code: {status}. Latency: {latency} ms")

        print("Test cycle completed.")
        print("Availability percentages:")
        print_availability_percentage(domain_stats)

        time.sleep(15)


def print_availability_percentage(domain_stats):
    for domain, stats in domain_stats.items():
        total = stats['total']
        up = stats['up']
        percentage = round(up / total * 100) if total != 0 else 0
        print(f"{domain} has {percentage}% availability percentage")


if __name__ == "__main__":
    config_file_path = sys.argv[1]
    fetch_health_check(config_file_path)


##### python health_check.py path/to/config.yaml