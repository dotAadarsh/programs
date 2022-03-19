public class DyanamicArray {
    private int array[];
    private int count;
    private int size;

    public DyanamicArray() {
        array = new int[1];
        count = 0;
        size = 1;
    }

    public void add(int element) {
        resize();
        array[count] = element;
        count++;
        
    }
    
    public void addAt(int index, int data) 
    { 
        resize();  
        for (int j = count - 1; j >= index; j--) 
        { 
          // shifting all element from right from given index 
          array[j + 1] = array[j]; 
        } 
    
        // insert data at given index 
        array[index] = data; 
        count++; 
    }

    private void resize() {
    }
}
