# FakeMetric - Prometheus Square Wave Generator

A script to generate a fake Prometheus square wave metric. 


## Run

Using Docker Compose:
```
docker-compose up
```

### python fakemetric.py
```
FakeMetric - Prometheus Square Wave Generator
usage: fakemetric.py [-h] [-p [PORT]] [-t [TIME]] [-m [METRIC]]

FakeMetric - Prometheus Square Wave Generator

optional arguments:
  -h, --help            show this help message and exit
  -p [PORT], --port [PORT]
                        Metric listening port. Default is 8000.
  -t [TIME], --time [TIME]
                        Duration in seconds of each status (low, high).
                        Default is 60 seconds.
  -m [METRIC], --metric [METRIC]
                        Name of exposed metric
```

