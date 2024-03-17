from flask import Flask, request, render_template
from v2 import quad

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quadratic_equation')
def quadratic_equation():
    # Add your backend logic for the quadratic equation solver here
    return render_template('quad.html')

@app.route('/cipher_text')
def cipher_text():
    # Add your backend logic for the cipher text encryption here
    return render_template('encrypt.html')

@app.route('/graph')
def graph():
    return render_template('graph.html')

@app.route('/matrix')
def matrix():
    return render_template('matrix.html')

@app.route('/quad_solve', methods=['POST'])
def solve():
    try:
        equation = request.form['equation']
        # Call your quadratic equation solver function here
        roots = quad(equation)
        return str(roots)
    except:
        return "Error: Unparsable Equation!"


if __name__=="__main__":
    app.run(debug=True)
