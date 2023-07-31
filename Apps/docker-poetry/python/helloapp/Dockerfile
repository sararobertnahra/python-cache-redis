FROM python:latest
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="${PATH}:/root/.local/bin:$PATH"
ENV CASA="Nossa casa!"
ENV REDIS="localhost"
WORKDIR "/app"
ADD . .
RUN poetry install
EXPOSE 5000
ENTRYPOINT ["poetry","run","start"]