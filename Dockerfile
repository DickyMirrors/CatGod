FROM croncorp/python-ffmpeg:latest
ADD . /app
WORKDIR /app


RUN pip install -f requirements.txt

CMD bash
