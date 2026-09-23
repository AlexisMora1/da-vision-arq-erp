FROM mcr.microsoft.com/devcontainers/python:1-3.13-bookworm

WORKDIR /workspace

# App (production) dependencies live at the repo root; dev-only tools live next to this Dockerfile.
COPY requirements.txt /tmp/requirements.txt
COPY .devcontainer/requirements.txt /tmp/requirements-dev.txt

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r /tmp/requirements.txt -r /tmp/requirements-dev.txt
