class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None

    def set_user(self, user):
        self.user = user

    def set_password(self, password):
        self.password = password

    @classmethod
    def create_with_auth(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection

    @staticmethod
    def log(msg):
        print('LOG:', msg)


c1 = Connection().create_with_auth('Nathan', '222331')
print(c1.log('Esta é a mensagem de log'))
# c1.set_user('luiz')
# c1.set_password('33221')
print(c1.user)
print(c1.password)
