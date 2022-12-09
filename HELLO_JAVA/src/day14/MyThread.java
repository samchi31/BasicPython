package day14;

public class MyThread {
	public static void main(String[] args) {
		new Thread(new Runnable() {
			public void run() {
				for(int i=1;i<=100000;i++) {
					System.out.print(i);
					if(i%100==0) {
						System.out.println();
					}
				}
			}
		}).start();
	}
}
