import re
l = ['color: #abcdef #abc #qwer', '#123456']
[print(j) for i in l for j in re.findall('[^#]#[a-f0-9]{3,6}', i, re.I)]
