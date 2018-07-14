# -*- coding: utf-8 -*-
from flask import Flask, request, render_template, url_for, json
app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/get_node_children", methods=["POST", "GET"])
def get_node_children():
	print(request.get_json()["name"]) # make here db query

	with open('./static/data/additionalData.json', 'r', encoding='utf-8') as f:
		data_json = json.load(f)
		# print(data_json)
	return json.dumps(data_json, ensure_ascii=False)

if __name__ == '__main__':
	app.run()
