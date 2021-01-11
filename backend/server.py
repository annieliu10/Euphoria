from flask import Flask, render_template, request, jsonify, make_response, abort
from flask_cors import CORS

from main import run_script

# from flask_httpauth import HTTPBasicAuth
import json


##initiate the flask server 
app = Flask(__name__)
CORS(app)

# #setting up an authentification 
# auth = HTTPBasicAuth()

configurations = {
    'password': "LYT2001",
    'user_name': "annieliu10",
    'reddit_community': 'ubc',
    'dm_message': "don't kill yourself, you're too sexy",
    'dm_title': "Mental health checkup",
    'is_running': False
}


# @auth.get_password
# def get_password(username):
#     if username == configurations['user_name']:
#         return configurations['password']
#     return None

# @auth.error_handler
# def unauthorized():
#     return make_response(jsonify({'error': 'Unauthorized access'}), 401)



@app.route("/")
def my_index():
    return "Config settings"


## login endpoint 
@app.route('/login', methods=["POST"])
def login():
    if not request.json or not "password" in request.json or not "user_name" in request.json:
        abort(400)
    if "password" in request.json and type(request.json['password']) is not str:
        abort (400)
    if "user_name" in request.json and type(request.json['user_name']) is not str:
        abort(400)
    configurations['user_name']= request.json['user_name']
    configurations['password']= request.json['password']
    return jsonify(username=configurations['user_name'],
                    password=configurations['password'],
                    result="Login account created!")


#User Form Fill to extract from subreddit
@app.route('/settings', methods=["PUT"])
def settings():
    if not request.json:
        abort(400, description="Resource not found")
    # if "user_name" in request.json and type(request.json['user_name']) is not str:
    #     abort(400, description="Resource not found")
    if "reddit_community" in request.json and type(request.json['reddit_community']) is not str:
        abort(400, description="Resource not found")
    if "dm_message" in request.json and type(request.json['dm_message']) is not str:
        abort(400, description="Resource not found")
    if "dm_title" in request.json and type(request.json['dm_title']) is not str:
        abort(400, description="Resource not found")
    
    ##change it or use default
    # configurations['user_name'] = request.json.get('user_name', configurations['user_name'])
    configurations['reddit_community'] = request.json.get('reddit_community', configurations['reddit_community'])
    configurations['dm_message'] = request.json.get('dm_message', configurations['dm_message'])
    configurations['dm_title']= request.json.get('dm_title', configurations['dm_title'])

    return jsonify({'configurations': configurations})


# # get configuration information
@app.route('/retrieve', methods=['GET'])
def retrieve():
    return jsonify({'configurations': configurations})



##an endpoint sets the flag to true and calls the runscript 
@app.route('/start', methods= ['GET'])
def start():
    configurations['is_running']= True
    
    # run_script()
    return jsonify({"running": True})
   





# ##manipulate the reddit community (str)
# @app.route('/target_subreddit', methods=["POST"])
# def change_target():
#     if not request.json or not "reddit_community" in request.json:
#         abort(400)
#     configurations['reddit_community'] = request.json['reddit_community']
#     return "Subreddit community is updated to " + configurations['reddit_community']

# ##manipulate sleep_interval
# @app.route('/sleep_interval', methods=["POST"])
# def change_sleep_interval():
#     if not request.json or not "sleep_interval" in request.json:
#         abort(400)

#     configurations['sleep_interval']= request.json['sleep_interval']
#     return "Sleep interval is updated to "+ configurations['sleep_interval']


##manipulate the title and content of the message 
# @app.route('/dm', methods=['POST'])
# def change_titleandmessage():
#     if not request.json:
#         abort(400)
#     if 'dm_title' in request.json and type(request.json['dm_title']) is not str:
#         abort (400)
#     if 'dm_message' in request.json and type(request.json['dm_message']) is not str:
#         abort (400)
#     configurations['dm_title'] = request.json.get('dm_title', configurations['dm_title'])
#     configurations['dm_message'] = request.json.get('dm_message', configurations['dm_message'])
#     return "The message title is updated"


@app.errorhandler(400)
def notworking(error):
    return make_response(jsonify({'error': "Not updated successfully"}), 400)


@app.errorhandler(404)
def notworking(error):
    return make_response(jsonify({'error': "Not found"}), 404)


if __name__ == '__main__':
    app.run(port=5000, debug= True)
                                                              