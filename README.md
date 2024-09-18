"# pipeline" 

streamlit -> lig p interface web, sem usar html e css.

    pip install streamlit

Para rodar o app.py, usar o comando abaixo no terminal

    > streamlit run app.py

pydantic -> faz validações de dados (contrato)  -> pandera é um fork de pydantic que faz validação de df
psycopg2 -> lib de acesso ao postgresql
sqlalchemy -> lib p manipular sql no postgres

    pip install psycopg2-binary
    pip install sqlalchemy

dotenv -> lib para pegar chaves do arquivo .env

    pip install python-dotenv

mkdocs -> lib q faz documentções

    pip install mkdocs mkdocs-material mkdocstrings mkdocstrings-python

Para rodar o mkdocs:

    > mkdocs new .
    > mkdocs serve

    para fazer o deploy:

    > mkdocs build
    > mkdocs gh-deploy
    