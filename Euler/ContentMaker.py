import os

template = """
<tr class="problem">
	<td class="id"><a href="https://projecteuler.net/problem=%s" target="_blank">%s</a></td>
	<td class="problemname">%s</td>
	<td class="time">%s</td>
</tr>
<tr>
	<td class="code" colspan="3">
		<pre><code class="language-python">%s</code></pre>
	</td>
</tr>"""


content = open("contentMaded.txt","a")

def writing(ida,properid,name,time,code):
	global content
	content.write(template %(properid,ida,name,time,code))

for x in os.listdir("E:\Other\Project Euler All Working"):
	asd = open("E:\Other\Project Euler All Working\\" + x,"r")
	lines = asd.readlines()

	code = ""
	for y in lines[4:]:
		code += y[:-1]
		code += "\n"

	writing(x[:3],int(x[:3]),lines[1][1:],lines[0][1:6],code)