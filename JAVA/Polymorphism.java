
class Spotify {
        public void album() {
            System.out.println("The top songs are");
        } 
    }

class Artist extends Spotify {
        public void album() {
            System.out.println("The top artist are");
        }
    }

class Polymorphism {
    public static void main(String[] args) {
        Spotify myalbum = new Spotify();
        Spotify myartistname = new Artist();
        myalbum.album();
        myartistname.album();
    }
}   