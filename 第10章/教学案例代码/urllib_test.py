from urllib import request, parse
url = "http://httpbin.org/get"
params = {
    "name1": "value1",
    "name2": "value2"
}
query_str = parse.urlencode(params)
u = request.urlopen(url, query_str.encode("utf-8"))  # POST
# u = request.urlopen("%s?%s" % (url, params))  # GET
resp = u.read()
print(resp)