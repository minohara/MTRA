public class ScreenI {
  public static void main(String[] args) {
    String studioName = "i studio";
    int sid = 9;
    char sRow = 'A';
    char eRow = 'I';
    int sCol = 1;
    int eCol = 20;

    System.out.println("use mtra;");
    System.out.format( "alter table seat auto_increment=%d;\n", (sid-1)*1000+1);
    for ( int r = sRow; r <= eRow; r++ ) {
      for ( int c = sCol; c <= eCol; c++ ) {
        double x = 2.0*(c - (eCol + sCol)/2.0);
        double y = 2.0*(r - sRow)+1;
        double z = 1.0*(r - sRow);
        switch (r) {
        case 'B': case 'D': case 'F': case 'H':
          if (c == 20) continue;
          x += 1;
          break;
        case 'I':
          if (c < 4 || c > 17) continue;
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
