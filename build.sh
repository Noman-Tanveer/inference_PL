docker build --rm -t fast:latest .
docker run -it -v fast_code:/app --rm -p 8000:8000 fast:latest
