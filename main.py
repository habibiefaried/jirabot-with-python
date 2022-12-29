from typing import Union

from fastapi import Request, FastAPI
from jirareq import comment, issue
from jira import JIRA
import sys

app = FastAPI()

jiraOptions = {"server": "http://194.233.68.255:48082/"}
tokenf = open("jiratoken", "r")

jira = JIRA(options=jiraOptions, token_auth=tokenf.readline())
myself = jira.myself()
try:
    print("Logged in as " + myself["name"])
except Exception as e:
    print(e)
    sys.exit(2)

## CONSTANT
WORKING_ON_IT = "Working on it..."
WAITING_APPROVAL = "Waiting for approval..."
APPROVED = "APPROVED"


@app.post("/{ticket_id}")
async def read_root(ticket_id, request: Request):
    x = await request.json()
    if x["webhookEvent"] == "comment_created":
        if x["comment"]["body"] == APPROVED:  # prevent infinite looping
            jira.add_comment(issue=ticket_id, body=WORKING_ON_IT)
            comment.process(x["comment"])

    elif x["webhookEvent"] == "jira:issue_created":
        print("Replying to " + ticket_id)
        jira.add_comment(issue=ticket_id, body=WAITING_APPROVAL)
        issue.process(x["issue"])
    return {"Hello": "World"}
