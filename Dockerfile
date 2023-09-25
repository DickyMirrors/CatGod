FROM croncorp/python-ffmpeg
ADD . /app
WORKDIR /app

RUN pip install -f requirements.txt

CMD bash
