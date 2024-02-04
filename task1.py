import pulp

if __name__ == '__main__':
    model = pulp.LpProblem("MaximizeProduction", pulp.LpMaximize)

    lemonade = pulp.LpVariable("Lemonade", lowBound=0, cat="Integer")
    juice = pulp.LpVariable("Juice", lowBound=0, cat="Integer")

    model += lemonade + juice, 'MaxCount'

    model += 2 * lemonade + juice <= 100, 'Water'
    model += lemonade <= 50, 'Sugar'
    model += lemonade <= 30, 'Lemon juice'
    model += 2*juice <= 40, 'Fruits'

    model.solve()

    print(pulp.LpStatus[model.status])
    print(f"Total cost = {pulp.value(model.objective)}")
    print(f"Lemonade = {lemonade.varValue}")
    print(f"Juice = {juice.varValue}")
