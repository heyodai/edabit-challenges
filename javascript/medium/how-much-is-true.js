/**
 * Nov 13, 2020
 * https://edabit.com/challenge/GLbuMfTtDWwDv2F73
 */

/**
 * Count the number of true bool elements in an array
 * @param {array} arr An array consisting of a number of bool values
 * @returns {int} Number of true elements
 */
function countTrue(arr) {
    // set up some variables
    var array_size = arr.length;
    var count = 0;

     // skip this if the array is empty
     if (array_size > 0) {
         // iterate through array elements
         for (var i=0; i < array_size; i++) {
             if (arr[i]) { // == true
                count++;
             }
         }
     }

     // return the result
     return count;
}