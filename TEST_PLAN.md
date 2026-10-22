# Reqres API Test Plan

## Objective and scope

Validate the Reqres users API with automated functional tests and an optional,
small Locust load test. No web application or web-app requirements were supplied,
so this plan covers the API assignment only.

## Functional test cases

| Test | Request | Expected result |
| --- | --- | --- |
| List users | `GET /api/users?page=2` | HTTP 200; response includes user data, page 2, and email fields |
| Get one user | `GET /api/users/2` | HTTP 200; response identifies user 2 and includes an email |
| Unknown user | `GET /api/users/99999` | HTTP 404 |

Run from the project directory in PowerShell. Set a valid Reqres API key in the
current session; do not put the key in source code or commit it.

```powershell
$env:REQRES_API_KEY = "your-real-api-key"
.\.venv\Scripts\python.exe -m pytest -v tests\test_reqres_api.py
```

## Optional load test

The Locust user requests `GET /api/users/2`, waits 1–2 seconds between requests,
and stops after at most 100 requests in a single Locust process. The API's daily
limit applies to all requests, including functional tests and repeated runs.
Count the functional and any previous load-test requests against that daily
limit; run only one load scenario if it would otherwise be exceeded.

Example: run a single five-user scenario for at most 30 seconds. Requests are
limited to 100 even if the run duration would allow more.

```powershell
$env:REQRES_API_KEY = "your-real-api-key"
.\.venv\Scripts\python.exe -m locust -f locust_load_test.py --headless -u 5 -r 1 --run-time 30s --csv reqres-5-users
```

For a ten-user scenario, use `-u 10 -r 2` instead of `-u 5 -r 1`, and run it
instead of—not in addition to—the five-user scenario on the same day.
Locust prints request counts, failures, and response-time statistics; the
`--csv` option saves the results for reporting.

## Results

| Run | Outcome |
| --- | --- |
| Functional API tests | 3 passed in 2.46 seconds (2026-10-21) |
| Locust load test | Not run; no load-test measurements have been recorded |
