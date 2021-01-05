
def convert_list_to_string_without_quote(list):
    str_list=','.join(str(x) for x in list)
    return str_list
def convert_list_to_string_with_quote(list):
    str_list='"'
    str_list=str_list+'","'.join(str(x) for x in list)
    str_list=str_list+'"'
    return str_list

