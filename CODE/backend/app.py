from flask import Flask, jsonify, request
from flask_cors import CORS

from optimizer import optimize_products


app = Flask(__name__)

CORS(app)


# -----------------------------------------
# HOME
# -----------------------------------------

@app.route("/")
def home():

    return jsonify({
        "status": "success",
        "message": "Warehouse Slotting Optimizer Backend is running"
    })


# -----------------------------------------
# STATUS
# -----------------------------------------

@app.route("/api/status")
def status():

    return jsonify({
        "status": "success",
        "message": "Backend connected successfully"
    })


# -----------------------------------------
# OPTIMIZE
# -----------------------------------------

@app.route("/api/optimize", methods=["POST"])
def optimize():

    try:

        data = request.get_json()

        if not data:

            return jsonify({
                "status": "error",
                "message": "No data received"
            }), 400


        products = data.get("products")


        if not products:

            return jsonify({
                "status": "error",
                "message": "No products received"
            }), 400


        if not isinstance(products, list):

            return jsonify({
                "status": "error",
                "message": "Products must be a list"
            }), 400


        optimized_products = optimize_products(products)


        return jsonify({

            "status": "success",

            "message": "Products optimized successfully",

            "optimized_products": optimized_products

        })


    except Exception as error:

        print("ERROR:", error)

        return jsonify({

            "status": "error",

            "message": str(error)

        }), 500


# -----------------------------------------
# RUN SERVER
# -----------------------------------------

if __name__ == "__main__":

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )