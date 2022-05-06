import scipy.io 
import numpy as np

#Read file and store data
data = scipy.io.loadmat('data.mat')
transactions = data['transactions']
products = data['products']
history = data['history']

########## Requirements ######
def req1(transactions):  
    try:
        #Declare 2 list to append the result into  ... 
        vector_max = []
        vector_min = []
        
        #Declare list
        commodity = []
        commodity_merge = []
        number_of_appearance = []
        save_max = []
        save_min = []

        #Declare variable
        count = 0

        #Get the size of the array
        rows_transactions = len(transactions)
        columns_transactions = len(transactions[0])

        #Copy commodity into new list
        for i in range(rows_transactions):
            commodity.append(transactions[i][1])
        
        #Merge all list from commodity together
        for i in commodity:
            for j in i:
                commodity_merge.append(j)
               
        #List of commodity
        commodity_merged = sorted(list(set(commodity_merge)))
        
        #Count the number of commodity
        for i in commodity_merged:
            for j in commodity:
                for k in j:
                    if(i == k.strip()):
                        count += 1
            number_of_appearance.append(count)
            count = 0

        #Convert two lists into a dictionary(commodity_merged & number_of_appearance)
        twolst_to_dictionary = {commodity_merged[i]: number_of_appearance[i] for i in range(len(commodity_merged))}
        
        #Get min & max values
        Max = max(twolst_to_dictionary.values())
        Min = min(twolst_to_dictionary.values())
        
        #Find max & min in list after counting
        for i in twolst_to_dictionary:
            if(twolst_to_dictionary[i] == Max):
                save_max.append(i)
            if(twolst_to_dictionary[i] == Min):
                save_min.append(i)
            
            
        #Export result following order
        return (save_max,save_min)
    except:
        return ([],[])
def req2(products):
    try:
        #Declare 2 list to append the result into  ... 
        vector_max = []
        vector_min = []

        #Declare list
        inventory = []
        product_Id = []
        int_inventory = []

        #Get the size of the array
        rows_products = len(products)
        columns_products = len(products[0])

        #Copy inventory into new list
        for i in range(rows_products):
            inventory.append(products[i][2].strip())
        
        #Convert list to int list
        for i in range(0, len(inventory)):
            inventory[i] = int(inventory[i])
        
        #Copy inventory into new list
        for i in range(rows_products):
            product_Id.append(products[i][0].strip())
        
        #Convert two lists into a dictionary(commodity_merged & number_of_appearance)
        twolst_to_dictionary = {product_Id[i]: inventory[i] for i in range(len(product_Id))}

        #Get min & max values
        Max = max(twolst_to_dictionary.values())
        Min = min(twolst_to_dictionary.values())
        
        #Find max & min in list after counting
        for i in twolst_to_dictionary:
            if(twolst_to_dictionary[i] == Max):
                vector_max.append(i)
            if(twolst_to_dictionary[i] == Min):
                vector_min.append(i)

        #Export result following order
        return((vector_max,vector_min))
    except:
        return([],[])

def req3(transactions, products):
    try:
        """-----------------PART 1-----------------"""
        #Declare list
        commodity = []
        commodity1 = []
        commodity_merge = []
        number_of_appearance = []
        products_price = []
        products_merge = []
        
        #Declare variable
        count = 0
        total_revenue = 0.0

        #Get the size of the array
        rows_transactions = len(transactions)
        columns_transactions = len(transactions[0])
        rows_products = len(products)
        columns_products = len(products[0])

        #Copy commodity into new list
        for i in range(rows_transactions):
            commodity.append(transactions[i][1])
        
        #Copy commodity into new list
        for i in range(rows_products):
            commodity1.append(products[i][0].strip())

        #Merge all list from commodity together
        for i in commodity:
            for j in i:
                commodity_merge.append(j)
        
        #List of commodity
        commodity_merged = sorted(list(set(commodity_merge)))
        
        #Count the number of commodity
        for i in commodity_merged:
            for j in commodity:
                for k in j:
                    if(i == k.strip()):
                        count += 1
            number_of_appearance.append(count)
            count = 0 #Set count = 0 for the next one
        
        #Read price list into new list
        for i in range(rows_products):
            products_price.append(int(products[i][1].strip()))
        
        #Convert two lists into a dictionary(commodity_merged & number_of_appearance)
        twolst_to_dictionary = {commodity_merged[i]: number_of_appearance[i] for i in range(len(commodity_merged))} #1
        twolst_to_dictionary1 = {commodity_merged[i]: products_price[i] for i in range(len(commodity_merged))} #Pricce #2
        twolst_to_dictionary2 = {commodity1[i]: products_price[i] for i in range(len(commodity1))}                       #3                                                                                                                                           
        
        """-----------------PART 2-----------------"""
        for i in twolst_to_dictionary2:
            for j in twolst_to_dictionary:
                if(i == j):
                    total_revenue += float(twolst_to_dictionary[j]) * float(twolst_to_dictionary2[i])
                else:
                    total_revenue += 0.0
        return total_revenue
    except:
        return 1

def req4(transactions, products):
    try:
        #Declare list
        commodity = []
        commodity1 = []
        commodity_merge = []
        number_of_appearance = []
        products_price = []
        each_revenue_list = []
        save_max = []

        #Declare variable
        count = 0
        total_revenue = 0

        #Get the size of the array
        rows_transactions = len(transactions)
        columns_transactions = len(transactions[0])
        rows_products = len(products)
        columns_products = len(products[0])

        #Copy commodity into new list
        for i in range(rows_transactions):
            commodity.append(transactions[i][1])
        
        #Copy commodity into new list
        for i in range(rows_products):
            commodity1.append(products[i][0].strip())

        #Merge all list from commodity together
        for i in commodity:
            for j in i:
                commodity_merge.append(j)
        
        #List of commodity
        commodity_merged = sorted(list(set(commodity_merge)))
        
        #Count the number of commodity
        for i in commodity_merged:
            for j in commodity:
                for k in j:
                    if(i == k):
                        count += 1
            number_of_appearance.append(count)
            count = 0 #Set count = 0 for the next one
        

        #Read price list into new list
        for i in range(rows_products):
            products_price.append(int(products[i][1].strip()))
        

        #Convert two lists into a dictionary(commodity_merged & number_of_appearance)
        twolst_to_dictionary = {commodity_merged[i]: number_of_appearance[i] for i in range(len(commodity_merged))} #1
        twolst_to_dictionary1 = {commodity_merged[i]: products_price[i] for i in range(len(commodity_merged))} #Pricce #2
        twolst_to_dictionary2 = {commodity1[i]: products_price[i] for i in range(len(commodity1))}                       #3 

        """-----------------PART 2-----------------"""
        for i in twolst_to_dictionary2:
            
            for j in twolst_to_dictionary:
                if(i == j):
                    total_revenue += twolst_to_dictionary[j] * twolst_to_dictionary2[i]
                    each_revenue_list.append(total_revenue)
                else:
                    total_revenue += 0
            total_revenue = 0
        
        #Convert to Dictionary
        twolst_to_dictionary3 = {commodity_merged[i]: each_revenue_list[i] for i in range(len(commodity_merged))}                       #4
        max_revenue = max(twolst_to_dictionary3.values())

        #Find max revenue
        for i in twolst_to_dictionary3:
            if twolst_to_dictionary3[i] == max_revenue:
                save_max.append(i)
        return save_max 
    except:
        return []

def req5(history, k):
    if type(k) != int or k < 0:
        return []

    elif abs(k) <= len(history) and type(k) != str:
        try:
            #List creating
            client_code = []
            client_code_merged = []
            transactions_ID = []
            transactions_ID_merged = []
            save_result = []
            list_client = []

            #Copy commodity into new list
            for i in range(len(history)):
                client_code.append(history[i][0])

            for i in range(len(history)):
                transactions_ID.append(history[i][1])
            
            #Merge all list from commodity together
            #1
            for i in client_code:
                for j in i:
                    client_code_merged.append(j)
            client_code_merged = sorted(list(set(client_code_merged)))
            #2
            for i in transactions_ID:
                transactions_ID_merged.append(i)
            
            #Count
            for i in transactions_ID_merged:
                save_result.append(len(i))

            #Convert two lists into a dictionary(commodity_merged & number_of_appearance)
            twolst_to_dictionary = {client_code_merged[i]: save_result[i] for i in range(len(client_code))}
            
            #Define a function to Convert to dictionary
            def Convert_to_dictionary(tup, di):
                di = dict(tup)
                return di

            dictionary = {}
            dictionary1 = Convert_to_dictionary(twolst_to_dictionary,dictionary)

            #Define a function to sort values in dictionary1
            def sort_dict_by_value(d, reverse = True):
                return dict(sorted(d.items(), key = lambda x: x[1], reverse = reverse))
            
            #Initialize value count
            count = 0
            #the list of customer codes
            for i in sort_dict_by_value(dictionary1):
                if(count == k):
                    break
                else:
                    list_client.append(i)
                    count += 1
            
            return list_client
        except:
            return []
    else:
        return []
def req6(transactions, history, k):
    try:
        #List creating
        client_code = []
        client_code_merged = []
        transactions_ID = []
        transactions_ID_merged = []
        commodity = []
        commodity_merge = []
        transactions_ID_each = []
        transactions_ID_each_merge = []
        vector_max = {}
        save_max = []

        #Copy commodity into new list
        for i in range(len(history)):
            client_code.append(history[i][0])

        for i in range(len(history)):
            transactions_ID.append(history[i][1])
        
        for i in range(len(transactions)):
            commodity.append(transactions[i][1])

        for i in range(len(transactions)):
            transactions_ID_each.append(transactions[i][0])
        
        #Merge all list from commodity together
        #1
        for i in client_code:
            for j in i:
                client_code_merged.append(j)
        client_code_merged = sorted(list(set(client_code_merged)))
        #2
        for i in transactions_ID:
            transactions_ID_merged.append(i)
        # print(transactions_ID_merged)
        #3
        for i in commodity:
            for j in i:
                commodity_merge.append(j)
        commodity_merged = sorted(list(set(commodity_merge)))
        # print(commodity_merged)
        #4
        for i in transactions_ID_each:
            for j in i:
                transactions_ID_each_merge.append(j)

        # print(transactions_ID_each_merge)
        
        #Convert two lists into a dictionary(commodity_merged & number_of_appearance)
        twolst_to_dictionary = {client_code_merged[i]: transactions_ID_merged[i] for i in range(len(client_code_merged))}
        twolst_to_dictionary1 = {transactions_ID_each_merge[i]: commodity[i] for i in range(len(transactions_ID_each_merge))}

        #/--------------------------***--------------------------/
        for i in twolst_to_dictionary:
            vector_max[i] = []
            for j in twolst_to_dictionary[i]:
                for z in twolst_to_dictionary1[j.strip()]:
                    vector_max[i].append(z)
        
        def count(list1,list2):
            count = 0
            save_count_list = []
            for i in list1:
                for j in list2:
                    if (i == j):
                        count += 1
                save_count_list.append(count)
                count = 0
            return save_count_list

        save_count_list = []
        save_count_list1 = []
        for i in vector_max:
            if (i == k):
                save_count_list = sorted(list(set(vector_max[i])))
                save_count_list1 = count(sorted(list(set(vector_max[i]))),vector_max[i])
        
        twolst_to_dictionary2 = {save_count_list[i]: save_count_list1[i] for i in range(len(save_count_list))}

        #Find max & min in list after counting
        result = []
        for i in twolst_to_dictionary2:
            if(twolst_to_dictionary2[i] == max(twolst_to_dictionary2.values())):
                result.append(i)
        return (result)
    except:
        return []
def req7(transactions, history):
    try:
        #List creating
        client_code = []
        client_code_merged = []
        transactions_ID = []
        transactions_ID_merged = []
        len_transactions_ID = []
        transactions_ID_each = []
        transactions_ID_each_merge = []
        commodity = []
        commodity_merge = []
        commodity = []
        vector_min = []
        vector_max = []
        tmp = []
        result = []
        result_merge = []
        result_merged = []
        result1 = []

        #Copy commodity into new list
        for i in range(len(history)):
            client_code.append(history[i][0])
        
        for i in range(len(history)):
            transactions_ID.append(history[i][1])

        for i in range(len(transactions)):
            transactions_ID_each.append(transactions[i][0])
        
        for i in range(len(transactions)):
            commodity.append(transactions[i][1])
        
        #Merge all list from commodity together
        #1
        for i in client_code:
            for j in i:
                client_code_merged.append(j)
        client_code_merged = sorted(list(set(client_code_merged)))
        #print(client_code_merged) #['U1', 'U2', 'U3', 'U4', 'U5']
        #2
        for i in transactions_ID:
            # print(i)
            transactions_ID_merged.append(i)
        for i in transactions_ID_merged:
            # print(i.tolist())
            tmp.append(i.tolist())
        #3 
        for i in transactions_ID_each:
            for j in i:
                transactions_ID_each_merge.append(j)
        #4
        for i in commodity:
            for j in i:
                commodity_merge.append(j)
        commodity_merged = sorted(list(set(commodity_merge)))
        
        twolst_to_dictionary = {client_code_merged[i]: tmp[i] for i in range(len(client_code_merged))}
        twolst_to_dictionary1 = {transactions_ID_each_merge[i]: commodity[i] for i in range(len(transactions_ID_each_merge))}

        #Loop FOR to get what i want
        for i in twolst_to_dictionary.values():
            len_transactions_ID.append(len(i))
            
        for i in twolst_to_dictionary.values():
            
            if len(i) == min(len_transactions_ID):
                vector_min.append(i)
                    
        for i in vector_min:
            for j in twolst_to_dictionary1:
                if (str(i[0]) == str(j)):
                    result.append(twolst_to_dictionary1[j])
                
        for i in result:
            for j in i:
                result_merge.append(j)
        
        result_merged = sorted(list(set(result_merge)))

        #Init
        count = 0
        number_of_appearance = []

        #Count the number of result_merge
        for i in result_merged:
            for j in result_merge:
                if(i == j):
                    count += 1
            number_of_appearance.append(count)
            count = 0

        #Dictionary of result_merged && number_of_appearance
        twolst_to_dictionary2 = {result_merged[i]: number_of_appearance[i] for i in range(len(result_merged))}

        #Get list of commodity
        for i in twolst_to_dictionary2:
            if(twolst_to_dictionary2[i] == max(twolst_to_dictionary2.values())):
                vector_max.append(i)

        return vector_max
    except:
        return []

def req8(transactions, history, k):
    try:
        def convertTuple(tup):
            st = ''.join(map(str, tup))
            return st
        commodity = []
        commodity_merge = []
        #Copy commodity into new list
        for i in range(len(transactions)):
            commodity.append(transactions[i][1])
        #Merge all list from commodity together
        for i in commodity:
            for j in i:
                commodity_merge.append(j)
        commodity_merged = sorted(list(set(commodity_merge)))
        dict_transactions = {}
        for i in range(len(transactions)):
            dict_transactions[convertTuple(tuple(transactions[i][0]))] = transactions[i][1].tolist()
        dict_history = {}
        for i in range(len(history)):
            dict_history[convertTuple(tuple(history[i][0]))] = history[i][1]
        #get the amout of k customer
        def get_customer_amount(dict_transactions, dict_history, k):
            list= []
            for i in dict_history:
                if k in i:
                    list = dict_history[i].tolist()   
            list_result = []
            for i in list:
                for j in dict_transactions:
                    if i.strip() == j.strip():
                        list_result.extend(dict_transactions[j])
            return list_result
        
        dict = {}
        for i in dict_history:
            if k not in i:
                dict[i] = np.array(sorted(get_customer_amount(dict_transactions, dict_history, i)))
        
        def Count_Frequency(list1,list2):
            freq ={}
            for item in list1:
                if (item in freq):
                    freq[item] += 1
                else:
                    freq[item] = 1

            for i in list2:
                if i not in freq:
                    freq[i] = 0
            return (freq)

        dictionary = sorted(Count_Frequency(get_customer_amount(dict_transactions, dict_history, k),commodity_merged))
        sorted_dict1 = {key:Count_Frequency(get_customer_amount(dict_transactions, dict_history, k),commodity_merged)[key] for key in dictionary}
        lst1 = []
        for i in sorted_dict1:
                lst1.append(sorted_dict1[i])
        lst = []
        for i in dict:
            dictionary1 = sorted(Count_Frequency(dict[i],commodity_merged))
            sorted_dict = {key:Count_Frequency(dict[i],commodity_merged)[key] for key in dictionary1}
            for j in sorted_dict:
                lst.append(sorted_dict[j])
                
        array = np.array(lst).reshape(len(commodity_merged)-1,len(commodity_merged))
        array1 = np.array(lst1)
        n_rank = np.linalg.matrix_rank(array)

        result = []
        n_rank = np.linalg.matrix_rank(array)
        for i in range(n_rank):
            cosine = np.dot(array1,np.array(array[i]))/(np.linalg.norm(array1)*np.linalg.norm(np.array(array[i])))
            result.append(cosine)
        lst2 = []
        for i in dict_history:
            if k not in i:
                lst2.append(i)
        twolst_to_dictionary = {lst2[i]: result[i] for i in range(len(lst2))}
        
        result2 = []
        for i in twolst_to_dictionary:
            if (twolst_to_dictionary[i] == max(twolst_to_dictionary.values())):
                result2.append(i)
        return(result2)
    except:
        return []

def req9(transactions, history, products):
    if type(transactions) == str or type(history) == str or type(products) == str:
        return []
    try:
        list = []
        for i in range(len(transactions)):
            for j in transactions[i][1]:
                list.append(j.strip())
        list = sorted(set(list)) 
        for i in range(len(products)):
            if str(products[i][0].strip()) not in list:
                list.clear()
                list.append(str(products[i][0].strip()))  
        return (list)
    except:
        return []
def req10(history, transactions, products, k):
    try:
        def convertTuple(tup):
            st = ''.join(map(str, tup))
            return st
        def flat(t):
            return [i for sub in t for i in sub]
        def delete(list):
            lst = []
            for i in list:
                lst.append(i.strip())
            return lst
        dict_transactions = {}
        for i in range(len(transactions)):
            dict_transactions[convertTuple(tuple(transactions[i][0]))] = transactions[i][1].tolist()
        #dict_transactions{'T100': ['I1', 'I2', 'I5'], 'T200': ['I2', 'I4'], 'T300': ['I2', 'I3'], 'T400': ['I1', 'I2', 'I4'], 'T500': ['I1', 'I3'], 'T600': ['I2', 'I3'], 'T700': ['I1', 'I3'], 'T800': ['I1', 'I2', 'I3', 'I5'], 'T900': ['I1', 'I2', 'I3'], 'T1000': ['I1', 'I3', 'I2']}
        dict_history = {}
        for i in range(len(history)):
            dict_history[convertTuple(tuple(history[i][0]))] = history[i][1].tolist()
        #dict_history{'U1': ['T100', 'T400'], 'U2': ['T200', 'T300', 'T700'], 'U3': ['T500', 'T600', 'T1000'], 'U4': ['T800'], 'U5': ['T900']}
        dict_products = {}
        for i in range(len(products)):
            dict_products[str(products[i][0].strip())] = int(products[i][3])
        #dict_products{'I1': 1, 'I2': 3, 'I3': 1, 'I4': 3, 'I5': 2, 'I6': 2}
        dict = {}
        for key in dict_history:
            list = []
            for key1 in dict_transactions:
                if key1 in delete(dict_history[key]):
                    list.append(dict_transactions[key1])
            dict[key] = flat(list) 
            #{'U1': ['I1', 'I2', 'I5', 'I1', 'I2', 'I4'], 'U2': ['I2', 'I4', 'I2', 'I3', 'I1', 'I3'], 'U3': ['I1', 'I3', 'I2'], 'U4': ['I1', 'I2', 'I3', 'I5'], 'U5': ['I1', 'I2', 'I3']}  
            for i in dict:
                for j in dict_products:
                    if j in dict[i]:
                        index = dict[i].index(j)
                        dict[i].pop(index)
                        dict[i].insert(index,dict_products[j])
                        #dict{'U1': [1, 3, 2, 1, 3, 3], 'U2': [3, 3, 3, 1, 1, 1], 'U3': [1, 1, 3, 1, 1, 1, 3], 'U4': [1, 3, 1, 2], 'U5': [1, 3, 1]}
        def Count_Frequency(list):
            (unique, counts) = np.unique(list, return_counts=True)
            frequencies = np.asarray((unique, counts)).T
            return frequencies
        def convert(list):
            number = 0
            for i in list:
                number = i
            return number
        dict1 = {}
        m = 0
        for i in dict:
            if k == i:
                for j in Count_Frequency(np.array(dict[i])).tolist():
                    dict1[j[0]] = convert(j[1:])
                for key in dict1:
                    if dict1[key] == max(dict1.values()):
                        m = key
                        break
        print(dict1)
        return m if (m != 0) else []
    except:
        return []
# print("Yeu cau 1:",req1(transactions))
# print("Yeu cau 1:",req1('transactions'))

# print("Yeu cau 2:",req2(products))
# print("Yeu cau 2:",req2('products'))

# print("Yeu cau 3:",req3(transactions, products))
# print("Yeu cau 3:",req3('transactions', products))
# print("Yeu cau 3:",req3('transactions', 'products'))

# print("Yeu cau 4:",req4(transactions, products))
# print("Yeu cau 4:",req4('transactions', products))
# print("Yeu cau 4:",req4('transactions', 'products'))

# print("Yeu cau 5: ",req5(history,-1))
# print("Yeu cau 5: ",req5(history,0))
# print("Yeu cau 5: ",req5(history,1))
# print("Yeu cau 5: ",req5(history,2))
# print("Yeu cau 5: ",req5(history,3))
# print("Yeu cau 5: ",req5(history,4))
# print("Yeu cau 5: ",req5(history,5))
# print("Yeu cau 5: ",req5(history,6))
# print("Yeu cau 5: ",req5(history,'a'))

# print("Yeu cau 6: ",req6(transactions,history,'U4'))
# print("Yeu cau 6: ",req6(transactions,history,'U3'))
# print("Yeu cau 6: ",req6(transactions,history,'U2'))
# print("Yeu cau 6: ",req6(transactions,history,'U1'))
# print("Yeu cau 6: ",req6(transactions,history,'U0'))
# print("Yeu cau 6: ",req6(transactions,history,1))

# print("Yeu cau 7: ",req7(transactions,history))
# print("Yeu cau 7: ",req7(transactions,'history'))

# print("Yeu cau 8: ",req8(transactions,history,'U0'))
# print("Yeu cau 8: ",req8(transactions,history,'U1'))
# print("Yeu cau 8: ",req8(transactions,history,'U2'))
# print("Yeu cau 8: ",req8(transactions,history,'U3'))
# print("Yeu cau 8: ",req8(transactions,history,'U4'))
# print("Yeu cau 8: ",req8(transactions,history,'U5'))
# print("Yeu cau 8: ",req8(transactions,history,'U6'))
# print("Yeu cau 8: ",req8(transactions,history,'a'))
# print("Yeu cau 8: ",req8(transactions,history,143))

# print("Yeu cau 9: ",req9(transactions, history, products))
# print("Yeu cau 9: ",req9('transactions', history, products))
# print("Yeu cau 9: ",req9(transactions, 'history', products))
# print("Yeu cau 9: ",req9(transactions, history, 'products'))

# print("Yeu cau 10: ",req10(history, transactions, products, 'u1'))
# print("Yeu cau 10: ",req10(history, transactions, products, 'U1'))
# print("Yeu cau 10: ",req10(history, transactions, products, 'U2'))
# print("Yeu cau 10: ",req10(history, transactions, products, 'U3'))
# print("Yeu cau 10: ",req10(history, transactions, products, 'U4'))
# print("Yeu cau 10: ",req10(history, transactions, products, 'U5'))
# print("Yeu cau 10: ",req10(history, transactions, products, 123))