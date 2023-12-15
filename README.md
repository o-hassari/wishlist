
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

RDF-G01FP


https://mondaycom.page.link/?apn=com.monday.monday&isi=1290128888&ibi=com.monday.monday&utm_source=email_notification&link=https%3A%2F%2Fdl.monday.com%2Fusers%2Finvitation%2Faccept%3Finvitation_method%3Duser%26invitation_token%3DSUGm8yZ4-qZR_rxySQ1h%26utm_campaign%3Dinvite%2Busers%26dl_slug%3Dmpi622655%26dl_msgid%3Deb73c5fb-9097-4bc4-a11e-864c826eb15e%26dl_category%3Ddevise_mailer-invite_user%257C%257Cmonday_domain%26dl_userid%3D51537555%26dl_sessionid%3D%26slug%3Dmpi622655