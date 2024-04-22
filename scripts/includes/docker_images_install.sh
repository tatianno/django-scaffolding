# Criando imagens docker
DJANGO_APP_IMAGE="django-app"
DJANGO_DOCKER_FILE_DIR="$ROOT_DIR/backend/docker/django-app"
NGINX_APP_IMAGE="nginx-app"
NGINX_DOCKER_FILE_DIR="$ROOT_DIR/backend/docker/nginx"
NEXTJS_APP_IMAGE="nextjs-app"
NEXTJS_DOCKER_FILE_DIR="$ROOT_DIR/frontend"

echo "Verificando imagens docker"
sleep 1

if ! docker image inspect "$DJANGO_APP_IMAGE" &> /dev/null; then
    cd $DJANGO_DOCKER_FILE_DIR
    docker build -t "$DJANGO_APP_IMAGE" .
fi

echo "$DJANGO_APP_IMAGE OK"

if ! docker image inspect "$NGINX_APP_IMAGE" &> /dev/null; then
    cd $NGINX_DOCKER_FILE_DIR
    docker build -t "$NGINX_APP_IMAGE" .
fi

echo "$NGINX_APP_IMAGE OK"

if ! docker image inspect "$NEXTJS_APP_IMAGE" &> /dev/null; then
    cd $NEXTJS_DOCKER_FILE_DIR
    docker build -t "$NEXTJS_APP_IMAGE" .
fi

echo "$NEXTJS_APP_IMAGE OK"

cd $CURRENT_DIR