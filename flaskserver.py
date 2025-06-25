from flask import Flask, request, jsonify
from flasgger import Swagger
import uuid

#Kann man auskommentieren um zu prüfen ob der Server läuft
#print("Flaskserver läuft – Initialisierung abgeschlossen!")

app = Flask(__name__)
swagger = Swagger(app, template_file='api_specification.yaml')

# Dummy-Datenbank
lists = {}  # todo_lists
entries = {}  # todo_entries

# Neue Liste erstellen
@app.route('/todo-list', methods=['POST'])
def addEntryToList():
    data = request.get_json()
    if not data or 'name' not in data:
        return jsonify({'error': 'Bad Request'}), 400

    list_id = str(uuid.uuid4())
    new_list = {'id': list_id, 'name': data['name']}
    lists[list_id] = new_list
    entries[list_id] = []
    return jsonify(new_list), 200

# Alle Listen anzeigen
@app.route('/todo-lists', methods=['GET'])
def getAllLists():
    return jsonify(list(lists.values())), 200

# Eine Liste anzeigen
@app.route('/todo-list/<list_id>', methods=['GET'])
def getListById(list_id):
    if list_id in lists:
        return jsonify(lists[list_id]), 200
    return '', 404

# Liste löschen
@app.route('/todo-list/<list_id>', methods=['DELETE'])
def deleteList(list_id):
    if list_id in lists:
        lists.pop(list_id)
        entries.pop(list_id, None)
        return jsonify({'msg': 'success'}), 200
    return '', 404

# Alle Einträge einer Liste anzeigen
@app.route('/todo-list/<list_id>/entries', methods=['GET'])
def getListEntries(list_id):
    if list_id not in entries:
        return '', 404
    return jsonify(entries[list_id]), 200

# Eintrag zu Liste hinzufügen
@app.route('/todo-list/<list_id>/entries', methods=['POST'])
def addEntryToTodoList(list_id):
    if list_id not in entries:
        return '', 404
    data = request.get_json()
    if not data or 'name' not in data or 'description' not in data:
        return '', 400

    entry_id = str(uuid.uuid4())
    entry = {
        'id': entry_id,
        'name': data['name'],
        'description': data['description'],
        'user_id': str(uuid.uuid4()),
        'list_id': list_id
    }
    entries[list_id].append(entry)
    return jsonify(entry), 200

# Eintrag aktualisieren
@app.route('/todo-list/<list_id>/entry/<entry_id>', methods=['PUT'])
def updateEntry(list_id, entry_id):
    if list_id not in entries:
        return '', 404

    data = request.get_json()

    for i, entry in enumerate(entries[list_id]):
        if entry['id'] == entry_id:
            entry.update({
                'name': data.get('name', entry['name']),
                'description': data.get('description', entry['description'])
            })
            return jsonify(entry), 200
    return '', 404


# Eintrag löschen
@app.route('/todo-list/<list_id>/entry/<entry_id>', methods=['DELETE'])
def deleteEntry(list_id, entry_id):
    if list_id not in entries:
        return '', 404

    for i, entry in enumerate(entries[list_id]):
        if entry['id'] == entry_id:
            entries[list_id].pop(i)
            return jsonify({'msg': 'success'}), 200

    return '', 404

if __name__ == '__main__':
    # app.run(debug=True) use this for testing purposes
    app.run(host='0.0.0.0', port=5000) #runs on port 5000
