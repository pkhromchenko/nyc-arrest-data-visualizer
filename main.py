import bottle
import os.path
import data #assumes that your functions from parts 2 & 3 are in a file named data.py
import csv
import json
from datetime import date
from datetime import datetime

def load_data():
   csv_file = "cache.csv"
   if not os.path.isfile(csv_file):
      url = "https://data.cityofnewyork.us/resource/uip8-fykc.json?$limit=50000&$select=arrest_date,pd_desc,ofns_desc,arrest_boro,arrest_precinct,law_cat_cd,age_group,perp_sex,perp_race"
      info = data.retrieve_json(url);
      needed_keys = ["arrest_date","age_group","arrest_boro","pd_desc","law_cat_cd"]
      for k in needed_keys :
        info = data.clean_list(k, info)
      data.cache_writer(info, csv_file)

@bottle.route('/')
def index():
    return bottle.static_file("index.html", root=".")

@bottle.route('/arrest.js')
def frontEnd():
  return bottle.static_file("arrest.js", root = ".")

@bottle.route('/ajax.js')
def ajax():
  return bottle.static_file("ajax.js", root = ".")

@bottle.route('/styles.css')
def styles():
    return bottle.static_file("styles.css", root=".")  

@bottle.get('/pieChart')
def pieChart():
  qsum = 0
  bksum = 0
  sisum = 0
  bxsum = 0
  msum = 0
  with open("cache.csv") as f:
    reader = csv.reader(f)
    headers = next(f)
    for line in reader:
      if line[3] == "Q":
        qsum += 1
      if line[3] == "B":
        bxsum += 1
      if line[3] == "K":
        bksum += 1
      if line[3] == "S":
        sisum += 1
      if line[3] == "M":
        msum += 1
    pieGraphData = [bksum,msum,bxsum,qsum,sisum]
    return json.dumps(pieGraphData)

@bottle.post('/barGraph')
def barGraph():
  dataJSON = bottle.request.body.read().decode()
  content = json.loads(dataJSON)
  sum1 = 0
  sum2 = 0
  sum3 = 0
  sum4 = 0
  sum5 = 0
  with open("cache.csv") as f:
    reader = csv.reader(f)
    headers = next(f)
    for line in reader:
      if line[3] == content["boroDiv"]:
        if line[6] == "<18":
          sum1 += 1
        if line[6] == "18-24":
          sum2 += 1
        if line[6] == "25-44":
          sum3 += 1
        if line[6] == "45-64":
          sum4 += 1
        if line[6] == "65+":
          sum5 += 1
    barGraphData = [sum1,sum2,sum3,sum4,sum5]
    return json.dumps(barGraphData)

@bottle.get('/lineChart')
def lineChart():
  newlst = [];
  newdct = {}
  with open("cache.csv") as f:
    reader = csv.reader(f)
    headers = next(f)
    for line in reader:
      newlst.append(line[0])
    for i in set(newlst):
      newdct[i] = newlst.count(i)
    lineChartData = ({k: newdct[k] for k in sorted(newdct)})
    return json.dumps(lineChartData)

load_data()
bottle.run(host="0.0.0.0", port=8080)
