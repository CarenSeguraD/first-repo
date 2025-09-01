# Step 1: Write the original secret message
sent_message = "Hey there! This is a secret message."

with open("sent_message.txt", "w") as file:
    file.write(sent_message)

# Step 2: Read + prepare to overwrite
with open("sent_message.txt", "r+") as file:
    # Read the sent message from the file
    original_message = file.read()

    # Move the cursor back to the beginning
    file.seek(0)

    # Step 3: Modify the message to simulate unsending
    unsent_message = "This message has been unsent."

    # Write the new message
    file.write(unsent_message)

    # Truncate the file to match the new message length
    file.truncate()

# Step 4: Print results
print("Original message:", original_message)
print("Updated message:", unsent_message)
