from flask import Flask, render_template
app = Flask(__name__)
@app.route('/<int:x>/<int:y>/<color1>/<color2>')          # The "@" decorator associates this route with the function immediately following
def checkerboard(x,y,color1,color2):
    return render_template("index.html", x = x, y = y,color1 = color1, color2=color2)


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.