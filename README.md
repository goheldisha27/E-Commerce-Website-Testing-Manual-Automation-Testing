# E-Commerce Website QA Testing Project

**Application under test:** https://www.saucedemo.com/  
**Focus:** Manual functional testing, test case design, defect reporting, test execution reporting, and optional Selenium automation.

## Project files
- `Test_Cases.xlsx` — 15 planned test cases for login, products, sorting, cart, checkout, and logout.
- `Bug_Report_Template.xlsx` — reusable defect-report template.
- `Test_Plan.docx` — scope, test approach, environment, and deliverables.
- `Test_Execution_Summary.docx` — execution report template; fill it only after running the tests.
- `automation/test_login.py` — optional Selenium tests for valid and invalid login.
- `automation/requirements.txt` — Python dependency list.

## Manual testing workflow
1. Open the demo website and review the test plan.
2. Execute each test case in `Test_Cases.xlsx`.
3. Record actual results and mark Pass/Fail/Blocked only after execution.
4. For a reproducible failure, complete `Bug_Report_Template.xlsx` and attach evidence.
5. Update `Test_Execution_Summary.docx` using your actual test results.

## Run Selenium tests (optional)
Install Python 3, then open a terminal in the `automation` folder and run:

```bash
python -m pip install -r requirements.txt
python -m unittest -v test_login.py
```

Chrome and internet access are required. Selenium Manager may manage the browser driver automatically.

## Test data
Use the public demo credentials displayed on the SauceDemo login page. The standard demo account is `standard_user` with password `secret_sauce`. Do not enter real personal or payment information.

## Important
This is a starter QA portfolio project. The test cases and templates are prepared, but execution results and defects are not fabricated. Run the tests and document only what you actually observe.
