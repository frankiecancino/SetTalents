from firebase import firebase

class Subscriptions(object):
    def __init__(self):
        self.firebase = firebase.FirebaseApplication('https://set-talents.firebaseio.com', None)

    def store_email(self, email):
        data = {'email_address': email}
        self.firebase.post('/emails', data)

