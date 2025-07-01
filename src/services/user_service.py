from ..repositories.user_repositories import UserRepository

class UserService():
    def __init__(self):
        self._repository=UserRepository()



    def create_user(self,user_details):
        self._repository.create_user(user_details)   
