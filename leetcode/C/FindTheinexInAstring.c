int strStr(char* haystack, char* needle){
  int haystackLenght = strlen(haystack);
  int needleLenght = strlen(needle);

  for(int i = 0; i <= haystackLenght; i++){
    if(strncmp(haystack + i, needle, needleLenght) == 0){
      return i;
    }
  }
  return -1;
}
