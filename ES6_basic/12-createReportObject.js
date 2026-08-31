/**
 * @typedef {Object.<string, Array.<string>>} employeeObject
 * @param {employeeObject} employeesList
 * @returns {{ allEmployees: employeeObject, getNumberOfDepartments: (arg0: employeeObject) => number}}
 */
export default function createReportObject(employeesList) {
  return {
    allEmployees: employeesList,
    getNumberOfDepartments: (employeesList) => {
      return Object.keys(employeesList).length;
    },
  };
}
