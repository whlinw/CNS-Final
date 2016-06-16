# CNS Final Project

## Extension

## Server

Default address: 140.112.30.39, port=4443

##### Set up the server
* ssh linux1.ntu.edu.tw

* Generate certificate
```
$ openssl req -newkey rsa:2048 -nodes -keyout domain.key -x509 -days 365 -out domain.crt
```

* Run server
```
$ python server.py
```

##### Get the expanded URL
```
https://140.112.30.39:4443/expand?url=SHORTENED_URL
```
