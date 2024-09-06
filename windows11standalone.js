const fs = require('fs');
const { spawn } = require('child_process');
const csvParser = require('csv-parser');
const inputFile = 'winstand11.csv';
const outputFile = 'output.json';
function runPowerShellCommand(command) {
    return new Promise((resolve, reject) => {
        const ps = spawn('powershell.exe', ['-Command', command]);
        let output = '';

        ps.stdout.on('data', (data) => {
            output += data.toString();
        });

        ps.stderr.on('data', (data) => {
            console.error(`Error: ${data}`);
            reject(data);
        });

        ps.on('close', () => {
            resolve(output.trim());
        });
    });
}
async function processCSV() {
    const results = [];
    const promises = [];

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

            const promise = runPowerShellCommand(command)
                .then((actualOutput) => {
                    const status = actualOutput === expectedOutput ? 'Pass' : 'Fail';
                    const result = {
                        'Guideline': guideline,
                        'Expected Output': expectedOutput,
                        'Actual Output': actualOutput,
                        'Status': status
                    };
                    results.push(result);
                })
                .catch((error) => {
                    const result = {
                        'Guideline': guideline,
                        'Expected Output': expectedOutput,
                        'Actual Output': 'Error executing command',
                        'Status': 'Error'
                    };
                    results.push(result);
                });

            promises.push(promise);
        })
        .on('end', async () => {

            await Promise.all(promises);
            writeResultsToJSON(results);
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

processCSV();
