from flask import Flask, request

app = Flask(__name__)

stores_list = [
    {
        "name" : "Demo Store"
        , "items" : [
            {
                "name" : "chair"
                , "price" : 15.99
            }
        ]
    }
]

@app.get( '/' ) # http://127.0.0.1:5000/
def welcomeNote():
    return { "Welcome" : "Welcome to Our Grocery App" }

@app.get( '/stores' ) # http://127.0.0.1:5000/stores
def get_stores():
    return { "Stores" : stores_list }
    # return str( stores )

@app.post( '/addStore' ) # http://127.0.0.1:5000/stores
def create_store():
    request_data = request.get_json()
    print( f"request_data = { request_data }" )

    new_store = {"name" : request_data["name"], "items" : [] }
    stores_list.append( new_store )

    return new_store, 201

@app.get( '/stores/<string:store>' ) # http://127.0.0.1:5000/store/store_name
def getStore(store):

    try:
        selected_store = list( filter( lambda i : i['name'] == store , stores_list ) )[0]
        return {"selected_store" : selected_store }, 200
    except Exception as e:
        return { "Error" : f"No Data Found, Exception = {e}" }, 404


@app.post( '/stores/<string:store>/addItem' ) # http://127.0.0.1:5000/store/store_name/addItem
def addItem(store):
    request_data = request.get_json()

    item_data = { "name" : request_data["name"]
                , "price" : request_data["price"]
                 }

    try:
        selected_store = list( filter( lambda i : i['name'] == store , stores_list ) )
        print( f"selected_store = { selected_store }" )

        selected_store = selected_store[0]
        selected_store["items"].append( item_data )

        return { "selected_store" : selected_store }, 201

    except Exception as e:
        return { "Error" : f"No Data Found, Exception = {e}" }, 404