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
                if len(proctime) ==5:
                    ProcessTime.append(list(proctime))
                    proctime = []
                    
                selmachine.append(int(str(pt.selected_machine)))
                if len(selmachine)==5:
                    selected_machine.append(list(selmachine))
                    selmachine=[]
   
            with open(wdat_file_path, 'w') as file:
                file.writelines(['Job =', str(job), ';\n'])
                file.writelines(['Machine =', str(machine), ';\n'])
                file.writelines(['Selected_machine =', str(selected_machine), ';\n'])
                file.writelines(['ProcessTime =', str(ProcessTime),';\n'])


            num+=1
        print(len(selected_machine))
        print(len(ProcessTime))
        return

ch_dat(50,5,'config_job50_task5_tools0.pkl')
