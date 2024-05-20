document.getElementById("registerForm").addEventListener("submit", function(event) {
  event.preventDefault(); // Prevent form submission

  // Get the entered email, email password, and hospital name
  var email = document.getElementById("email").value;
  var password = document.getElementById("password").value;
  var hospitalName = document.getElementById("hospitalName").value;

  // Perform registration validation and processing
  // ...

  // Redirect to the login page or next page
  // window.location.href = "login.html";
});