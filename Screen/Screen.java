public class Screen {
  public static void main(String[] args) {
    String studioName = "a studio";
    char sRow = 'A';
    char eRow = 'O';
    int sCol = 1;
    int eCol = 22;

    for ( int r = sRow; r < eRow; r++ ) {
      for ( int c = sCol; c <= eCol; c++ ) {
        if ( r >= 'C' || ( 5 <= c && c <= 18 )) {
          double x = 2*(c - (eCol + sCol)/2.0);
          if ( c <= 4 ) x -= 2;
          else if ( c >= 19 ) x += 2;
          System.out.format("insert into seat(`screen_id`, `row`, `column`, `pos_x`, `pos_y`, `pos_z`) values (1, \"%c\", %2d, %3.0f, %3.0f, %3.0f);\n", r, c, x, (r - 'B')*2.0+1, (r - 'B')*1.0);
        }
      }
    }
    for ( int c = 1; c <= 16; c++ ) {
      double x = 2*(c - (1 + 16)/2.0);
      if ( x < 0 ) x -= 2;
      else x += 2;
      System.out.format("insert into seat(`screen_id`, `row`, `column`, `pos_x`, `pos_y`, `pos_z`) values (1, \"S\", %2d, %3.0f, %3.0f, %3.0f);\n", c, x, 35.0, 17.0);
    }
  }
}
