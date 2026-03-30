from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/add', methods=['GET', 'POST'])
def add_numbers():
    """
    Add two numbers and return the result.
    
    GET: /add?a=5&b=7
    POST: {"a": 5, "b": 7}
    """
    try:
        if request.method == 'POST':
            data = request.get_json()
            a = float(data.get('a'))
            b = float(data.get('b'))
        else:  # GET request
            a = float(request.args.get('a'))
            b = float(request.args.get('b'))
        
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
            'GET': '/add?a=5&b=7',
            'POST': '/add with JSON body {"a": 5, "b": 7}'
        }
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
