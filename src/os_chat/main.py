from phi.assistant import Assistant
from prompt_toolkit import prompt
from .tools import (
    list_osquery_tables, 
    osquery_sql_query, 
    list_log_files, 
    read_file_content, 
    get_nvidia_smi_output
)


def setup_assistant():
    assistant = Assistant(
        tools=[
            list_osquery_tables, 
            osquery_sql_query, 
            list_log_files, 
            read_file_content,
            get_nvidia_smi_output,
        ], 
        show_tool_calls=False, 
        add_chat_history_to_messages=False,
        add_datetime_to_instructions=True
    )
    return assistant


def main():
    print("Start running os-chat...")
    print("Enter 'exit' to quit.")
    assistant = setup_assistant()

    keep_running = True
    while keep_running:
        user_input = prompt("How can I help you? \n")
        if user_input == "exit":
            keep_running = False
            break
        assistant.print_response(user_input)
    print("Exiting os-chat...")


if __name__ == "__main__":
    main()
