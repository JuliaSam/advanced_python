from functools import reduce
from settings import INSTALLED_APPS

def get_server_actions():
    return reduce(
        lambda value, item: value + getattr(utem, 'actionnames', []),
        reduce(
            lambda value, item: value + [getattr(item, 'actions', [])],
            reduce(
                lambda value, item: value + [__import__(f'{item}.actions')],
                INSTALLED_APPS,
                []
            ),
            []
        ),
        []
    )

def resolve(action_name, actions=None):
    actions_list = actions or get_server_actions()
    actions_mapping = {
        action.get('action'): action.get('controller')
        for action in actions_list
    }
    print(actions_mapping)
    return actions_mapping.get(action_name)
