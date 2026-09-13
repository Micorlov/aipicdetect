"""Budget guard: revoke public access to the Cloud Run service once the month's cost reaches the budget."""

import base64
import json
import os

import functions_framework
from google.cloud import run_v2

SERVICE = os.environ["SERVICE_NAME"]
PUBLIC_MEMBER = "allUsers"
INVOKER_ROLE = "roles/run.invoker"


@functions_framework.cloud_event
def guard(cloud_event) -> None:
    payload = json.loads(base64.b64decode(cloud_event.data["message"]["data"]))
    cost = float(payload["costAmount"])
    budget = float(payload["budgetAmount"])
    currency = payload.get("currencyCode", "")
    print(f"budget check: cost {cost} / budget {budget} {currency}")
    if cost < budget:
        return

    client = run_v2.ServicesClient()
    policy = client.get_iam_policy(request={"resource": SERVICE})
    invoker = next((b for b in policy.bindings if b.role == INVOKER_ROLE), None)
    if invoker is None or PUBLIC_MEMBER not in invoker.members:
        print("public access already revoked")
        return

    invoker.members.remove(PUBLIC_MEMBER)
    client.set_iam_policy(request={"resource": SERVICE, "policy": policy})
    print(f"budget exceeded: public access to {SERVICE} revoked")
