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
        <td>${appointment.status}</td>
      `;
      appointmentDataContainer.appendChild(row);
    });
  })
  .catch(error => {
    console.error('Error:', error);
  });