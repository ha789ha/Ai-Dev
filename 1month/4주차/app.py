from flask import Flask, jsonify, request

app = Flask(__name__)

menus = [
    {'id':1, 'name':'espresso', 'price':3800},
    {'id':2, 'name':'americano', 'price':4100},
    {'id':3, 'name':'latte', 'price':3000}
]

@app.route('/')
def hello_flask():
    return 'Hello, world'

# GET/menus
@app.route('/menus')
def get_menus():
    return jsonify({'menus':menus})

# POST / menus
@app.route('/menus', methods=['POST']) # method의 디폴트는 GET이다
def create_menu(): # requestrk json이라 가정
    # 전달받은 자료를 menus 자원에 추가
    request_data = request.get_json() # {'name':....}
    new_menu = {
        'id':4,
        'name':request_data['name'],
        'price':request_data['price']
    }
    menus.append(new_menu)
    return jsonify(new_menu)

# PUT / menus
@app.route('/menus', methods=['PUT'])
def update_menu():
    data = request.get_json()
    menu = {
        'id':data['id'],
        'name':data['name'],
        'price':data['price']
    }
    menus[data['id']-1]['name'] = data['name']
    menus[data['id']-1]['price'] = data['price']
    
    return jsonify(menus[data['id']-1])   
 
 # DELETE / menus
@app.route('/menus', methods=['DELETE'])
def delete_menu():
    data = request.get_json()
    menu = {
        'id':data['id']
    }
    menus.pop(data['id']-1)
    return jsonify(menus)   
    
    
    
if __name__ == "__main__":
    app.run()
    
