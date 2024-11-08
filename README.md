# Установка Docker

```shell
# Добавим Docker репозиторий:
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
```

```shell
# Установим Docker
sudo apt update
sudo apt install docker-ce vim -y
```

```shell
# Убедимся в успешности установки Docker
sudo systemctl status docker
# Если установка прошла неуспешно, команда выдаст ответ:
# Unit docker.service could not be found.
```

```shell
# Добавим Docker в автозагрузку:
sudo systemctl enable docker
```

```shell
# Запуск Docker не из под sudo (Опционально):
sudo groupadd docker
sudo usermod -aG docker ${USER}
newgrp docker
```

```shell
# Протестируем Docker:
docker run hello-world
```

```shell
# Вывод команды:

# Hello from Docker!
# This message shows that your installation appears to be working correctly.
# ...
```


# Управление приложением


## Первоначальный запуск (deploy) приложения в контейнерах

```shell
./scripts/docker_deploy.sh
```

## Остановка всех контейнеров приложения, и удаление образов

```shell
./scripts/docker_delete.sh
```

## Остановка всех контейнров приложения

```shell
./scripts/docker_stop.sh
```

## Запуск (уже созданных с помощью deploy) образов контейнера

```shell
./scripts/docker_start.sh
```

## Посмотреть список запущенных контейнеров

```shell
docker ps -a
```

## Логи контейнера

```shell
docker logs <container_name>
```

## Зайти в shell контейнера

```shell
docker exec -it <container_name> bash
```
