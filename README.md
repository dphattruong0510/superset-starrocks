# This is the docker compose file include : starrocks-allin1 , superset, postgresql(store metadata of superset) , redis and customization image icon and app name
### For using : 
  - Clone the repo
  - Run the command  to access CLI MySQL of Starrocks: docker exec -it starrocks mysql -P 9030 -h 127.0.0.1 -u root --prompt="StarRocks > "
  - CREATE DATABASE quickstart; USE quickstart;
  - Then open http://localhost:8088 to access superset
    + username: admin / password: admin
  - Connect to starrocks through MySQL connector : port 9030 , database: quickstart, username: root, password : blank
