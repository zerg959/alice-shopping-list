from flask import Flask, request, jsonify
import alice_handler
import os

app = Flask(__name__)

# Создаем папку instance, если её нет
os.makedirs("instance", exist_ok=True)
from database import init_db
init_db()

@app.route('/alice', methods=['POST'])
def handle_alice():
    data = request.json
    response = alice_handler.process(data)
    return jsonify(response)

@app.route('/lists', methods=['GET'])
def get_lists():
    user = request.args.get('user')
    lists = database.get_all_lists(user)
    return jsonify([{'id': lid, 'user': user, 'content': content} for lid, user, content in lists])

@app.route('/edit', methods=['POST'])
def edit_list():
    list_id = request.json.get('id')
    new_content = request.json.get('content')
    success = database.update_list(list_id, new_content)
    return jsonify({'success': success})