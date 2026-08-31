/**
 * @param {String} departmentName
 * @param {Array.<String>} employees
 * @returns {Object.<String, Array.<String>>}
 */
export default function createEmployeesObject(departmentName, employees) {
  return { [departmentName]: [...employees] };
}
