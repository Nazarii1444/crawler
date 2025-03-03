FROM python:3.11

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./src /app/src

COPY ./start.sh /app/start.sh
RUN chmod +x /app/start.sh

ENV PYTHONPATH=/app
ENV C_FORCE_ROOT=1

EXPOSE 8000

CMD ["/app/start.sh", "server"]