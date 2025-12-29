function lengthOfLongestSubstring(s: string): number {
    let maxLength = 0;
    for (let i = 0; i < s.length; i++) {
        const seenChars = new Set<string>();
        for (let j = i; j < s.length; j++) {
            const currentChar = s[j];
            if (seenChars.has(currentChar)) {
                break;
            }
            seenChars.add(currentChar);
            maxLength = Math.max(maxLength, seenChars.size);
        }
    }
    return maxLength;
};