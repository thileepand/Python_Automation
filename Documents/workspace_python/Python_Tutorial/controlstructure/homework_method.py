"""
Method exercise
Create a method, which takes a state and gross income as the arguments and returns the net income after deduction tax based on the state.

Assume federal tax: 10%
Assume state tax on your wish.

You don't have to do for all the states , just take 3-4 to solve the purpose of the exercise.
"""

def calculateNetIncome(gross, state):
    """
    Calculate net income after federal and state tax
    :param gross: Gross income
    :param state: State name
    :return: Net income
    """
    state_tax = {'TN':10, 'BA':9, 'KA':8, 'KE':7}

    #Calculate net income after federal tax
    net = gross - (gross * .10)

    #Calculate net income after state tax
    if state in state_tax:
        net = net - (gross * state_tax[state] / 100)
        print("your net income all the heavy taxes is:" + str(net))
        return net
    else:
        print("state not in the list")
        return None

calculateNetIncome(10000, 'TN')
