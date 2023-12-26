from flask import Flask, request, jsonify

app = Flask(__name__)

# Example data: a dictionary to store resources (replace this with a database in a real application)
resources = {
    1: {'name': 'Resource 1'},
    2: {'name': 'Resource 2'},
}

@app.route('/api/resource/<int:resource_id>', methods=['PUT'])
def update_resource(resource_id):
    if resource_id not in resources:
        return jsonify({'message': 'Resource not found'}), 404

    data = request.get_json()
    if not data:
        return jsonify({'message': 'No data provided'}), 400

    # Update the resource with the new data
    resources[resource_id]['name'] = data.get('name', resources[resource_id]['name'])

    return jsonify({'message': 'Resource updated successfully', 'resource': resources[resource_id]}), 200

if __name__ == '__main__':
    app.run(debug=True)
