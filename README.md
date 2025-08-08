
 ````bash
 py -3 -m venv .venv
 ````

 ````bash
.venv\Scripts\activate.bat 
 ````

 ````bash
pip install -r requirements.txt
 ````

 ````bash
pip freeze > requirements.txt
 ````

## To start server in dev mode (live server):
 ````bash
uvicorn main:src --reload
 ````

````bash
uvicorn src.main:app --reload
````

```bash
gunicorn src.main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:80
```
