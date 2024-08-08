import xml.etree.ElementTree as ET

with open('85.dat','r') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if line.startswith('Job'):
        Job = int(lines[0].split("=")[1].strip().rstrip(';'))
        
    elif line.startswith('Machine'):
        Machine = int(lines[1].split("=")[1].strip().rstrip(';'))
    
    elif line.startswith('Selected_machine'):
        Selected_machine = [[int(x) for x in row.replace('[','').replace(']','').split(',')] 
                            for row in line.split('=')[1].split(';')[0].split('], [')]
    elif line.startswith('ProcessTime'):
        ProcessTime = [[int(x) for x in row.replace('[','').replace(']','').split(',')] 
                       for row in line.split('=')[1].split(';')[0].split('], [')]
        break

print(Job)
print(Machine)

root = ET.Element("data")

for i in range(1,Job+1):
    job = ET.SubElement(root, 'job', {'id': str(i)})
    
    for j in range(Machine):
        process = ET.SubElement(job, 'process', {'id': str(j+1)})
        
        for k in range(Machine):
            time = str(ProcessTime[i-1][j]) if k == Selected_machine[i-1][j] else '-1'
            machine = ET.SubElement(process, 'machine', {'id': str(k+1), 'time': time})

with open('job50_5.xml', 'w') as g:
    g.write('<?xml version="1.0" encoding="utf-8"?>\n')
    xml_str = ET.tostring(root, encoding="unicode")
    xml_str = xml_str.replace("><", ">\n <")
    g.write(xml_str)