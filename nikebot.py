# Import the necessary libraries
import datetime
import requests
import json

# Set the drop time (9:00 AM in this example)
drop_time = "23:19:20"

# Set the URL of the drop page
drop_url = "https://www.nike.com/pl/launch/t/nike-sb-dunk-low-x-concepts-orange-lobster"

# Set the URL of the cart page
cart_url = "https://www.nike.com/cart"

# Set the authentication headers
headers = {
    "Authorization": "Bearer YOUR_AUTH_TOKEN"
}

# Set the product data
product_data = {
    "productId": "FD8776-800",
    "qty": 1
}

# Wait until the drop time
while True:
    # Get the current time
    current_time = datetime.datetime.now().strftime("%H:%M:%S")

    # Check if the current time is the drop time
    if current_time == drop_time:
        # Add the product to the cart
        response = requests.post(
            cart_url,
            headers=headers,
            json=product_data
        )

        # Check the response status code
        if response.status_code == 200:
            # Product added to cart successfully
            break
        else:
            # Failed to add product to cart
            print("Failed to add product to cart")
