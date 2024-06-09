# A9 Jira Chat Agent

Welcome to the Jira Chat Agent! This project is a simple interactive chat agent built with Streamlit that allows you to interact with your Jira projects and issues. You can create new issues and search for existing ones using natural language queries.

## Introduction

This was generated (in one pass) by A9 Streamlit Helper, an AI assistant designed to help you create interactive, user-friendly data applications using the Streamlit framework. My goal is to simplify data analysis and decision-making processes by providing you with efficient and intuitive solutions. This Jira Chat Agent is one such solution, aimed at making your project management tasks easier and more efficient.

This project is brought to you by A9, a Streamlit developer with a strong grasp of Python, analytical thinking, and a knack for creative problem-solving. A9 focuses on delivering impactful data-driven solutions through optimized app performance and aesthetically pleasing interfaces.

## Features

- **Create Issues**: Quickly create new issues in your Jira projects.
- **Search Issues**: Search for issues in your Jira projects using JQL (Jira Query Language).

## Getting Started

### Prerequisites

Before you begin, make sure you have the following installed:

- Python 3.7+
- Streamlit
- Jira API client (`jira`)

You can install the required packages using pip:

```sh
pip install streamlit jira

streamlit run jira_chat_agent.py
```

## 1. Setup 

``` sh
git clone https://github.com/your-username/jira-chat-agent.git
cd jira-chat-agent

``` python
JIRA_SERVER = 'https://your-domain.atlassian.net'
JIRA_USER = 'your-email@example.com'
JIRA_API_TOKEN = 'your-api-token'
```


## 2.	Configure Jira Credentials: Replace the placeholder values in the script with your Jira instance details:

---

Using the Chat Agent

	1.	Open the Sidebar: On the left side of the app, open the sidebar to enter your query.
	2.	Ask a Question: Type your query in natural language (e.g., “create issue” or “search issue”).
	3.	Provide Details: Depending on your query, you might need to enter additional details like project key, summary, description, or JQL.
	4.	Get Response: The chat agent will process your query and display the response on the main screen.

Example Queries

	•	Create an Issue:
	•	Type “create issue” in the sidebar.
	•	Enter the project key, summary, and description.
	•	Click “Create Issue”.
	•	Search for Issues:
	•	Type “search issue” in the sidebar.
	•	Enter the JQL query (e.g., project=PROJ AND status=Open).
	•	Click “Search Issues”.


