from flask import Flask, jsonify, request
import redis
import click
app = Flask(__name__)

redis_client = redis.Redis(host='redis', port=6379, db=0)

# Endpoint GET /product/<id>
@app.route('/product/<id>', methods=['GET'])
def get_product(id):
    product_data = redis_client.hgetall(id)
    if not product_data:
        return jsonify({'error': 'Product not found.'}), 404
    product_data = {k.decode(): v.decode() for k, v in product_data.items()}
    return jsonify(product_data), 200


# Endpoint POST /product/<id>
@app.route('/product/<id>', methods=['POST'])
def create_product(id):
    data = request.get_json()

    redis_client.hmset(id, data)

    return jsonify({'message': 'Product created successfully.'}), 201


@app.cli.command()
@click.argument('id')
def delete_product(id):
    redis_client.delete(id)

    print(f'Product {id} deleted successfully.')


