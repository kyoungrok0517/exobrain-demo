# exo_web
good

# Docker 이미지 삭제

```
sudo docker stop $(sudo docker ps -a -q)
sudo docker rm $(sudo docker ps -a -q)
sudo docker rmi $(sudo docker images -q)
```

# Docker Django Server Run

```
sudo docker build -t exo_web .
sudo docker run -d -p 80:80 --name exo_web_container exo_web
```
