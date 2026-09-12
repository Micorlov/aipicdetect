FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

WORKDIR /app
ENV UV_COMPILE_BYTECODE=1 UV_LINK_MODE=copy HF_HOME=/data/hf

COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev --no-install-project

COPY src ./src
RUN uv sync --frozen --no-dev

VOLUME /data
EXPOSE 8000
CMD ["uv", "run", "--no-sync", "picai", "serve", "--host", "0.0.0.0", "--port", "8000"]
