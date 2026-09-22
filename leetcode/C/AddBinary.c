char* addBinary(char* a, char* b) {
    int lenA = strlen(a);
    int lenB = strlen(b);
    int maxLen = (lenA > lenB ? lenA : lenB) + 1;

    char* result = (char*)malloc(sizeof(char) * (maxLen + 1));
    result[maxLen] = '\0';

    int i = lenA - 1;
    int j = lenB - 1;
    int k = maxLen - 1;
    int carry = 0;

    while (i >= 0 || j >= 0 || carry) {
        int sum = carry;
        if (i >= 0) {
            sum += a[i] - '0';
            i--;
        }
        if (j >= 0) {
            sum += b[j] - '0';
            j--;
        }

        result[k--] = (sum % 2) + '0';
        carry = sum / 2;
    }

    if (k == 0) {
        memmove(result, result + 1, maxLen);
    }

    return result;
}
