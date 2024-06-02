import re

class EmailAddressParser:
    def __init__(self, email_addresses):
        self.email_addresses = email_addresses

    def parse(self):
        # Use regex to split the string by commas, spaces, or both
        addresses = re.split(r'[,\s]+', self.email_addresses)
        # Remove empty strings if any
        addresses = list(filter(None, addresses))
        
        # Define a regex pattern for a valid email address
        email_regex = re.compile(r'^[\w\.-]+@[\w\.-]+\.\w+$')
        
        # Filter out invalid email addresses
        valid_addresses = [email for email in addresses if email_regex.match(email)]
        
        # Return unique and sorted valid addresses
        return sorted(set(valid_addresses))


email_addresses = "john@doe.com, person@somewhere.org john@doe.com invalid-email@.com"
parser = EmailAddressParser(email_addresses)
print(parser.parse())  # => ["john@doe.com", "person@somewhere.org"]
