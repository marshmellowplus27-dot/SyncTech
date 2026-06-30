# --- Challenge: Fill in the Logic Gates ---

print("=== SyncTech Advanced Scanner ===")

essay = input("Enter the student's essay to scan:\n").lower()

# Here are the flags we are checking for:
has_copied_text = "i copied this from wikipedia" in essay
has_bad_word = "hate" in essay

print("\n--- SCANNER RESULTS ---")

#TODO 1: Write an 'if' statement.
if has_copied_text:  
  print("Alert: Plagiarism detected! Grade: F") 
# If 'has_copied_text' is True, print: "ALERT: Plagiarism detected! Grade: F"


# TODO 2: Write an 'elif' statement.
elif has_bad_word: 
   print("Warning: Negative tone detected. Please rewrite.")
# If 'has_bad_word' is True, print: "WARNING: Negative tone detected. Please rewrite."


# TODO 3: Write an 'else' statement.
else: 
  print("Success: Essay passed the security scan!")
# If everything is clear, print: "SUCCESS: Essay passed the security scan!"