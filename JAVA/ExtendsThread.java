public class ExtendsThread extends Thread{
    public static void main(String[] args) {
        ExtendsThread thread = new ExtendsThread();
        thread.start();
        System.out.println("Outside the thread");
    }
    
    public void run() {
        System.out.println("This runs inside thread");
    }
}
