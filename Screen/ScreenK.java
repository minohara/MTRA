public class ScreenK {
  public static void main(String[] args) {
    String studioName = "k studio";
    int sid = 11;
    char sRow = 'A';
    char eRow = 'K';
    int sCol = 1;
    int eCol = 19;

    System.out.println("use mtra;");
    System.out.format( "alter table seat auto_increment=%d;\n", (sid-1)*1000+1);
    for ( int r = sRow; r <= eRow; r++ ) {
      for ( int c = sCol; c <= eCol; c++ ) {
        double x = 2.0*(c - (eCol + sCol)/2.0);
        double y = 2.0*(r - sRow)+1;
        double z = 1.0*(r - sRow);
        switch (r) {
        case 'C':
          if (c < 2 || c > 17) continue;
          x += 1;
          break;
        case 'D': case 'F': case 'H':
          if (c == 19) continue;
          x += 1;
          break;
        case 'A': case 'B': case 'I':
          if (c < 3 || c > 17) continue;
          break;
        case 'J': case 'K':
          if (c < 5 || c > 15) continue;
          break;
        default:
          break;
        }
        System.out.format("insert into seat"
         +"(`screen_id`, `row`, `column`, `pos_x`, `pos_y`, `pos_z`)"
         +" values (%d, \"%c\", %2d, %3.0f, %3.0f, %3.0f);\n",
         sid, r, c, x, y, z);
      }
    }
  }
}
