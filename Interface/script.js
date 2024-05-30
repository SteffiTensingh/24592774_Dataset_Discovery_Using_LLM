// script.js
async function submitQuery() {
    const query = document.getElementById('query').value;
    const response = await fetch('/submit_query', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ query }),
    });

    const data = await response.json();
    displayResults(data);
}

function displayResults(data) {
    const resultsDiv = document.getElementById('results');
    resultsDiv.innerHTML = '';

    if (data.results && data.results.length > 0) {
        data.results.forEach(result => {
            const resultItem = document.createElement('div');
            resultItem.className = 'result-item';
            resultItem.innerHTML = `<h3>${result.title}</h3>
                                    <p>${result.description}</p>
                                    <a href="${result.dataset_url}" target="_blank">View Dataset</a>`;
            resultsDiv.appendChild(resultItem);
        });
    } else {
        resultsDiv.innerHTML = '<p>No relevant datasets found.</p>';
    }
}
