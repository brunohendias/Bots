FROM python:alpine

WORKDIR /app

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY requirements.txt ./
RUN pip install -r requirements.txt

RUN TZ=America/New_York

COPY . .

CMD ["jurigged", "-v","run.py"]
