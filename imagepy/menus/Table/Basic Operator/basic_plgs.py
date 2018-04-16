from imagepy.core.engine import Table
from imagepy import IPy

class Transpose(Table):
	title = 'Table Transpose'

	def run(self, tps, data, snap, para = None):
		tps.set_data(data.T)

class Corp(Table):
	title = 'Table Corp'
	note = ['req_sel']
	def run(self, tps, data, snap, para):
		tps.set_data(data.loc[tps.rowmsk, tps.colmsk])

class Duplicate(Table):
	title = 'Table Duplicate'
	para = {'name':'Undefined'}

	def load(self, tps):
		self.para['name'] = tps.title+'-copy'
		self.view = [(str, 'Name', 'name','')]
		return True

	def run(self, tps, data, snap, para = None):
		newdata = data.loc[tps.rowmsk, tps.colmsk]
		IPy.table(para['name'], newdata)

class DeleteRow(Table):
	title = 'Delete Rows'
	note = ['row_sel']

	def run(self, tps, data, snap, para = None):
		data.drop(tps.rowmsk, inplace=True)

class DeleteCol(Table):
	title = 'Delete Columns'
	note = ['col_sel']

	def run(self, tps, data, snap, para = None):
		data.drop(tps.colmsk, axis=1, inplace=True)

class AppendRow(Table):
	title = 'Append Rows'
	para = {'count':1, 'fill':True}
	view = [(int, (1,100), 0, 'count', 'count', ''),
			(bool, 'fill by last row', 'fill')]

	def run(self, tps, data, snap, para = None):
		newdata = data.reindex(index=range(data.shape[0]+para['count']), \
			method=[None,'pad'][para['fill']])
		tps.set_data(newdata)

class AddCol(Table):
	title = 'Add Column'
	para = {'name':'new', 'any':1.0}
	view = [(str, 'name', 'name', ''),
			('any', 'value', 'any')]

	def run(self, tps, data, snap, para = None):
		ctype = data.columns.dtype.type
		data[ctype(para['name'])] = para['any']
		print(data.info())

plgs = [Transpose, Duplicate, Corp, '-', DeleteRow, DeleteCol, AppendRow, AddCol]