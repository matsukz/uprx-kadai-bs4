## コンテナ操作
* `docker-compose.yml`があるディレクトリでコンソールを起動してコマンド実行
    * 初回起動
        ```cmd
        docker-compose up -d
        ```

    * ２回目以降の起動
        * docker desktopの再生ボタン
    * 停止
        ```
        docker-compose stop
        ```
        もしくは、docker desktopの停止ボタン
    * 削除
        ```
        docker-compose down
        ```
        もしくは、docker desktopの削除ボタン

## pip追加
1. `requirements.txt`に必要なモジュール名を追加します
2. 保存してコンテナを削除します
    ```cmd
    docker-compose down
    ```

3. 以下のコマンドを入力します
    ```cmd
    docker-compose build --no-cache
    ```
4. 初回起動の操作を行ないます
    
## 使い方
docker-desktopで操作します。
1. docker desktopでPythonのコンテナを開く
2. `Exec`のタブを開く
3. `#`が表示されたら以下のコマンドを入力する
    ```bash
    pwd
    ```
    * `/src`が返ってくればOK
    * 違う場合は以下のコマンドを
        ```bash
        cd /src
        ```
    
    * ここがwindows側のsrcフォルダと連動している

4. python実行
    ```bash
    python3 <スクリプト名>
    ```

### ブラウザの観察
1. `localhost:7900`にアクセスします
2. パスワード入力が求められるので`secret`と入力します
