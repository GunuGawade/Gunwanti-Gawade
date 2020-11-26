import json

with open('emp_details.json') as f:
    data = json.load(f)

def find_average_age():
    return sum([data[i]["age"] for i in data])/len(data)

def find_average_age_for_dept(dept):
    avg=[data[i]["age"] for i in data if data[i]["dept"]==dept]
    return sum(avg)/len(avg)

def main():

    print("Average emp age is:", find_average_age())

    print("Average emp age for dept d1:", find_average_age_for_dept("d1"))
    print("Average emp age for dept d2:", find_average_age_for_dept("d2"))

if __name__ == "__main__":
    main()