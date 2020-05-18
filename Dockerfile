FROM python:3.8-alpine
COPY . /app/
WORKDIR /app
RUN apk add make postgresql-libs
RUN apk add --virtual .build-dependencies gcc musl-dev postgresql-dev
RUN make install
RUN apk --purge del .build-dependencies
EXPOSE 8080
CMD make run
