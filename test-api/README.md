# Python Flask Test API

## Commands to get started:

```
workon test-api
deactivate 
pip freeze
pip install flask flask-cors
mkvirtualenv test-api

https://virtualenvwrapper.readthedocs.io/en/latest/install.html

```

```
subl app.py == which makes a .py file and opens up sublime text which we made a hello_world program

using jsonify: it made a json response which is readable to machine 
```

### ***Input***

You will enter the below url in your browser to do **live** currency conversion from **Euro** to **Canadian Dollars (CAD)** and pass a float value ***in normal english language we would say a decimal point value*** to get the output....

```
http://127.0.0.1:5000/currency/euro/cad/500
```

### ***Output***

After doing the above step now you will get a .json output on your page which will show you the live (current day) currency conversion from Euro to CAD:

```
-> {"message": "You will receive: 656.33 CAD"}
```
