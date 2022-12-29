# jirabot-with-python
JIRA interaction when service ticket is created and commented

# Steps
* Need to install JIRA service desk -> https://github.com/teamatldocker/jira
* Make sure JIRA service management license is enabled -> <JIRA IP>/plugins/servlet/applications/versions-licenses
* Create service project with "Basic". Try to create it first
* The service desk should be avaiable in -> <JIRA IP>/servicedesk/customer/portal/1
* Create webhook -> <JIRA IP>/plugins/servlet/webhooks with scope "Comment" and "Issue" created only. put JQL query to indicate filter. Don't forget to put your endpoint too
* Test by creating issue and putting comments
