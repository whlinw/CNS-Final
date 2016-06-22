import json
def get_header():
	header = """
	<head>
	<meta charset="utf-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
	<link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css">
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.4/jquery.min.js"></script>
	<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.2/js/bootstrap.min.js" integrity="sha384-vZ2WRJMwsjRMW/8U7i6PWi6AlO1L79snBrmgiDpgIWJ82z8eA5lenwvxbMV1PAh7" crossorigin="anonymous"></script>
	<style>
	.bs-callout { padding: 10px; margin: 10px 0; border: 1px solid #eee; border-left-width: 5px; border-radius: 3px;}
	.bs-callout h4 { margin-top: 0; margin-bottom: 5px; }
	.bs-callout p:last-child { margin-bottom: 0; }
	.bs-callout code { border-radius: 3px; }
	.bs-callout+.bs-callout { margin-top: -5px; }
	.bs-callout-default { border-left-color: #777; }
	.bs-callout-default h4 { color: #777; }
	.bs-callout-success { border-left-color: #5cb85c; }
	.bs-callout-success h4 { color: #5cb85c; }
	.bs-callout-danger { border-left-color: #d9534f; }
	.bs-callout-danger h4 { color: #d9534f; }
	.bs-callout-warning { border-left-color: #f0ad4e; }
	.bs-callout-warning h4 { color: #f0ad4e; }
	.inline {display:inline; margin-right: 20px;}
	</style>
	</head>
	"""
	return header

# <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.2/css/bootstrap.min.css" integrity="sha384-y3tfxAZXuh4HwSYylfB+J125MxIs6mR5FOHamPBG064zB+AFeWH94NdvaCBm8qnd" crossorigin="anonymous">

def get_data(content):
	data = json.loads(content)
	table = """
	<div class="container">
	<table class="table col-md-4">
	<thead>
	</thead>
	<tbody>
	"""
	<div class="table-responsive">
	print('JSON:', data)
	if data['evil'] == 'True':
		table += '<tr class="table-error"><th scope="row">' + 'URL' + '</th>' + '<td class="col-md-4">' + data['url'] + '</td></tr>'
	else:
		table += '<tr class="table-success"><th scope="row">' + 'URL' + '</th>' + '<td class="col-md-4">' + data['url'] + '</td></tr>'
	if data['grade'] == 'A':
		table += '<tr class="table-success"><th scope="row">' + 'Grade' + '</th>' + '<td class="col-md-4">' + data['grade'] + '</td></tr>'
	elif data['grade'] == 'C':
		table += '<tr class="table-error"><th scope="row">' + 'Grade' + '</th>' + '<td class="col-md-4">' + data['grade'] + '</td></tr>'
	else:
		table += '<tr class="table-warning"><th scope="row">' + 'Grade' + '</th>' + '<td class="col-md-4">' + data['grade'] + '</td></tr>'
	table += '<tr><th scope="row">' + '# Result' + '</th>' + '<td class="col-md-4">' + data['num'] + '</td></tr>'
	table += '<tr><th scope="row">' + 'Title' + '</th>' + '<td class="col-md-4">' + data['title'] + '</td></tr>'
	table += '<tr><th scope="row">' + 'Description' + '</th>' + '<td class="col-md-4">' + data['content'][:200] + '</td></tr>'
	table += '</tbody></table></div></div>'
	return table	

def get_data_callout(content):
	data = json.loads(content)
	table = '<div class="container">'
	table = ''
	if data['evil'] == 'True':
		table += '<div class="bs-callout bs-callout-danger">' + '<h4>URL</h4>' + data['url'] + '</div>'

	else:
		table += '<div class="bs-callout bs-callout-success">' + '<h4>URL</h4>' + data['url'] + '</div>'

	if data['grade'] == 'A':
		table += '<div class="bs-callout bs-callout-success">' + '<h4 class="inline">Grade</h4>' + data['grade'] + '</div>'
	elif data['grade'] == 'F':
		table += '<div class="bs-callout bs-callout-danger">' + '<h4 class="inline">Grade</h4>' + data['grade'] + '</div>'
	else:
		table += '<div class="bs-callout bs-callout-warning">' + '<h4 class="inline">Grade</h4>' + data['grade'] + '</div>'

	table += '<div class="bs-callout bs-callout-default">' + '<h4 class="inline">Search result</h4>' + data['num'] + '</div>'
	table += '<div class="bs-callout bs-callout-default">' + '<h4>Title</h4>' + data['title'] + '</div>'
	table += '<div class="bs-callout bs-callout-default">' + '<h4>Description</h4>' + data['content'][:300] + '</div>'
	table += '</div>'
	return table

def makeHTML(content):
	html = '<!DOCTYPE html>\n<html lang="en">\n' + get_header() + '<body>' + \
			get_data_callout(content) + '</body></html>'
	return html