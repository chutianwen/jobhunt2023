from flask import Flask, jsonify, request, send_from_directory

app = Flask(__name__)

posts = []
next_id = 1

@app.route('/')
def index():
    return send_from_directory('.', 'index2.html')

@app.route('/post', methods=['POST'])
def create_post():
    global next_id
    text = request.form['text']
    post = {'id': next_id, 'text': text, 'likes': 0}
    posts.append(post)
    next_id += 1
    return jsonify(post)

@app.route('/like', methods=['POST'])
def like_post():
    id = int(request.form['id'])
    for post in posts:
        if post['id'] == id:
            post['likes'] += 1
            return jsonify(post)
    return jsonify({'error': 'Post not found'})

@app.route('/posts')
def get_posts():
    return jsonify(posts)

if __name__ == '__main__':
    app.run(host='localhost', port=8080)

import string
string.a