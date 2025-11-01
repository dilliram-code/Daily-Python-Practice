'''----------------------PROJECT: DUPLICATE EMAILS---------------'''

emails = [
    "ram@gmail.com", "sita@yahoo.com", "hari@gmail.com",
    "ram@gmail.com", "gita@gmail.com", "sita@yahoo.com"
]

def duplicate_email_finder(emails):
  seen = set()
  duplicates = set()
  for email in emails:
    if email in seen:
      duplicates.add(email)
    else:
      seen.add(email)
  return duplicates

duplicate_emails = duplicate_email_finder(emails)
print(f"The duplicate emails are: ", duplicate_emails)
