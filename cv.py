#!/usr/bin/env python3

import re


def maybe_right(d:dict, right_class:str, right2_class:str):
	content:str = ""
	right_indx:int = d["right_indx"]
	if d.get(["right","right2","nothinghere"][right_indx]) is not None:
		content = '<span class="alignright ' + [right_class,right2_class][right_indx] + '">' + d[["right","right2"][right_indx]] + '</span>'
		d["right_indx"] += 1
	return content

def largefirstchar_each_word(title:str):
	return re.sub('\\b([A-Z][a-z]+(?:\'s)?)\\b', '<span class="largefirstchar">\\1</span>', title)

def process_dict(d:dict, tagname:str, extra_classnames:str, depth:int, subtitle_class:str, right_class:str, right2_class:str, stylised_dots_level:int, normal_dots_level:int):
	idstr:str = ""
	if "id" in d:
		idstr += " id=\"" + d["id"] + "\""
	if extra_classnames != "":
		idstr += ' class="' + extra_classnames + '"'
	contentstr:str = ""
	contentindent:str = "\n"+"\t"*(depth+1)
	d["right_indx"] = 0
	if "subtitle_class" in d:
		subtitle_class = d["subtitle_class"]
	if "right_class" in d:
		right_class = d["right_class"]
	if "right2_class" in d:
		right2_class = d["right2_class"]
	if "title" in d:
		contentstr += contentindent + '<h2>' + largefirstchar_each_word(d["title"]) + '</h2>' + maybe_right(d,right_class,right2_class)
	if "smalltitle" in d:
		contentstr += contentindent + '<div><span class="hh2">' + d["smalltitle"] + '</span>' + maybe_right(d,right_class,right2_class) + '</div>'
	if "subtitle" in d:
		contentstr += contentindent + '<div><span class="'+subtitle_class+'">' + largefirstchar_each_word(d["subtitle"]) + '</span>' + maybe_right(d,right_class,right2_class) + '</div>'
	if "img" in d:
		contentstr += contentindent + '<div><img class="'+d["imgclass"]+'" src="imgs/'+d["img"]+'"/>' + maybe_right(d,right_class,right2_class) + '</div>'
	if "p" in d:
		p:list = d["p"]
		if type(p) is not list:
			p = [p]
		for pp in p:
			if pp == "":
				contentstr += "<br>"
			else:
				contentstr += contentindent + '<div><span>' + pp + '</span>' + maybe_right(d,right_class,right2_class) + '</div>'
	if "boxes" in d:
		contentstr += '<div class="boxcontainer">'
		for box in d["boxes"]:
			contentstr += '<div class="box">' + box + '</div>'
		contentstr += '</div>'
	if "stylised_dots" in d:
		d["children"] = d["stylised_dots"]
		stylised_dots_level += 1
		if stylised_dots_level == 1:
			tagname = "ul"
			contentstr = contentindent + '<li class="entry1">' + contentstr + '</li>'
	elif "dots" in d:
		d["children"] = d["dots"]
		normal_dots_level += 1
		stylised_dots_level = 0
	else:
		normal_dots_level = 0
		stylised_dots_level = 0
	childcontentstr:str = ""
	if "children" in d:
		child_class:str = d.get("child_class", "")
		child_tagname:str = "div"
		
		if normal_dots_level != 0:
			childcontentstr += "<ul>"
		
		if (stylised_dots_level != 0) or (normal_dots_level != 0):
			child_tagname = "li"
			if stylised_dots_level != 0:
				child_class += " entry"+str(stylised_dots_level)
		
		for c in d["children"]:
			childcontentstr += process_dict(c, child_tagname, child_class, depth+1, subtitle_class, right_class, right2_class, stylised_dots_level, normal_dots_level)
		
		if normal_dots_level != 0:
			childcontentstr += "</ul>"
	if "<div></div>" in childcontentstr:
		print("WARNING: Empty: ", depth, d)
	return "\n"+"\t"*depth+"<"+tagname+idstr+">" + contentstr + childcontentstr + "\n"+"\t"*depth + "</"+tagname+">"


def process_yaml_dict(d:dict):
	html:str = """<!DOCTYPE html>
<html>
<head>
	<title>NOTE: More settings -> Print backgrounds</title>
	<link rel="stylesheet" href="cv.css"></link>
</head>
<body>"""
	for dd in d["sections"]:
		html += process_dict(dd, "div", "", 0, None, "", "", 0, 0)
	html += """\n</body></html>"""
	return html


if __name__ == "__main__":
	from yaml import safe_load
	import argparse
	
	parser = argparse.ArgumentParser()
	parser.add_argument("yaml_fp")
	parser.add_argument("out_fp")
	args = parser.parse_args()
	
	d:dict = None
	with open(args.yaml_fp) as f:
		d = safe_load(f)
	
	with open(args.out_fp,"w") as f:
		f.write(process_yaml_dict(d))