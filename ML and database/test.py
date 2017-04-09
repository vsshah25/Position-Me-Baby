from __future__ import division 
from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import StandardScaler 
import pandas as pd 
import numpy as np 
from sklearn.externals import joblib
import matplotlib.pyplot as plt


def average(rssi_list,n):
	list_len = len(rssi_list)
	print list_len,n
	no_of_chuncks = int(list_len/n)
	print list_len%n

	rssi_list_1 = rssi_list[0:no_of_chuncks*n]
	rssi_list_2 = rssi_list[no_of_chuncks*n:no_of_chuncks*n+1]

	rssi_array_1 = np.array(rssi_list_1)
	rssi_list_2 = np.array(rssi_list_2)
	rssi_shaped_array = np.reshape(rssi_array_1, (no_of_chuncks,n) )
	per_avg_array = np.array([])

	for i in range(len(rssi_shaped_array)):
		temp_array = rssi_shaped_array[i:i+1][0]
		avg = np.mean(temp_array)
		temp_avg_array = np.array([avg]*n)

		per_avg_array = np.concatenate((per_avg_array,temp_avg_array))
	
	filtered_array = np.concatenate((per_avg_array,rssi_list_2))

	return filtered_array



def data_cleaning(dataframe):
	# for i in range(len(dataframe)):

	# 	row = dataframe.loc[i:i]
	print "filtering dataset... "
	
	print "checking values of x and y coordinates"
	dataframe = dataframe[dataframe.x < 999]
	dataframe = dataframe[dataframe.y < 999]
	print "checked"

	dataframe = dataframe[dataframe.obj0 + dataframe.obj1 + dataframe.obj2 + dataframe.obj3 + dataframe.obj4 < 11]
	dataframe = dataframe[dataframe.obj0 + dataframe.obj1 + dataframe.obj2 + dataframe.obj3 + dataframe.obj4 > -1]
	
	print "checking ids of nodeMCU's"
	dataframe = dataframe[dataframe.obj0 < 6]
	dataframe = dataframe[dataframe.obj1 < 6]
	dataframe = dataframe[dataframe.obj2 < 6]
	dataframe = dataframe[dataframe.obj3 < 6]
	dataframe = dataframe[dataframe.obj4 < 6]

	dataframe = dataframe[dataframe.obj0 > -1]
	dataframe = dataframe[dataframe.obj1 > -1]
	dataframe = dataframe[dataframe.obj2 > -1]
	dataframe = dataframe[dataframe.obj3 > -1]
	dataframe = dataframe[dataframe.obj4 > -1]
	print 'checked'

	print "checking errors in received datapacket"
	dataframe = dataframe[dataframe.obj0 != dataframe.obj1]
	dataframe = dataframe[dataframe.obj0 != dataframe.obj2]
	dataframe = dataframe[dataframe.obj0 != dataframe.obj3]
	dataframe = dataframe[dataframe.obj0 != dataframe.obj4]
	
	dataframe = dataframe[dataframe.obj1 != dataframe.obj2]
	dataframe = dataframe[dataframe.obj1 != dataframe.obj3]
	dataframe = dataframe[dataframe.obj1 != dataframe.obj4]
	
	dataframe = dataframe[dataframe.obj2 != dataframe.obj3]
	dataframe = dataframe[dataframe.obj2 != dataframe.obj4]

	dataframe = dataframe[dataframe.obj3 != dataframe.obj4]
	print 'checked'

	RSSI_columns = ['obj0','rssi0','obj1','rssi1','obj2','rssi2','obj3','rssi3','obj4','rssi4']

	print "dataset filtered"
	return dataframe

def RSSI_id(dataframe,Nodemcu_id):
	object_ids = ['obj0','obj1','obj2','obj3','obj4']
	rssi_columns = ['rssi0','rssi1','rssi2','rssi3','rssi4']
	rssi_list = []
	RSSI_columns = ['obj0','rssi0','obj1','rssi1','obj2','rssi2','obj3','rssi3','obj4','rssi4']
	 
	
	for i in range(len(dataframe)): 
		for j in range(5):				
			if len(dataframe[RSSI_columns].loc[i:i].values) > 0:	
				if dataframe[RSSI_columns].loc[i:i][object_ids[j]].values == Nodemcu_id:
					 print "At row  ", i ,' for reference point: ', Nodemcu_id, 'sorting rssi values'
					 rssi_list = rssi_list + list(dataframe[RSSI_columns].loc[i:i][rssi_columns[j]].values)
		
	return rssi_list	




def train(input):
	Datafile = input['Datafile']                    #input the datafile
	data = pd.read_csv(Datafile)					#load the datafile and create a dataframe			
	data = data_cleaning(data)                      #Filter out garbage data           	
	
	train_dataframe = pd.DataFrame()
	Tvar_dataframe = pd.DataFrame()
	
	RSSI_columns = ['obj0','rssi0','obj1','rssi1','obj2','rssi2','obj3','rssi3','obj4','rssi4']
	router_pos = [0,137.6]

	# train_dataframe['rssi_0'] =  RSSI_id(data,0)

	print average(RSSI_id(data,0),5)
	# x_router = [router_pos[0]]*len(train_dataframe)
	# y_router = [router_pos[0]]*len(train_dataframe)

	# x_ref = [228,228,-186.8,-186.8]
	# y_ref = [-147.6,137.6,-147.6,137.6]
	# train_dataframe['eta_1'] =  compute_eta( RSSI_id(data,1), x_router,y_router,x_ref[0],y_ref[0]) 
	# train_dataframe['eta_2'] =  compute_eta( RSSI_id(data,2), x_router,y_router,x_ref[1],y_ref[1])
	# train_dataframe['eta_3'] =  compute_eta( RSSI_id(data,3), x_router,y_router,x_ref[2],y_ref[2])
	# train_dataframe['eta_4'] =  compute_eta( RSSI_id(data,4), x_router,y_router,x_ref[3],y_ref[3])



train({"Datafile":"/media/pranav/Common_space1/projects/Local_positioning_system/ML and database/database/test_database/size500Dataset.csv"})