FROM python:3.9-alpine

ENV APP_ROOT_DIR=/backend

WORKDIR ${APP_ROOT_DIR}

# Install dependencies for wait-for-it
RUN apk update && apk add bash

# Setup virtualenv by moving it's /bin to the beginning of PATH
ENV VIRTUAL_ENV_PATH=${APP_ROOT_DIR}/venv
RUN python3 -m venv ${VIRTUAL_ENV_PATH}
ENV PATH="$VIRTUAL_ENV_PATH/bin:$PATH"

# Install the required packages
COPY requirements.txt .
RUN pip install -r requirements.txt

# Setup the app environment and run it
# Make sure to bind-mount the /app directory!
WORKDIR ${APP_ROOT_DIR}/app

ENV FLASK_APP=fibonacci
ENV FLASK_ENV=development

COPY wait-for-it.sh .
COPY wait_for_db_and_run.sh .
CMD ["./wait_for_db_and_run.sh"]
# CMD ["python", "-m", "flask", "run", "--no-debugger", "--host", "0.0.0.0", "--port", "8080"]
