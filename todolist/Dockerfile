6 lines (5 sloc)  122 Bytes

FROM python:3.9.12

RUN pip install --upgrade pip
COPY ./ ./
RUN pip install -r requirements.txt
RUN pip install gunicorn