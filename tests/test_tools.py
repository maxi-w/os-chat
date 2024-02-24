from src.os_chat.tools import list_log_files


def test_list_log_files():
    log_files = list_log_files()
    assert isinstance(log_files, str)
