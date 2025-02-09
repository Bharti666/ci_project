import matplotlib.pyplot as plt
fig,ax=plt.subplots()

fruits=['apple','blueberry','cherry','orange']
counts=[30,40,50,20]
bar_lables=['red','blue','_red','orange']
bar_colors=['tab:red','tab:blue','tab:red','tab:orange']
ax.bar(fruits,counts,label=bar_lables,color=bar_colors)
ax.set_ylabel('fruits supply')
ax.set_title('fruits supply by kind and color')
ax.legend(title='Fruit color')

plt.savefig('bars.png',bbox_inches='tight')