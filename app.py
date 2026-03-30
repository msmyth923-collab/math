from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/add', methods=['GET', 'POST'])
def add_numbers():
    """
    Add two numbers and return the result.
    
    GET: /add?a=5&b=3
    POST: {"a": 5, "b": 3}
    """
    try:
        if request.method == 'POST':
            data = request.get_json(silent=True)
            if data is None:
                return jsonify({'error': 'Request body must be JSON.'}), 400
            a = data.get('a')
            b = data.get('b')
        else:  # GET request
            a = request.args.get('a')
            b = request.args.get('b')
        
        if a is None or b is None:
            return jsonify({'error': 'Missing required parameters: a and b.'}), 400
        
        a = float(a)
        b = float(b)
        
        result = a + b
        return jsonify({
            'a': a,
            'b': b,
            'result': result
        })
    except (TypeError, ValueError):
        return jsonify({'error': 'Invalid input. Please provide numeric values for a and b.'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        'message': 'Adder Service',
        'usage': {
            'GET': '/add?a=5&b=3',
            'POST': '/add with JSON body {"a": 5, "b": 3}'
        }
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
