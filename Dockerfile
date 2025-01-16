FROM python:3.11-slim-bullseye

# Taken from https://stackoverflow.com/questions/53835198/integrating-python-poetry-with-docker
ENV YOUR_ENV=prod \
  PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  # Poetry's configuration:
  POETRY_NO_INTERACTION=1 \
  POETRY_VIRTUALENVS_CREATE=false \
  POETRY_CACHE_DIR='/var/cache/pypoetry' \
  POETRY_HOME='/usr/local' \
  POETRY_VERSION=1.8.2

RUN apt update && \
    apt upgrade -y && \
    apt install -y curl ffmpeg libsm6 libxext6

# System deps:
RUN curl -sSL https://install.python-poetry.org | python -

# Copy only requirements to cache them in docker layer
WORKDIR /workdir

ADD pyproject.toml README.md /workdir/

# RUN poetry install --no-directory $(test "$YOUR_ENV" == prod && echo "--only=main") --no-interaction

RUN poetry install --no-directory --with nocuda  --no-interaction

ADD src /workdir/
ADD scripts /workdir/

EXPOSE 8888

# Project initialization:
RUN poetry install $(test "$YOUR_ENV" == prod && echo "--only=main") --no-interaction

WORKDIR /workdir/home

ENTRYPOINT [ "poetry", "run" ]
CMD [ "jupyter", "lab", "--no-browser", "--allow-root", "--ip", "0.0.0.0", "--NotebookApp.token=''", "--NotebookApp.password=''" ]