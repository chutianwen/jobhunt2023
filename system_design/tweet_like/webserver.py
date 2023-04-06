from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__)

# data storage
posts = []
post_id = 1

# routes
@app.route('/')
def index():
    return send_from_directory('.', 'index2.html')

@app.route('/posts', methods=['GET'])
def get_posts():
    return jsonify(posts)

@app.route('/post', methods=['POST'])
def create_post():
    global post_id
    content = request.form['post_content']
    post = {'id': post_id, 'content': content, 'likes': 0}
    post_id += 1
    posts.append(post)
    return jsonify(post)

@app.route('/like/<int:post_id>', methods=['POST'])
def like_post(post_id):
    for post in posts:
        if post['id'] == post_id:
            post['likes'] += 1
            return jsonify(post)
    return jsonify({'error': 'post not found'})


# Start the web server
if __name__ == '__main__':
    app.run(host='localhost', port=8080)
