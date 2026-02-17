file = open("honeypot.txt", "r", encoding="utf-8", errors="ignore")
lines = file.readlines()
file.close()

failed = {}

# analyze only first 500 lines (keeps it fast)
for line in lines[:500]:

    if "Failed password" in line:
        parts = line.split()

        if "from" in parts:
            index = parts.index("from")
            ip = parts[index + 1]

            if ip in failed:
                failed[ip] = failed[ip] + 1
            else:
                failed[ip] = 1

report = open("report.txt", "w")

report.write("Cloud Security Honeypot Report\n")
report.write("-----------------------------\n")

for ip in failed:
    if failed[ip] >= 3:
        report.write(ip + " failed " + str(failed[ip]) + " times\n")

report.close()

print("Done. Open report.txt")
