# Template monorepo
This is the repository for microservices. The repository is structured as a monorepo: each directory should contain a separate Python-based microservice. The microservices should be based on the [Python microservice template](https://github.com/HIRO-MicroDataCenters-BV/template-python) provided by HIRO.
The repository structure should look like this:

<details>
  <summary>Sample structure</summary>


```
/my-python-project
|
|-- /microservice1
|   |-- /app
|   |   |-- __init__.py
|   |   |-- main.py
|   |   `-- tests
|   |       |-- __init__.py
|   |       `-- test_main.py
|   |
|   |-- /charts
|   |   `-- /app
|   |       `-- Chart.yaml
|   |
|   |-- Dockerfile
|   `-- pyproject.toml
|
|-- /microservice2
|   |-- /app
|   |   |-- __init__.py
|   |   |-- main.py
|   |   `-- tests
|   |       |-- __init__.py
|   |       `-- test_main.py
|   |
|   |-- /charts
|   |   `-- /app
|   |       `-- Chart.yaml
|   |
|   |-- Dockerfile
|   `-- pyproject.toml
|
`-- README.md  (the one you're reading right now)

```


</details>

## Requirements
Python 3.7+  

## Installation
If you don't have `pre-commit` installed run:

```bash
pip install pre-commit
pre-commit install
```

## Add a new microservice
1. Create a subdirectory at the root of the repository and copy the microservice's source code into it.
2. Create a folder named microservice in .github/workflows and place the files to build and deploy your microservice into this folder.
3. Add microservice hooks to the .pre-commit-config.yaml.
4. Go to the microservice folder and install dependencies.
5. Go back to the root of the repository and commit changes.

## Working on a microservice
1. Go to the microservice directory.
2. Install dependencies:
    ```bash
    poetry config virtualenvs.in-project true
    poetry install --no-root --with dev,test
    ```
3. Run the code, tests, etc. within the microservice environment:
    ```bash
    poetry run pytest
    ```
