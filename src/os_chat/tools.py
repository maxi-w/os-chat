import os
import socket
import osquery
import subprocess


instance = osquery.SpawnInstance()
instance.open()


def osquery_sql_query(sql_query: str) -> str:
    """Use this function to call osquery SQL queries.

    Args:
        sql_query (str): An sql query executed with osquery.
    Returns:
        str: Response from osquery.
    """
    return str(instance.client.query(sql_query).__dict__)


def list_osquery_tables() -> str:
    """Use this function to find all available tables in osquery.

    Returns:
        str: List of tables in osquery.
    """
    return str(instance.client.query(".tables"))


def list_log_files() -> str:
    """List all log files in /var/log.
    
    Returns:
        list: List of log files in /var/log.
    """
    log_dir = "/var/log/"
    return str([f for f in os.listdir(log_dir) if os.path.isfile(os.path.join(log_dir, f))])


def read_file_content(file_path)  -> str:
    """Read the content of a file.

    Args:
        file_path (str): The path to the file.

    Returns:
        str: The content of the file.
    """
    with open(file_path, 'r') as file:
        return file.read()


def get_nvidia_smi_output() -> str:
    """Execute the nvidia-smi command and return GPU info.

    Returns:
        str: The output of the nvidia-smi command.
    """
    result = subprocess.run(['nvidia-smi'], stdout=subprocess.PIPE)
    return result.stdout.decode('utf-8')

def get_ip_address():
    """Get network interfaces and their IP addresses.
    
    Returns:
        str: Info about network interfaces and their IP addresses.
    """
    result = subprocess.run(['ifconfig'], stdout=subprocess.PIPE)
    return result.stdout.decode('utf-8')
