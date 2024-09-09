FROM python:3.12.4
RUN pip install poetry
WORKDIR /src
COPY . /src
RUN poetry install
EXPOSE 8501
ENTRYPOINT [ "poetry", "run", "streamlit", "run", "backend/main.py", "--server.port=8501",  "server.address=0.0.0.0" ]
