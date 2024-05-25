// ...existing code...

// Fetch the child data from the database
fetch('/api/children')
  .then(response => response.json())
  .then(data => {
    // Get the registered children count from the data
    var registeredChildrenCount = data.length;

    // Update the registered children count in the HTML
    document.getElementById("registered-children-count").textContent = registeredChildrenCount;

    // Display the child data in the table
    var childDataContainer = document.getElementById("child-data");
    data.forEach(child => {
      var row = document.createElement("tr");
      row.innerHTML = `
        <td>${child.number}</td>
        <td>${child.name}</td>
        <td>${child.dateOfBirth}</td>
        <td>${child.parentNumber}</td>
      `;
      childDataContainer.appendChild(row);
    });
  })
  .catch(error => {
    console.error('Error:', error);
  });

// Search button click event handler
document.getElementById("search-button").addEventListener("click", function() {
  var searchInput = document.getElementById("search-input").value.toLowerCase();
  var childDataContainer = document.getElementById("child-data");
  childDataContainer.innerHTML = ""; // Clear previous search results

  // Filter child data based on search input
  var filteredData = data.filter(child => child.name.toLowerCase().includes(searchInput));

  // Display the filtered child data in the table
  filteredData.forEach(child => {
    var row = document.createElement("tr");
    row.innerHTML = `
      <td>${child.number}</td>
      <td>${child.name}</td>
      <td>${child.dateOfBirth}</td>
      <td>${child.parentNumber}</td>
    `;
    childDataContainer.appendChild(row);
  });
});