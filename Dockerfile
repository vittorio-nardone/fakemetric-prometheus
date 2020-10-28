FROM python:3.6.8-slim

WORKDIR /app

RUN apt-get -y update  && apt-get install -y \
  python3-dev \
  apt-utils \
  python-dev \
  build-essential \
&& rm -rf /var/lib/apt/lists/*


RUN pip install prometheus_client

# Copy application files
COPY app/* ./

# Modify CMD to run the app that you require. 
CMD ["/bin/bash"]