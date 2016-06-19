import json
def get_header():
	header = """
	<head>
	<meta charset="utf-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.2/css/bootstrap.min.css" integrity="sha384-y3tfxAZXuh4HwSYylfB+J125MxIs6mR5FOHamPBG064zB+AFeWH94NdvaCBm8qnd" crossorigin="anonymous">
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.4/jquery.min.js"></script>
	<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.2/js/bootstrap.min.js" integrity="sha384-vZ2WRJMwsjRMW/8U7i6PWi6AlO1L79snBrmgiDpgIWJ82z8eA5lenwvxbMV1PAh7" crossorigin="anonymous"></script>
	</head>
	"""
	return header

def get_data(content):
	data = json.loads(content)
	table = """
	<div class="container">
	<table class="table">
	<thead>
	</thead>
	<tbody>
	"""
	if data['evil'] == 'True':
		table += '<tr class="table-error"><th scope="row">' + 'URL' + '</th>' + '<td>' + data['url'] + '</td></tr>'
	else:
		table += '<tr class="table-success"><th scope="row">' + 'URL' + '</th>' + '<td>' + data['url'] + '</td></tr>'
	if data['grade'] == 'A':
		table += '<tr class="table-success"><th scope="row">' + 'Grade' + '</th>' + '<td>' + data['grade'] + '</td></tr>'
	elif data['grade'] == 'C':
		table += '<tr class="table-error"><th scope="row">' + 'Grade' + '</th>' + '<td>' + data['grade'] + '</td></tr>'
	else:
		table += '<tr class="table-warning"><th scope="row">' + 'Grade' + '</th>' + '<td>' + data['grade'] + '</td></tr>'
	table += '<tr><th scope="row">' + 'Search' + '</th>' + '<td>' + data['title'] + '</td></tr>'
	table += '</tbody></table></div>'
	return table

def makeHTML(content):
	# res = json.loads(content)
	# html = '<html>' + get_header() + '<body width="300px" height="150px">' + \
	#  '<h4>URL</h4><p>' + res['url'] + '</p>' + \
	#  '<h4>Evil</h4><p>' + res['evil'] + '</p>' + \
	#  '<h4>Search num</h4><p>' + res['num'] + '</p>' + \
	#  '<h4>Search title</h4><p>' + res['title'] + '</p>' + \
	#  '<h4>Search content</h4><p>' + res['content'] + '</p>' + \
	#  '<h4>SSL Grade</h4><p>' + res['grade'] + '</p>' + \
	#  '</body></html>'
	html = '<!DOCTYPE html>\n<html lang="en">\n' + get_header() + '<body width="300px" height="150px">' + \
			get_data(content) + '</body></html>'
	return html