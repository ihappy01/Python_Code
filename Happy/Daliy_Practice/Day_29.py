# # Sample employee dictionary
# employee_details = {
#     1: {"name": "John", "age": 30, "department": "HR"},
#     2: {"name": "Alice", "age": 25, "department": "IT"},
#     3: {"name": "Bob", "age": 35, "department": "Finance"},
#     # ... (more employees)
# }
#
# def get_employee_detail(employee_id):
#     try:
#         employee = employee_details[employee_id]
#         if isinstance(employee, dict):
#             return employee
#         else:
#             return "Employee detail is not a dictionary."
#     except KeyError:
#         return "Employee ID not found in the dictionary."
#     except :
#         return "Employee ID not found"
#
# # Example usage:
# employee_id_to_find = '&'
# employee_detail = get_employee_detail(employee_id_to_find)
#
# print(f"Employee ID {employee_id_to_find} Details:")
# print(employee_detail)



# def greeting(fx):
#     def mfx():
#         print("Hello Good Morning")
#         fx()
#     return mfx
#
#
# @greeting
# def add():
#     print(7+9)
#
# add()


import re

text='''Chloroform, or trichloromethane (often abbreviated as TCM), is an organic compound with the formula 
CHCl3 and a common solvent. It is a very volatile, colorless, strong-smelling, 
dense liquid produced on a large scale as a precursor to PTFE and refrigerants[10] and 
is a trihalomethane that serves as a powerful anesthetic, euphoriant, anxiolytic, and 
sedative when inhaled or ingested. Chloroform was used as an anesthetic between the 19th century 
and the first half of the 20th century  10.123.456'''

match = re.findall(r'\d{2}.\d{3}.\d{3}',text)
print(match)



# match = re.findall(r'\w+',text)
# match = re.search(r'\w+',text)
# matches = re.finditer(r'\w+',text)

# print(match)
# length = list(matches)
# print(length)
# print(len(length))
# matches = re.finditer()

# for match in matches:
#     print(match)