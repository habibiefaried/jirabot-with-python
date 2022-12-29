## Issue created

```
{
    "timestamp": 1672219977993,
    "webhookEvent": "jira:issue_created",
    "issue_event_type_name": "issue_created",
    "user": {
        "self": "http://194.233.68.255:48082/rest/api/2/user?username=habibiefaried",
        "name": "habibiefaried",
        "key": "JIRAUSER10000",
        "emailAddress": "habibiefaried@gmail.com",
        "avatarUrls": {
            "48x48": "https://www.gravatar.com/avatar/cb74b3079de22fbf1f4a2f86463cae73?d=mm&s=48",
            "24x24": "https://www.gravatar.com/avatar/cb74b3079de22fbf1f4a2f86463cae73?d=mm&s=24",
            "16x16": "https://www.gravatar.com/avatar/cb74b3079de22fbf1f4a2f86463cae73?d=mm&s=16",
            "32x32": "https://www.gravatar.com/avatar/cb74b3079de22fbf1f4a2f86463cae73?d=mm&s=32"
        },
        "displayName": "Habibie Faried",
        "active": true,
        "timeZone": "GMT"
    },
    "issue": {
        "id": "10011",
        "self": "http://194.233.68.255:48082/rest/api/2/issue/10011",
        "key": "ST-6",
        "fields": {
            "issuetype": {
                "self": "http://194.233.68.255:48082/rest/api/2/issuetype/10004",
                "id": "10004",
                "description": "Created by Jira Service Management.",
                "iconUrl": "http://194.233.68.255:48082/secure/viewavatar?size=xsmall&avatarId=10641&avatarType=issuetype",
                "name": "Service Request",
                "subtask": false,
                "avatarId": 10641
            },
            "timespent": null,
            "project": {
                "self": "http://194.233.68.255:48082/rest/api/2/project/10001",
                "id": "10001",
                "key": "ST",
                "name": "service test",
                "projectTypeKey": "service_desk",
                "avatarUrls": {
                    "48x48": "http://194.233.68.255:48082/secure/projectavatar?avatarId=10324",
                    "24x24": "http://194.233.68.255:48082/secure/projectavatar?size=small&avatarId=10324",
                    "16x16": "http://194.233.68.255:48082/secure/projectavatar?size=xsmall&avatarId=10324",
                    "32x32": "http://194.233.68.255:48082/secure/projectavatar?size=medium&avatarId=10324"
                }
            },
            "fixVersions": [],
            "customfield_10110": null,
            "customfield_10111": null,
            "aggregatetimespent": null,
            "resolution": null,
            "customfield_10112": null,
            "customfield_10113": [],
            "customfield_10114": {
                "_links": {
                    "jiraRest": "http://194.233.68.255:48082/rest/api/2/issue/10011",
                    "web": "http://194.233.68.255:48082/servicedesk/customer/portal/1/ST-6",
                    "self": "http://194.233.68.255:48082/rest/servicedeskapi/request/10011"
                },
                "requestType": {
                    "id": "5",
                    "_links": {
                        "self": "http://194.233.68.255:48082/rest/servicedeskapi/servicedesk/1/requesttype/5"
                    },
                    "name": "New employee",
                    "description": "Onboard a new hire.",
                    "helpText": "",
                    "serviceDeskId": "1",
                    "groupIds": [
                        "1"
                    ],
                    "icon": {
                        "id": "10631",
                        "_links": {
                            "iconUrls": {
                                "48x48": "http://194.233.68.255:48082/secure/viewavatar?avatarType=SD_REQTYPE&size=large&avatarId=10631",
                                "24x24": "http://194.233.68.255:48082/secure/viewavatar?avatarType=SD_REQTYPE&size=small&avatarId=10631",
                                "16x16": "http://194.233.68.255:48082/secure/viewavatar?avatarType=SD_REQTYPE&size=xsmall&avatarId=10631",
                                "32x32": "http://194.233.68.255:48082/secure/viewavatar?avatarType=SD_REQTYPE&size=medium&avatarId=10631"
                            }
                        }
                    }
                },
                "currentStatus": {
                    "status": "Waiting for support",
                    "statusDate": {
                        "iso8601": "2022-12-28T09:32:57+0000",
                        "jira": "2022-12-28T09:32:57.836+0000",
                        "friendly": "Just now",
                        "epochMillis": 1672219977836
                    }
                }
            },
            "customfield_10104": null,
            "customfield_10105": "0|i0002f:",
            "customfield_10106": null,
            "customfield_10107": null,
            "customfield_10108": null,
            "customfield_10109": null,
            "resolutiondate": null,
            "workratio": -1,
            "lastViewed": null,
            "watches": {
                "self": "http://194.233.68.255:48082/rest/api/2/issue/ST-6/watchers",
                "watchCount": 0,
                "isWatching": false
            },
            "created": "2022-12-28T09:32:57.836+0000",
            "priority": {
                "self": "http://194.233.68.255:48082/rest/api/2/priority/3",
                "iconUrl": "http://194.233.68.255:48082/images/icons/priorities/medium.svg",
                "name": "Medium",
                "id": "3"
            },
            "customfield_10100": null,
            "labels": [],
            "timeestimate": null,
            "aggregatetimeoriginalestimate": null,
            "versions": [],
            "issuelinks": [],
            "assignee": null,
            "updated": "2022-12-28T09:32:57.836+0000",
            "status": {
                "self": "http://194.233.68.255:48082/rest/api/2/status/10003",
                "description": "This was auto-generated by Jira Service Management during workflow import",
                "iconUrl": "http://194.233.68.255:48082/images/icons/status_generic.gif",
                "name": "Waiting for support",
                "id": "10003",
                "statusCategory": {
                    "self": "http://194.233.68.255:48082/rest/api/2/statuscategory/4",
                    "id": 4,
                    "key": "indeterminate",
                    "colorName": "yellow",
                    "name": "In Progress"
                }
            },
            "components": [],
            "timeoriginalestimate": null,
            "description": "FIELD-2",
            "archiveddate": null,
            "timetracking": {},
            "attachment": [],
            "aggregatetimeestimate": null,
            "summary": "FIELD-1",
            "creator": {
                "self": "http://194.233.68.255:48082/rest/api/2/user?username=habibiefaried",
                "name": "habibiefaried",
                "key": "JIRAUSER10000",
                "emailAddress": "habibiefaried@gmail.com",
                "avatarUrls": {
                    "48x48": "https://www.gravatar.com/avatar/cb74b3079de22fbf1f4a2f86463cae73?d=mm&s=48",
                    "24x24": "https://www.gravatar.com/avatar/cb74b3079de22fbf1f4a2f86463cae73?d=mm&s=24",
                    "16x16": "https://www.gravatar.com/avatar/cb74b3079de22fbf1f4a2f86463cae73?d=mm&s=16",
                    "32x32": "https://www.gravatar.com/avatar/cb74b3079de22fbf1f4a2f86463cae73?d=mm&s=32"
                },
                "displayName": "Habibie Faried",
                "active": true,
                "timeZone": "GMT"
            },
            "subtasks": [],
            "reporter": {
                "self": "http://194.233.68.255:48082/rest/api/2/user?username=habibiefaried",
                "name": "habibiefaried",
                "key": "JIRAUSER10000",
                "emailAddress": "habibiefaried@gmail.com",
                "avatarUrls": {
                    "48x48": "https://www.gravatar.com/avatar/cb74b3079de22fbf1f4a2f86463cae73?d=mm&s=48",
                    "24x24": "https://www.gravatar.com/avatar/cb74b3079de22fbf1f4a2f86463cae73?d=mm&s=24",
                    "16x16": "https://www.gravatar.com/avatar/cb74b3079de22fbf1f4a2f86463cae73?d=mm&s=16",
                    "32x32": "https://www.gravatar.com/avatar/cb74b3079de22fbf1f4a2f86463cae73?d=mm&s=32"
                },
                "displayName": "Habibie Faried",
                "active": true,
                "timeZone": "GMT"
            },
            "customfield_10120": null,
            "customfield_10000": "{summaryBean=com.atlassian.jira.plugin.devstatus.rest.SummaryBean@d2235f81[summary={pullrequest=com.atlassian.jira.plugin.devstatus.rest.SummaryItemBean@6b13ff69[overall=PullRequestOverallBean{stateCount=0, state='OPEN', details=PullRequestOverallDetails{openCount=0, mergedCount=0, declinedCount=0}},byInstanceType={}], build=com.atlassian.jira.plugin.devstatus.rest.SummaryItemBean@2a0246[overall=com.atlassian.jira.plugin.devstatus.summary.beans.BuildOverallBean@ada29c8d[failedBuildCount=0,successfulBuildCount=0,unknownBuildCount=0,count=0,lastUpdated=<null>,lastUpdatedTimestamp=<null>],byInstanceType={}], review=com.atlassian.jira.plugin.devstatus.rest.SummaryItemBean@cefe46c2[overall=com.atlassian.jira.plugin.devstatus.summary.beans.ReviewsOverallBean@6ab12812[stateCount=0,state=<null>,dueDate=<null>,overDue=false,count=0,lastUpdated=<null>,lastUpdatedTimestamp=<null>],byInstanceType={}], deployment-environment=com.atlassian.jira.plugin.devstatus.rest.SummaryItemBean@3663ed3f[overall=com.atlassian.jira.plugin.devstatus.summary.beans.DeploymentOverallBean@96bab94c[topEnvironments=[],showProjects=false,successfulCount=0,count=0,lastUpdated=<null>,lastUpdatedTimestamp=<null>],byInstanceType={}], repository=com.atlassian.jira.plugin.devstatus.rest.SummaryItemBean@77e53aa4[overall=com.atlassian.jira.plugin.devstatus.summary.beans.CommitOverallBean@e01bcf8b[count=0,lastUpdated=<null>,lastUpdatedTimestamp=<null>],byInstanceType={}], branch=com.atlassian.jira.plugin.devstatus.rest.SummaryItemBean@5f3136a7[overall=com.atlassian.jira.plugin.devstatus.summary.beans.BranchOverallBean@fa5c4812[count=0,lastUpdated=<null>,lastUpdatedTimestamp=<null>],byInstanceType={}]},errors=[],configErrors=[]], devSummaryJson={\"cachedValue\":{\"errors\":[],\"configErrors\":[],\"summary\":{\"pullrequest\":{\"overall\":{\"count\":0,\"lastUpdated\":null,\"stateCount\":0,\"state\":\"OPEN\",\"details\":{\"openCount\":0,\"mergedCount\":0,\"declinedCount\":0,\"total\":0},\"open\":true},\"byInstanceType\":{}},\"build\":{\"overall\":{\"count\":0,\"lastUpdated\":null,\"failedBuildCount\":0,\"successfulBuildCount\":0,\"unknownBuildCount\":0},\"byInstanceType\":{}},\"review\":{\"overall\":{\"count\":0,\"lastUpdated\":null,\"stateCount\":0,\"state\":null,\"dueDate\":null,\"overDue\":false,\"completed\":false},\"byInstanceType\":{}},\"deployment-environment\":{\"overall\":{\"count\":0,\"lastUpdated\":null,\"topEnvironments\":[],\"showProjects\":false,\"successfulCount\":0},\"byInstanceType\":{}},\"repository\":{\"overall\":{\"count\":0,\"lastUpdated\":null},\"byInstanceType\":{}},\"branch\":{\"overall\":{\"count\":0,\"lastUpdated\":null},\"byInstanceType\":{}}}},\"isStale\":false}}",
            "customfield_10121": {
                "self": "http://194.233.68.255:48082/rest/api/2/customFieldOption/10002",
                "value": "hahaha",
                "id": "10002",
                "disabled": false
            },
            "aggregateprogress": {
                "progress": 0,
                "total": 0
            },
            "customfield_10115": [],
            "customfield_10116": null,
            "environment": null,
            "customfield_10117": null,
            "customfield_10118": null,
            "customfield_10119": null,
            "duedate": "2023-03-17",
            "progress": {
                "progress": 0,
                "total": 0
            },
            "comment": {
                "comments": [],
                "maxResults": 0,
                "total": 0,
                "startAt": 0
            },
            "votes": {
                "self": "http://194.233.68.255:48082/rest/api/2/issue/ST-6/votes",
                "votes": 0,
                "hasVoted": false
            },
            "worklog": {
                "startAt": 0,
                "maxResults": 20,
                "total": 0,
                "worklogs": []
            },
            "archivedby": null
        }
    }
}
```

## Comment created

```
{
    "timestamp": 1672219779154,
    "webhookEvent": "comment_created",
    "comment": {
        "self": "http://194.233.68.255:48082/rest/api/2/issue/10010/comment/10002",
        "id": "10002",
        "author": {
            "self": "http://194.233.68.255:48082/rest/api/2/user?username=habibiefaried",
            "name": "habibiefaried",
            "key": "JIRAUSER10000",
            "emailAddress": "habibiefaried@gmail.com",
            "avatarUrls": {
                "48x48": "https://www.gravatar.com/avatar/cb74b3079de22fbf1f4a2f86463cae73?d=mm&s=48",
                "24x24": "https://www.gravatar.com/avatar/cb74b3079de22fbf1f4a2f86463cae73?d=mm&s=24",
                "16x16": "https://www.gravatar.com/avatar/cb74b3079de22fbf1f4a2f86463cae73?d=mm&s=16",
                "32x32": "https://www.gravatar.com/avatar/cb74b3079de22fbf1f4a2f86463cae73?d=mm&s=32"
            },
            "displayName": "Habibie Faried",
            "active": true,
            "timeZone": "GMT"
        },
        "body": "testtest",
        "updateAuthor": {
            "self": "http://194.233.68.255:48082/rest/api/2/user?username=habibiefaried",
            "name": "habibiefaried",
            "key": "JIRAUSER10000",
            "emailAddress": "habibiefaried@gmail.com",
            "avatarUrls": {
                "48x48": "https://www.gravatar.com/avatar/cb74b3079de22fbf1f4a2f86463cae73?d=mm&s=48",
                "24x24": "https://www.gravatar.com/avatar/cb74b3079de22fbf1f4a2f86463cae73?d=mm&s=24",
                "16x16": "https://www.gravatar.com/avatar/cb74b3079de22fbf1f4a2f86463cae73?d=mm&s=16",
                "32x32": "https://www.gravatar.com/avatar/cb74b3079de22fbf1f4a2f86463cae73?d=mm&s=32"
            },
            "displayName": "Habibie Faried",
            "active": true,
            "timeZone": "GMT"
        },
        "created": "2022-12-28T09:29:39.154+0000",
        "updated": "2022-12-28T09:29:39.154+0000"
    }
}
```