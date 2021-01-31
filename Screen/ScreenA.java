public class ScreenA {
  public static void main(String[] args) {
    String studioName = "a studio";
    int sid = 1;
    char sRow = 'B';
    char eRow = 'S';
    int sCol = 1;
    int eCol = 22;

    System.out.println("use mtra;");
//    System.out.format( "alter table seat auto_increment=%d;\n", (sid-1)*1000+1);
    for ( int r = sRow; r <= eRow; r++ ) {
      for ( int c = sCol; c <= eCol; c++ ) {
        double x = 2.0*(c - (eCol + sCol)/2.0);
        double y = 2.0*(r - sRow)+1;
        double z = 1.0*(r - sRow);
        if ( r <= 'R' ) {
          if ( c < 5 ) {
            x -= 2;
          }
          else if ( c > 18 ) {
            x += 2;
          }
          if ( r == 'B' && (c < 5 || c > 18)) {
            continue;
          }
        }
        else {
          if ( c <= 8 ) {
            x += 4;
          }
          else if ( c <= 16 ) {
            x += 8;
          }
          else {
            continue;
          }
        }
        System.out.format("insert into seat"
         +"(`screen_id`, `row`, `column`, `pos_x`, `pos_y`, `pos_z`)"
         +" values (%d, \"%c\", %2d, %3.0f, %3.0f, %3.0f);\n",
         sid, r, c, x, y, z);
      }
    }
  }
}
