int areCollinear(double Ax, double Ay, double Bx, double By, double Cx, double Cy) {
    double BA_x = Bx - Ax;
    double BA_y = By - Ay;
    double CA_x = Cx - Ax;
    double CA_y = Cy - Ay;

    double det = BA_x * CA_y - BA_y * CA_x;

    if (det == 0) {
        return 1;  // Points are collinear
    } else {
        return 0;  // Points are not collinear
    }
}
