# if/elif/else inside loops
user_statuses = ["active", "banned", "active", "pending"]

for status in user_statuses:
    
    if status == "active":
        print("✅ Access Granted!")
    elif status == "banned":
        print("❌ Access Denied! Security alerted.")
    else:
        print("⚠️ Please verify your email first.")

# Grades check using within the for loop and if/else condition
grades = [85, 42, 90, 30, 78]

for grade in grades:
    if grade >= 50:
        print("You are Pass")
    else:
        print("You are Fail")        

# The Accumulator Pattern
logs_string = "error info error warning info error"
log_list = logs_string.split()

log_error = "error"

logs_list = 0

for log in log_list:
    if log == log_error:
        logs_list = logs_list + 1
    
print(f"Total errors is {logs_list}")      

# Flag Variable
rooms = ["safe", "safe", "broken window", "safe"]

alarm_triggered = False 

for room in rooms:
    if room == "broken window":
        alarm_triggered = True 

if alarm_triggered == True:
    print("🚨 Call the police!")
else:
    print("✅ The museum is secure.")

    