public class ScreenD {
  public static void main(String[] args) {
    String studioName = "d studio";
    int sid = 4;
    char sRow = 'A';
    char eRow = 'I';
    int sCol = 1;
    int eCol = 23;

    System.out.println("use mtra;");
    System.out.format( "alter table seat auto_increment=%d;\n", (sid-1)*1000+1);
    for ( int r = sRow; r <= eRow; r++ ) {
      for ( int c = sCol; c <= eCol; c++ ) {
        double x = 2.0*(c - (eCol + sCol)/2.0);
        double y = 2.0*(r - sRow)+1;
        double z = 1.0*(r - sRow);
        if (r <= 'G' ) {
          if ( c < 3 || c > 22) {
            continue;
          }
          else if ( c >= 5 && c < 18 ){
            x += 2;
          }
          else if ( c >= 18 ){
            x += 4;
          }
          if ( r == 'A' && (c < 5 || c > 17) ) {
            continue;
          }
          else if ( r == 'B' && c < 5 ) {
            continue;
          }
        }
        else {
          if ( c < 3) {
            x -= 2;
          }
          else if ( c > 21 ) {
            x += 2;
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
