class Fruit:
    def __init__(self, name, color, cost=0):
        self.name = name
        self.color = color
        self.cost = cost

    def __str__(self):
        return f"{self.name} - {self.color} {self.cost}"

# Define a custom sorting key function to sort by cost
def sort_by_cost(fruit):
    return fruit.cost

fruits = [Fruit('apple', 'red', 1.5), Fruit('banana', 'yellow', 3.5), Fruit('grape', 'purple', 0.5)]

# Sort the fruits list based on cost
sorted_fruits = sorted(fruits, key=sort_by_cost)

# Print the sorted list
for fruit in sorted_fruits:
    print(fruit)