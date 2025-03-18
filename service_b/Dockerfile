FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /apps

COPY --from=ghcr.io/astral-sh/uv:0.5.1 /uv /uvx /bin/

WORKDIR /apps/service_b

ENV UV_LINK_MODE=copy \
    UV_COMPILE_BYTECODE=1 \
    UV_PYTHON_DOWNLOADS=never

COPY ./pyproject.toml ./uv.lock ./
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=./uv.lock,target=service_b/uv.lock \
    --mount=type=bind,source=./pyproject.toml,target=service_b/pyproject.toml \
    uv sync --frozen --no-install-project --no-dev

COPY service_b /apps/service_b

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-dev && uv pip install -e .

WORKDIR /apps/service_b

EXPOSE $PORT

ENV PATH="/apps/service_b/.venv/bin:$PATH"

CMD ["bash"]
