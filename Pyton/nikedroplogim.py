import requests
import json

# Set the URL for the drop page and the desired shoe
drop_url = "https://www.nike.com/drop/shoes"
shoe_id = 123456

# Set the time for the drop (9:00 AM in this example)
drop_time = "09:00:00"

username = "your_username"
password = "your_password"

max_attempts = 10
delay = 5
shoe_bought = False
attempts = 0


while not shoe_bought and attempts < max_attempts:

    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    if current_time == drop_time:

        login_url = "https://www.nike.com/login"
        data = {"username": username, "password": password}
        response = requests.post(login_url, data=data)

        if response.status_code == 200:

            add_to_cart_url = f"{drop_url}/{shoe_id}/add-to-cart"
            response = requests.post(add_to_cart_url)

            if response.status_code == 200:

                cart_url = "https://www.nike.com/cart"
                response = requests.get(cart_url)
                cart = json.loads(response.text)

                if shoe_id in cart["items"]:
                    checkout_url = "https://www.nike.com/checkout"
                    response = requests.post(checkout_url)

                    if response.status_code == 200:
                        shoe_bought = True

    if not shoe_bought:
        time.sleep(delay)
        attempts += 1


if shoe_bought:
    print("Successfully bought the desired shoe!")


else:
    print("Failed to buy the desired shoe :(")
