# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 08:36:48 2020

@author: lsttl
"""

orders = [["David","3","Ceviche"],["Corina","10","Beef Burrito"],["David","3","Fried Chicken"],["Carla","5","Water"],["Carla","5","Ceviche"],["Rous","3","Ceviche"]]



class Solution:
    def displayTable(self, orders):
    # def displayTable(self, orders: List[List[str]]) -> List[List[str]]:    
        # first get the array of unique table and unique order terms
        import numpy as np
        L=len(orders)
        Table=np.array([])
        Order=np.array([])
        for k in range(L):
            Table=np.append(Table,int(orders[k][1]))
            Order=np.append(Order, orders[k][2])
        # get the unique terms and sort
        Table=np.sort(np.unique(Table))
        Order=np.sort(np.unique(Order))
        Lorder=len(Order)
        # get the first row of output list
        Output=[]
        Output.append(np.append('Table', Order))
        # add row for each table with the item number initialized as 0
        for tab in Table:
            Output.append([tab]+[0]*Lorder)
        # go through each item in orders and add up the count
        for orde in orders:
            tabind=np.where(Table==int(orde[1]))[0].item()
            ordind=np.where(Order==orde[2])[0].item()
            #print('tabind: ', tabind)
            #print('ordind: ', ordind)
            Output[tabind+1][ordind+1]=Output[tabind+1][ordind+1]+1
        # convert integer into str
        for k in range(1, len(Output)):
            Output[k]=np.char.mod('%d', Output[k])
        
        return Output

class Solution2:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        food_set = set()
        table_set = set()
        display = []

        for table in orders:
            table_set.add(table[1])
            food_set.add(table[2])

        table_set = sorted(table_set, key=lambda x: int(x)) # become a list
        foods = sorted(food_set)
        my_dict = {table: [0] * len(foods) for table in table_set}
        index_table = {x[1]: x[0] for x in enumerate(foods)}

        head = ['Table']
        head.extend(foods)
        display.append(head)

        for order in orders:
            table, food = order[1], order[2]
            my_dict[table][index_table[food]] += 1

        for k, v in my_dict.items():
            my_list = [k]
            my_list.extend(map(str, v))
            display.append(my_list)
        
        return display

