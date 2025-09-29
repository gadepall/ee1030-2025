int dividing_point(double x1, double x2, double y1, double y2, double l, double m) {
    /* Returns the quadrant of the point dividing points with coordinates (x1, y1) and (x2, y2) in the ratio l:m */
    double x = (x1*m + x2*l)/(l+m);
    double y = (y1*m + y2*l)/(l+m);

    if (x < 0 && y < 0){
        return 3;
    } else if (x < 0 && y > 0){
        return 2;
    } else if (x > 0 && y < 0){
        return 4;
    } else if (x > 0 && y > 0){
        return 1;
    }
}