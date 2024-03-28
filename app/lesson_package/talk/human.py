from lesson_package.tools import utils


def sing():
    return 'sing'


def cry():
    # return 'cry'
    return utils.say_twice('cry')