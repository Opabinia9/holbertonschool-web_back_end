/**
 * @param {string} path
 */
function countStudents(path) {
  const fs = require('node:fs');

  try {
    const data = fs.readFileSync(path, 'utf8');

    /**
     * parse cvs data into a 2d array of strings
     * @type {Array.<Array.<string>>}
     */
    const rows = data
      .trim()
      .split('\n')
      .map((row) => row.split(','));

    /**
     * @callback CSVToDict
     * @param {Object.<string, string>} dict
     * @param {string} header
     * @param {number} col
     * @returns {Object.<string, string>}
     */
    /** @type {Array.<Object.<string, string>>} */
    const students = rows.slice(1).map((row) =>
      rows[0].reduce(
        /** @type {CSVToDict} */
        (dict, header, col) => {
          dict[header] = row[col];
          return dict;
        },
        {},
      ),
    );

    /**
     * @callback CategorizByField
     * @param {Object.<string, Array<Object.<string, string>>>} acc
     * @param {Object.<string, string>} student
     * @returns {Object.<string, Array<Object.<string, string>>>}
     */
    /** @type {Object.<string, Array<Object.<string, string>>>} */
    const fields = students.reduce(
      /** @type {CategorizByField} */
      (acc, student) => {
        acc[student.field] ??= [];
        acc[student.field].push(student);
        return acc;
      },
      {},
    );

    console.log(`Number of students: ${students.length}`);

    for (let x of Object.keys(fields)) {
      console.log(
        `Number of students in ${x}: ${fields[x].length}. List: ${fields[x]
          .map((row) => {
            return row['firstname'];
          })
          .join(', ')}`,
      );
    }
  } catch (error) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
