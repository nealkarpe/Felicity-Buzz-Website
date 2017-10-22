from flask import Flask, request, redirect, url_for, render_template


# this creates our Flask app
app = Flask(__name__, static_url_path='/static')


@app.errorhandler(404)
def error(error):
    title = "Oops! Nothing here"
    return render_template('error.html', title=title)


@app.route('/', methods=['GET'])
def home():
    title = "Felicity Buzz"
    return render_template('main.html', title=title)


@app.route('/about', methods=['GET'])
def contact(): 
    title = "About Us"
    return render_template('about.html', title=title)

@app.route('/team', methods=['GET'])
def team():
    title = "Meet the team"
    server_team = ['Arjun Nemani', 'Anukul Sangwan']
    others = ['Gunjan Karamchandani', 'Neal Karpe', 'Sayak Kundu', 
    'Kunal Garg', 'Mohammed Ali']
    members = []
    for _ in server_team:
        members.append({
            'name' : _,
            'position' : 'Server Team',
            'avatar' : 'https://api.adorable.io/avatars/140/' + _
            })
    for _ in others:
        members.append({
            'name' : _,
            'position' : 'Web Dev',
            'avatar' : 'https://api.adorable.io/avatars/140/' + _
            })
    return render_template('team.html', title=title, members=members)

@app.route('/zombiezone', methods=['GET'])
def zombie():
    title = "Zombie Zone"
    filename = url_for('static', filename='images/zombiezone.jpg')
    width = "width:69%"
    return render_template('poster.html', title=title, filename=filename, width=width)

@app.route('/toastmasters', methods=['GET'])
def toastmaster():
    title = "Toastmaster"
    filename = url_for('static', filename="images/toastmaster.jpg")
    width = "width:35%"
    return render_template('poster.html', title=title, filename=filename, width=width)

@app.route('/schedule', methods=['GET'])
def schedule():
    title = "Schedule"
    filename = url_for('static', filename="images/schedule.jpg")
    width = "width:100%"
    return render_template('poster.html', title=title, filename=filename, width=width)


@app.route('/debate', methods=['GET'])
def debate():
    title = "Debate"
    filename = url_for('static', filename="images/debate.jpg")
    width = "width:37%"
    return render_template('poster.html', title=title, filename=filename, width=width)

@app.route('/codecraft', methods=['GET'])
def codecraft():
    return redirect("http://codeforces.com/group/yny9prUF8z/contest/216594/standings/groupmates/true")

@app.route('/litquiz', methods=['GET'])
def litquiz():
    return redirect("https://goo.gl/forms/iDUuQbnArg80qi4D2")

@app.route('/gordianknot', methods=['GET'])
def gordianknot():
    return redirect("https://enigmatic-retreat-58843.herokuapp.com/")


'''
zombiezone - INTERNAL
toastmaster - INTERNAL
litquiz - EXTERNAL
codecraft - EXTERNAL
cachein - EXTERNAL
gordianknot - EXTERNAL
'''