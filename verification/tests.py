"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": ["34"],
            "answer": True,
        },
        {
            "input": ["df"],
            "answer": False,
        },
        {
            "input": [""],
            "answer": False,
        },
        {
            "input": ["ITS A NUMBER"],
            "answer": False,
        },
        {
            "input": ["5a"],
            "answer": False,
        },
        {
            "input": ["a5"],
            "answer": False,
        },
    ],
    "Extra": [
        {
            "input": ["1033"],
            "answer": True,
        },
        {
            "input": ["1oo220"],
            "answer": False,
        },
        {
            "input": ["1l0O"],
            "answer": False,
        },
        {
            "input": ["1OOO"],
            "answer": False,
        },
        {
            "input": ["100000O00"],
            "answer": False,
        },
        {
            "input": ["77765362"],
            "answer": True,
        },
    ]
}
