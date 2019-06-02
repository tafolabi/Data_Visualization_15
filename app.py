from flask import Flask, jsonify, render_template
import sqlalchemy
import flask_sqlalchemy
import pandas
import os

#print(os.environ)
if !os.environ[]:
    import config
    print(config.name)

    username:password:hostname:port number:databasename