API Automation Framework (Pytest + Requests)
🚀 Overview


This is an API test automation framework built using Python and Pytest.
It validates REST APIs using response assertions, schema validation, and CI/CD integration via GitHub Actions.


API used for testing: https://jsonplaceholder.typicode.com


🧰 Tech Stack
Python
Pytest
Requests
JSON Schema (jsonschema)
GitHub Actions (CI/CD)


📁 Project Structure
API-Automation/
│
├── tests/
│   ├── api/
│   │   ├── test_posts.py
│   │   ├── test_comments.py
│
├── utils/
│   ├── api_client.py
│   ├── schema_validator.py
│
├── schemas/
│   ├── posts_schema.json
│   ├── comments_schema.json
│
├── conftest.py
├── requirements.txt
├── pytest.ini
├── .github/workflows/
│   └── python-app.yml


🧪 What is Covered in Testing

✔ API Functional Testing
GET / POST / PUT / DELETE requests
Status code validation
Response body validation
Query parameter testing

✔ Response Validation
JSON schema validation
Key/value assertions
Data type validation

✔ Headers Validation
Content-Type verification
Response header checks

✔ Negative Testing
Invalid endpoints
Invalid queries
Expected failures (xfail)

🧠 Key Concepts Learned
🔹 Pytest Framework
Fixtures (conftest.py)
Test structuring with classes
Markers (xfail, parameterization)
Scope handling issues

🔹 API Automation Design
Built reusable API client class
Centralized base URL handling
Reduced repeated request code

🔹 Schema Validation
Validated API contract using JSON Schema
Ensured response structure consistency

🔹 Debugging Real Issues
Fixed fixture scope mismatch errors
Handled JSON decode errors
Fixed list vs object response issues

🔹 CI/CD (GitHub Actions)
Automated test execution on push/pull request
Installed dependencies in pipeline
Ran linting + pytest in CI

🔹 Code Quality
Used Flake8 for static code checks
Maintained clean and consistent code style

⚙️ How to Run
Install dependencies
pip install -r requirements.txt
Run tests
pytest -v
Run with HTML report
pytest --html=reports/report.html

🔄 CI/CD Pipeline (GitHub Actions)

Pipeline automatically:

Checkout code
Setup Python environment
Install dependencies
Run Flake8 lint checks
Execute pytest suite

🎯 Key Outcome
Built a modular API automation framework
Learned real-world pytest architecture
Understood schema-based validation
Fixed CI/CD pipeline failures
Gained debugging experience in test automation

📌 Future Enhancements
Add logging framework
Add Allure reporting
Dockerize test execution
Add environment configs (dev/qa/prod)
Expand API coverage with authentication testing
