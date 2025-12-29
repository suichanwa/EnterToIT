function isMatch(s: string, p: string): boolean {
    const regexPattern = '^' + p.replace(/\./g, '.').replace(/\*/g, '.*') + '$';
    const regex = new RegExp(regexPattern);
    return regex.test(s);
};