from subprocess import *


def execute_java(*args):
    process = Popen(['java', '-jar'] + list(args), stdout=PIPE, stderr=PIPE)
    result = []
    while process.poll() is None:
        line = process.stdout.readline()
        if line != '' and line.endswith('\n'):
            result.append(line[:-1])
    return result
