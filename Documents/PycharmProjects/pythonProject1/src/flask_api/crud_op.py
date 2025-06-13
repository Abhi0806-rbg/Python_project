from flask import Flask, jsonify, request

app = Flask(__name__)

# Dummy contact list
contacts = [
    {"id": 1, "name": "Abhi", "email": "abhi@example.com", "phone": "9849555642"},
    {"id": 2, "name": "Subbu", "email": "subbu@example.com", "phone": "6393334762"},
]

@app.route('/')
def home():
    return "Welcome to the Contact Management API!"

# GET all contacts
@app.route('/contacts', methods=['GET'])
def get_contacts():
    return jsonify(contacts)

# GET a contact by ID
@app.route('/contacts/<int:contact_id>', methods=['GET'])
def get_contact(contact_id):
    contact = next((c for c in contacts if c['id'] == contact_id), None)
    return jsonify(contact) if contact else (jsonify({"message": "Contact not found"}), 404)

# POST a new contact
@app.route('/contacts', methods=['POST'])
def create_contact():
    data = request.get_json()
    if not data or not all(k in data for k in ('name', 'email', 'phone')):
        return jsonify({"message": "Invalid contact data"}), 400
    new_contact = {
        "id": contacts[-1]['id'] + 1 if contacts else 1,
        "name": data['name'],
        "email": data['email'],
        "phone": data['phone']
    }
    contacts.append(new_contact)
    return jsonify(new_contact), 201

# PUT (update) a contact
@app.route('/contacts/<int:contact_id>', methods=['PUT'])
def update_contact(contact_id):
    contact = next((c for c in contacts if c['id'] == contact_id), None)
    if not contact:
        return jsonify({"message": "Contact not found"}), 404
    data = request.get_json()
    contact['name'] = data.get('name', contact['name'])
    contact['email'] = data.get('email', contact['email'])
    contact['phone'] = data.get('phone', contact['phone'])
    return jsonify(contact)

# DELETE a contact
@app.route('/contacts/<int:contact_id>', methods=['DELETE'])
def delete_contact(contact_id):
    global contacts
    contacts = [c for c in contacts if c['id'] != contact_id]
    return jsonify({"message": "Contact deleted"}), 200

if __name__ == '__main__':
    app.run(debug=True)

