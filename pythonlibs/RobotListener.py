import xml.etree.ElementTree as ET
import os
import xml.dom.minidom as minidom

class RobotListener:

    ROBOT_LISTENER_API_VERSION = 2

    def to_boolean(self, str):
        return str.lower() in ("yes", "true", "t", "1")

    def __init__(self, output_dir, keep_fail_data='False', use_pabot='False', pretty_xml='False'):
        self.output_dir = output_dir
        self.keep_fail_data = self.to_boolean(keep_fail_data)
        self.use_pabot = self.to_boolean(use_pabot)
        self.pretty_xml = self.to_boolean(pretty_xml)
        self.robot = ET.Element('robot')
        self.stack = [self.robot]

    def start_suite(self, name, attrs):
        suite = ET.SubElement(self.stack[-1], 'suite')
        suite.set('id', attrs['id'])
        suite.set('name', name)
        self.stack.append(suite)
        if self.use_pabot:
            self.suite_long_name = attrs['longname']

    def start_test(self, name, attrs):
        test = ET.SubElement(self.stack[-1], 'test')
        test.set('id', attrs['id'])
        test.set('name', name)
        self.stack.append(test)

    def start_keyword(self, name, attrs):
        kw = ET.SubElement(self.stack[-1], 'kw')
        type = attrs['type'].lower()
        if 'setup' in type:
            kw.set('type', 'setup')
        elif 'teardown' in type:
            kw.set('type', 'teardown')
        kw.set('name', name)
        if self.keep_fail_data:
            args = attrs['args']
            if len(args) > 0:
                arguments = ET.SubElement(kw, 'arguments')
                for a in args:
                    arg = ET.SubElement(arguments, 'arg')
                    arg.text = a
        self.stack.append(kw)

    def log_message(self, message):
        if self.keep_fail_data:
            kw = self.stack[-1]
            msg = ET.SubElement(kw, 'msg')
            msg.set('level', message['level'])
            msg.set('timestamp', message['timestamp'])
            msg.text = message['message']

    def end_keyword(self, name, attrs):
        kw = self.stack.pop()
        status = ET.SubElement(kw, 'status')
        status.set('status', attrs['status'])
        status.set('starttime', attrs['starttime'])
        status.set('endtime', attrs['endtime'])
        if self.keep_fail_data and attrs['status'] == 'PASS':
            childs = list(kw.findall('msg'))
            for child in childs:
                kw.remove(child)
            childs = list(kw.findall('arguments'))
            for child in childs:
                kw.remove(child)
            childs = list(kw.findall('kw'))
            for child in childs:
                kw.remove(child)

    def end_test(self, name, attrs):
        test = self.stack.pop()
        status = ET.SubElement(test, 'status')
        status.set('status', attrs['status'])
        status.set('starttime', attrs['starttime'])
        status.set('endtime', attrs['endtime'])

    def end_suite(self, name, attrs):
        suite = self.stack.pop()
        status = ET.SubElement(suite, 'status')
        status.set('status', attrs['status'])
        status.set('starttime', attrs['starttime'])
        status.set('endtime', attrs['endtime'])

    def close(self):
        data = ET.tostring(self.robot)
        if self.pretty_xml:
            data = minidom.parseString(data).toprettyxml(indent="  ")
        if self.use_pabot:
            path = os.path.join(self.output_dir,'pabot_results',self.suite_long_name,'output.xml')
        else:
            path = os.path.join(self.output_dir,'output.xml')
        outfile = open(path, "w+")
        outfile.write(data)
        outfile.close()