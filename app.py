from flask import Flask, request, jsonify
import pandas as pd


app = Flask(__name__)

'''
tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]
'''
data = pd.read_csv('data.csv')



@app.route('/retrofit')
def query():
	year = int(request.args.get('year'))
	flr = int(request.args.get('flr'))
	return jsonify({'abc': int(data[(data['year'] == year)].iloc[0]['nump'])})


'''
def get_tasks(task_id):
	task = [task for task in tasks if task['id'] == task_id]
	if len(task) == 0:
		abort(404)
	return jsonify({'task': task[0]})
'''

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")