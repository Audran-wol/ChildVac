// Fetch the hospitals data from the database
fetch('/api/hospitals')
  .then(response => response.json())
  .then(data => {
    // Get the approved and pending hospitals count from the data
    var approvedHospitalsCount = data.approvedCount;
    var pendingHospitalsCount = data.pendingCount;

    // Update the approved hospitals count in the HTML
    document.getElementById("approved-hospitals-count").textContent = approvedHospitalsCount;

    // Update the pending hospitals count in the HTML
    document.getElementById("pending-hospitals-count").textContent = pendingHospitalsCount;
  })
  .catch(error => {
    console.error('Error:', error);
  });