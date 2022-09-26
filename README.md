To check Dockerfile run: </br>
docker build -t test .   </br>
docker run -p 8000:8000 -it test </br>
</br>
</br>
</br>
Push to dockerhub</br>
docker build -t kirillkotovsky/django:1.0 ./web</br>
docker login -u kirillkotovsky </br>
docker push kirillkotovsky/django:1.0</br>
