from sklearn.neural_network import MLPRegressor
import pandas as pd 
import numpy as np 





def extract_dist(dataframe):
	x_cor = dataframe['x'].values
	y_cor = dataframe['y'].values
	dist = np.sqrt(np.square(x_cor) + np.square(y_cor))

	return dist

def RSSI_id(dataframe,Nodemcu_id):
	object_ids = ['obj0','obj1','obj2','obj3','obj4']
	rssi_columns = ['rssi0','rssi1','rssi2','rssi3','rssi4']
	rssi_list = []
	RSSI_columns = ['obj0','rssi0','obj1','rssi1','obj2','rssi2','obj3','rssi3','obj4','rssi4']
	 
	for j in range(5):
		for i in range(len(dataframe)): 
			if dataframe[RSSI_columns].loc[i:i][object_ids[j]].values == Nodemcu_id:
				 rssi_list = rssi_list + list(dataframe[RSSI_columns].loc[i:i][rssi_columns[j]].values)
		
	return rssi_list	

def data_cleaning(dataframe):
	# for i in range(len(dataframe)):

	# 	row = dataframe.loc[i:i]
	dataframe = dataframe[dataframe.x < 999]
	dataframe = dataframe[dataframe.y < 999]

	dataframe = dataframe[dataframe.obj0 + dataframe.obj1 + dataframe.obj2 + dataframe.obj3 + dataframe.obj4 < 11]
	dataframe = dataframe[dataframe.obj0 + dataframe.obj1 + dataframe.obj2 + dataframe.obj3 + dataframe.obj4 > -1]
	
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

	


	
	
	return dataframe



	
def train(input):
	Datafile = input['Datafile']
	data = pd.read_csv(Datafile)

	meas_dist = extract_dist(data)

	train_dataframe = pd.DataFrame(meas_dist)

	RSSI_columns = ['obj0','rssi0','obj1','rssi1','obj2','rssi2','obj3','rssi3','obj4','rssi4']

	data = data_cleaning(data)

	data.to_csv('cleaned_data.csv')
	print RSSI_id(data,0), len(RSSI_id(data,0)), len(data)
	# print data.loc[0:0]['x'] 
	

 

# # create Trainig Dataset
# train_x=[[x] for x in  range(200)]               #features. A matrix                     
# train_y=[x[0]**2 for x in train_x]                #distance
 

# #create neural net regressor
# reg = MLPRegressor(hidden_layer_sizes=(50,),algorithm="l-bfgs")
# reg.fit(train_x,train_y)
 
# #test prediction
# # test_x=[[x] for x in  range(201,220,2)]
 
# predict=reg.predict(test_x)
# print "_Input_\t_output_"
# for i in range(len(test_x)):
#     print "  ",test_x[i],"---->",predict[i]
#  

train({"Datafile":  "/media/pranav/Common_space1/projects/Local_positioning_system/ML and database/size500Dataset.csv"})
