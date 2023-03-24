# ================ SCRIPT #1 =============== 
# import psutil
# import openai


# # Set your OpenAI API key
# openai.api_key = "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"


# # Collect system performance data
# cpu_percent = psutil.cpu_percent()
# memory_info = psutil.virtual_memory()
# disk_usage = psutil.disk_usage('/')

# # Generate report using OpenAI API
# prompt = f"My system performance is: CPU usage is {cpu_percent}%, memory usage is {memory_info.percent}%, and disk usage is {disk_usage.percent}%."
# response = openai.Completion.create(
#     engine="text-davinci-002",
#     prompt=prompt,
#     max_tokens=100
# )
# report = response.choices[0].text

# # Write report to file
# with open('system_report.txt', 'w') as file:
#     file.write(report)


# ================ SCRIPT #2 (Improved) =============== 
import psutil
import openai
import api_key


openai.api_key = "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"
# Pls, Set your OpenAI API key (It consumes tokens from this account, so it may not be enought for bigger token consumption)


# Collect system performance data
cpu_percent = psutil.cpu_percent()
cpu_cores = psutil.cpu_count(logical=True)
memory_info = psutil.virtual_memory()
disk_usage = psutil.disk_usage('/')

# Generate report using OpenAI API
prompt = f"My system performance is: CPU usage is {cpu_percent}% on {cpu_cores} cores, memory usage is {memory_info.percent}%, and disk usage is {disk_usage.percent}%."
response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=prompt,
    max_tokens=500
)
report = response.choices[0].text

# Add detailed analysis and recommendations to report
# Some HostedGraphite alerts could be added here as well, Not sure yet how to integrate it to the code.. 
if cpu_percent > 80:
    report += "\n\nYour CPU usage is high. You may want to close some resource-intensive applications or consider upgrading your CPU."
if memory_info.percent > 80:
    report += "\n\nYour memory usage is high. You may want to close some applications or consider upgrading your RAM."
if disk_usage.percent > 80:
    report += "\n\nYour disk usage is high. You may want to delete some unnecessary files or consider upgrading your storage."

# Write report to file
with open('system_report.txt', 'w') as file:
    file.write(report)
    
# Print report to console
print(report)