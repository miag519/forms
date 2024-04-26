from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('home.html')


@app.route("/response", methods=['POST', 'GET'])
def render_response():
    error = None
    color = request.args['color'] 
    if color == 'pink':
            reply1 = "That's my favorite color, too!"
        else:
            reply1 = "My favorite color is pink."
        n = int(request.args['multNum']) #values in request.args are strings by default
            reply2 = "2 x " + str(n) + " = " + str((2*n))
        return render_template('response.html', response1 = reply1, response2 = reply2)
    else:
        error = 'Invalid response'
        return render_template('response.html', error=error)
   
   
if __name__=="__main__":
    app.run(debug=False)