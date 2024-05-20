document.getElementById("signupForm").addEventListener("submit", function(event) {
  event.preventDefault(); // Prevent form submission

  // Get the entered username, email, and password
  var username = document.getElementById("username").value;
  var email = document.getElementById("email").value;
  var password = document.getElementById("password").value;

  // Perform sign-up validation and processing
  // ...

  // Redirect to the login page or next page
  // window.location.href = "login.html";
});