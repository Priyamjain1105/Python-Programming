from flask import render_template,request,jsonify,redirect, url_for

# sno  name position salary

def register_routes(app):
    @app.route('/')
    def home():
        return render_template('index.html')