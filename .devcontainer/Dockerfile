# Note: You can use any Debian/Ubuntu based image you want. 
FROM python:3.13.2-bookworm

# [Optional] Uncomment this section to install additional OS packages.
# RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
#     && apt-get -y install --no-install-recommends <your-package-list-here>
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=${WORKDIR}
# ENV PYTHONPATH=${PYTHONPATH}:${VENDORDIR}
ENV PIPENV_VENV_IN_PROJECT=1
ENV POETRY_VIRTUALENVS_IN_PROJECT=true

RUN pip install --upgrade pip
RUN pip install pdm