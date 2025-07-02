from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Hardcoded user for demo
USER_CREDENTIALS = {
    'username': 'admin',
    'password': '1234'
}


@app.route('/calc')
def dashboard():
    return render_template('calc.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == USER_CREDENTIALS['username'] and password == USER_CREDENTIALS['password']:
            return redirect(url_for('calc.html'))
        else:
            error = 'Invalid Credentials. Please try again.'
    return render_template('login.html', error=error)

if __name__ == '__main__':
    app.run(debug=True)
