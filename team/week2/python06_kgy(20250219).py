import sys
src = sys.argv[1]
dst = sys.argv[2]
f= open(src)
tab_content = f.read()
f.close()

space_content = tab_content.replace("\t", " "*4)
print(space_content)

f = open(dst, 'w')
f.write(space_content)
f.close()
