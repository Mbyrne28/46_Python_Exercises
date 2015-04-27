import re

def reg_tester(pattern, string):

    print(pattern, string, re.findall(pattern, string))
    match = re.search(pattern, string)
    if match:
        print(format(match.group(1)))




reg_tester(".[e].", "hello w.orld.")
reg_tester(".[\.].", "hello world.")
reg_tester(".[\.].", "hello w.orld.")
reg_tester(".(\.)", "hello world.")
reg_tester("\w", "hello world.")
reg_tester("w", "hello world.")
reg_tester("[\.][a-z]", "hello w.orld.")
