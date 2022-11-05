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
            "input": ["df"],
            "answer": False,
            "explanation": "It not a number"
        },
        {
            "input": ["34"],
            "answer": True,
            "explanation": "It's a number"
        }
    ],
    "Extra": [
        {
            "input": ["1033"],
            "answer": True,
            "explanation": "It's a number"
        },
        {
            "input": ["1oo220"],
            "answer": False,
            "explanation": "There are letters"
        }
    ]
}
