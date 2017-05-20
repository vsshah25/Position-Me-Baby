from __future__ import division 
from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import StandardScaler 
import pandas as pd 
import numpy as np 
from sklearn.externals import joblib
import matplotlib.pyplot as plt
import multiprocessing as mp
import serial 
from sklearn.decomposition import PCA
# def readata_convertoList():

# 	serialReceiver = serial.Serial(
#     port='/dev/ttyUSB0',
#     baudrate=115200,
#     stopbits=serial.STOPBITS_ONE,)

#     while serialReceiver.isOpen():
# 		received_tuple = serialReceiver.read()


def average(rssi_list,n,Id):
	list_len = len(rssi_list)
	no_of_chuncks = int(list_len/n)
	

	rssi_list_1 = rssi_list[0:no_of_chuncks*n]
	rssi_list_2 = rssi_list[no_of_chuncks*n:no_of_chuncks*n+1]

	rssi_array_1 = np.array(rssi_list_1)
	rssi_list_2 = np.array(rssi_list_2)
	rssi_shaped_array = np.reshape(rssi_array_1, (no_of_chuncks,n) )
	per_avg_array = np.array([])

	for i in range(len(rssi_shaped_array)):
		print i ,': applying averaging filter on RSSI values of reference point', Id, ' with chunk size' ,n
		temp_array = rssi_shaped_array[i:i+1][0]
		avg = np.mean(temp_array)
		temp_avg_array = np.array([avg]*n)
		per_avg_array = np.concatenate((per_avg_array,temp_avg_array))
	
	filtered_array = np.concatenate((per_avg_array,rssi_list_2))

	return filtered_array
def reduceDimension(input_dataset,n_out_features):
	n = n_out_features
	print "Applying PCA. Reducing dimension to ", n   
	pca = PCA(n_components=n)
	dataframe = pca.fit_transform(input_dataset)
	print "returned reduced dataset"  
	return dataframe
def compute_eta(rssi_list,x_router,y_router,x_ref,y_ref,Id):
	
	rssi_d = np.array(rssi_list)

	if len(rssi_d.shape) == 1:
		
		ref_dist = np.array([191.08]*len(rssi_d))           # reference distance is taken to be 1  
		RSSI_at_ref_dist = np.array([65]*len(rssi_d))  # RSSI at reference distance is taken to be 30      
		
		x_ref_cor = [x_ref]*len(rssi_d)
		y_ref_cor = [y_ref]*len(rssi_d)
		x_ref_cor = np.array(x_ref_cor)
		y_ref_cor = np.array(y_ref_cor)
		
		dist = np.sqrt(np.square(x_router - x_ref_cor) + np.square(y_router - y_ref_cor))
		eta = (rssi_d - RSSI_at_ref_dist)/(10*np.log10(dist/ref_dist))

	if len(rssi_d.shape) == 0:
		rssi_d = rssi_list
		RSSI_at_ref_dist = 67
		ref_dist = 191.08												
		x_ref = np.array(x_ref)
		y_ref = np.array(y_ref)

		dist = np.sqrt(np.square(x_router - x_ref) + np.square(y_router - y_ref))
		eta = (rssi_d - RSSI_at_ref_dist)/(10*np.log10(dist/ref_dist))

	
	print 'computing eta for reference point', Id	
	return eta
def extract_dist(router_pos,x_cList,y_cList):
	x_cor = np.array(x_cList)
	y_cor = np.array(y_cList)
	x_router = np.array([router_pos[0]]*len(x_cor))
	y_router = np.array([router_pos[1]]*len(y_cor))
	dist = np.sqrt(np.square(x_cor-x_router) + np.square(y_cor-y_router))
	return dist

def get_angle(x_cor,y_cor,len_list):
	ang = np.arctan(y_cor/x_cor)
	ang_list = np.array([ang]*len_list)
	return ang_list

def RSSI_id(dataframe,Nodemcu_id):
	object_ids = ['obj0','obj1','obj2','obj3','obj4']
	rssi_columns = ['rssi0','rssi1','rssi2','rssi3','rssi4']
	rssi_list = []
	RSSI_columns = ['obj0','rssi0','obj1','rssi1','obj2','rssi2','obj3','rssi3','obj4','rssi4']
	 
	
	for i in range(len(dataframe)): 
		for j in range(5):				
			if len(dataframe[RSSI_columns].loc[i:i].values) > 0:	
				if dataframe[RSSI_columns].loc[i:i][object_ids[j]].values == Nodemcu_id:
					 print "At row  ", i ,' for reference point', Nodemcu_id, 'sorting rssi values'
					 rssi_list = rssi_list + list(dataframe[RSSI_columns].loc[i:i][rssi_columns[j]].values)
		
	return rssi_list	
def data_cleaning(dataframe):
	# for i in range(len(dataframe)):

	# 	row = dataframe.loc[i:i]
	print "data cleaning initiated"
	
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
	
def train(input):
	Datafile = input['Datafile']                    #input the datafile
	data = pd.read_csv(Datafile)					#load the datafile and create a dataframe			
	data = data_cleaning(data)                      #Filter out garbage data           	
	data.to_csv('cleaned_dataset.csv')

	train_dataframe = pd.DataFrame()
	Tvar_dataframe = pd.DataFrame()
	
	RSSI_columns = ['obj0','rssi0','obj1','rssi1','obj2','rssi2','obj3','rssi3','obj4','rssi4']
	router_pos = [0,137.6]

	train_dataframe['rssi_0'] =  RSSI_id(data,0)


	x_router = [router_pos[0]]*len(train_dataframe)
	y_router = [router_pos[1]]*len(train_dataframe)

	x_ref = [228,228,-186.8,-186.8]
	y_ref = [-147.6,137.6,-147.6,137.6]
	
	rssi_list_1 = RSSI_id(data,1)  
	rssi_list_2 = RSSI_id(data,2)
	rssi_list_3 = RSSI_id(data,3)
	rssi_list_4 = RSSI_id(data,4)

	rssi_list_1 = np.ravel(average(rssi_list_1,5,1))
	rssi_list_2 = np.ravel(average(rssi_list_2,5,2))
	rssi_list_3 = np.ravel(average(rssi_list_3,5,3))
	rssi_list_4 = np.ravel(average(rssi_list_4,5,4))

	train_dataframe['eta_1'] =  compute_eta( rssi_list_1, x_router,y_router,x_ref[0],y_ref[0],1) 
	train_dataframe['eta_2'] =  compute_eta( rssi_list_2, x_router,y_router,x_ref[1],y_ref[1],2)
	train_dataframe['eta_3'] =  compute_eta( rssi_list_3, x_router,y_router,x_ref[2],y_ref[2],3)
	train_dataframe['eta_4'] =  compute_eta( rssi_list_4, x_router,y_router,x_ref[3],y_ref[3],4)

	
	# print train_dataframe.head()
	# print train_dataframe.loc[:,['dist_ref1','dist_ref2']].head()
	#print reduceDimension(np.array(train_dataframe.loc[:,['dist_ref1','dist_ref2','dist_ref3','dist_ref4']]), 2)
		
	meas_dist = extract_dist(router_pos, data['x'].values,data['y'].values)
	meas_dist = meas_dist[0:len(train_dataframe)]
	Tvar_dataframe['distance'] = meas_dist
	Tvar_dataframe = np.array(Tvar_dataframe)
	Tvar_dataframe = np.ravel(Tvar_dataframe)


	# print 'logging training data...'
	# train_dataframe.to_csv('training_data.csv')
	# print 'training data saved in training_data.csv'
	
	print 'normalizing data... '	
	scaler = StandardScaler()  
	scaler.fit(train_dataframe)  
	train_dataframe = scaler.transform(train_dataframe) 
	print 'Normalization done'

	print 'logging normalized data...'
	normalized_data = pd.DataFrame(train_dataframe)
	normalized_data['distance'] = Tvar_dataframe
	normalized_data.to_csv('normalized_trainingData.csv')
	print 'normalized data saved in normalized_trainingData.csv'
	
	train_dataframe = pd.DataFrame(train_dataframe)
	ref_distFrame = pd.DataFrame()
	ref_distFrame['dist_ref1'] =  extract_dist(router_pos,[x_ref[0]]*len(train_dataframe),[y_ref[0]]*len(train_dataframe))
	ref_distFrame['dist_ref2'] =  extract_dist(router_pos,[x_ref[1]]*len(train_dataframe),[y_ref[1]]*len(train_dataframe))
	ref_distFrame['dist_ref3'] =  extract_dist(router_pos,[x_ref[2]]*len(train_dataframe),[y_ref[2]]*len(train_dataframe))
	ref_distFrame['dist_ref4'] =  extract_dist(router_pos,[x_ref[3]]*len(train_dataframe),[y_ref[3]]*len(train_dataframe))

	train_dataframe['dist_ref1'] = ref_distFrame['dist_ref1']/ref_distFrame['dist_ref1']
	train_dataframe['dist_ref2'] = ref_distFrame['dist_ref2']/ref_distFrame['dist_ref1']
	train_dataframe['dist_ref3'] = ref_distFrame['dist_ref3']/ref_distFrame['dist_ref1']
	train_dataframe['dist_ref4'] = ref_distFrame['dist_ref4']/ref_distFrame['dist_ref1']

	train_dataframe['ang_ref1'] = get_angle(x_ref[0],y_ref[0],len(train_dataframe))
	train_dataframe['ang_ref2'] = get_angle(x_ref[1],y_ref[1],len(train_dataframe))
	train_dataframe['ang_ref3'] = get_angle(x_ref[2],y_ref[2],len(train_dataframe))
	train_dataframe['ang_ref4'] = get_angle(x_ref[3],y_ref[3],len(train_dataframe))

	
	print 'logging training data...'
	train_dataframe.to_csv('training_data.csv')
	print 'training data saved in training_data.csv'

	print "training dataset"
	print train_dataframe

	print "Target variable "	
	print  Tvar_dataframe


	reg = MLPRegressor(solver='lbfgs')
	print 'training neural net....'
	reg.fit(train_dataframe, Tvar_dataframe)
	joblib.dump(reg, 'model_pos1.pkl')
	print 'neural net trained. Model saved in a pickle file as an object'

def predict(input_data):
	
	input_rssi_data = input_data
	input_data = np.array(input_data)
	
	router_pos = [0,137.6]
	x_ref = [228,228,-186.8,-186.8]
	y_ref = [-147.6,137.6,-147.6,137.6]

	x_router = []
	y_router = []

	if(len(input_data.shape)==1):
		x_router = [router_pos[0]]
		y_router = [router_pos[0]]

	if(len(input_data.shape)==2):
		x_router = [router_pos[0]]*len(input_data.shape[1])
		y_router = [router_pos[0]]*len(input_data.shape[1])


	input_rssi_data[1] = compute_eta( np.array(input_rssi_data[1]), x_router,y_router,x_ref[0],y_ref[0],1)
	input_rssi_data[2] = compute_eta( np.array(input_rssi_data[2]), x_router,y_router,x_ref[1],y_ref[1],2)
	input_rssi_data[3] = compute_eta( np.array(input_rssi_data[3]), x_router,y_router,x_ref[2],y_ref[2],3)
	input_rssi_data[4] = compute_eta( np.array(input_rssi_data[4]), x_router,y_router,x_ref[3],y_ref[3],4)

	reg = joblib.load('model_pos1.pkl') 
	print input_rssi_data
	scaler = StandardScaler()  
	scaler.fit(input_rssi_data)  
	input_rssi_data = scaler.transform(input_rssi_data)  
	print input_rssi_data
	est_distance = reg.predict(input_rssi_data)
	return est_distance

#train({"Datafile":  "/media/pranav/Common_space2/projects/Local_positioning_system/ML and database/database/pos1.csv"})
train({"Datafile":"/media/pranav/Common_space2/projects/Local_positioning_system/ML and database/database/test_database/size500Dataset.csv"})
#print predict([65,64,81,72,64])


