FROM python:3.8

# flask / pytest のインストール
RUN pip3 install flask pytest

# sqlite3用
RUN mkdir /db

WORKDIR /app

CMD ["/bin/bash"]