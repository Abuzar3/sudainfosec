import string
import itertools

def brute_force(password_length, password_characters):
  """
  This function performs a brute force attack on a password.

  Args:
    password_length: The length of the password.
    password_characters: The characters that can be used in the password.

  Returns:
    The password, if it is found.
  """

  for password in itertools.product(password_characters, repeat=password_length):
    password = "".join(password)
    # Check if the password is correct.
    if password == "correct_password":
      return password

  return None

password_length = 8
password_characters = string.ascii_lowercase + string.digits

password = brute_force(password_length, password_characters)

if password is not None:
  print("The password is: {}".format(password))
else:
  print("The password was not found.")
