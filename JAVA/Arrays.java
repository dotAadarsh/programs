//Arrays are used to store multiple values in a single variable, instead of declaring separate variables for each value.

public class Arrays {
    public static void main(String[] args){
       
        String[] tv_series = {"Better Call Saul", "Breaking Bad", "Narcos"};
        System.out.println(tv_series[0]);

        int[] ranking = {1,2,3};
        System.out.println(ranking[0]);
        
        System.out.println(tv_series.length);

        for(String any : tv_series) {
            System.out.println(any);
        }   

        //Multidimensional Arrays
        int[][] numbers = {{1,2,3}, {4,5,6} };

        //To access the elements of the array, specify two indexes: one for the array, and one for the element inside that array
        int blah = numbers[1][2];
        System.out.println(blah);

        //to get the elements 
        for(int i=0;i<numbers.length;i++) {
            for(int j=0; j<numbers[i].length;j++) {
                System.out.println(numbers[i][j]);
            }
        }

        

    }
}
