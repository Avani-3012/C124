from flask import Flask,jsonify,request

app = Flask(__name__)
contact_group = [{'id':1,'Name':'Avani','done':False},{'id':2,'Name':'Khedkar','done':False}]

@app.route("/", methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message": "Please provide the data!"
        },400)

    contact = {
        'id': contact_group[-1]['id'] + 1,
        'Name': request.json['Name'],
        'Contact':request.json.get('Contact',""),
        'done': False,
    }
    contact_group.append(contact)
    return jsonify({
        "status":"success",
        "message": "Task added succesfully!"
    })


if __name__ =='__main__':
    app.run(debug=True)