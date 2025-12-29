function mySqrt(x: number): number {
    function sqrtFcuntion(n: number, n1: number)
    {
        if (n1 * n1 > n) {
            return n1 - 1;
        }
        else {
            return sqrtFcuntion(n, n1 + 1);
        }
    }

    return sqrtFcuntion(x, 1);
};

//taht turn out to be a pretty shitty solution, but i guess it works