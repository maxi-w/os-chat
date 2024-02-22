import os
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
            str: Response from osquery.
        """
        # results = instance.client.query(".tables")
        return str(instance.client.query(sql_query).__dict__)
    
    def list_osquery_tables() -> dict:
        """Use this function to find all available tables in osquery.

        Returns:
            str: List of tables in osquery.
        """
        return str(instance.client.query(".tables"))
    
    def list_log_files():
        """List all log files in /var/log.
        
        Returns:
            list: List of log files in /var/log.
        """
        log_dir = "/var/log/"
        return str([f for f in os.listdir(log_dir) if os.path.isfile(os.path.join(log_dir, f))])
    
    def read_file_content(file_path):
        """Read the content of a file.

        Args:
            file_path (str): The path to the file.

        Returns:
            str: The content of the file.
        """
        with open(file_path, 'r') as file:
            return file.read()
    
    assistant = Assistant(
        tools=[
            list_osquery_tables, 
            osquery_sql_query, 
            list_log_files, 
            read_file_content
        ], 
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
    main()
