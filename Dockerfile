FROM python:3.6-stretch

LABEL author_name="Pascal van Kooten"
LABEL author_email="kootenpv@gmail.com"

COPY requirements.txt ./

RUN pip install -r requirements.txt

WORKDIR challenge

COPY challenge/data data/
COPY challenge/*.py ./

#### user stuff
COPY challenge/solutions solutions/

# setup complete. find the latest sol.py
RUN ls -1rtd solutions/** | tail -n 1 > solution_test.txt

ENTRYPOINT pytest -s test_solution.py
