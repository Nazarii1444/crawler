Docker

```bash
docker build --no-cache -t fastapi-crawler .
```

```bash
docker run -p 8000:8000 fastapi-crawler
```

```bash
docker-compose up --build
```

## Todo:
- [x] requirements.txt > uv
- [x] middlewares.py
- [x] logger -> config.py
- [x] command to export dependencies
- [x] start.sh in dockerfile
- [x] add variables in docker for start.sh
- [x] add endpoint to check task status
- [ ] configure nginx as reverse proxy
- [ ] uvicorn docs: how to scale workers
- [x] Add timing to url processing
- [x] broker="redis://redis:6379/0", backend="redis://redis:6379/0" -> to config
- [x] Time how long without depth ~587.615065574646s (9.78m)
- [x] (Ideas) crawler with multithreading
- [x] Create router
- [x] UV with requirements.txt in docker