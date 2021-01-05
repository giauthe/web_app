TMTimport os
import sys
import datetime
import shutil
import traceback
import base64
import zipfile
import json
import requests

class TMTUtil:
    #instance = None

    TEST_PASSED = "passed"
    TEST_FAILED = "failed"
    TEST_NOT_READY = "not_ready"
    TEST_NOT_TESTED = "not_tested"

    def __init__(self, host, port, username, password, proxy=None):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.proxy = proxy
        #self.proxy = "127.0.0.1:8888"

    @staticmethod
    def new_instance(host, port, username, password, proxy=None):
        instance = TMTUtil(host, port)
        return instance

    @staticmethod
    def post_test_result_to_tmt(instance, id, test_case_code, result, remark):
        try:
            msg = {
                "test_case_results" : [
                    {
                        "test_case_code" : test_case_code,
                        "result" : result,
                        "remark" : remark,
                    }
                ]
            }
            auth = base64.b64encode(instance.username + ":" + instance.password)
            headers = { "Content-Type" : "application/json", "Authorization" : auth }
            response = send_https_post_request(instance.host, instance.port, "/remote/update_latest_test_result/"+str(id), json.dumps(msg), instance.proxy, **headers)
            #print response
            j = json.loads(response)
            if j["result"] == "ok":
                return True
        except:
            traceback.print_exc(file=sys.stdout)
        return False

    @staticmethod
    def post_all_test_result_to_tmt(instance, id, server, is_completed, report_path, result_path):
        try:
            # create zip file
            # create temp working folder
            temp_dir = "output"
            zip_file = 'output.zip'
            report_dir = os.path.join(temp_dir, "report")
            result_dir = os.path.join(temp_dir, "result")
            shutil.rmtree(temp_dir, True)
            if os.path.exists(zip_file):
                os.remove(zip_file)
            os.mkdir(temp_dir)
            # copy files
            if report_path is not None:
                shutil.copytree(report_path, report_dir)
            if result_path is not None:
                shutil.copytree(result_path, result_dir)
            # create done.log
            done_file = os.path.join(temp_dir, "done.log")
            f = open(done_file, 'w')
            f.write(str(datetime.datetime.now()) + "\n")
            f.close()
            # zip all
            zipf = zipfile.ZipFile(zip_file, 'w')
            for root, dirs, files in os.walk(temp_dir):
                for file in files:
                    zipf.write(os.path.join(root, file))
            zipf.close()
            # convert to base64
            with open(zip_file, mode='rb') as file: # b is important -> binary
                fileContent = file.read()
            content = base64.b64encode(fileContent)

            # create request message
            msg = {
                    "server" : server,
                    "complete" : is_completed,
                    "output" : content,
            }
            auth = base64.b64encode(instance.username + ":" + instance.password)
            headers = { "Content-Type" : "application/json", "Authorization" : auth }
            #response = send_https_post_request(instance.host, instance.port, "/remote/mark_complete_latest_test_result/"+str(id), json.dumps(msg), instance.proxy, **headers)
            url = "https://"+instance.host+":"+str(instance.port)+"/remote/mark_complete_latest_test_result/"+str(id)
            print url
            response = requests.post(url,verify=False, headers = headers, data = json.dumps(msg))
            print "Reponse: status=%d message=%s" % (response.status_code, response.text)
            # remove temp files
            shutil.rmtree(temp_dir, True)
            if os.path.exists(zip_file):
                os.remove(zip_file)
                # check result
            j = json.loads(response.text)
            if j["result"] == "ok":
                return True
        except:
            traceback.print_exc(file=sys.stdout)
        return False




if len(sys.argv)>1 and len(sys.argv)<10:
    print "usage: TMTUtil.py [host] [port] [username] [password] [test_execution_id] [client_name] [is_completed] [report_path] [result_path]"
    print "example: TMTUtil.py ascendtmt.tmn-dev.net 443 morakot Welcome1 280 myclient True  \"D:/Git/te53_r110_tr1463/report\" \"D:/Git/te53_r110_tr1463/result\""
elif len(sys.argv)==10:
    host = sys.argv[1]
    port = sys.argv[2]
    user = sys.argv[3]
    pwd =  sys.argv[4]
    id = int(sys.argv[5])
    server =  sys.argv[6]
    complete = sys.argv[7] in ["true", "True", "TRUE"]
    report_path = sys.argv[8]
    result_path = sys.argv[9]
    # adjust
    if report_path.lower()=="none" or len(report_path)==0:
        report_path = None
    if result_path.lower()=="none" or len(result_path)==0:
        result_path = None
    # do post
    tmt = TMTUtil(host, int(port), user, pwd, None)
    TMTUtil.post_all_test_result_to_tmt(tmt, id, server, complete, report_path, result_path)

#tmt = TMTUtil("ascendtmt.tmn-dev.com", 443, "morakot", "Welcome1", "127.0.0.1:8888")
#tmt = TMTUtil("127.0.0.1", 3000, "admin", "admin1234", "127.0.0.1:8888")
#print TMTUtil.post_test_result_to_tmt(tmt, 53, "TC_BPAY_01334", TMTUtil.TEST_FAILED, "done")
#print TMTUtil.post_all_test_result_to_tmt(tmt, 280, "127.0.0.1", True, "D:/Git/tmt/inwarmy-testmgt/public/tasks/te53_r110_tr1463/1.1.1.1/report", "D:/Git/tmt/inwarmy-testmgt/public/tasks/te53_r110_tr1463/1.1.1.1/result")
# ascendtmt.tmn-dev.com 443 morakot Welcome1 280 myclient True  D:/Git/tmt/inwarmy-testmgt/public/tasks/te53_r110_tr1463/1.1.1.1/report D:/Git/tmt/inwarmy-testmgt/public/tasks/te53_r110_tr1463/1.1.1.1/result

#test_case_results
#send_http_post_request
