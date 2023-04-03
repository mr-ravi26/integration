import os
from jira import JIRA

# requirements
# pip install jira

class JiraIntegration():

    def __init__(self):
        jira_api_key = "<personal access token from cofluence setting page>"
        self.jira = JIRA(
            server="https://xyz.atlassian.net", 
            basic_auth=('sample@example.com', jira_api_key)
    )

    def create_jira_ticket(self, event):
        issue_dict = {
            'project': {'key': 'SD'},
            'summary': 'Small summry / Title',
            'description': 'Ticket description (Supports Rich text markup)',
            'issuetype': {'name': 'Task'},
        }

        new_issue = self.jira.create_issue(fields=issue_dict)

        # Add created issue to any epic
        self.jira.add_issues_to_epic('EPIC-CODE', new_issue.key)

        # you can use Ticket ID and Redirect URL for further uses.
        return {
            'key': new_issue.key,
            'link': new_issue.permalink()
        }




