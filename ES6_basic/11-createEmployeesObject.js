/**
 * @typedef {Object.<string, Array.<string>>} employeeObject
 * @param {string} departmentName
 * @param {Array.<string>} employees
 * @returns {employeeObject}
 */
export default function createEmployeesObject(departmentName, employees) {
  return { [departmentName]: [...employees] };
}
