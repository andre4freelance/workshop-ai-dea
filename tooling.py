import psutil
import platform
import socket
from datetime import datetime
from ollama import chat

def get_system_info():
    hostname = socket.gethostname()
    cpu_usage = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    total_ram = memory.total / (1024 ** 3)
    uptime_seconds = datetime.now().timestamp() - psutil.boot_time()
    uptime_hours = uptime_seconds / 3600

    return f"""{"=" * 50}
Hostname    : {hostname}
OS          : {platform.system()} {platform.release()}
CPU Load    : {cpu_usage:.1f}%
RAM Usage   : {memory.percent:.1f}%
Total RAM   : {total_ram:.2f} GB
Uptime      : {uptime_hours:.1f} hours
{"=" * 50}"""

messages=[
        {
            "role": "user", 
            "content": "Cek status server ini?", 
        }
    ]

response = chat(
    model="MonAI:v3",
    messages=messages,
    tools=[get_system_info],
    think=False
)

messages.append(response.message)
if response.message.tool_calls:
    call = response.message.tool_calls[0]
    tool_name = call.function.name

    result = get_system_info()
    
    messages.append(
        {
            "role": "tool",
            "name": tool_name,
            "content": str(result),
        }
    )
    
    final_response = chat(
        model="MonAI:v3",
        messages=messages,
        tools=[get_system_info],
        think=False
    )
    print(f"[Tooling AI Response]: {final_response.message.content}")
else:
    print(f"[Non Tooling AI Response]: {response.message.content}")