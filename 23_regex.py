import re

foo = "Do I eat them.On a plane. Do i eat them.On a train."

result = re.split("\.", foo)
test=""
for i in result:
        if len(i)>0:
            test += i + ". "


print(test)
