// ...existing code...

// Fetch the appointment data from the database
fetch('/api/appointments')
  .then(response => response.json())
  .then(data => {
    // Get the number of appointments scheduled from the data
    var appointmentCount = data.length;

    // Update the appointment count in the HTML
    document.getElementById("appointment-count").textContent = appointmentCount;

    // Display the appointment data in the table
    var appointmentDataContainer = document.getElementById("appointment-data");
    data.forEach(appointment => {
      var row = document.createElement("tr");
      row.innerHTML = `
        <td>${appointment.number}</td>
        <td>${appointment.hospital}</td>
        <td>${appointment.childName}</td>
        <td>${appointment.dateOfBirth}</td>
        <td>${appointment.parentNumber}</td>
      `;
      appointmentDataContainer.appendChild(row);
    });
  })
  .catch(error => {
    console.error('Error:', error);
  });

// Search button click event handler
document.getElementById("search-button").addEventListener("click", function() {
  var searchInput = document.getElementById("search-input").value.toLowerCase();
  var appointmentDataContainer = document.getElementById("appointment-data");
  appointmentDataContainer.innerHTML = ""; // Clear previous search results

  // Filter appointment data based on search input
  var filteredData = data.filter(appointment => appointment.childName.toLowerCase().includes(searchInput));

  // Display the filtered appointment data in the table
  filteredData.forEach(appointment => {
    var row = document.createElement("tr");
    row.innerHTML = `
      <td>${appointment.number}</td>
      <td>${appointment.hospital}</td>
      <td>${appointment.childName}</td>
      <td>${appointment.dateOfBirth}</td>
      <td>${appointment.parentNumber}</td>
    `;
    appointmentDataContainer.appendChild(row);
  });
});