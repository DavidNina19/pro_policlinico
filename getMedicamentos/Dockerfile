FROM python:3.11-alpine
WORKDIR /app
COPY requirements.txt .
RUN apk update \
    && apk add --no-cache gcc musl-dev mariadb-connector-c-dev python3-dev \
    && pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "manage.py", "runserver", "0.0.0.0:5000"]