FROM python:3.7.2-alpine3.8

# Set up octobot's environment
COPY . /bot/ogame
WORKDIR /bot/ogame

# installation
RUN pip3 install -r requirements.txt

ENTRYPOINT ["python", "./start.py"]
