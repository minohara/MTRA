public class ScreenC {
  public static void main(String[] args) {
    String studioName = "c studio";
    int sid = 3;
    char sRow = 'A';
    char eRow = 'N';
    int sCol = 1;
    int eCol = 18;

    System.out.println("use mtra;");
    System.out.format( "alter table seat auto_increment=%d;\n", (sid-1)*1000+1);
    for ( int r = sRow; r <= eRow; r++ ) {
      for ( int c = sCol; c <= eCol; c++ ) {
        double x = 2.0*(c - (eCol + sCol)/2.0);
        double y = 2.0*(r - sRow)+1;
        double z = 1.0*(r - sRow);
        if (r <= 'K' ) {
          if ( c < 3 || c > 16) {
            continue;
          }
          else if ( c > 4 && c < 13 ){
            x += 2;
          }
          else if ( c > 12 ){
            x += 4;
          }
          if ( r == 'A' && (c < 5 || c > 12) ) {
            continue;
          }
          else if ( r == 'B' && c > 12 ) {
            continue;
          }
        }
        else {
          if ( r == 'M' && c >= 6 && c <= 13) {
            continue;
          }
          if ( r == 'N' && c >= 5 && c <= 14) {
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
