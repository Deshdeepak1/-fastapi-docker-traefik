# FastAPI with Docker and Traefik


## How to excecute


### Development

`docker-compose up -d --build`

Api - http://fastapi.localhost:8008/
Traefik dashboard - http://fastapi.localhost:8008/

Download csv.gz file - `wget --content-disposition --method POST http://fastapi.localhost:8008/file`


### Production

- Change domain in docker-compose.prod.yml
- Change email in traefik.prod.toml

`docker-compose -f docker-compose.prod.yml up -d --build`

Api - https://fastapi-traefik.deshdeepak.xyz/
Download csv.gz file - `wget --content-disposition --method POST https://fastapi-traefik.deshdeepak.xyz/file`
