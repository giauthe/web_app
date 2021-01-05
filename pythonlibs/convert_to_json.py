from unflatten import unflatten

def convert_to_int_param(arg1):
    if arg1 != 'param_not_used':
        return int(arg1)
    else:
        return 'param_not_used'

def create_json_data_for_user_ref_object(user_ref_type, user_ref_value):
    if user_ref_type != 'param_not_used':
        return  '\"ref\":{\"type\":\"'+user_ref_type+'\",\"value\":\"'+user_ref_value+'"}'
    else:
        return ''

def create_json_data_for_user_id_object(user_id, user_type):
    if str(user_id) != 'param_not_used':
        return  '"user_id":"'+str(user_id)+'","user_type":"'+user_type+'"'
    else:
        return ''

def create_json_data_for_user_type_object(key_name, user_type_id, user_type_name):
    if user_type_id != 'param_not_used' or user_type_name != 'param_not_used':
        return  '\"'+key_name+'\":{\"id\":\"'+user_type_id+'\",\"name\":\"'+user_type_name+'"},'
    else:
        return ''

def get_nested_dict(dictionary):
    nested_dict = unflatten(dictionary)

    return nested_dict