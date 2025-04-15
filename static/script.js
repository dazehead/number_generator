function getNumber() {
    fetch('/run-script')
    .then(response => response.json())
    .then(data => {
        document.getElementById('random').innerText= 'Generated number: ' + data.number;
        document.getElementById('result').innerText='Total Count of Button Presses: ' + data.counter

    })
    .catch(error => {
        document.getElementById('result').innerText= 'Error fetching number';
        console.error(error)
    });
}