
import os
import gevent
from gevent.lock import Semaphore
from locust import HttpUser, between, task
from locust.exception import StopUser

MAX_REQUESTS = 100

_request_count = 0
_request_lock = Semaphore()
_stop_requested = False


class ReqresUser(HttpUser):
    host = "https://reqres.in"
    wait_time = between(2, 4)

    def on_start(self):
        api_key = os.getenv("REQRES_API_KEY")
        if not api_key:
            raise RuntimeError(
                "Set REQRES_API_KEY before starting Locust."
            )

        self.client.headers.update({"x-api-key": api_key})

    @task
    def get_single_user(self):
        global _request_count, _stop_requested

        with _request_lock:
            if _request_count >= MAX_REQUESTS:
                if not _stop_requested:
                    _stop_requested = True
                    gevent.spawn(self.environment.runner.quit)
                raise StopUser()

            # Reserve a request slot before sending.
            _request_count += 1

        with self.client.get(
            "/api/users/2",
            name="GET /api/users/2",
            catch_response=True,
        ) as response:
            if response.status_code != 200:
                response.failure(
                    f"Expected HTTP 200, got {response.status_code}"
                )
            else:
                try:
                    body = response.json()
                    if body.get("data", {}).get("id") != 2:
                        response.failure("Unexpected user ID")
                    else:
                        response.success()
                except ValueError:
                    response.failure("Invalid JSON response")
