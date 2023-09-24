import random

from flask import Flask,request,Request,redirect,render_template
from fuzzywuzzy import fuzz
import spacy
from pymongo import MongoClient

client = MongoClient('localhost',27017)
db = client.users
user = db.users

# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("login.html")

@app.route("/register")
def reg():
    return render_template("register.html")


@app.route("/login",methods=["POST"])
def login():
    # data=request.form.to_dict()
    # fuser = user.find_one(data)
    # fid = str(fuser["_id"])
    # name = str(fuser["name"])
    # points = str(fuser["points"])
    return render_template("dashboard.html",name="Vijay",points="10")



@app.route("/startjournel")
def journel():
    return render_template("journel.html")



@app.route("/create",methods=["POST"])
def create():
    data = request.form.to_dict()
    print(data)

    # cuser = user.insert_one(data)

    return render_template("login.html")

nlp = spacy.load("en_core_web_sm")


activities_dict = {
    "Playful": "Create a playful scavenger hunt with clues for family or friends to enjoy.",
    "Motivated": "Write down three long-term goals and brainstorm the first step for each.",
    "Relaxed": "Take a leisurely bath with soothing music and scented candles.",
    "Curious": "Watch a documentary on a topic you've always been curious about.",
    "Adventurous": "Plan a weekend camping trip or a day hike to explore nature.",
    "Focused": "Use the Pomodoro Technique (25 minutes of focused work, followed by a 5-minute break) to tackle a task.",
    "Appreciative": "Create a 'gratitude jar' and write down something you're grateful for each day, then read them at the end of the year.",
    "Mindful": "Practice a body scan meditation to become more aware of physical sensations.",
    "Generous": "Donate gently used clothing or household items to a local charity.",
    "Humble": "Reflect on a time you made a mistake and consider the lessons learned from it.",
    "Optimistic": "Make a vision board with images and quotes that represent your future aspirations.",
    "Inventive": "Spend time building and experimenting with a DIY project or craft.",
    "Comforted": "Spend a cozy evening by the fireplace with a good book or movie.",
    "Resourceful": "Solve a household problem using items you have on hand, like creating an organization system.",
    "Eager": "Start a new book or audiobook in a genre you're excited to explore.",
    "Respectful": "Reach out to someone you admire or appreciate and express your respect and admiration.",
    "Empathetic": "Volunteer at a local shelter or community organization to help those in need.",
    "Joyful": "Plan a day trip to an amusement park or an entertainment venue that brings you joy.",
    "Energetic": "Try a high-energy workout routine or dance workout to boost your vitality.",
    "Productive": "Tackle a small home improvement project or reorganize a cluttered area in your home.",
    "Invent": "Brainstorm and sketch out ideas for a new gadget or product that could make life easier.",
    "Exercise": "Try a new workout routine, like yoga, Pilates, or high-intensity interval training (HIIT).",
    "Sculpt": "Create a sculpture or artwork using clay, wood, or other materials you enjoy working with.",
    "Cherish": "Spend quality time with a loved one and create lasting memories together.",
    "Hike": "Go on a day-long hike in a nearby national park or wilderness area to reconnect with nature.",
    "Experiment": "Conduct a kitchen science experiment, such as making homemade lava lamps or growing crystals.",
    "Choreograph": "Choreograph a dance routine to your favorite song and perform it for fun.",
    "Cycle": "Take a bike ride through a scenic route or explore a new biking trail in your area.",
    "Paint": "Set up an easel and paint a canvas with a scene from your imagination or your surroundings.",
    "Compose": "Write a piece of music or a song, and if you play an instrument, add melodies and harmonies.",
    "Renovate": "Select a room in your home and plan a DIY renovation or redecoration project.",
    "Garden": "Start a small garden, whether it's with flowers, herbs, or vegetables, and nurture it.",
    "Climb": "Try indoor rock climbing or sign up for an introductory climbing class.",
    "Decorate": "Create homemade decorations for an upcoming holiday or special occasion.",
    "Dine": "Explore a new restaurant or café in your area and savor the cuisine.",
    "Act": "Join a local theater group or take acting lessons to explore your dramatic side.",
    "Sail": "Take a sailing lesson or rent a sailboat for a peaceful day on the water.",
    "Explore": "Visit a nearby museum or historical site to learn about local culture and history.",
    "Race": "Participate in a charity run or fun run event in your community.",
    "Collect": "Start a collection of something you're passionate about, like vintage books or coins.",
    "Relieved": "Practice progressive muscle relaxation to release tension in your body.",
    "Content": "Enjoy a favorite cup of tea or coffee in a quiet, comfortable spot.",
    "Resilient": "Write down a recent challenge you faced and how you overcame it, focusing on your inner strength.",
    "Satisfied": "Treat yourself to a small indulgence, like a piece of chocolate or a favorite snack.",
    "Empowered": "Learn a basic self-defense move and practice it for safety and confidence.",
    "Inspired": "Read a motivational quote or watch a TED Talk by a great speaker for inspiration.",
    "Fulfilled": "Donate to a charity or cause you care about and feel the satisfaction of making a difference.",
    "Calm": "Create a calming bedtime routine, like reading a book or taking a warm bath.",
    "Adventurous": "Try a new outdoor activity like hiking, biking, or kayaking.",
    "Mindful": "Eat a meal slowly, savoring each bite and focusing on the taste and texture.",
    "Organized": "Use a bullet journal or a digital task manager to plan your day and stay organized.",
    "Eager": "Enroll in an online course or class to learn something new.",
    "Playful": "Spend time with a pet or engage in a fun, playful activity like building with LEGO bricks.",
    "Confident": "Stand in front of a mirror and practice positive affirmations for self-confidence.",
    "Grateful": "Write a thank-you note to someone who has made a positive impact in your life.",
    "Patient": "Try your hand at a slow-cooking recipe, like a stew or chili, and enjoy the process.",
    "Eloquent": "Practice public speaking by recording a short speech or presentation.",
    "Loving": "Reach out to a family member or close friend with a heartfelt message or call."
}


def find_approximate_match(input_text, activities_dict):
    # Initialize variables to store the best match and its similarity score
    best_match = None
    best_score = 0

    # Iterate through the keys in the dictionary
    for mood, activity in activities_dict.items():
        # Calculate the similarity score between the input and the current key
        similarity_score = fuzz.partial_ratio(input_text.lower(), mood.lower())

        # Update the best match if the current score is higher
        if similarity_score > best_score:
            best_match = mood
            best_score = similarity_score

    # If a match with a sufficient similarity score is found, return it
    if best_score >= 70:  # You can adjust the similarity threshold as needed
        return activities_dict[best_match]
    else:
        random_key = random.choice(list(activities_dict.keys()))
        random_value = activities_dict[random_key]
        return random_value



@app.route("/task",methods=["POST"])
def task():
    data = request.form.to_dict()
    text = data["journel"]
    tokens = nlp(text)
    te = ""
    for t in tokens:
        if t.pos_ == 'VERB':
            te = t



    task = find_approximate_match(str(te),activities_dict)
    return render_template("task.html",task = task)

@app.route("/success",methods=["POST"])
def sucess():
    return redirect("/")



# main driver function
if __name__ == '__main__':
    # run() method of Flask class runs the application
    # on the local development server.
    app.run()