public class Example5 {
    
    public static void printUnorderedPairs(int[] arrA, int[] arrB) {
        for(int i = 0; i<arrA.length; i++) {
            for(int j=0; j<arrB.length; j++) {
                for(int k =0;k<100000;k++) {
                    System.out.println(arrA[i] + "," + arrB[j]);
                }
            }
        }
    }
    
    public static void main(String[] args) {
        int arrA[] = {1,2,3,4,5};
        int arrB[] = {3,5,7,9,11};
        printUnorderedPairs(arrA, arrB);
    
    }
}

// 100,000 units of work is still constant, so the runtime is 0( ab)