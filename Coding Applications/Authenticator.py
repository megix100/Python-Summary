# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
print("\nCreating Authenticator")
user1 = {
    'name': 'Sorna',
    'valid': True
}

user2 = {
    'name': 'Fabio',
    'valid': True
}

def authenticated(fn):
  def wrapper(*args, **kwargs):
    if args[0]['valid']: #Search the first element from all the arguments and then from Valid inside the keys of this argument and see if it is True
        fn(*args, **kwargs)
  return wrapper

@authenticated
def message_friends(user):
    print(f'message has been sent by {user["name"]}')

message_friends(user1)
message_friends(user2)