import re
from collections import Counter

from flask import Flask, render_template, request

app = Flask(__name__)


def parse(data):
	pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
	ips = re.findall(pattern, data)
	results = Counter(ips).most_common(10)
	return results



@app.route('/', methods=['POST','GET'])
def index():
	if request.method == 'POST':
		log = request.files['log_file'].read()
		txt = str(log,'utf8')
		result = parse(txt)

		ban = []

		for key,value in result:
			if value > 1:
				ban.append({'ip':key,'counts':value})
		return render_template('index.html', ips=ban)
	else:
		return render_template('index.html')


if __name__ == '__main__':
	app.run(debug=True)