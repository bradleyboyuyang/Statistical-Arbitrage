FROM python:3.8-slim-buster
WORKDIR /arb_test
COPY . .
RUN pip3 install -r requirements.txt
CMD ["python3", "test.py"]
