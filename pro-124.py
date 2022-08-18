from asyncio import tasks
from telnetlib import STATUS
from flask import Flask,jsonify, request
app = Flask(__name__)

data = [
    {
        "id":1,
        "Contact":'9987644456',
        "Name":'Raju',
        'done':False
    },
        {
        "id":2,
        "Contact":'9876543222',
        "Name":'Rahul',
        'done':False
    }
]

@app.route('/add-data',methods=['POST'])
def add_task():
    if not request.json:
        return jsonify({'status':'error','message':'Pl provide the data!'},400)

    contact =     {
        "id":data[-1]['id']+1,
        "Name":request.json['Name'],
        'Contact': request.json.get('Contact',''),
        'done':False
    }
    data.append(contact)
    return jsonify({'status':'sucess','message':'added sucessfully'},400)

@app.route('/get-data')
def get_contact():
    return jsonify({'data':data})

if (__name__ =='_main_'):
    app.run(debug=True)

