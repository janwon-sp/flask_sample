# flask_sample
Python3.8 + Flask + sqlite3 でFlaskいじるためのリポジトリ

flaskのソースは[quickstart](https://flask.palletsprojects.com/en/1.1.x/quickstart/)を参考に


## Docker内でのflaskの起動
```
export FLASK_APP=app.py
flask run --host 0.0.0.0
```

## テスト
### テストの実行
```
pytest app_test.py
```

### カバレッジの表示
```
pytest --cov --cov-branch -v app_test.py
```
