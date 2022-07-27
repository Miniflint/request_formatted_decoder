import urllib.parse
import subprocess
import json

###################################
# author: Miniflint
# made 28.07.2022
###################################

FILE_PATH = "test_json.txt"
STR_REPLACE = "signed_body=SIGNATURE."

def open_notepad():
	subprocess.call(['notepad.exe', FILE_PATH])

def delete_first_char(url_decoded:str):
	temp = url_decoded.split("{",1)
	temp[0]=temp[0].replace(STR_REPLACE, "")
	url_decoded = "{".join(temp)
	return (url_decoded)

def decode_in_json(decoded_url):
	parse = json.loads(decoded_url)
	fully_parsed = json.dumps(parse, indent=4, sort_keys=True)
	return (fully_parsed)

def decode_url(url):
	decoded_url = urllib.parse.unquote(url)
	return (decoded_url)

def write_file(json_parsed):
	with open(FILE_PATH, "w") as f:
		f.write(json_parsed)

def decode_url_handling(url):
	decoded_url = decode_url(url)
	del_decoded_url = delete_first_char(decoded_url)
	fully_parsed = decode_in_json(del_decoded_url)
	write_file(fully_parsed)
	open_notepad()

def de_intent_url():
	with open(FILE_PATH, 'r') as handle:
		parse = json.load(handle)
	fully_parsed = json.dumps(parse, indent=0, sort_keys=False)
	fully_parsed = fully_parsed.replace("\n", "")
	return (fully_parsed)

def encode_url(str_to_encode):
	decoded_url = urllib.parse.quote(str_to_encode)
	return (decoded_url)

def recode_url_handling():
	string = de_intent_url()
	recoded = encode_url(string)
	newstr = f"{STR_REPLACE}{recoded}"
	write_file(newstr)
	open_notepad()

def main():
	url = input("Enter your coded string here: ")
	decode_url_handling(url)
	recode_url_handling()

main()