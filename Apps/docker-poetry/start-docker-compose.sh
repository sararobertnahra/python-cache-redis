docker compose down && docker rmi -f $(docker images -aq) && docker compose up --force-recreate -d

curl http://localhost:8001/hello
curl http://localhost:8000/hello
