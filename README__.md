Test API

Commands to get started:

workon test-api
deactivate 
pip freeze
pip install flask flask-cors
mkvirtualenv test-api



subl app.py == which made a .py file in which we made a hello_world program

using jsonify: it made a json response which is readable to machine 



http://.../currency/USD/CAD/500
-> {"message": "You will receive: 656.33 CAD"}








```
@app.route('/<name>') #gives routes/directory 
def hello_name(name):
    if name == 'adeel': 
    	return jsonify({"message": "hello adeel"})

    return 'hello,' + name
```
@app.route('/<name>')
def hello_name(name):
    if name == 'adeel': 
    	return jsonify({"message": "hello adeel"})

    return 'hello,' + name


@app.route('/<name>/<age>')
def hello_name_age(name,age):
    if name == 'adeel': 
    	return jsonify({"message": "hello adeel", "age" : age})

    return 'hello,' + name




if __name__== '__main__':
	app.run(debug=True, port=5000)
