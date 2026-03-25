from flask import Flask, request, jsonify, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory(os.path.dirname(__file__), 'index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    
    appetizers = data['appetizers']
    main_courses = data['mainCourses']
    desserts = data['desserts']
    drinks = data['drinks']
    num_of_friends = data['numFriends']
    tip_percent = data['tipPercent'] / 100  # Convert percentage to decimal
    
    running_total = appetizers + main_courses + desserts + drinks
    tip = running_total * tip_percent
    total_with_tip = running_total + tip
    final_bill = total_with_tip / num_of_friends
    each_pays = round(final_bill, 2)
    
    return jsonify({
        'totalBill': running_total,
        'tipAmount': tip,
        'totalWithTip': total_with_tip,
        'eachPays': each_pays
    })

if __name__ == '__main__':
    app.run(debug=True)