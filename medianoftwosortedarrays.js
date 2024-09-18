function findMedianSortedArrays(arr1, arr2) {
    const totalLength = arr1.length + arr2.length;
    const isEven = totalLength % 2 === 0;
    const midIndex = Math.floor(totalLength / 2);
    
    let i = 0, j = 0, k = 0;
    let last = 0, secondLast = 0;

    // Merge until we reach the median index
    while (i < arr1.length && j < arr2.length) {
        secondLast = last;

        if (arr1[i] < arr2[j]) {
            last = arr1[i++];
        } else {
            last = arr2[j++];
        }

        // If we have reached the middle index, break
        if (k === midIndex) {
            break;
        }

        k++;
    }

    // If we haven't reached the median and one array is exhausted, process the remaining elements
    while (i < arr1.length && k <= midIndex) {
        secondLast = last;
        last = arr1[i++];
        if (k === midIndex) {
            break;
        }
        k++;
    }

    while (j < arr2.length && k <= midIndex) {
        secondLast = last;
        last = arr2[j++];
        if (k === midIndex) {
            break;
        }
        k++;
    }

    // Return the median based on whether the total length is even or odd
    if (isEven) {
        return (last + secondLast) / 2;
    } else {
        return last;
    }
}
