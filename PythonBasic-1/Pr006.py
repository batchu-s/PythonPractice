# Acceppts the comma seperated values string and converts them into list and Tuple
data = input("Enter the data:")
data_list = data.split(',')
print(data_list)
data_tuple = tuple(data_list)
print(data_tuple)