void sectionFormula(float p1[3], float p2[3], float m, float n, float res[3]) {
    res[0] = (m * p2[0] + n * p1[0]) / (m + n);
    res[1] = (m * p2[1] + n * p1[1]) / (m + n);
    res[2] = (m * p2[2] + n * p1[2]) / (m + n);
}

void sectionFormulaExternal(float p1[3], float p2[3], float m, float n, float res[3]) {
    res[0] = (m * p2[0] - n * p1[0]) / (m - n);
    res[1] = (m * p2[1] - n * p1[1]) / (m - n);
    res[2] = (m * p2[2] - n * p1[2]) / (m - n);
}
