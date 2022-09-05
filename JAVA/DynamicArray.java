public class DynamicArray {
    private int array[];
    private int count;
    private int size;

    public DynamicArray() {
        array = new int[1];
        count = 0;
        size = 1;
    }

    public void add(int data) {
        if(count == size) {
            growsize();
        }
        array[count] = data;
        count++;
    }

    public static void main(String[] args) {
        DynamicArray da = new DynamicArray();

        da.add(1);
        da.add(2);
        da.add(3);
        da.add(4);
        da.add(5);
        da.add(6);
        da.add(7);
        da.add(8);
        da.add(9);

        System.out.println("Elements of array");
        for(int i = 0;i<da.size;i++) {
            System.out.println(da.array[i] + " ");
        }


    }
}