from views import console

DEFAULT_ROBOT_NAME = "Roboko"


class Robot(object):
    """Robotクラスのベースモデル"""

    def __init__(self, name=DEFAULT_ROBOT_NAME, user_name="", speak_color='green') -> None:
        self.name = name
        self.user_name = user_name
        self.speak_color = speak_color
    
    def hello(self):
        while True:
            template = console.get_template('template_hello.txt', self.speak_color)
            user_name = input(template.substitute({'robot_name': self.name}))

            if user_name:
                self.user_name = user_name.title()
                break

class RestaurantRobot(Robot):

    def __init__(self, name=DEFAULT_ROBOT_NAME,) -> None:
        super().__init__(name=name)
        # self.ranking_mode; = ranking.RankingModel()
    
    def _hello_decorator(func):
        def wrapper(self):
            # self.user_nameが空の場合hello()メソッドを呼び出す
            if not self.user_name:
                self.hello()
            return func(self)
        return wrapper
    
    @_hello_decorator
    def recommend_restaurant(self):
        # new_reccomend_restaurant = self.ranking_model.get_most_popular()
    
    def ask_user_favorite(self):

    def thank_you(self):