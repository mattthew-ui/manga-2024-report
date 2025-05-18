from flask import Flask, render_template, request, jsonify, flash, redirect, session, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text, create_engine, text, Float
from enum import IntEnum, Enum
import random
import bcrypt
import mysql.connector
from datetime import datetime, timezone
from sqlalchemy.types import Enum as SQLAlchemyEnum
from decimal import Decimal
from werkzeug.utils import secure_filename
import os 
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/Awards')
def The_Awards():
    return render_template('TheAwards.html')


@app.route('/The_numbers')
def The_numbers():
    return render_template('TheMangaReport24.html')