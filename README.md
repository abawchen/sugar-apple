## Sugar-Apple

### apple (backend)

On the terminal, create a new virtual python environment by [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/):
```shell
$ mkvirtualenv --python=$(which python3.5) venv
```

With the virtual environment activated, install related packages:
```shell
$ cd apple
$ pip install -r requirements.txt
```

Create `apple/app/instance/config.py` for `SQLALCHEMY_DATABASE_URI`, and you have to setup the corresponding database at the same time, sample config as:
```
SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://root:password@127.0.0.1:3306/sugar-apple'
```

[Experimental] Install the interactive sugar-apple backend cli (called apple):
```shell
$ pip install --editable .
```

Use cli to persist data to database:
```shell
$ sugar-apple
Version: 0.0.1
Syntax: apple <command> [params] [options]
apple> apple download
apple> apple unzip
apple> apple transcode
apple> apple normalize
apple> apple persist
apple> exit
```

Start flask server:
```shell
$ export FLASK_APP=app/app.py && flask run -p 5001
```

Then you can visit `http://127.0.0.1:5001/graphql` to test graphql

---

*Happy Coding!*