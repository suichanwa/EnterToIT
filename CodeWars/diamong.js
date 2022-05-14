function diamond(n) {

    if(n < 3 || n % 2 == 0) {
        return null;
    }

    var middle = parseInt((n + 1) / 2);
    var j, diam = '';
    for(var i = 1; i <= n; i++) {
        j = i <= middle ? i : n - i + 1;
        diam += ' '.repeat(middle - j) + '*'.repeat(2 * j - 1) + '\n';
    }
    return diam;
}