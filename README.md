# Project4-Tyr

## Description

Simple gym diary to record training sessions. 

### Tech Used
```
python3
flask
flask-cors
flask-sqlalchemy
flask-login
SQLite
jinja2
Bootstrap in jinja
os import path
Blueprint from flask 
Werkzeug.security
javascript
```

### User Stories

Instead of keeping a physical pen and paper to write down completed workouts. The app allows the user to key in similar data and treat the app as a digital diary. 

The user will be able to:
- Sign Up as a user
- Login as a user
- Once logged in, can create, read, update(edit), and delete diary entries. 

## Planning and Development Process

- A basic story of your planning and developing this project.
- Attempted entirely new framework, languages and tech. 
- Initially planned Database models in PostgreSQL, had plans to use that and POSTMAN. 
- Had difficulties learning FLASK and its modules and integrating POSTGRESQL + running POSTMAN so switched to SQLite, had to learn that too. 
- Used Jinja instead of react, bootstrap as integrated CSS. Used Jinja with templates for base.html inheritors. Almost like react components. 
- FLASK difficulties in that to do heavy stuff you need to install quite abit of modules, django already comes with alot of modules. 
- FLASK has two ways of creating an app, either conventionally with flask run via environment declarations/files, OR, using a FLASK APP FACTORY, which comes with its own limitations. The upside is its modularity compared to the standard app.py where its easier to write all the routes in the main folder but then its one huge messy mess. 
- SQLite with SQLViewer makes it really easy to use SQLite as a db, but it is limited to an overall small amount of data compared to strong postgresql and mysql. Fit for lightweight apps or certain type of apps that dont use powerful databases like MySQL or PostgreSQL.

### Problem-Solving Strategy

Quite abit of documentation reading and trial and error since most of the tech used in this project is new to me.

### Unsolved problems

Opening and viewing full card data on button click. 

---

## Acknowledgments

Desmond for suggesting flask. Was painful but fun. 

---
