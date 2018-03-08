FROM python:3.6-stretch

LABEL author_name="Pascal van Kooten"
LABEL author_email="kootenpv@gmail.com"

COPY requirements.txt ./

RUN pip install -r requirements.txt

WORKDIR challenge

COPY challenge/data data/
COPY challenge/*.py ./
COPY challenge/solutions solutions/

ENTRYPOINT pytest -s test_solution.py
