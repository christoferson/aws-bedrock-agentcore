## Setup

### Create Virtual Environment

uv venv --python 3.12

### Activate Virtual Environment

.venv\Scripts\activate

### Install Dependencies

pip install -r requirements.txt

### Set Bedrock Credentials

set AWS_PROFILE=xxx

# Initialize a new uv project in current directory
uv init

# Add your dependencies
uv add bedrock-agentcore
uv add strands-agents

# Run your script
uv run my_agent.py

# Test Locally

curl -X POST http://localhost:8080/invocations -H "Content-Type: application/json" -d "{\"prompt\": \"Hello!\"}"

{"result": {"role": "assistant", "content": [{"text": "Hello! It's nice to meet you. How are you doing today? Is there anything I can help you with?"}]}}
