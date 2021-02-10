# Container image that runs your code
FROM python:3.7-alpine

# Install pre-req
COPY requirements.txt /
RUN pip install -r /requirements.txt

# Copies your code file from your action repository to the filesystem path `/` of the container
COPY entrypoint.py /entrypoint.py

# Code file to execute when the docker container starts up (`entrypoint.sh`)
ENTRYPOINT ["python3", "-u", "/entrypoint.py"]
