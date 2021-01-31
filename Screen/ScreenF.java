public class ScreenF {
  public static void main(String[] args) {
    String studioName = "f studio";
    int sid = 6;
    char sRow = 'A';
    char eRow = 'M';
    int sCol = 1;
    int eCol = 20;

    System.out.println("use mtra;");
    System.out.format( "alter table seat auto_increment=%d;\n", (sid-1)*1000+1);
    for ( int r = sRow; r <= eRow; r++ ) {
      for ( int c = sCol; c <= eCol; c++ ) {
        double x = 2.0*(c - (eCol + sCol)/2.0);
        double y = 2.0*(r - sRow)+1;
        double z = 1.0*(r - sRow);
        switch ( r ) {
          case 'A':
            if ( c < 3 || c > 18) continue;
            if ( c <=5 ) x -= 2;
            else if ( c >= 16 ) x += 2;
            break;
          case 'B': case 'C': case 'D': case 'E':
          case 'G': case 'K':
            if ( c < 2 || c > 19 ) continue;
            if ( c <=5 ) x -= 2;
            else if ( c >= 16 ) x += 2;
            break;
          case 'F': case 'J':
            if ( c == 15 ) continue;
            if ( c <=5 ) x -= 2;
            else if ( c >= 16 ) x += 2;
            else x += 1;
            break;
          case 'H': case 'L':
            if ( c < 2 || c == 15 || c > 19) continue;
            if ( c <=5 ) x -= 2;
            else if ( c >= 16 ) x += 2;
            else x += 1;
            break;
          case 'I':
            if ( c <=5 ) x -= 2;
            else if ( c >= 16 ) x += 2;
            break;
          case 'M':
            if ( c < 6 || c > 15 ) continue;
            break;
          default:
            System.err.println("error!");
        }
        System.out.format("insert into seat"
         +"(`screen_id`, `row`, `column`, `pos_x`, `pos_y`, `pos_z`)"
         +" values (%d, \"%c\", %2d, %3.0f, %3.0f, %3.0f);\n",
         sid, r, c, x, y, z);
      }
    }
  }
}
