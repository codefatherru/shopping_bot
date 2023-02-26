

set SIM_BOT_TOKEN=%1

set DOCKER_NAME=simbot

docker build -t %DOCKER_NAME% .
docker rm -f %DOCKER_NAME% || true
docker run --name %DOCKER_NAME% -d --restart=unless-stopped -e SIM_BOT_TOKEN=%SIM_BOT_TOKEN% -e PYTHONUNBUFFERED=1  %DOCKER_NAME%
docker logs -f %DOCKER_NAME%

pause