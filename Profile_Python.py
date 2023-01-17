from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    user= {
        'name':'Álvaro Aguado',
        'job': 'Junior Backend Developer',
        'picture' : 'profile.jpg',
        'links': [
            {'name': 'Linkedin', 'url': 'https://twitter.com/in/alvaroaguadod','is_primary': True},
            {'name': 'Github', 'url': 'https://github.com/alvaroaguadod'},
        ],
        'about_me':[
            "I'm a Junior Backend Developer with some experience in both front-end and back-end development, but my main learning focus is back-end.",
            "I felt in love with Python. I like its practicality and its ability to write readable, maintable, and scalable code.",
            "I enjoy studying in depth Django and Flask.",
            "I'm considering to obtain the AWS Certified Cloud Practitioner"],
        'email' : 'soyalvaroaguado@gmail.com',
        'skills': ['HTML', 'CSS', 'JavaScript', 'Python', 'Flask'],
        'portfolio': 'https://alvaroaguadod.github.io'  
    }
    
    return render_template('profile.html', title='My Profile', user=user)