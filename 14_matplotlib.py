import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]
# plt.plot(x, y)
# plt.xlabel('x-axis')    
# plt.ylabel('y-axis')
# plt.title('Line Graph')
# plt.show()

# plt.scatter(x, y)
# plt.xlabel('x-axis')
# plt.ylabel('y-axis')
# plt.title('Scatter Plot')
# plt.show()

# # bar plot
# plt.bar(x, y)
# plt.xlabel('x-axis')
# plt.ylabel('y-axis')
# plt.title('Bar Plot')
# plt.show()

# pie chart
labels = ['A', 'B', 'C', 'D', 'E']
sizes = [20, 30, 25, 15, 10]
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title('Pie Chart')  
plt.show()