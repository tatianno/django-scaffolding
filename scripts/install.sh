CURRENT_DIR=$(pwd)
ROOT_DIR=$(cd ../ && pwd)
PROMETHEUS_DIR="$ROOT_DIR/sre/prometheus/data"
GRAFANA_DIR="$ROOT_DIR/sre/grafana"
ENV_PATH="$ROOT_DIR/.env"
GID=$(id -g)

# source includes/docker_images_install.sh

mkdir -p $PROMETHEUS_DIR
mkdir -p $GRAFANA_DIR

chown -R $UID:$GID $PROMETHEUS_DIR
chown -R $UID:$GID $GRAFANA_DIR

if ! grep -q "UID=1000" $ENV_PATH; then
    echo "UID=$UID" >> $ENV_PATH
fi

if ! grep -q "GID=1000" $ENV_PATH; then
    echo "GID=$GID" >> $ENV_PATH
fi

cd $ROOT_DIR