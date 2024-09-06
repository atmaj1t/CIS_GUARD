const fs = require('fs');
const { spawn } = require('child_process');
const csvParser = require('csv-parser');
const inputFile = 'ubuntu22.csv';
const outputFile = 'output.json';
function runShellCommand(command) {
    return new Promise((resolve, reject) => {
        const shell = spawn('bash', ['-c', command]);
        let output = '';

        shell.stdout.on('data', (data) => {
            output += data.toString();
        });

        shell.stderr.on('data', (data) => {
            console.error(`Error: ${data}`);
            reject(data);
        });

        shell.on('close', () => {
            resolve(output.trim());
        });
    });
}
async function processCSV() {
    const results = [];
    const promises = [];

    return new Promise((resolve, reject) => {
        fs.createReadStream(inputFile)
            .pipe(csvParser())
            .on('data', (row) => {
                const guideline = row['Guideline'];
                let command = row['Command to Check'];
                let expectedOutput = row['Expected Output'];
                if (command.includes(',')) {
                    const parts = command.split(',');
                    if (parts.length === 2) {
                        command = parts[0].trim();
                        expectedOutput = parts[1].trim();
                    }
                }

                const promise = runShellCommand(command)
                    .then((actualOutput) => {
                        const status = actualOutput.includes(expectedOutput) ? 'Pass' : 'Fail';
                        const result = {
                            'Guideline': guideline,
                            'Expected Output': expectedOutput,
                            'Actual Output': actualOutput,
                            'Status': status
                        };
                        results.push(result);
                        console.log(result);
                        console.log('-----------------------------------');
                    })
                    .catch((error) => {
                        const result = {
                            'Guideline': guideline,
                            'Expected Output': expectedOutput,
                            'Actual Output': 'Error executing command',
                            'Status': 'Error'
                        };
                        results.push(result);
                        console.log(result);
                        console.log('-----------------------------------');
                    });

                promises.push(promise); 
            })
            .on('end', async () => {
                try {
                    await Promise.all(promises);
                    writeResultsToJSON(results);
                    resolve();
                } catch (error) {
                    reject(error);
                }
            });
    });
}
function writeResultsToJSON(results) {
    fs.writeFile(outputFile, JSON.stringify(results, null, 2), (err) => {
        if (err) {
            console.error('Error writing JSON file:', err);
        } else {
            console.log('Results have been written to output.json');
        }
    });
}
processCSV().catch(err => console.error('Processing error:', err));
