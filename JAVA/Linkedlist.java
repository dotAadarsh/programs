import java.util.LinkedList;

public class Linkedlist {
    public static void main(String [] args){
        LinkedList<Integer> queue = new LinkedList<Integer>();
        queue.add(10);
        queue.add(20);
        queue.add(30);
        queue.add(40);
        System.out.println(queue);

       // Use addFirst() to add the item to the beginning
      queue.addFirst(0);
      System.out.println(queue);

      // Use addLast() to add the item to the end
      queue.addLast(50);
      System.out.println(queue);

      // Use removeFirst() remove the first item from the list
      queue.removeFirst();
      System.out.println(queue);

      // Use removeLast() remove the last item from the list
      queue.removeLast();
      System.out.println(queue);

      // Use getFirst() to display the first item in the list
      System.out.println(queue.getFirst());

      // Use getLast() to display the last item in the list
      System.out.println(queue.getLast());

    }
    
}
