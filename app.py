import streamlit as st
from jira import JIRA

# Replace these with your Jira instance details
JIRA_SERVER = 'https://jira.atlassian.net'
JIRA_USER = 'user@domain.com'
JIRA_API_TOKEN = ''

def create_jira_client():
    jira_options = {'server': JIRA_SERVER}
    jira = JIRA(options=jira_options, basic_auth=(JIRA_USER, JIRA_API_TOKEN))
    return jira

def main():
    st.title("Jira Chat Agent")
    st.write("Interact with your Jira projects and issues using this chat agent.")
    
    # Sidebar for user inputs
    st.sidebar.title("Chat with Jira")
    user_query = st.sidebar.text_input("Ask Jira", "")
    
    if user_query:
        response = process_query(user_query)
        if isinstance(response, list):
            for res in response:
                st.write(res)
        else:
            st.write(response)

def process_query(query):
    jira = create_jira_client()
    
    if "create issue" in query.lower():
        project_key = st.sidebar.text_input("Project Key", "PROJ")
        summary = st.sidebar.text_input("Summary", "Issue summary")
        description = st.sidebar.text_area("Description", "Issue description")
        if st.sidebar.button("Create Issue"):
            try:
                new_issue = jira.create_issue(
                    project=project_key,
                    summary=summary,
                    description=description,
                    issuetype={'name': 'Task'}
                )
                return f"Issue {new_issue.key} created successfully!"
            except Exception as e:
                return f"Failed to create issue: {str(e)}"
    
    elif "search issue" in query.lower():
        jql = st.sidebar.text_input("JQL", "project=PROJ AND status=Open")
        if st.sidebar.button("Search Issues"):
            try:
                issues = jira.search_issues(jql)
                return [f"{issue.key}: {issue.fields.summary}" for issue in issues]
            except Exception as e:
                return f"Failed to search issues: {str(e)}"
    
    return "Sorry, I didn't understand that."

if __name__ == "__main__":
    main()
