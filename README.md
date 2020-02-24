# Short_URL
A short url API server application. (Flask + Redis + Container)

## Quick Start
```
$ docker-compose up
```

## Test subcommand
```
$ curl --header "Content-Type: application/json"   --request POST   --data '{"url":"http://tw.yahoo.com"}'   http://localhost:8080/shortURL
```

## Features
1. Use Flask as API framework for this project.
2. Use redis as database.
3. This project could run in container, so don't need to install redis and flask. Just start up the container, then you could test short api in your localhost.

## How it works
```
.
├── app.py              // Start point
├── backend             // Dockerfile for server image
├── conf                // Configuration for server
│   ├── conf.ini
├── docker-compose.yml  // You could use this file to start up the container.
├── README.md 
├── requirements.txt    // Required python package
└── router
    ├── helper.py       // Define helper function for short url service
    ├── __init__.py     // Define router
...
```

## Demo
* Test url
```
https://tw.news.yahoo.com/topic/yahoo-today
```
![](https://raw.githubusercontent.com/amosricky/Short_URL/master/src/demo.gif)

* Postman demo
![](https://raw.githubusercontent.com/amosricky/Short_URL/master/src/demo_postman.png)