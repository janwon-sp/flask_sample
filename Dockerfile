FROM python:3.8

# flaskのインストール
RUN pip3 install flask

WORKDIR /app

CMD ["/bin/bash"]