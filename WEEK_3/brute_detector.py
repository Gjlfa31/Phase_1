attack_count = 0

with open("auth_audit.log", "r") as log_file:
    with open("brute_report.txt", "w") as report_file:

        # Step 4: The Conveyor Belt (The Loop)
        for line in log_file:

            # Step 5: The Signature Search
            # We only care about lines containing "Failed password"
            if "Failed password" in line:

                # Step 6: Save the line to the report
                report_file.write(line)

                # Step 7: Increment the counter
                attack_count = attack_count + 1


print(f"[*] Audit Complete. Extracted {attack_count} threat signatures to brute_report.txt")


