from __future__ import division 
from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import StandardScaler 
import pandas as pd 
import numpy as np 
from sklearn.externals import joblib


def compute_eta(rssi_list,x_obj,y_obj,x_ref,y_ref):
	rssi_d = np.array(rssi_list)

	ref_dist = np.array([1]*len(rssi_d))     #a reference dist 
	RSSI_at_ref_dist = np.array([30]*len(rssi_d))     
	
	x_ref_cor = [x_ref]*len(rssi_d)
	y_ref_cor = [y_ref]*len(rssi_d)
	x_ref_cor = np.array(x_ref_cor)
	y_ref_cor = np.array(y_ref_cor)
	
	dist = np.sqrt(np.square(x_obj - x_ref_cor) + np.square(y_obj - y_ref_cor))
	eta = (rssi_d - RSSI_at_ref_dist)/(10*np.log10(dist/ref_dist))
	
	return eta


def extract_dist(dataframe,router_pos):
	x_cor = dataframe['x'].values
	y_cor = dataframe['y'].values
	x_router = [router_pos[0]]*len(x_cor)
	y_router = [router_pos[1]]*len(y_cor)

	dist = np.sqrt(np.square(x_cor-x_router) + np.square(y_cor-y_router))

	return dist

def RSSI_id(dataframe,Nodemcu_id):
	object_ids = ['obj0','obj1','obj2','obj3','obj4']
	rssi_columns = ['rssi0','rssi1','rssi2','rssi3','rssi4']
	rssi_list = []
	RSSI_columns = ['obj0','rssi0','obj1','rssi1','obj2','rssi2','obj3','rssi3','obj4','rssi4']
	 
	
	for i in range(len(dataframe)): 
		for j in range(5):				
			if len(dataframe[RSSI_columns].loc[i:i].values) > 0:	
				if dataframe[RSSI_columns].loc[i:i][object_ids[j]].values == Nodemcu_id:
					 print "at row  ", i ,' for nodemcuID: ', Nodemcu_id
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


	RSSI_columns = ['obj0','rssi0','obj1','rssi1','obj2','rssi2','obj3','rssi3','obj4','rssi4']

	
	return dataframe



	
def train(input):
	Datafile = input['Datafile']                    #input the datafile
	data = pd.read_csv(Datafile)					#load the datafile and create a dataframe			
	data = data_cleaning(data)                      #Filter out garbage data           	
	
	train_dataframe = pd.DataFrame()
	Tvar_dataframe = pd.DataFrame()
	
	RSSI_columns = ['obj0','rssi0','obj1','rssi1','obj2','rssi2','obj3','rssi3','obj4','rssi4']


	train_dataframe['rssi_0'] =  RSSI_id(data,0)

	x_cordinates = list(data['x'])[0:len(train_dataframe)]
	y_cordinates = list(data['y'])[0:len(train_dataframe)]

	x_ref = [0,0,0,0]
	y_ref = [0,0,0,0]
	train_dataframe['eta_1'] =  compute_eta( RSSI_id(data,1), x_cordinates,y_cordinates,x_ref[0],y_ref[0]) 
	train_dataframe['eta_2'] =  compute_eta( RSSI_id(data,2), x_cordinates,y_cordinates,x_ref[1],y_ref[1])
	train_dataframe['eta_3'] =  compute_eta( RSSI_id(data,3), x_cordinates,y_cordinates,x_ref[2],y_ref[2])
	train_dataframe['eta_4'] =  compute_eta( RSSI_id(data,4), x_cordinates,y_cordinates,x_ref[3],y_ref[3])

	router_pos = [0,0]
	meas_dist = extract_dist(data,router_pos)
	meas_dist = meas_dist[0:len(train_dataframe)]
	Tvar_dataframe['distance'] = meas_dist
	Tvar_dataframe = np.array(Tvar_dataframe)
	Tvar_dataframe = np.ravel(Tvar_dataframe)

	
	scaler = StandardScaler()  
	
	scaler.fit(train_dataframe)  
	train_dataframe = scaler.transform(train_dataframe)  

	reg = MLPRegressor(solver='lbfgs')
	reg.fit(train_dataframe, Tvar_dataframe)
	joblib.dump(reg, 'model.pkl')


def predict(input_data):
	
	input_rssi_data = input_data


	reg = joblib.load('model.pkl') 	
	est_distance = reg.predict(input_rssi_data)


train({"Datafile":  "/media/pranav/Common_space1/projects/Local_positioning_system/ML and database/database/pos1.csv"})
