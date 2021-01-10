function login(form) {
  un = form.Username.value;
  pw = form.Password.value;
  credentials = { username: un, password: pw };
  console.log("this is working");
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function () {
    if (this.readyState == 4 && this.status == 200) {
      document.getElementById("demo").innerHTML = this.responseText;
      // loginResults();
    }
  };

  xhttp.open("POST", "https://localhost:5000/login", true);
  xhttp.setRequestHeader("Content-type", "application/json");
  xhttp.send(credentials);
}

window.addEventListener(window, "load", function () {
  var loginForm = document.getElementById("LoginForm");
  window.addEventListener(loginForm, "submit", function () {
    login(loginForm);
  });
});
