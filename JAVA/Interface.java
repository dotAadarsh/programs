interface Spotify {
    public void album();
    public void artist();
}

class Artist implements Spotify {
    public void album() {
        System.out.println("Sour");
    }

    public void artist() {
        System.out.println("Olivia");
    }
}

public class Interface {
    public static void main (String[] args) {
        Artist myartist = new Artist();
        myartist.album();
        myartist.artist();
    }
}
