# Back End Developer Capstone Project

This project is part of the Meta Backend Course on Coursera. It's a comprehensive demonstration of backend development skills, featuring a restaurant management system.

## 🌐 Web Interface

You can interact with the application directly from your web browser:

- **Menu Item Details**: To view the details of a single menu item, visit: [http://127.0.0.1:8000/restaurant/menu/1](http://127.0.0.1:8000/restaurant/menu/1)
- **Booking List**: To view the list of all bookings, visit: [http://127.0.0.1:8000/restaurant/booking/tables/](http://127.0.0.1:8000/restaurant/booking/tables/)

## 🛠 Insomnia

For a more developer-focused interaction, you can use Insomnia:

- **Authentication**: Make a POST request to [http://127.0.0.1:8000/restaurant/api-token-auth/](http://127.0.0.1:8000/restaurant/api-token-auth/) to authenticate. You can provide either the user's credentials or the admin's.

- **Menu Details**: To get the details of all menu items, make a GET request to [http://127.0.0.1:8000/restaurant/menu/1](http://127.0.0.1:8000/restaurant/menu/1)

- **Add Menu Item**: To add a menu item, make a POST request to [http://127.0.0.1:8000/restaurant/menu/](http://127.0.0.1:8000/restaurant/menu/) and provide the details in JSON format in the body of the request.

- **Booking Details**: To get the details of bookings, make a GET request to [http://127.0.0.1:8000/restaurant/booking/tables/](http://127.0.0.1:8000/restaurant/booking/tables/)

- **User Token**: To create tokens for the user, visit [http://127.0.0.1:8000/auth/token/login/](http://127.0.0.1:8000/auth/token/login/)

Enjoy exploring the project!