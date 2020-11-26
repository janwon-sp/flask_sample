FROM python:3.8

# sqliteのインストール
RUN apt-get update -y && apt-get install -y sqlite3 libsqlite3-dev\
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# flask / pytest のインストール
RUN pip3 install flask pytest pytest-cov

# sqlite3用
RUN mkdir /db

WORKDIR /app

CMD ["/bin/bash"]