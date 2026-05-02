# Edtech-Web-application

Project Title :
Automated Testing of the Web Application using Python

---

Project Objective :

The primary objective of this project is to automate the testing of the GUVI web application (https://www.guvi.in) by simulating real user interactions and validating key UI functionalities. The automation ensures the reliability, usability, and correctness of the application across different scenarios.

---

Scope of Testing :

- Cross-browser testing (Chrome, Firefox, Edge, Safari)
- UI validation and functional testing
- Navigation flow verification
- Login and logout functionality testing
- Positive and negative test scenarios

---

Tech Stack :

- Programming Language: Python
- Automation Tool: Selenium WebDriver
- Test Framework: PyTest
- Driver Management: WebDriver Manager
- Reporting: PyTest HTML Report

---

Project Structure :

guvi-automation/
│── tests/
│ ├── test_home.py
│ ├── test_login.py
│ ├── test_navigation.py
│
│── pages/
│ ├── base_page.py
│ ├── home_page.py
│ ├── login_page.py
│
│── utils/
│ ├── driver_factory.py
│ ├── logger.py
│
│── reports/
│── screenshots/
│── conftest.py
│── requirements.txt
│── README.md

---

Setup Instructions :

1. Clone the Repository

git clone <https://github.com/sundharam-19>
cd guvi-automation

2. Install Dependencies

pip install -r requirements.txt

3. Run Tests

pytest

4. Generate HTML Report

pytest --html=reports/report.html

---

Test Cases Covered :

🔹 Test Case 1

- Verify if the URL loads successfully

🔹 Test Case 2

- Validate webpage title

🔹 Test Case 3

- Check visibility & clickability of Login button

🔹 Test Case 4

- Check visibility & clickability of Sign-Up button

🔹 Test Case 5

- Validate redirection to Sign-Up page

🔹 Test Case 6

- Verify login with valid credentials

🔹 Test Case 7

- Verify login with invalid credentials

🔹 Test Case 8

- Validate presence of menu items (Courses, LIVE Classes, Practice)

🔹 Test Case 9

- Verify presence of Dobby Assistant chatbot

🔹 Test Case 10

- Validate logout functionality

---

Framework Design :

1.Page Object Model (POM)

The project follows the Page Object Model design pattern to :

- Improve code reusability
- Enhance readability
- Simplify maintenance

2.Cross-Browser Testing

Implemented using parameterization in PyTest.

3.Exception Handling

Robust exception handling is implemented to ensure test stability.

---

Reporting :

- HTML reports are generated after execution
- Screenshots can be captured on failure (optional enhancement)

---

Key Features :

- Modular and scalable framework
- Clean and maintainable code
- Reusable components
- Cross-browser compatibility
- Automated test execution

---

Best Practices Followed :

- Object-Oriented Programming (OOP)
- Proper code documentation
- Meaningful naming conventions
- Separation of concerns
- Test isolation

---
