## import modules here 
import pandas as pd
import numpy as np


################# Question 1 #################

# helper functions
def read_data(filename):
    df = pd.read_csv(filename, sep='\t')
    return (df)

def project_data(df, d):
    # Return only the d-th column of INPUT
    return df.iloc[:, d]

def select_data(df, d, val):
    # SELECT * FROM INPUT WHERE input.d = val
    col_name = df.columns[d]
    return df[df[col_name] == val]

def remove_first_dim(df):
    # Remove the first dim of the input
    return df.iloc[:, 1:]

def slice_data_dim0(df, v):
    # syntactic sugar to get R_{ALL} in a less verbose way
    df_temp = select_data(df, 0, v)
    return remove_first_dim(df_temp)

'''def buc_rec_optimized(df):# do not change the heading of the function
    dims = df.shape[1]

    if dims == 1:
        input_sum = sum(project_data(df, 0))
        print('=>\t{}'.format(input_sum))
    else:
        dim0_vals = set(project_data(df, 0).values)

        for dim0_v in dim0_vals:
            sub_data = slice_data_dim0(df, dim0_v)
            buc_rec_optimized(sub_data)
        sub_data = remove_first_dim(df)
        buc_rec_optimized(sub_data)'''

def buc_rec_optimized(df):# do not change the heading of the function
    if df.shape[0] == 0:
        new_data = pd.DataFrame(columns=df.keys())
        single_tuple(df,new)
    else:
        new_data = pd.DataFrame(columns=df.keys())
        store_array = []
        buc(df,store_array,new_data)
    return new_data

def global_save(list):
    L =[]
    for i in list:
        L.append(i)
    return L

def single_tuple(df, new):
    pass

def buc(df,saved,new):
    dims = df.shape[1]
    if dims == 1:
        temp1 = global_save(saved)
        total = sum(project_data(df, 0))
        temp1.append(total)
        new.loc[len(new)] = temp1
    else:
        # the general case
        dim0_vals = set(project_data(df, 0).values)
        #key = project_data(df, 0).keys
        for dim0_v in dim0_vals:
            array2 = global_save(saved)
            array2.append(dim0_v)
            sub_data = slice_data_dim0(df, dim0_v)
            buc(sub_data, array2, new)
        ## for R_{ALL}
        array3 = global_save(saved)
        sub_data = remove_first_dim(df)
        array3.append('ALL')
        buc(sub_data,array3,new)

################# Question 2 #################

def v_opt_dp(x, num_bins):# do not change the heading of the function
    pass # **replace** this line with your code

