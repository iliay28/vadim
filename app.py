from flask import Flask, render_template, request, redirect
import os
import pandas as pd

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html", title="Hello")

@app.route("/mondhtat")
def world():
    return render_template("Мондштат.html", title="Hello")

@app.route("/gaid")
def kli():
    return render_template("gaid.html", title="Hello")

@app.route("/novosti")
def new():
    return render_template("Новости.html", title="Hello")

@app.route("/about")
def about():
    return render_template("О нас.html", title="Hello")

@app.route("/otziv")
def creat():
    files_paths = os.listdir('./files')
    list_files = []
    for file_name in files_paths:
        file_content = open(f'./files/{file_name}', 'r').readlines()
        list_files.append([file_name, file_content])
    return render_template("otziv.html", list_files=list_files)

@app.route('/show', methods=['GET', 'POST'])
def show():
    if request.method == 'POST':
        file_name = request.form.get('file_name')
        file_context = request.form.get('file_context')
        fw = open(f'./files/{file_name}', 'w')
        fw.write(file_context)
        fw.close()
    return render_template('show.html', message=file_name)