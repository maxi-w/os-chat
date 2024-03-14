from phi.assistant import Assistant
from phi.llm.openai import OpenAIChat
from prompt_toolkit import prompt
from phi.llm.ollama import Ollama
from phi.llm.base import LLM
from .tools import (
    list_osquery_tables, 
    osquery_sql_query, 
    list_log_files, 
    read_file_content, 
    run_shell_command
)


def select_model(model_mame: str) -> LLM:
    if model_mame in ["llama2", "llama2:7b-chat", "openhermes", "nous-hermes2"]:
        return Ollama(model=model_mame)
    elif model_mame == "gpt-3.5-turbo":
        return OpenAIChat(
            model="gpt-3.5-turbo",
            max_tokens=1024,
            temperature=0.9,
        )
    else:
        raise ValueError(f"Model {model_mame} not supported.")


def setup_assistant(model_name: str = "gpt-3.5-turbo"):
    assistant = Assistant(
        llm=select_model(model_name),
        tools=[
            list_osquery_tables, 
            osquery_sql_query, 
            list_log_files, 
            read_file_content,
            run_shell_command,
        ], 
        show_tool_calls=False, 
        add_chat_history_to_messages=False,
        add_datetime_to_instructions=True,
        debug_mode=True,
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
