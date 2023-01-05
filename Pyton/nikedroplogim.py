import requests
import json

# Set the URL for the drop page and the desired shoe
drop_url = "https://www.nike.com/drop/shoes"
shoe_id = 123456

# Set the time for the drop (9:00 AM in this example)
drop_time = "09:00:00"

# Set your Nike account credentials
username = "your_username"
password = "your_password"

# Set the number of attempts to buy the shoe (e.g. 10 attempts)
max_attempts = 10

# Set the delay between attempts (e.g. 5 seconds)
delay = 5

# Set a flag to indicate whether the shoe was successfully bought
shoe_bought = False

# Set a counter for the number of attempts
attempts = 0

# Loop until the shoe is bought or the max number of attempts is reached
while not shoe_bought and attempts < max_attempts:
    # Check the current time
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    
    # If it is time for the drop, try to buy the shoe
    if current_time == drop_time:
        # Log in to your Nike account
        login_url = "https://www.nike.com/login"
        data = {"username": username, "password": password}
        response = requests.post(login_url, data=data)
        
        # Check if the login was successful
        if response.status_code == 200:
            # Add the desired shoe to your cart
            add_to_cart_url = f"{drop_url}/{shoe_id}/add-to-cart"
            response = requests.post(add_to_cart_url)
            
            # Check if the shoe was added to the cart successfully
            if response.status_code == 200:
                # Check the contents of the cart
                cart_url = "https://www.nike.com/cart"
                response = requests.get(cart_url)
                cart = json.loads(response.text)
                
                # If the desired shoe is in the cart, try to checkout
                if shoe_id in cart["items"]:
                    checkout_url = "https://www.nike.com/checkout"
                    response = requests.post(checkout_url)
                    
                    # If the checkout was successful, set the flag to indicate that the shoe was bought
                    if response.status_code == 200:
                        shoe_bought = True
            
    # If the shoe was not bought, wait for the specified delay and try again
    if not shoe_bought:
        time.sleep(delay)
        attempts += 1

# If the shoe was bought, print a success message
if shoe_bought:
    print("Successfully bought the desired shoe!")

# If the max number of attempts was reached, print a failure message
else:
    print("Failed to buy the desired shoe :(")
