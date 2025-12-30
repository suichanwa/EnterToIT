/**
 Do not return anything, modify nums1 in-place instead.
 */
function merge(nums1: number[], m: number, nums2: number[], n: number): void {
    function mergeSort(arr1: number[], len1: number, arr2: number[], len2: number): number[] {
        const merged: number[] = [];
        let i = 0;
        let j = 0;
        while (i < len1 && j < len2) {
            if (arr1[i] < arr2[j]) {
                merged.push(arr1[i]);
                i++;
            } else {
                merged.push(arr2[j]);
                j++;
            }
        }
        while (i < len1) {
            merged.push(arr1[i]);
            i++;
        }
        while (j < len2) {
            merged.push(arr2[j]);
            j++;
        }
        return merged;
    }
    const mergedArray = mergeSort(nums1.slice(0, m), m, nums2, n);

    for (let i = 0; i < mergedArray.length; i++) {
        nums1[i] = mergedArray[i];
    }
};