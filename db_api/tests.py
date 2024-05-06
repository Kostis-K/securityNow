from django.test import TestCase

# Create your tests here.
import json

# Define test data
test_data = {
    "username": "test_user1",
    "first_name": "Kostis",
    "last_name": "Karampouzouklhs"
}

# Serialize the data
serialized_data = json.dumps(test_data)

# Print or inspect the result
print(serialized_data)