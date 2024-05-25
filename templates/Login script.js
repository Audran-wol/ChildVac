document.getElementById("loginForm").addEventListener("submit", function(event) {
  event.preventDefault(); // Prevent form submission

  // Get the entered username and password
  var username = document.getElementById("username").value;
  var password = document.getElementById("password").value;

  // Perform login validation
  if (username === "admin" && password === "password") {
    alert("Login successful!");
    // Redirect to the dashboard or next page
    // window.location.href = "Parent home.html";
  } else {
    alert("Invalid username or password. Please try again.");
  }
});