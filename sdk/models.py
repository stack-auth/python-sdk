
class User:
    def __init__(self, user_id, display_name):
        self.user_id = user_id
        self.display_name = display_name

    @classmethod
    def from_dict(cls, data):
        return cls(
            user_id=data.get('user_id'),
            display_name=data.get('display_name')
        )
