//-- set
 int Job = ...; //�۾���
 int Machine = ...; //���� ==> ��� job�� ���� ��ŭ�� operations�� ����  ==> ���� job�� operation�� ������ ������ formulation�� �ٽ� �ؾ� ��
  
 range J = 1..Job; //�۾� �ε��� ����
 range M = 0..Machine;//��� �ε��� ����  // 0�� dummy machine��
 
  //-- parameter
 int Selected_machine[J][M] = ...;  // job�� �� operation�� ��� machine���� �����Ǵ����� ��Ÿ��, ���� job j�� m��° operation�� �������� ���� ���, mch[j][m]=0���� ��
 float ProcessTime[J][M] = ...;  // job�� �� operation�� �ش� machine������ �����ð�, ���� job j�� m��° opeartion�� �������� ���� ��� p[j][m]=0���� ��
 float Deadline[J] = ...;    // �� job�� due date
 
//-- decision variable 
 dvar float+ s[J][M];   // �� operation�� �۾� ���� ����  s[j][m]: job j�� ��� m������ �۾� ���� ���� (����: job j�� m��° opeartion�� ���۽����� �ƴ�)
 dvar float+ f[J][M];   // �� operation�� �۾� ���� ����: job j�� ��� m������ �۾� ���� ����
 dvar float+ tardi[J];  // �� job�� tardiness

 dvar boolean dsj[J][J][M]; // �� operation�� �۾� ������ ����� ��Ÿ���� ��������, ���� job i�� job j���� ��� m���� ���� �����Ǹ� ==> dsj[i][j][m]=1 
 dvar float makespan;
  
//-- Mixed Integer Linear Program
 //minimize sum(j in J)tardi[j];  // �� �������� ��� �ּ�ȭ
 minimize makespan;  // Makespan �ּ�ȭ

 subject to
 {            
   c1: // opearion�� �۾� ���� ���� ���  
     forall(j in J, k in M)
       f[j][Selected_machine[j][k]] == s[j][Selected_machine[j][k]] + ProcessTime[j][k];   
   c2: // �� job�� ���� operation�� ���۽����� ���� operation�� ������� ���� ���ų� Ŀ�� ��
     forall(i in J,  h in M : h > 1)
       s[i][Selected_machine[i][h]] >= f[i][Selected_machine[i][h-1]];
   c3: // ���� ��迡���� ���δٸ� �� job�� �� operation ���� �۾� ������ ���� 
     forall(i in J, j in J, k in M:  i < j )
       s[j][k] >= f[i][k] + 10000 * (dsj[i][j][k] - 1);       
   c4: // ���� ��迡���� �� operation ���� �۾� ������ ����
     forall(i in J, j in J, k in M:  i < j )
       s[i][k] >= f[j][k] - 10000 * dsj[i][j][k];       
   
   /*
   c5: // �� job�� tardiness ���
     forall(j in J)
       tardi[j] >=  f[j][Selected_machine[j][Machine]] - Deadline[j];
        
   */
   c5: // makespan ���
     forall(j in J)
       makespan >=  f[j][Selected_machine[j][Machine]];   
   
       
  }     



// ILOG Script for flow control
main {  
 		
	for(var i=3; i<=3; i++)    {    
		
		var source = new IloOplModelSource("jobshop.mod"); // creat source using *.mod
		var def = new IloOplModelDefinition(source); // create model definition
		var opl; 

   		// ������� ����
		var result = new IloOplOutputFile("C:\\Users\\wlsdm\\Desktop\\test\\Result100_" + i + ".txt");
		var result2 = new IloOplOutputFile("C:\\Users\\wlsdm\\Desktop\\test\\Job100_makespan_" + i + ".txt");
		var time;
		var gap;
		var fileName;
		var data;
		var chkindex;
   
		result2.writeln("cplex" + "    " + "time");
  
		chkindex = 0;
		cplex.tilim = 30000;
		cplex.mipemphasis = 1;  // �����ظ� ������ �ð��ȿ� ã�� ������ ���� �����ظ� ã�µ��� ������ ��
				
		fileName = "data/" + i + ".dat";
		writeln("Problem = " + fileName);
		result.writeln("Problem = " + fileName);
				
		time = new Date();
		gap = time.getTime();
		opl = new IloOplModel(def,cplex);  // create model instance
		data= new IloOplDataSource(fileName);
		opl.addDataSource(data);
		opl.generate();
				
		if (cplex.solve()) { 
			writeln("OBJ = " + cplex.getObjValue());  
        	result.writeln("OBJ = " + cplex.getObjValue());
        	result.writeln("starting time = " + "\n" + opl.s);
        	result.writeln("finishing time = " + "\n" + opl.f);
        	chkindex = 1;
      	} 
      	else    {
        	writeln("No solution found.");
        	result.writeln("No solution found.");
      	}
             
        time = new Date(); 
      	gap = time.getTime() - gap;
      
      	writeln("time = " + gap);
      	result.writeln("time = " + gap);
  
      	result.writeln("------------------");

      	if(chkindex ==1) { 
      		result2.writeln(fileName + "	" + cplex.getObjValue() + "	" + gap/1000);
      	}
      	else    {
        	result2.writeln("No solution found.");
        }
      	
    }           
 	
 	result.close();
 	opl.end();
 	data.end();
 	def.end();
 	cplex.end();
 	source.end(); 
}

