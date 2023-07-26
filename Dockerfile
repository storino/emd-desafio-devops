FROM python:3.10.0-slim-bullseye

ENV PYTHONUNBUFFERED True

WORKDIR /app

COPY . ./

RUN pip install --no-cache-dir poetry==1.5.1

RUN poetry config virtualenvs.create false \
    && poetry install --without=dev --without=doc --no-interaction --no-ansi

RUN chmod u+x scripts/scope.sh

CMD ["chmod", "u+x", "scripts/scope.sh"]

ENTRYPOINT ["./scripts/scope.sh"]