from flask import Flask, render_template, request

app = Flask(__name)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        mobile = request.form['mobile']
        telegram = request.form['telegram']

        # Save the data to your GitHub repository or database here

        return f"Hello, {name}! Your data has been submitted successfully."

if __name__ == '__main__':
    app.run(debug=True)
