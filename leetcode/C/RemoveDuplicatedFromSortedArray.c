int removeDuplicated(int* nums, int numsSize){
  int a = 1;

  for (int i = 1; i < numsSize; i++){
    if (nums[i] != nums[i - 1]){
      nums[a] = nums[i];
      a++;
    }
  }
  return a;
}
