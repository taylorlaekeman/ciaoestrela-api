FROM python:3.8-alpine
COPY Makefile /app/
COPY requirements.txt /app/
COPY manage.py /app/
COPY ciaoestrela_api /app/ciaoestrela_api
RUN apk add make postgresql-libs
RUN apk add --virtual .build-dependencies gcc musl-dev postgresql-dev
RUN make -C app install
RUN make -C app build
RUN apk --purge del .build-dependencies
EXPOSE 8080
CMD make -C app run
