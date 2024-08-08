import pickle
from typing import List, Dict
from src.data_generator.task import Task

def ch_dat(job, machine, data_file_path):
    num = 1
    with open(data_file_path, 'rb') as f:
        data = pickle.load(f)
        for d in data:
            wdat_file_path = str(num)+'.dat'
            ProcessTime = []
            selected_machine = []
            proctime = []
            selmachine = []
            deadline = []
            D_line = []
            
            for pt in d:
                proctime.append(int(str(pt.runtime)))
                if len(proctime) ==10:
                    ProcessTime.append([0] + list(proctime))
                    proctime = []     
                selmachine.append(int(str(pt.selected_machine)))
                if len(selmachine)==10:
                    selected_machine.append([0] + [x+1 for x in selmachine])
                    selmachine=[]
                    D_line.append(int(str(pt.deadline)))
                    if len(selected_machine) == len(deadline) +1:
                        deadline.append(list(D_line))
                        D_line = []

            deadline_flat = [elem for sublist in deadline for elem in sublist]        
            with open(wdat_file_path, 'w') as file:
                file.writelines(['Machine =', str(machine), ';\n'])
                file.writelines(['Job =', str(job), ';\n'])
                file.writelines(['Selected_machine =', str(selected_machine), ';\n'])
                file.writelines(['ProcessTime =', str(ProcessTime),';\n'])
                file.writelines(['Deadline =', str(deadline_flat), ';'])

            num+=1
        return
    
ch_dat(100,10,'config_job100_task10_tools0.pkl')
