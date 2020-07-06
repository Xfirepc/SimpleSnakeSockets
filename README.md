# Snake with Sockets and Pygame

**Requirements**

You need install this libraries to play.

- [Pip](https://pypi.org/)
- [Pygame](https://github.com/pygame/pygame)

This modules are installed on python3
- [Pickle](https://docs.python.org/3/library/pickle.html)
- [Pygame](http://localhost/)
- [Threading](https://docs.python.org/3/library/threading.html)
- [Socket](https://docs.python.org/3/library/socket.html)



**Install**

Install pygame by console.

```shell
git clone https://github.com/Xfirepc/SimpleSnakeSockets
cd SimpleSnakeSockets


py -m pip install -r requirements.txt
# Or
python3 -m pip install -r requirements.txt


```

**Play**

First, you need run server.

```shell
py server.py 127.0.0.1
# Or
python3 server.py localhost

```
Run game and play

```shell
py play.py 127.0.0.1
# Or
python3 play.py localhost

```
The args passed is the server ip by default use localhost,you can pass other ip as the example ```py play.py 192.168.0.100``` 