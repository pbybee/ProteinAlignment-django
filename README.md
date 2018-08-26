# ProteinAlignment-django

This is a simple protein alignment app written for django with nginx webserver, postgres database, and deployed with docker-compose

To run this site. Clone the repo and run docker-compose commands.

```
git clone git@github.com:pbybee/ProteinAlignment-django.git
cd ProteinAlignment-django/web
sudo docker-compose build
sudo docker-compose up
```

In a web browswer navigate to [localhost:80/align](localhost/align](although you shouldn't need to specify port 80)

![running docker-compose](https://github.com/pbybee/ProteinAlignment-django/blob/master/docker-compose-cmds.gif)

![doing an alignment](https://github.com/pbybee/ProteinAlignment-django/blob/master/web%20port%2080.gif)
