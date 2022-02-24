//To inherit from a class, use the extends keyword.

class ArtistInheritance {
    protected String Artist = "Olivia Rodrigo";

    public static void total() {
        System.out.println("2 album");
    }
}

class Song extends ArtistInheritance {
    private String albumName = "Sour";

    public static void main(String[] args) {
        Song myfav = new Song();
        Song.total();
        System.out.println(myfav.Artist + myfav.albumName); 
        
    }
}


