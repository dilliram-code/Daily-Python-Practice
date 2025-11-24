'''---------------------Hospital Management System---------------------'''

import uuid
from datetime import datetime, timedelta

def generate_id(prefix=""):
  return prefix + uuid.uuid4().hex[:6]

print(generate_id())