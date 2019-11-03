from flask import Flask, request, render_template, session, flash, redirect, url_for
from flask_bootstrap import Bootstrap
from flaskext.mysql import MySQL
from flask_session import Session
# from flask_ckeditor import CKEditor
import yaml
import csv
import json
from bikes import api_utils
import pandas as pd

# import tensorflow as tf
# from keras.models import load_model

# initial global parameters
mysql = MySQL()
application = app = Flask(__name__)
db = yaml.load(open('./config/db.yaml'))
mysql.init_app(app)
Bootstrap(app)
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SECRET_KEY'] = b'_5#y2L"F4Q8z\n\xec]/'

# config db parameters
app.config['MYSQL_DATABASE_HOST'] = db['mysql_host']
app.config['MYSQL_DATABASE_PORT'] = db['mysql_port']
app.config['MYSQL_DATABASE_USER'] = db['mysql_user']
app.config['MYSQL_DATABASE_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DATABASE_DB'] = db['mysql_db']
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'


def initbikedata():
    pass
    # global model, graph
    # load pre-train model
    # model = load_model('./model/mnistCNN.h5')
    # graph = tf.get_default_graph()



@app.route('/', methods=['POST', 'GET'])
def index():
    # session['user_id'] = None
    return render_template("index.html")


@app.route('/logout')
def logout():
    # remove teh username from teh session if it is their
    session.pop('username', None)
    session.pop('user_id', None)
    return redirect(url_for('index'))


@app.route('/addtravel', methods=['POST', 'GET'])
def addtravel():
    # conn = mysql.connect()
    # cur = conn.cursor()
    list_depar = []
    list_arr = []

    if request.method == 'POST':
        _title = request.form['travelTitle']
        _departure = request.form['departure']
        _destination = request.form['destination']
        if (session.get('user_id') is not None):
            if (session['user_id'] != None):
                _user_id = session['user_id']
        _datetime = request.form['plandaytime']
        # if(len(_datetime)!=0):
        _date = _datetime.split('T')[0]
        _year_list = _date.split('-')
        _year = _year_list[0]
        _month = _year_list[1]
        _day = _year_list[2]
        _time = _datetime.split('T')[1]
        _hour = _time.split(':')[0]
        _min = _time.split(':')[1]
        _second = 0  # by default
        # generate input data
        inputdata = {
            "departure_station": _departure,
            "Year": _year,
            "Month": _month,
            "Day": _day,
            "Hour": _hour,
            "Minute": _min,
            "Second": 0,
            "arrival_station": _destination
        }
        package = api_utils.get_all_infos(inputdata)
        dataresult = api_utils.predict_packages(package)
        itemsorted = sorted(dataresult) #A_1, A_2, A_3...
        # available depature stations
        inforlist = {
            'title': _title,
            'departure':_departure,
            'destination':_destination,
            'plan_time':_datetime
        }
        for tmp in itemsorted:
            dict_depar = dataresult[tmp]
            if ('A' in tmp):
                list_depar.append(dict_depar)
            if ('D' in tmp):
                doc_data = {
                    "dock_name": dict_depar['name'],
                    "dock_esti": dict_depar['estimate'],
                    "dock_cap": dict_depar['capacity']
                }
                list_arr.append(doc_data)

        # available docks
        # df = pd.DataFrame(data=inputdata,index=[0])
        # model.predit(df)
    if (len(list_depar) != 0 and len(list_arr) != 0):
        if (session.get('user_id') is not None):
            if (session['user_id'] != None):
                saveplan(inforlist)
        return render_template('addtravel.html', list_depar=list_depar, list_arr=list_arr, inforlist=inforlist)
    else:
        return render_template('addtravel.html')

@app.route('/deletetravel/<string:travel_id>', methods=['POST', 'GET'])
def deletetask(travel_id):
    if request.method == 'GET':
        cnn = mysql.connect()
        cur = cnn.cursor()
        args = (session['user_id'], travel_id)
        cur.callproc('sp_deletetravel', args)
        travel_result = cur.fetchall()
        if len(travel_result) is 0:
            cnn.commit()
            cur.close()
            cnn.close()
            return redirect('/travellist')
    return redirect('/travellist')

@app.route('/gmap/<string:bikestation>', methods=['POST', 'GET'])
def gmap(bikestation):
    #read csv file
    with open('./bikes/stationlocation.csv', newline='') as csvlocaiton:
        reader = csv.DictReader(csvlocaiton)
        for row in reader:
            if(row['Station'] == bikestation):
                bikestation = [row['Latitude'], row['Longitude'], row['Station'] ]
                break
    return render_template('gmap.html',bikestation=bikestation)

# @app.route('/renewtravel/<string:travel_title>/<string:travel_depart>/<string:travel_dest>', methods=['POST', 'GET'])
# def renewtravel(travel_title, travel_depart, travel_dest):
#     # conn = mysql.connect()
#     # cur = conn.cursor()
#     list_depar = []
#     list_arr = []
#
#     if request.method == 'POST':
#         _title = request.form['travelTitle']
#         _departure = request.form['departure']
#         _destination = request.form['destination']
#         if (session['user_id'] != None):
#             _user_id = session['user_id']
#         _datetime = request.form['plandaytime']
#         # if(len(_datetime)!=0):
#         _date = _datetime.split('T')[0]
#         _year_list = _date.split('-')
#         _year = _year_list[0]
#         _month = _year_list[1]
#         _day = _year_list[2]
#         _time = _datetime.split('T')[1]
#         _hour = _time.split(':')[0]
#         _min = _time.split(':')[1]
#         _second = 0  # by default
#         # generate input data
#         inputdata = {
#             "departure_station": _departure,
#             "Year": _year,
#             "Month": _month,
#             "Day": _day,
#             "Hour": _hour,
#             "Minute": _min,
#             "Second": 0,
#             "arrival_station": _destination
#         }
#         package = api_utils.get_all_infos(inputdata)
#         dataresult = api_utils.predict_packages(package)
#         itemsorted = sorted(dataresult) #A_1, A_2, A_3...
#         # available depature stations
#         inforlist = {
#             'title': _title,
#             'departure':_departure,
#             'destination':_destination,
#             'plan_time':_datetime
#         }
#         for tmp in itemsorted:
#             dict_depar = dataresult[tmp]
#             if ('A' in tmp):
#                 list_depar.append(dict_depar)
#             if ('D' in tmp):
#                 doc_data = {
#                     "dock_name": dict_depar['name'],
#                     "dock_esti": dict_depar['estimate'],
#                     "dock_cap": dict_depar['capacity']
#                 }
#                 list_arr.append(doc_data)
#
#         # available docks
#         # df = pd.DataFrame(data=inputdata,index=[0])
#         # model.predit(df)
#     if (len(list_depar) != 0 and len(list_arr) != 0):
#         if (session['user_id'] != None):
#             saveplan(inforlist)
#         return render_template('addtravel.html', list_depar=list_depar, list_arr=list_arr, inforlist=inforlist)
#     else:
#         return render_template('addtravel.html')

def saveplan(inforlist):
    conn = mysql.connect()
    cursor = conn.cursor()
    args = (session['user_id'], inforlist['title'], inforlist['departure'],
            inforlist['destination'], inforlist['plan_time'])
    cursor.callproc('sp_addtravelplan', args)
    result = cursor.fetchall()
    if len(result) is 0:
        conn.commit()
        cursor.close()

@app.route('/travellist', methods=['POST','GET'])
def travellist():
    if request.method == "GET":
        if (session.get('user_id') is None):
            return redirect(url_for('index'))
        # login and show the travel list
        # sql = "SELECT LIST_TRAVELTITLE, LIST_DEPARTURE, LIST_DESTINATION, LIST_PLANTIME FROM TRAVELLIST" \
        #       "WHERE LIST_USERID " + session['user_id']
        cnn = mysql.connect()
        cur = cnn.cursor()
        args = (session['user_id'], session['username'])
        cur.callproc('sp_travellist', args)
        travel_result = cur.fetchall()
        if len(travel_result) > 0:
            cnn.commit()
            cur.close()
            return render_template('travellist.html', travel_result=travel_result)
    return redirect(url_for('index'))

@app.route('/signin', methods=['POST'])  # login
def signin():
    # try:
    _name = request.form['txtUsername']
    _password = request.form['txtPassword']

    conn = mysql.connect()
    cursor = conn.cursor()
    if _name and _password:
        args = (_name, _password)
        cursor.callproc('sp_verifyUserAccount', args)
        returnData = cursor.fetchall()
        if len(returnData) is 1:
            conn.commit()
            cursor.close()
            conn.close()
            session['username'] = _name  # has some problem
            session['user_id'] = returnData[0][0]
            return redirect('/')
        else:
            return render_template("signup.html")
    return redirect('/')

@app.route('/signup', methods=['POST', 'GET'])  # create user
def signup():
    # read the post value from UI
    if request.method == 'POST':
        _name = request.form['inputName']
        _password = request.form['inputPassword']
        _email = request.form['inputEmail']
        # vaildate if input all three item
        if _name and _password and _email:
            conn = mysql.connect()
            cursor = conn.cursor()
            # _hash_password = werkzeug.security.generate_password_hash(_password)
            cursor.callproc('sp_createNewUser', (_name, _password, _email))
            returnData = cursor.fetchall()
            print(returnData)
            if len(returnData) is 0:
                conn.commit()
                cursor.close()
                conn.close()
            return redirect('/')
    return render_template('signup.html')

if __name__ == "__main__":
    mysess = Session()
    mysess.init_app(app)
    app.run(debug=True, port=5021)
