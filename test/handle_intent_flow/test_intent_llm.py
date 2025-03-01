import sys
import os

# Get absolute path of current file
current_file_path = os.path.abspath(__file__)

# Get project root path (2 levels up)
project_root = os.path.dirname(os.path.dirname(os.path.dirname(current_file_path)))

# Add project root to Python path
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from engine.flow.handle_intent_flow.handle_intent_flow import handle_intent_flow
from engine.utils.json_util import extract_json_from_str

def main():
    input_messages = "panda: who is the president of the United States now?"
    message = """This is a requirement from Twitter: {input_messages}. Answer Twitter requests with your process. If you answer with a 'call_tool' operation, save the knowledge into a document and upload it to **gitbook**.
    """
    input_message = message.format(input_messages=input_messages)
    # chat_messages = input("Enter your message: ")
    # chat_messages = [{"role": "user", "content": input_messages}]
    print(input_message)
    result = handle_intent_flow(chat_messages=[], input_message=input_message, user_id="local-dev")
    print(result)



if __name__ == "__main__":
    import time
    start_time = time.time()
    main()
    end_time = time.time()
    print(f"Execution time: {end_time - start_time:.2f} seconds")
