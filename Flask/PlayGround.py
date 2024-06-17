from flask import Flask, render_template # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/play/<int:timess>/<colorr>')          # The "@" decorator associates this route with the function immediately following
def hello_world(timess,colorr):
    return render_template("indexone.html", times = timess, color = colorr)
    
@app.route('/dojo')
def dojo():
  return "Dojo!"

@app.route('/say/<name>')
def sayingName(name):
  return f"Hi {name.capitalize()}!"

@app.route('/repeat/<int:nr>/<namee>')
def repeatingName(namee,nr):
  return f"{namee*nr}"

@app.route('/<path:catch_all>')
def catch_all(catch_all):
    return "Sorry! No response. Try again."

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.