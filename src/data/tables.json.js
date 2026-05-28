const response = await fetch("http://168.231.75.245:3010/api/tables");
const data = await response.json();
process.stdout.write(JSON.stringify(data));