from prometheus_client import start_http_server, Gauge, REGISTRY
import argparse
import time

def main():
    print('FakeMetric - Prometheus Square Wave Generator')
    parser = argparse.ArgumentParser(
        description='FakeMetric - Prometheus Square Wave Generator')
    parser.add_argument('-p','--port', default=8000, type=int, help='Metric listening port. Default is 8000.', nargs='?')
    parser.add_argument('-t','--time', default=60, type=int, help='Duration in seconds of each status (low, high). Default is 60 seconds.', nargs='?')
    parser.add_argument('-m','--metric', default='fake_metric', type=str, help='Name of exposed metric', nargs='?')
    args = parser.parse_args()

    g = Gauge(args.metric, 'This is a fake square wave metric')
    gaugeValue = False

    print('> Starting web server and processing requests')
    start_http_server(args.port)

    print('> Endless loop started. Press CTRL+C to terminate.')
    try:
        elapsed = args.time
        while True:
            elapsed += 1
            if elapsed > args.time:
                if gaugeValue:
                    g.set(0)
                else:
                    g.set(100)
                gaugeValue = not gaugeValue
                elapsed = 0
            time.sleep(1)
    except KeyboardInterrupt:
        pass
    print('\nFinished.')


if __name__ == "__main__":
    main()
