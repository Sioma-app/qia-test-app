FROM python:3.12-slim
WORKDIR /app
COPY server.py .
COPY static/ static/
ENV PORT=3000
EXPOSE 3000
CMD ["python", "server.py"]
