FROM croncorp/python-ffmpeg:3.10.4-slim-bullseye
ARG DEBIAN_FRONTEND=noninteractive

# RUN apt update && \
# apt install -y <some packages> \
#   && rm -rf /var/lib/apt/lists/*```

ADD . /app
WORKDIR /app

RUN pip install -r requirements.txt

CMD bash
