public class ScreenB {
  public static void main(String[] args) {
    String studioName = "b studio";
    int sid = 2;
    char sRow = 'A';
    char eRow = 'O';
    int sCol = 1;
    int eCol = 23;

    System.out.println("use mtra;");
    System.out.format( "alter table seat auto_increment=%d;\n", (sid-1)*1000+1);
    for ( int r = sRow; r <= eRow; r++ ) {
      for ( int c = sCol; c <= eCol; c++ ) {
        double x = 2.0*(c - (eCol + sCol)/2.0);
        double y = 2.0*(r - sRow)+1;
        double z = 1.0*(r - sRow);
        if (r == 'A') {
          if ( c < 3 || c > 17) {
            continue;
          }
          x += 1;
        }
        else if ( r >= 'B' && r <= 'D') {
          if ( c < 3 ) {
            x -= 2;
          }
          else if ( c < 21 ) {
            x += 1;
          }
          else if ( c < 23 ) {
            x += 4;
          }
          else {
            continue;
          }
        }
        else {
          if ( c < 5 ) {
            x -= 2;
          }
          else if ( c > 19 ) {
            x += 2;
          }
          if ( r == 'M' && c >= 9 && c <= 15) {
            continue;
          }
          if ( r == 'N' && c >= 8 && c <= 16) {
            continue;
          }
          if ( r == 'O' && c >= 5 && c <= 19) {
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
