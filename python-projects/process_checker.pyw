import psutil
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import time
import json

"""
This program is needed to check the processes on your PC or Remote Desktop and notify Slack of their status.
"""

# Settings autotest
hostname = "Personal Computer"

'''or using the next code: 

import socket
hostname=socket.gethostname()

or using the next code:

import os
hostname = os.uname()[1]
'''
autotest_name = "process_checker"               
developer_id = "###########"  # ID of user in slack

# Resources
process_list = []  # list of the process which we check, like the 'Skype.exe'

# Notification
slack_channel_id = "slack_channel_id"
slack_token = "slack_token"
slack_channel_name = "#slack_channel_name"
thread_ts = None
report_thread = False

def slack_message(message, priority_color, thread_ts=None):
    client = WebClient(token=slack_token)
    response = client.chat_postMessage(
        channel=slack_channel_id,
        thread_ts=thread_ts,
        attachments=[
            {
                "color": "#5e5ea9",
                "blocks": [
                    {
                        "type": "section",
                        "text": {"type": "mrkdwn", "text": f"{message}"},
                    }
                ],
            }
        ],
    )
    return response


def slack_report():
    global report_thread, thread_ts
    if report_thread == False:
        message = slack_message(
            f"*Autotest*: Checking the operation of the software \n"
            f"*Source*: {hostname}\n"
            f"*Developer*: <@{developer_id}>",
            thread_ts=None,
        )
        thread_ts = message["ts"]
        report_thread = True


def get_process(process):
    print(f"---- Start to find  {process} -----")
    proc_status = False
    for proc in psutil.process_iter():
        proc_name = proc.name()
        # print(proc_name)
        if proc_name == process:
            print(f"---- {process} is active")
            proc_status = True
            break
    if proc_status == False:
        print(f"---- {process} is not active. ")
    print("\n============================\n")
    return proc_status


def main():
    print("\n============================\n")

    # Get the processes status
    for process in process_list:
        result = get_process(process)
        if result == False:
            if report_thread == False:
                slack_report()
            slack_message(
                f"*Software*: {process}\n"
                f"*Message*: The software is not active\n",
                f"#5e5ea9",
                thread_ts=thread_ts,
            )


if __name__ == "__main__":
    time_start = time.time()
    print("---- Start the script ----")
    main()
    print(f"---- End work of the script during: {time.time()-time_start}s")
    exit(1)
