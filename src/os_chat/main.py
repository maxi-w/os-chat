import osquery

from phi.assistant import Assistant
from prompt_toolkit import prompt


def hallo():
    return True


def setup_assistant():
    instance = osquery.SpawnInstance()
    instance.open()

    def osquery_sql_query(sql_query: str) -> dict:
        """Use this function to call osquery SQL queries.

        Args:
            sql_query (str): An sql query executed with osquery.
        Returns:
            str: Respose from osquery.
        """
        # results = instance.client.query(".tables")
        return str(instance.client.query(sql_query).__dict__)
    
    assistant = Assistant(
        tools=[osquery_sql_query], 
        show_tool_calls=False, 
        add_chat_history_to_messages=True,
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
    # Execute the main script
    main()
