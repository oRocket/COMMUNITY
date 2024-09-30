# Community Watch App

## Homepage Screenshot
![Homepage](images/homepage.jpg)

## Overview
The Community Watch App is designed to help communities report and manage incidents effectively. Users can report incidents, view reported incidents, and receive notifications about new reports.


## Access the App
You can access the live version of the Community Watch App at [Community Watch](https://orocket.pythonanywhere.com/).

## Features
- User authentication
- Report new incidents
- View all reported incidents
- Notification alerts for new incidents

## Technologies Used
- Django (Backend)
- HTML/CSS (Frontend)
- Bootstrap (Styling)
- JavaScript (Client-side interactivity)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/oRocket/neighborhood_watch.git
   cd neighborhood_watch
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations:
   ```bash
   python manage.py migrate
   ```

5. Start the development server:
   ```bash
   python manage.py runserver
   ```

6. Access the app at `http://127.0.0.1:8000/`.

## Usage
- Register or log in to your account.
- Navigate to the "Report New Incident" section to report an incident.
- View all reported incidents on the dashboard.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## Author
Albert Opoku-Twumasi
[GitHub Profile](https://github.com/oRocket)

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
