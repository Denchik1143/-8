from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/project1')
def projects1():
    return render_template('project1.html')

@app.route('/project2')
def projects2():
    return render_template('project2.html')

@app.route('/game')
def game():
    return render_template('game.html')

@app.route('/project/<int:project_id>')
def project_details(project_id):
    # Assuming you have some logic to fetch project details based on project_id
    return render_template('project_details.html', project_id=project_id)

if __name__ == '__main__':
    app.run(debug=True)
