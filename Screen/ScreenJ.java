public class ScreenJ {
  public static void main(String[] args) {
    String studioName = "j studio";
    int sid = 10;
    char sRow = 'A';
    char eRow = 'F';
    int sCol = 1;
    int eCol = 15;

    System.out.println("use mtra;");
    System.out.format( "alter table seat auto_increment=%d;\n", (sid-1)*1000+1);
    for ( int r = sRow; r <= eRow; r++ ) {
      for ( int c = sCol; c <= eCol; c++ ) {
        double x = 2.0*(c - (eCol + sCol)/2.0);
        double y = 2.0*(r - sRow)+1;
        double z = 1.0*(r - sRow);
        switch (r) {
        case 'A':
          if (c < 3 || c > 12) continue;
          x += 1;
          break;
        case 'B': case 'D':
          if (c == 15) continue;
          x += 1;
          break;
        case 'F':
          if (c < 4 || c > 12) continue;
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
