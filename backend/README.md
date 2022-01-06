# Lab8 - Fibonacci - backend

This is backend part of dockerized Fibonacci calculator app. It's written in Python using Flask framework.

## Running the container stand-alone (for development)

First, build it, nothing special involved there:

```bash
docker build -t fibo_backend:dev .
```

Then, you can run it with a handy script file i've made, only thing you have to provide it is the name of the container (with tag, if you have one)

```bash
./run_dev_container.sh fibo_backend:dev
```

This script runs the container with current directory mounted as /backend/app (so you don't have to re-build the container every time you make a change), and forwards the app to port 8080

### IMPORTANT: Database requirements

The backend is currently configured to work with database that should be running in separate container. Since the instruction above was made before integrating the backend with database, i strongly recommend running the whole application with `docker-compose` instead of the single dockerfile, otherwise you will have to modify the code to connect to locally hosted MySQL instance.

Note that code hot-reloading will work even when the backend is run via `docker-compose`, so there's really no down-side of that, except longer startup time.

## Documentation

This backend is extremely simple, and the list of HTTP endpoints (with examples) is provided below:

| Endpoint                  | Example         | Response                                                                       | Description                                                                                                                       |
|---------------------------|-----------------|--------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| `/calculate/<number:int>` | `/calculate/10` | `{ "requested": 10, "requested_value_too_big": false, "value": 55 }`           | Calculates the value of `number`th element in fibonacci sequence and returns a JSON response.                                     |
|                           | `/calculate/51` | `{ "requested": 51, "requested_value_too_big": true, "value": 0 }`             | Requested value limit is 50, hard-coded.                                                                                          |
| `/history/<items:int>`    | `/history/5`    | `{ "count": 2, "items": [{"index": 3, "value": 2}, {"index": 5, "value": 5}]}` | Returns a JSON with item count, and list of fibonacci's sequence values and it's indexes sorted by date and time of calculation.  |
|                           | `/history/5`    | `{ "count": 0, "items": []}`                                                   | If there's no items in history, list will be empty.                                                                               |

## Additional scripts

There are two additional scripts in this directory, used by the container:

* `wait-for-it.sh` - courtesy of [vishnubob](https://github.com/vishnubob/wait-for-it), a script that i'm using for delaying the startup of backend server until the database is up and running
* `wait_for_db_and_run.sh` - the script that's executed by container to start the app, runs the script above and the starts the server
