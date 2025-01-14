
# Project-5-Brevets-DB

Reimplement the RUSA ACP control time calculator with flask,
ajax and MongoDB.

## Objectives:

* Understand how can we build multiple container using Docker
  compose.
* Understand the basics of the microservices notion.

## Dependencies:

* Designed for Unix, mostly interoperable on Linux or macOS.
  May also work on Windows, but no promises. A Linux
  virtual machine may work. You may want to test on shared
  server (if available).
* You must install [docker](https://www.docker.com/products/docker-desktop/).

## Instructions:

* You have a minimal implementation of Docker compose under the
  [todo](todo) directory. Using compose, you can connect the flask
  app to MongoDB (as demonstrated in class). We also recommend you
  look at the  `MongoCommands.md` file provided under resources in
  Blackboard.
* You will also need your `acp_times.py` from project-4. Weather
  it is 100% correct or not is not important.
* Given your version of project-4, you will add the following
  functionalities:
  * a) Create two buttons <kbd>Submit</kbd> and <kbd>Display</kbd>
    in the `brevets.html` page.
  * b) On clicking the <kbd>Submit</kbd> button, the control times
    should be entered into the database.
  * c) On clicking the <kbd>Display</kbd> button, the entries
    from the database should be displayed in a new page.
* You have to handle error cases appropriately. For example,
  "Submit" should return an error if there are no control times.
  One can imagine many such cases: you'll come up with as many cases
  as possible.
* For this project you have to use docker-compose just like the
  example we provided under the [todo](todo) directory. Meaning, 
  the database should be running on one container and the application
  on another one.
* We provided the same files found in project-4 here under the
  [brevets'](brevets) directory. Please note that the directory does
  not have a `credentials.ini` file. You have to provide it yourself for
  the application to work as it used to be. Also, you have to copy all
  the files you solved on project-4 (`acp_times.py`, `flask_brevets.py`,
  and `brevets.html`) to this project before you start.
* The `docker-compose.yml` file is not given for the [brevets'](brevets)
  directory. You have to create it yourself.
