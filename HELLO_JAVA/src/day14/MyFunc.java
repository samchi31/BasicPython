package day14;

public class MyFunc {
	public static void showNum() {
		for(int i=1;i<=100000;i++) {
			System.out.print(i);
			if(i%100==0) {
				System.out.println();
			}
		}
	}
	public static void showAscii() {
		for(char c='가';c<='힣';c++) {
			System.out.print(c);
			if(c%100==0) {
				System.out.println();
			}
		}
	}
	public static void main(String[] args) {
		showNum();
	}
}
