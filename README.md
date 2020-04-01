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

# For linux
pip install -r requirements.txt

# For windows
py -m pip install -r requirements.txt

```


**Play**

First, you need run server with.

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
The argv passed is the server ip by defaul use localhost but you can pass other ip in the ```py play.py 192.168.0.100``` 