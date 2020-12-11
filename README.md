# Description
a flask projec skeleton

# Usage

Run in dev mode

```
python3 wsgi.py
```

Run in production mode

```
gunicorn -c guni.py wsgi:app
```

Run in Docker 
**NOT READY!!!**

Use `Dockerfile` to build docker image and run.

```
docker build -t <image>:<tag> .
docker run -d -p 80:80 <image>:<tag>
```

