FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

RUN useradd -m -u 1000 app

WORKDIR /app
ENV UV_COMPILE_BYTECODE=1 UV_LINK_MODE=copy HF_HOME=/data/hf

COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev --no-install-project

COPY src ./src
RUN uv sync --frozen --no-dev

# Hugging Face Spaces runs the container as uid 1000; keep the model cache and app writable for it
RUN mkdir -p /data && chown -R app:app /data /app
USER app

VOLUME /data
EXPOSE 8000
CMD ["uv", "run", "--no-sync", "aipicdetect", "serve", "--host", "0.0.0.0", "--port", "8000"]
