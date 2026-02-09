import java.util.*;

public class RoundRobin_OdarveRenaire{
	private static Scanner inp = new Scanner(System.in);
	private static int maxProcessIndex = 0;
	
	public static void main(String[] args){
		int n, tq, timer = 0;
		float avgWait = 0, avgTT = 0;
		System.out.print("Enter the quantum time : ");
		tq = inp.nextInt();
		if(tq <= 0){
			System.out.println("Error: Quantum time must be positive!");
			return;
		}
		System.out.print("Enter the number of processes : ");
		n = inp.nextInt();
		if(n <= 0){
			System.out.println("Error: Number of processes must be positive!");
			return;
		}
		int arrival[] = new int[n];
		int burst[] = new int[n];
		int wait[] = new int[n];
		int turn[] = new int[n];
		int queue[] = new int[n];
		int temp_burst[] = new int[n];
		boolean complete[] = new boolean[n];

		for(int i = 0; i < n; i++){
			System.out.print("Enter the arrival time of the process "+ (i+1) +": ");
			arrival[i] = inp.nextInt();
			if(arrival[i] < 0){
				System.out.println("Error: Arrival time cannot be negative!");
				return;
			}
			System.out.print("Enter the burst time of the process "+ (i+1) +": ");
			burst[i] = inp.nextInt();
			if(burst[i] <= 0){
				System.out.println("Error: Burst time must be positive!");
				return;
			}
			temp_burst[i] = burst[i];			
		}
		
		// Sort processes by arrival time
		for(int i = 0; i < n - 1; i++){
			for(int j = 0; j < n - i - 1; j++){
				if(arrival[j] > arrival[j + 1]){
					int temp = arrival[j];
					arrival[j] = arrival[j + 1];
					arrival[j + 1] = temp;
					temp = burst[j];
					burst[j] = burst[j + 1];
					burst[j + 1] = temp;
					temp = temp_burst[j];
					temp_burst[j] = temp_burst[j + 1];
					temp_burst[j + 1] = temp;
				}
			}
		}

		for(int i = 0; i < n; i++){
			complete[i] = false;
			queue[i] = 0;
		}
		while(timer < arrival[0])
			timer++; 
		queue[0] = 1;
		
		while(true){
			boolean flag = true;
			for(int i = 0; i < n; i++){
				if(temp_burst[i] != 0){
					flag = false;
					break;
				}
			}
			if(flag)
				break;

			for(int i = 0; (i < n) && (queue[i] != 0); i++){
				int ctr = 0;
				while((ctr < tq) && (temp_burst[queue[0]-1] > 0)){
					temp_burst[queue[0]-1] -= 1;
					timer += 1;
					ctr++;
					checkNewArrival(timer, arrival, n, queue);
				}
				if((temp_burst[queue[0]-1] == 0) && (complete[queue[0]-1] == false)){
					turn[queue[0]-1] = timer;
					complete[queue[0]-1] = true;
				}
				
				boolean idle = true;
				if(queue[n-1] == 0){
					for(int k = 0; k < n && queue[k] != 0; k++){
						if(complete[queue[k]-1] == false){
							idle = false;
						}
					}
				}
				else
					idle = false;

				if(idle){
					timer++;
					checkNewArrival(timer, arrival, n, queue);
				}
			
				queueMaintainence(queue,n);
			}
		}

		for(int i = 0; i < n; i++){
			turn[i] = turn[i] - arrival[i];
			wait[i] = turn[i] - burst[i];
		}

		System.out.print("\nProgram No.\tArrival Time\tBurst Time\tWait Time\tTurnAround Time"
						+ "\n");
		for(int i = 0; i < n; i++){
			System.out.print(i+1+"\t\t"+arrival[i]+"\t\t"+burst[i]
							+"\t\t"+wait[i]+"\t\t"+turn[i]+ "\n");
		}
		for(int i =0; i< n; i++){
			avgWait += wait[i];
			avgTT += turn[i]; 
		}
		System.out.print("\nAverage Wait time : "+(avgWait/n)
						+"\nAverage Turn Around Time : "+(avgTT/n));
	}
	public static void queueUpdation(int queue[],int timer,int arrival[],int n){
		int zeroIndex = -1;
		for(int i = 0; i < n; i++){
			if(queue[i] == 0){
				zeroIndex = i;
				break;
			}
		}
		if(zeroIndex == -1)
			return;
		queue[zeroIndex] = maxProcessIndex + 1;
	}

	public static void checkNewArrival(int timer, int arrival[], int n, int queue[]){
		if(timer <= arrival[n-1]){
			boolean newArrival = false;
			for(int j = (maxProcessIndex+1); j < n; j++){
				if(arrival[j] <= timer){
					if(maxProcessIndex < j){
						maxProcessIndex = j;
						newArrival = true;
					}
				}
			}
			if(newArrival)
				queueUpdation(queue,timer,arrival,n);
		}
	}

	public static void queueMaintainence(int queue[], int n){

		for(int i = 0; (i < n-1) && (queue[i+1] != 0) ; i++){
			int temp = queue[i];
			queue[i] = queue[i+1];
			queue[i+1] = temp; 
		}
	}
}
