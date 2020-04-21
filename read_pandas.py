import pandas as pd
def read_pandas(input_pk,header=0,index_col=[0],):
	if input_pk.endswith('pk'):
		with open(input_pk,'rb') as f:
			df = pd.read_pickle(f)
		# df = pd.read_pickle(input_pk)
	elif input_pk.endswith('csv'):
		df = pd.read_csv(input_pk,index_col=index_col,header=header,sep=',')
	elif input_pk.endswith('list'):
		df = pd.read_csv(input_pk,index_col=index_col,header=None)
	elif input_pk.endswith('tsv'):
		df = pd.read_csv(input_pk,index_col=index_col,header=header,sep='\t')
	else:
		assert 0, (input_pk,)
	return df