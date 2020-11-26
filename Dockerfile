FROM python:3.8

# flask / pytest, pytest-cov のインストール
RUN pip3 install flask pytest pytest-cov

# sqlite3用
RUN mkdir /db

WORKDIR /app

CMD ["/bin/bash"]