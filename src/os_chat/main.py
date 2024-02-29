from phi.assistant import Assistant
from phi.llm.openai import OpenAIChat
from prompt_toolkit import prompt
from .tools import (
    list_osquery_tables, 
    osquery_sql_query, 
    list_log_files, 
    read_file_content, 
    run_shell_command
)


def setup_assistant(openai_model: str = "gpt-3.5-turbo"):
    assistant = Assistant(
        llm=OpenAIChat(
            model=openai_model,
            max_tokens=1024,
            temperature=0.9,
        ),
        tools=[
            list_osquery_tables, 
            osquery_sql_query, 
            list_log_files, 
            read_file_content,
            run_shell_command,
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
