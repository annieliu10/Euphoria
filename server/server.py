from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from flask_httpauth import HTTPBasicAuth
import json

##initiate the flask server 
app = Flask(__name__)
CORS(app)

#setting up an authentification 
auth = HTTPBasicAuth()

configurations = {
    'password': "LYT2001",
    'user_name': "annieliu10",
    'reddit_community': 'ubc',
    'sleep_interval': 123123,
    'dm_message': "don't kill yourself, you're too sexy",
    'dm_title': "Mental health checkup",
}

@auth.get_password
def get_password(username):
    if username == configurations['user_name']:
        return configurations['password']
    return None

@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)



@app.route("/")
def my_index():
    return "Config settings"


## can only update the password if you can access it with your old password
@app.route('/password', methods=["POST"])
@auth.login_required
def password():
    # if request.method == 'GET':
    #     return jsonify ({'password': configurations['password']})
     
    if not request.json or not "password" in request.json:
        abort(400)

    configurations['password'] = request.json['password']
    return "Password is updated to " + configurations['password']

##manipulate the username
@app.route('/username', methods=["POST"])
def change_username():
    if not request.json or not "user_name" in request.json:
        abort(400)
    configurations['user_name'] = request.json['user_name']
    return "User name is updated to " + configurations['user_name']



##manipulate the reddit community (str)
@app.route('/target_subreddit', methods=["POST"])
def change_target():
    if not request.json or not "reddit_community" in request.json:
        abort(400)
    configurations['reddit_community'] = request.json['reddit_community']
    return "Subreddit community is updated to " + configurations['reddit_community']

##manipulate sleep_interval
@app.route('/sleep_interval', methods=["POST"])
def change_sleep_interval():
    if not request.json or not "sleep_interval" in request.json:
        abort(400)

    configurations['sleep_interval']= request.json['sleep_interval']
    return "Sleep interval is updated to "+ configurations['sleep_interval']


# ##manipulate the title of the message 
# @app.route('/dm_title', methods=['POST'])
# def change_title():
#     if not request.json or not "dm_title" in request.json:
#         abort(400)

#     configurations['dm_title'] = request.json['dm_title']
#     return "The message title is updated to "+ configurations['dm_title']


# ##manipulate the dm message content 
# @app.route('/dm_message', methods=["POST"])
# def change_message():
#     if not request.json or not "dm_message" in request.json:
#         abort(400)

#     configurations['dm_message']= request.json['dm_message']
#     return "The automated message content is updated to "+ configurations['dm_message']


##manipulate the title and content of the message 
@app.route('/dm', methods=['POST'])
def change_titleandmessage():
    if not request.json:
        abort(400)
    if 'dm_title' in request.json and type(request.json['dm_title']) is not str:
        abort (400)
    if 'dm_message' in request.json and type(request.json['dm_message']) is not str:
        abort (400)
    configurations['dm_title'] = request.json.get('dm_title', configurations['dm_title'])
    configurations['dm_message'] = request.json.get('dm_message', configurations['dm_message'])
    return "The message title is updated"



@app.errorhandler(400)
def notworking(error):
    return make_response(jsonify({'error': "Not updated successfully"}), 400)




if __name__ == '__main__':
    app.run(debug=True)







    

if __name__ == '__main__':
    app.run(debug=True)







    