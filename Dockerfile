FROM python:3.11-slim

WORKDIR /app
COPY batch.py /app/batch.py

# 動作確認用：ログを即時に出す
ENV PYTHONUNBUFFERED=1

CMD ["python", "/app/batch.py"]