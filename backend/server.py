# Import flask and datetime module for showing date and time
from flask import Flask, jsonify
import datetime
  
x = datetime.datetime.now()
  
# Initializing flask app
app = Flask(__name__)
  
  
# Route for seeing a data
@app.route('/data')
def get_time():
    dicto = {
        'Name':"geek23", 
        "Age":"22",
        "Date":x, 
        "programming":"python"
        }
  
    # Returning an api for showing in  reactjs
    return jsonify(dicto)
  

# Route for seeing a data
@app.route('/data1')
def get_data():
    dicto = {
        'Name':"deepak", 
        "Age":"28",
        "Date":x, 
        "programming":"new api check"
        }
  
    # Returning an api for showing in  reactjs
    return jsonify(dicto)
      
# Running app
if __name__ == '__main__':
    app.run(debug=True)
