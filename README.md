# CNS Final Project

## Extension

## Server

Default address: 140.112.30.32, port=4443

##### Set up the server
* ssh linux1.csie.ntu.edu.tw

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
https://140.112.30.32:4443/expand?url=SHORTENED_URL
```

##### Check if the URL domain is evil
```
https://140.112.30.32:4443/check?url=SHORTENED_URL
```
