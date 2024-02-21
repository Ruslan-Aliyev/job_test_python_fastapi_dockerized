This is a dockerized version of https://github.com/Ruslan-Aliyev/job_test_python_fastapi

# Usage

```
docker-compose up -d --build
docker-compose exec fastapi-docker poetry run alembic upgrade head
```

CRUDs remains the same: https://github.com/Ruslan-Aliyev/job_test_python_fastapi?tab=readme-ov-file#usage

# Tutorials

- PIP
  - https://github.com/AmishaChordia/FastAPI-PostgreSQL-Docker 
  - https://testdriven.io/blog/fastapi-docker-traefik/
    - https://github.com/testdrivenio/fastapi-docker-traefik 
- Poetry
  - https://stackoverflow.com/questions/53835198/integrating-python-poetry-with-docker/54763270#54763270 
  - https://fastapi.tiangolo.com/deployment/docker/
  - https://github.com/Kostiantyn-Salnykov/fastapi_quickstart 
  - https://github.com/svx/poetry-fastapi-docker
  - https://github.com/brent-stone/fastapi_demo 
  - https://github.com/Salfiii/fastapi-template 
  - https://medium.com/@albertazzir/blazing-fast-python-docker-builds-with-poetry-a78a66f5aed0 
  - https://medium.com/@harpalsahota/dockerizing-python-poetry-applications-1aa3acb76287 
  - https://github.com/orgs/python-poetry/discussions/1879
  - https://www.youtube.com/watch?v=CzAyaSolZjY 
  - https://www.youtube.com/watch?v=3pTohbtroRs
    - https://www.youtube.com/watch?v=XYmZAGo9fTE 
    - https://www.youtube.com/watch?v=Z8_P5pjmlrg 
  - https://www.youtube.com/watch?v=4EZ3xFcTwHo 
  - https://www.youtube.com/watch?v=hXYFS2pOEH8
  - https://www.youtube.com/watch?v=BI4LLkCTQ5s 
- DB 
  - https://github.com/testdrivenio/fastapi-sqlmodel-alembic 
  - https://python.plainenglish.io/fastapi-sqlalchemy-2-0-pydantic-v2-alembic-postgres-and-docker-2c429acfc333
  - https://medium.com/@johnidouglasmarangon/using-migrations-in-python-sqlalchemy-with-alembic-docker-solution-bd79b219d6a 
- More
  - https://medium.com/@asoldan1459/fastapi-postgresql-alembic-sqlalchemy-rabbitmq-docker-example-10c34f100167?source=email-530931b916fc-1707595396711-digest.reader--10c34f100167----0-98------------------7c79d550_ef4f_46a7_bc8b_a7e542122908-1 

