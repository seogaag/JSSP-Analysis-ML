job_n = 50
task_n = 5

data_num = "Data 85"
num = "5"
data_file_finishtime = "G:\\내 드라이브\\Job-Shop-Scheduling-Genetic-Algorithm-master\\Tardiness\\finishtime_j"+str(job_n)+"_dat"+num +".txt"
data_file_deadline = "G:\\내 드라이브\\Job-Shop-Scheduling-Genetic-Algorithm-master\\Tardiness\\deadline_j"+str(job_n)+"_t0.txt"

# finishtime 불러오기
def load_finish(data_file_finishtime):
    with open(data_file_finishtime,'r') as f:
        lines = f.readlines()
    finishtimes = []
    fintime = []
    for i, line in enumerate(lines):
        fin_d = line.split(" ")
        for f in fin_d:
            if f != "\n":
                fintime.append(int(f))
            if len(fintime)==task_n: # task 수
                finishtimes.append(fintime)
                fintime = []
    print("Finish: ", finishtimes)
    return finishtimes

# deadline 불러오기
def load_deadline(data_file_deadline, data_num):
    with open(data_file_deadline,'r') as f:
        lines = f.readlines()

    for i, line in enumerate(lines):
        if line.startswith(data_num):
            start_index = lines[i+1].index("[[")
            end_index = lines[i+1].index("]]", start_index) + 2
            list_str = lines[i+1][start_index:end_index]

            deadline = eval(list_str)
            print(deadline)
    return deadline

def cal_tardiness(fintime_list, deadline_list):
    tardiness = 0
    with open('G:\\내 드라이브\\Job-Shop-Scheduling-Genetic-Algorithm-master\\Tardiness\\tardiness_job'+str(job_n)+'_t0_dat'+num+'.txt','w') as f:

        for i in range(job_n):
            for j in range(task_n):
                if int(fintime_list[i][j]) > int(deadline_list[i][j]):
                    tardiness += int(fintime_list[i][j]) - int(deadline_list[i][j])
                    print("i: ", i, ", j: ",j, ", tardiness = ", int(fintime_list[i][j])," - ",int(deadline_list[i][j]))
                    f.writelines(["i: ", str(i), ", j: ",str(j), ", tardiness = ", str(int(fintime_list[i][j]))," - ",str(int(deadline_list[i][j]))," = ", str(int(fintime_list[i][j])-int(deadline_list[i][j])),"\n"])
        print(tardiness)

    
        f.writelines(["\nTardiness = ",str(tardiness),"\n"])
        


fintime_list = load_finish(data_file_finishtime=data_file_finishtime)
deadline_list = load_deadline(data_file_deadline = data_file_deadline, data_num=data_num)
cal_tardiness(fintime_list=fintime_list, deadline_list=deadline_list)