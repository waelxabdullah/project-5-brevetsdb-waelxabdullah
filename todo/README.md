# Build Instructions

To build this project, all you need is to run the following command:

```shell
docker-compose up -d
```

The command above will build two images one for the `web` service
and one for the database `db` service. Also, it will create two images
named dynamically based on the root directory, the service, and the
instant id. In this example the root directory is named `todo`. Thus, 
we will have two containers named `todo-web-1` and `todo-db-1`.

If you want to silence the containers, you can use the `-d` option.
```shell
docker-compose up -d
```

Example:
```shell
docker-compose up -d           
[+] Running 3/3
 ✔ Network todo_default  Created
 ✔ Container todo-db-1   Started 
 ✔ Container todo-web-1  Started 
```

Once you are done, you can use the command below to tear down the
containers and delete them.

```shell
docker-compose down
```

Example:
```shell
docker-compose down 
[+] Running 3/2
 ✔ Container todo-web-1  Removed                                                                                                        0.8s 
 ✔ Container todo-db-1   Removed                                                                                                        0.1s 
 ✔ Network todo_default  Removed                                                                                                        0.1s
```