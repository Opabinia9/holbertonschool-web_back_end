/**
 * prepend string to each value in an array
 * @param {Array} array
 * @param {String} appendString
 * @returns {Array}
 */
export default function appendToEachArrayValue(array, appendString) {
  for (const value of array) {
    array[array.indexOf(value)] = appendString + value;
  }

  return array;
}
