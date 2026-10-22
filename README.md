\# Python Automation Testing Framework



A Python-based automation testing framework that combines UI automation, REST API testing, automated test reporting, and continuous integration using Jenkins.



\## Project Overview



This project automates web application UI scenarios and REST API validation. It uses Playwright and Pytest for test execution, Allure and Pytest HTML for reporting, and Jenkins for automated CI pipeline execution.



\## Tech Stack



\- \*\*Programming Language:\*\* Python

\- \*\*UI Automation:\*\* Playwright

\- \*\*Test Framework:\*\* Pytest

\- \*\*API Testing:\*\* Requests

\- \*\*Test Reports:\*\* Allure Report, Pytest HTML

\- \*\*CI/CD:\*\* Jenkins

\- \*\*Browser:\*\* Chromium

\- \*\*Version Control:\*\* Git (for repository management)



\## Project Structure



```text

C:\\aasignment

â”œâ”€â”€ tests/

â”‚   â”œâ”€â”€ api\_tests.py

â”‚   â”œâ”€â”€ ui\_tests.py

â”‚   â””â”€â”€ conftest.py

â”œâ”€â”€ screenshots/

â”œâ”€â”€ reports/

â”‚   â””â”€â”€ report.html

â”œâ”€â”€ allure-results/

â”œâ”€â”€ allure-report/

â”œâ”€â”€ requirements.txt

â”œâ”€â”€ pytest.ini

â”œâ”€â”€ Jenkinsfile

â”œâ”€â”€ TEST\_PLAN.md

â””â”€â”€ README.md

```



\*\*Note:\*\* Generated reports, screenshots, and local environment files may be excluded from version control according to the project's `.gitignore` configuration.



\## Test Coverage



\### UI Automation



\- Verify the homepage loads successfully.

\- Verify contact-page navigation.

\- Run browser tests using Playwright and Pytest.

\- Capture screenshots when UI tests fail.

\- Attach failure screenshots to Allure results.



\### REST API Testing



\- Validate the list-users endpoint.

\- Validate the single-user endpoint.

\- Verify the expected 404 response for a nonexistent user.

\- Use an API key stored securely in an environment variable or Jenkins credential.



\## Prerequisites



Install the following before running the project:



\- Python

\- Java (for Allure reporting)

\- Playwright browser dependencies

\- Allure command-line tool

\- Jenkins (for CI pipeline execution)



\## Setup and Installation



Open PowerShell and navigate to the project directory:



```powershell

cd C:\\aasignment

```



Activate the virtual environment:



```powershell

.\\.venv\\Scripts\\Activate.ps1

```



Install dependencies:



```powershell

python -m pip install -r requirements.txt

python -m pip install pytest-playwright pytest-html allure-pytest

```



If Chromium is not installed for Playwright, install it using:



```powershell

python -m playwright install chromium

```



\## Running Tests



Run all tests:



```powershell

python -m pytest -v tests

```



Run UI tests only:



```powershell

python -m pytest -v tests\\ui\_tests.py

```



Run API tests only:



```powershell

python -m pytest -v tests\\api\_tests.py

```



\### API Credential Configuration



The API tests require a valid ReqRes API key.



Set the key in PowerShell for the current session:



```powershell

$env:REQRES\_API\_KEY = "YOUR\_API\_KEY"

```



Then execute the API tests:



```powershell

python -m pytest -v tests\\api\_tests.py

```



Replace the placeholder with your valid key. Never commit API keys or other secrets to GitHub.



\## Generating Test Reports



\### Pytest HTML Report



```powershell

python -m pytest -v tests --html=reports/report.html --self-contained-html

```



Open the generated report:



```powershell

Start-Process .\\reports\\report.html

```



\### Allure Report



Generate Allure result data:



```powershell

python -m pytest -v tests --alluredir=allure-results

```



Generate the report:



```powershell

allure generate allure-results --clean -o allure-report

```



Open the report:



```powershell

allure open allure-report

```



Ensure Java and Allure are correctly configured in your environment. If the `allure` command is not in `PATH`, use the full path to `allure.bat`.



\## Jenkins CI Pipeline



The Jenkins pipeline automates the following stages:



1\. Check Python, Playwright, Java, and Allure environments.

2\. Install project dependencies.

3\. Verify API credential availability.

4\. Execute UI and API tests.

5\. Generate Pytest HTML and Allure reports.

6\. Archive test artifacts and publish reports.



\### Jenkins Job



\*\*Job name:\*\* `Python-Automation-Tests`



\*\*Project directory:\*\* `C:\\aasignment`



The pipeline uses Jenkins credentials for the ReqRes API key. Configure the credential ID `reqres-api-key` in Jenkins before running the job.



\### Latest Verified Execution



\- \*\*Build:\*\* #19

\- \*\*Total tests:\*\* 5

\- \*\*Passed:\*\* 5

\- \*\*Failed:\*\* 0

\- \*\*Result:\*\* SUCCESS

\- \*\*Reports:\*\* Pytest HTML and Allure reports generated successfully



These results describe the verified execution of Build #19; future runs may have different results.



\## Screenshot on Test Failure



The Pytest reporting hook in `tests/conftest.py` captures a full-page screenshot when a test fails during its execution phase.



Screenshots are saved to the `screenshots/` directory and attached to the corresponding Allure test result.



This helps with debugging UI failures and investigating unexpected application behavior.



\## Key Learning Outcomes



\- Building UI automation tests using Playwright and Pytest.

\- Validating REST API responses.

\- Managing credentials through environment variables and Jenkins.

\- Generating HTML and Allure reports.

\- Capturing failure screenshots and attaching them to test results.

\- Integrating automated tests into a Jenkins pipeline.



\## Future Improvements



\- Add more positive and negative API scenarios.

\- Add reusable Page Object Model classes.

\- Add retry and flaky-test analysis.

\- Integrate GitHub-based source control and automated pipeline triggers.

\- Add richer test data management and environment configuration.



\## Author



\*\*QA Automation / SDET Portfolio Project\*\*



Technologies: Python | Playwright | Pytest | REST API Testing | Jenkins | Allure
