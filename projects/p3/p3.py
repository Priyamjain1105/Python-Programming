# app.py
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

# Create a simple Flask app instance
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projects/p3/orders.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Order model
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(50), default='Pending')

    def __repr__(self):
        return f"<Order {self.id}>"

# Create the database and some initial data
@app.before_first_request
def create_tables():
    db.create_all()
    # Add some initial orders if they don't exist
    if not Order.query.first():
        order1 = Order(status='Pending')
        order2 = Order(status='Shipped')
        order3 = Order(status='Delivered')
        db.session.add_all([order1, order2, order3])
        db.session.commit()

# --- ROUTES ---

# This route displays the list of orders
@app.route('/')
def index():
    orders = Order.query.all()
    return render_template('index.html', orders=orders)

# This is the new route you need to handle the update
# It accepts a POST request from our JavaScript
@app.route('/update_order_status', methods=['POST'])
def update_order_status():
    # Get the data sent from the JavaScript fetch request
    data = request.get_json()
    order_id = data.get('order_id')
    new_status = data.get('new_status')

    # Find the order in the database
    order = Order.query.get(order_id)

    if order:
        # Update the order's status and commit to the database
        order.status = new_status
        db.session.commit()
        # Return a success message as a JSON response
        return jsonify({'success': True, 'message': 'Order updated successfully!', 'new_status': new_status})
    else:
        # If the order is not found, return a failure message
        return jsonify({'success': False, 'message': 'Order not found!'}), 404

if __name__ == '__main__':
    # Make sure the 'templates' directory exists
    if not os.path.exists('templates'):
        os.makedirs('templates')

    # Create the HTML file if it doesn't exist
    html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Order List</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    fontFamily: {
                        sans: ['Inter', 'sans-serif'],
                    },
                },
            },
        };
    </script>
</head>
<body class="bg-gray-100 p-8 font-sans">

    <div class="max-w-4xl mx-auto bg-white p-6 rounded-lg shadow-xl">
        <h1 class="text-3xl font-bold mb-6 text-gray-800">Order Management</h1>
        <p class="text-gray-600 mb-6">Click an update button to change an order's status and see the change instantly, without a page reload.</p>

        <div class="space-y-4">
            {% for order in orders %}
            <div class="order-item bg-gray-50 p-4 rounded-lg flex items-center justify-between shadow-sm" data-order-id="{{ order.id }}">
                <div>
                    <span class="font-semibold text-lg text-gray-900">Order #{{ order.id }}</span>
                    <span class="text-sm text-gray-500 ml-2">Status:</span>
                    <span id="status-{{ order.id }}" class="order-status text-blue-600 font-medium ml-1">
                        {{ order.status }}
                    </span>
                </div>
                <div class="flex items-center space-x-2">
                    <input type="text" id="new-status-{{ order.id }}" value="Shipped" placeholder="New Status"
                           class="w-32 px-3 py-1 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500">
                    <button onclick="updateOrder({{ order.id }})"
                            class="update-btn px-4 py-2 bg-blue-500 text-white font-medium rounded-lg hover:bg-blue-600 transition-colors duration-200 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2">
                        Update
                    </button>
                </div>
            </div>
            {% endfor %}
        </div>

        <div id="message-box" class="fixed bottom-4 right-4 bg-green-500 text-white px-6 py-3 rounded-lg shadow-xl hidden transition-all duration-300">
            Order updated successfully!
        </div>
    </div>

    <script>
        function showMessage(message, type) {
            const msgBox = document.getElementById('message-box');
            msgBox.textContent = message;
            if (type === 'success') {
                msgBox.className = 'fixed bottom-4 right-4 bg-green-500 text-white px-6 py-3 rounded-lg shadow-xl block transition-all duration-300';
            } else {
                msgBox.className = 'fixed bottom-4 right-4 bg-red-500 text-white px-6 py-3 rounded-lg shadow-xl block transition-all duration-300';
            }
            // Hide the message after 3 seconds
            setTimeout(() => {
                msgBox.className = 'fixed bottom-4 right-4 bg-green-500 text-white px-6 py-3 rounded-lg shadow-xl hidden transition-all duration-300';
            }, 3000);
        }

        async function updateOrder(orderId) {
            // Get the new status from the corresponding input field
            const newStatusInput = document.getElementById(`new-status-${orderId}`);
            const newStatus = newStatusInput.value;

            // Prepare the data to send to the Flask route
            const data = {
                order_id: orderId,
                new_status: newStatus
            };

            try {
                // Use the fetch API to send a POST request
                const response = await fetch('/update_order_status', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(data), // Convert the JavaScript object to a JSON string
                });

                // Parse the JSON response from the server
                const result = await response.json();

                if (result.success) {
                    // Update the status on the page without reloading
                    const statusElement = document.getElementById(`status-${orderId}`);
                    statusElement.textContent = result.new_status;
                    showMessage(result.message, 'success');
                } else {
                    showMessage(result.message, 'error');
                    console.error('Error:', result.message);
                }
            } catch (error) {
                console.error('Fetch error:', error);
                showMessage('An error occurred while updating the order.', 'error');
            }
        }
    </script>
</body>
</html>
"""
    with open('templates/index.html', 'w') as f:
        f.write(html_content)

    app.run(debug=True)
