プロジェクト作成
```
$ docker compose run --rm web django-admin startproject new_project_name .
```

マイグレーション実行
```
$ docker compose run --rm web python manage.py migrate
```

アプリ作成
```
$ docker compose run --rm web python manage.py startapp new_app_name
```

起動
```
$ docker compose up --build
```

コンテナ削除
```
$ docker-compose down --volumes --remove-orphans
```