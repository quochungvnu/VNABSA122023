import json

senttag2opinion = {'pos': 'great', 'neg': 'bad', 'neu': 'ok'}
sentword2opinion = {'positive': 'great', 'negative': 'bad', 'neutral': 'ok'}

rest_aspect_cate_list = ["Design", "General", "Material", "Price", "Service"]

laptop_aspect_cate_list = [
    "Design", "General", "Material", "Price", "Service"
]

with open("force_tokens.json", 'r') as f:
    force_tokens = json.load(f)

cate_list = {
    "rest14": rest_aspect_cate_list,
    "rest15": rest_aspect_cate_list,
    "rest": rest_aspect_cate_list,
    "rest16": rest_aspect_cate_list,
    "laptop": laptop_aspect_cate_list,
    "laptop14": laptop_aspect_cate_list
}

task_data_list = {
    "aste": ["laptop14", "rest14", "rest15", "rest16"],
    "tasd": ['rest15', "rest16"],
    "acos": ['laptop16', "rest16"],
    "asqp": ['rest15', "rest16"],
}
force_words = {
    'aste': {
        'rest15': list(senttag2opinion.values()) + ['*'],
        'rest16': list(senttag2opinion.values()) + ['*'],
        'rest14': list(senttag2opinion.values()) + ['*'],
        'laptop14': list(senttag2opinion.values()) + ['*']
    },
    'tasd': {
        "rest15": rest_aspect_cate_list + list(sentword2opinion.values()) + ['*'],
        "rest16": rest_aspect_cate_list + list(sentword2opinion.values()) + ['*']
    },
    'acos': {
        "rest": rest_aspect_cate_list + list(sentword2opinion.values()) + ['*'],
        "laptop": laptop_aspect_cate_list + list(sentword2opinion.values()) + ['*'],
    },
    'asqp': {
        "rest15": rest_aspect_cate_list + list(sentword2opinion.values()) + ['*'],
        "rest16": rest_aspect_cate_list + list(sentword2opinion.values()) + ['*'],
    }
}


optim_orders_all = {
            "aste": {
                "laptop14": [
                    '[O] [A] [S]', '[A] [O] [S]', '[O] [S] [A]',
                    '[A] [S] [O]', '[S] [O] [A]', '[S] [A] [O]'
                ],
                "rest14": [
                    '[O] [A] [S]', '[O] [S] [A]', '[A] [O] [S]',
                    '[A] [S] [O]', '[S] [O] [A]', '[S] [A] [O]'
                ],
                "rest15": [
                    '[A] [O] [S]', '[O] [A] [S]', '[O] [S] [A]',
                    '[A] [S] [O]', '[S] [O] [A]', '[S] [A] [O]'
                ],
                "rest16": [
                    '[O] [A] [S]', '[A] [O] [S]', '[O] [S] [A]',
                    '[A] [S] [O]', '[S] [O] [A]', '[S] [A] [O]'
                ],
            },
            "tasd": {
                "rest15": [
                    '[A] [C] [S]', '[A] [S] [C]', '[C] [S] [A]',
                    '[C] [A] [S]', '[S] [C] [A]', '[S] [A] [C]'
                ],
                "rest16": [
                    '[A] [C] [S]', '[A] [S] [C]', '[C] [S] [A]',
                    '[C] [A] [S]', '[S] [C] [A]', '[S] [A] [C]'
                ]
            },
            "acos": {
                "laptop16": [  # ot null -> sp
                    '[A] [O] [S] [C]', '[A] [S] [O] [C]',
                    '[A] [O] [C] [S]', '[O] [A] [S] [C]',
                    '[O] [A] [C] [S]', '[A] [S] [C] [O]',
                    '[A] [C] [O] [S]', '[O] [C] [A] [S]',
                    '[O] [S] [A] [C]', '[A] [C] [S] [O]',
                    '[O] [C] [S] [A]', '[O] [S] [C] [A]',
                    '[S] [A] [O] [C]', '[C] [O] [A] [S]',
                    '[C] [S] [A] [O]', '[C] [A] [O] [S]',
                    '[C] [S] [O] [A]', '[C] [O] [S] [A]',
                    '[S] [O] [A] [C]', '[C] [A] [S] [O]',
                    '[S] [O] [C] [A]', '[S] [C] [O] [A]',
                    '[S] [A] [C] [O]', '[S] [C] [A] [O]'
                ],
                "rest16": [  # ot null -> sp
                    '[A] [O] [S] [C]', '[A] [O] [C] [S]',
                    '[A] [S] [O] [C]', '[O] [A] [C] [S]',
                    '[O] [A] [S] [C]', '[O] [S] [C] [A]',
                    '[A] [C] [O] [S]', '[O] [C] [A] [S]',
                    '[O] [S] [A] [C]', '[A] [S] [C] [O]',
                    '[A] [C] [S] [O]', '[O] [C] [S] [A]',
                    '[C] [O] [A] [S]', '[C] [A] [O] [S]',
                    '[C] [S] [O] [A]', '[C] [O] [S] [A]',
                    '[S] [A] [O] [C]', '[C] [S] [A] [O]',
                    '[C] [A] [S] [O]', '[S] [O] [A] [C]',
                    '[S] [C] [O] [A]', '[S] [O] [C] [A]',
                    '[S] [C] [A] [O]', '[S] [A] [C] [O]'
                ],
            },
            "asqp": {
                "rest15": [
                    '[A] [O] [S] [C]', '[O] [A] [C] [S]',
                    '[A] [O] [C] [S]', '[O] [A] [S] [C]',
                    '[O] [S] [C] [A]', '[A] [S] [O] [C]',
                    '[O] [C] [A] [S]', '[O] [S] [A] [C]',
                    '[A] [C] [O] [S]', '[O] [C] [S] [A]',
                    '[A] [C] [S] [O]', '[C] [O] [A] [S]',
                    '[A] [S] [C] [O]', '[C] [A] [O] [S]',
                    '[C] [S] [O] [A]', '[C] [O] [S] [A]',
                    '[C] [S] [A] [O]', '[C] [A] [S] [O]',
                    '[S] [A] [O] [C]', '[S] [O] [A] [C]',
                    '[S] [C] [O] [A]', '[S] [O] [C] [A]',
                    '[S] [C] [A] [O]', '[S] [A] [C] [O]'
                ],
                "rest16": [
                    '[O] [A] [C] [S]', '[A] [O] [S] [C]',
                    '[O] [A] [S] [C]', '[O] [S] [C] [A]',
                    '[A] [O] [C] [S]', '[O] [S] [A] [C]',
                    '[O] [C] [A] [S]', '[A] [S] [O] [C]',
                    '[O] [C] [S] [A]', '[A] [C] [O] [S]',
                    '[A] [C] [S] [O]', '[C] [O] [A] [S]',
                    '[A] [S] [C] [O]', '[C] [A] [O] [S]',
                    '[C] [O] [S] [A]', '[C] [S] [O] [A]',
                    '[C] [S] [A] [O]', '[S] [A] [O] [C]',
                    '[C] [A] [S] [O]', '[S] [O] [A] [C]',
                    '[S] [O] [C] [A]', '[S] [C] [O] [A]',
                    '[S] [C] [A] [O]', '[S] [A] [C] [O]'
                ],
            },
        }


heuristic_orders = {
    'aste': ['[A] [O] [S]'],
    'tasd': ['[A] [C] [S]'],
    'asqp': ['[A] [O] [C] [S]'],
    'acos': ['[A] [O] [C] [S]'],
}