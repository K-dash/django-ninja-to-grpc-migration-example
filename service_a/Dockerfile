FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /apps

RUN apt update \
    && apt upgrade -y \
    && apt install --no-install-recommends -y tzdata curl \
    && apt clean \
    && rm -rf /var/lib/apt/lists/*

COPY --from=ghcr.io/astral-sh/uv:0.5.1 /uv /uvx /bin/

WORKDIR /apps/service_a

ENV UV_LINK_MODE=copy \
    UV_COMPILE_BYTECODE=1 \
    UV_PYTHON_DOWNLOADS=never

COPY ./pyproject.toml ./uv.lock ./
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=./uv.lock,target=service_a/uv.lock \
    --mount=type=bind,source=./pyproject.toml,target=service_a/pyproject.toml \
    uv sync --frozen --no-install-project --no-dev

COPY service_a /apps/service_a

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-dev && uv pip install -e .

WORKDIR /apps/service_a

EXPOSE $PORT

ENV PATH="/apps/service_a/.venv/bin:$PATH"

CMD ["bash"]
