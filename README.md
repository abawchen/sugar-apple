## Sugar-Apple

這是一個從[政府資料開放平臺](https://data.gov.tw/)抓取[不動產買賣實價登錄批次資料](https://data.gov.tw/dataset/6213)的專案，可將下載資料轉檔進資料庫。將持續開發以下功能：

- Backend
    - [ ] Data query api by graphQL
    - [ ] Integration with more meta / real estate data 
      - [x] Crawler task (refer to [crawler](https://github.com/abawchen/sugar-apple/wiki/Cralwer))
      - [ ] Data integration 
    - [ ] Find out the bargaining space
- Frontend(Web)
    - [ ] Friendly ui query
    - [ ] Data visualization

### apple (backend)

On the terminal, create a new virtual python environment by [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/), or refer [cheatsheet](https://github.com/abawchen/sugar-apple/wiki#cheatsheet) for more detail:
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

### sugar (frontend)

Install dependencies:
```bash
$ cd sugar
$ yarn
```

Configure Webpack:
```bash
# for development
$ cp webpack.config.example.js webpack.config.dev.js

# for production
$ cp webpack.config.example.js webpack.config.prod.js
```

Output bundle:
```bash
# for development
$ npm run build:dev

# for production
$ npm run build
```

Start dev server:
```bash
$ npm start
```
Now the client app is running at `http://{webpackDevServerHost}:{webpackdevServerPort}`

---

*Happy Coding!*
