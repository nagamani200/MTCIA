sample_dict= {
    'physics': 82,
    'math':85,
    'Telugu':90,
}
"""print(min(sample_dict))"""


print(min(sample_dict, key=sample_dict.get))
