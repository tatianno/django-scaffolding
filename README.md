# Scaffoding para projeto com Django e Nextjs


## Arquivo .env

```
SECRET_KEY=<SECRET KEY>

MYSQL_HOST=<HOST>
MYSQL_ROOT_PASSWORD=<PASSWORD>
MYSQL_DATABASE=<DB_NAME>
MYSQL_USER=<USERNAME>
MYSQL_PASSWORD=<PASSWORD>

RABBITMQ_HOST=rabbitmq
RABBITMQ_DEFAULT_USER=<USERNAME>
RABBITMQ_DEFAULT_PASS=<PASSWORD>

REDIS_SERVER=<HOST REDIS>

MYSQL_DIR=/usr/src/django-scaffod/backend/docker/mysql/data
NGINX_DIR=/usr/src/django-scaffod/backend/docker/nginx
LETS_ENCRYPT_DIR=/usr/src/django-scaffod/backend/docker/letsencrypt
BACKEND_DIR=/usr/src/django-scaffod/backend/src
FRONTEND_DIR=/usr/src/django-scaffod/frontend
ROMETHEUS_DIR=/usr/src/django-scaffod/sre/prometheus
GRAFANA_DIR=/usr/src/django-scaffod/sre/grafana
UID=1000
GID=1000
```