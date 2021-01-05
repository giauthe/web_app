import json
import requests
def get_all_values_of_specific_key (json_data,key):

    print("before ----" + str(json_data))
    json_data_string = str(json_data).replace("u'", "'").encode('unicode-escape')
    json_data_string = str(json_data_string).replace("'","\"")  # provided JSON content doesn't contains single quotes as part of values.
    json_data_string = str(json_data_string).replace("False", "false")
    json_data_string = str(json_data_string).replace("True", "true")
    json_data_string = str(json_data_string).replace("None", "null")
    print(json_data_string)
    data = json.loads(json_data_string)
    # data = json.loads(json_data)
    names = map(lambda datum: datum[key], data)
    return names

def create_mock_to_prepare_data(port,name,menu,mb_host,mb_port):
    data = {"protocol":"http","port":port,"name":name,"stubs":[{"responses":[{"inject":"function (request, state, logger) { \n var data = JSON.parse(request.body); \n var scope = data['scope']; \n if (typeof state.requests === 'undefined') { \n state.requests = {}; \n } \n state.requests[scope] = { headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ 'data': data}) };\n return { headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ 'status': { 'code':'success', 'message':'Success' }, 'data': data }) }; \n}"}],"predicates":[{"equals":{"method":"POST","path":"/"+menu}}]},{"responses":[{"inject":"function (request, state, logger) { \n var scope = request.path.substr(request.path.lastIndexOf('/') + 1); \n if (typeof state.requests === 'undefined') { \n state.requests = {}; \n } \n if (state.requests[scope]) { \n logger.info('found prepare data for scope ' + scope + '%s'); \n return state.requests[scope]; \n } \n return { headers: { 'Content-Type': 'application/json' }, \n  body: JSON.stringify({ 'data' : 'not found' }) }; \n }"}],"predicates":[{"equals":{"method":"GET"}},{"startsWith":{"path":"/"+menu}}]}]}
    r = requests.post(mb_host+':'+mb_port+'/imposters', data=json.dumps(data))
    print(r.status_code, r.reason,r.text)
    return r



if __name__ == '__main__':
    # json_data_string = "[{ 'name' : 'aaa', 'contact' : '123' }]"
    # json_data_string = "[{'created_timestamp': '2018-08-20T03:41:21Z', 'currency': 'USD', 'description': 'robot_service_description','is_deleted': false, 'last_updated_timestamp': '2018-08-20T03:41:21Z', 'service_group_id': 1300,'service_id': 1497, 'service_name': 'robot_evnjmehOQo', 'status': 1}]"
    # json_data_string="[{'created_timestamp': '2018-08-20T04:11:39Z', 'currency': 'USD', 'description': '5LF6N4Z4VO2SOK2RSA5EZ4V7ACRWI63T26VQKNPSCNJWPQZSUH', 'is_deleted': False, 'last_updated_timestamp': '2018-08-20T04:11:39Z', 'service_group_id': 1790, 'service_id': 1979, 'service_name': 'EEJ4CRQ34IY6SVQAPTTIK4QINAZ6NEKDIRD7UO7XCQM2ZXCJVU', 'status': 1}]"
    # json_data_string = "[{'created_timestamp': '2018-08-20T03:41:21Z', 'currency': 'USD'}]"
    # json_data_string = "[{'created_timestamp': '2018-08-20T03:41:21Z', 'currency': 123}]"
    # print   "aaaa " + str(get_all_values_of_specific_key(json_data_string,"service_name"))
    create_mock_to_prepare_data()

def build_json (json_data):

    print("before ----" + str(json_data))
    json_data_string = str(json_data).replace("u'", "'").encode('unicode-escape')
    json_data_string = str(json_data_string).replace("'","\"")  # provided JSON content doesn't contains single quotes as part of values.
    json_data_string = str(json_data_string).replace("False", "false")
    json_data_string = str(json_data_string).replace("True", "true")
    return json_data_string

