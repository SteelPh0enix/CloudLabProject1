# Lab8 - Fibonacci - frontend

This is frontend part of dockerized Fibonacci calculator app. It's written in Python using Django framework.

## Running the container stand-alone (for development)

First, build it, nothing special there:

```bash
docker build -t fibo_frontend:dev .
```

Then, you can run it with a handy script file i've made, only thing you have to provide it is the name of the container (with tag, if you have one)

```bash
./run_dev_container.sh fibo_frontend:dev
```

This script runs the container with current directory mounted as /frontend/app (so you don't have to re-build the container every time you make a change), and forwards the app to port 80

### Documentation

This frontend has three pages available:

* `/` - index, an info page with references to fibonacci calculator, project documentation and link to Github repository
* `/fibo_calculator` - fibonacci calculator
* `/documentation` - documentation, copy of `README.md` from repository in HTML format
