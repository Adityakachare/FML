from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')  # Define route for the About page
def about():
    return render_template('index.html')  # Render the same index.html template for the About page

# @app.route('/brain')
# def brain():
#     return render_template('brain.html')

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
