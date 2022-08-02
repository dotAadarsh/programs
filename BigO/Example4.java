public class Example4 {
    
    public static void printUnorderedPairs(int[] arrA, int[] arrB) {
        for(int i = 0; i<arrA.length; i++) {
            for(int j=0; j<arrB.length; j++) {
                if(arrA[i]<arrB[j]) {
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

//  if statement within j's for loop is 0(1)
// For each element of arr A, the inner for loop goes through b iterations, where b = arrB. length. lf a = arrayA.length,then the runtime is O(ab).