# Task 7
import json
firm_dict = {}
profits = []
losses = []
average_profits = []
with open('text_task_7.txt', encoding='utf-8') as f_obj:
    lines = f_obj.readlines()
    for line in lines:
        name, form, revenue, costs = line.split()
        profit = int(revenue) - int(costs)
        firm_dict[name] = profit
        if profit > 0:
            profits.append(profit)
        else:
            losses.append(profit)
    average_profits.append(sum(profits) / len(profits))
    firms_info = [firm_dict, {'average profit': average_profits}, {'losses': losses}]
with open('text_task_7.json', 'w') as f_json:
    json.dump(firms_info, f_json)

with open('text_task_7.json') as f_json:
    print(json.load(f_json))
