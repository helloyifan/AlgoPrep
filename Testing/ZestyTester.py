'''
Takes list of lists 
{
    'description': [
        args_list,
        ...
    ]
}
'''

def runTests(func, tests):
    for i, description in enumerate(tests):
        ret = func(*tests[description]) #Spread
        print("Test #:", i, "description: ", description)
        print("Result:")
        print(ret)
        print("__________________________________________")
        print("(╯°□°)╯︵ ┻━┻ (╯°□°)╯︵ ┻━┻ (╯°□°)╯︵ ┻━┻ ")

## Ignore below, just random stuff i used to debug while building this trash

# testcases = {
#     'test 1 description': [
#         1,
#         2,
#         3,
#         4
#     ],
#     'test 2 description': [
#         'sam',
#         'i',
#         'am',
#         '42',
#     ],
# }


# def bruhman(a, b, c, d):
#     return a + b + c + d

# zt = ZestyTester(bruhman, testcases)


# class Bruh:
#     def yobruhman(self, a, b, c, d):
#         return a + b + c + d

# b = Bruh()
# zt = ZestyTester(b.yobruhman, testcases)

