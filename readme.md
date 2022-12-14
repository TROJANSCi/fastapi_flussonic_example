## FastAPI and Flussonic with securing Access to Streams (Authorization with Token) example.

---

### How to run

Run

```sh
$ docker-compose up -d --build
```
+ [FastAPI](https://fastapi.tiangolo.com/) docs: http://127.0.0.1:8000/docs
    * [Playerjs](https://playerjs.com/) url: http://127.0.0.1:8000/playerjs/{video}
    * Iframes url: http://127.0.0.1:8000/embed/{video}

* [Flussonic](https://flussonic.com/) url: http://127.0.0.1:80

---

Flussonic connection setup `settings.hjson`

```
This script gets Flussonic address from a query. String 'http://flussonic-ip'
"flussonic_host": "http://127.0.0.1"

The key from flussonic.conf file. KEEP IT IN SECRET.
"secretkey": "SECRET"

The link will become invalid in 3 hours.
"life_time": 10800

This script gets the stream name from a query. string (script.php?stream=bbc)
"stream_path": "vod/"

(v20.07) Set ipaddr = 'no_check_ip' if you want to exclude client device IP addresses from checking or true for tracking
"ipaddr": true

Allowed time desync between Flussonic and hosting servers in seconds.
"desync": 300
 ```