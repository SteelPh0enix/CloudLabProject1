FROM python:3.9-alpine

ENV APP_ROOT_DIR=/frontend

WORKDIR ${APP_ROOT_DIR}

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

COPY run_with_migrations.sh .

CMD ["./run_with_migrations.sh"]

