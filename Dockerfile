FROM python:3.8.2-alpine as base_image
# Base image
ADD . /application
WORKDIR /application
RUN set -e; \
	apk add --no-cache --virtual .build-deps \
		gcc \
		libc-dev \
		linux-headers \
	; \
	pip install -r src/requirements.txt; \
	apk del .build-deps;
EXPOSE 5000
VOLUME /application
WORKDIR /application/src

FROM base_image
# Run unittests based on base image
RUN set -e; \
	pip install -r test_requirements.txt; \
	pytest -v;

FROM base_image
# Run application
CMD uwsgi --http :5000  --manage-script-name --mount /=vmware_exporter:app --enable-threads --processes 2
