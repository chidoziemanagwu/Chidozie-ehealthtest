// =========================================================
// * fixXxer_Django - v1.0.0
// =========================================================
// * Product Page: https://www.fixertech.dev/libraries/fixXxer_Django/

// * Copyright  ThefixXxer (https://www.fixertech.dev)
// * Coded by ThefixXxer
// =========================================================
// * The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.


// Grabbers For All Important Targets
const usernameField = document.querySelector("#usernameField");
const feedBackArea = document.querySelector(".usernameFeedBackArea");
const usernameSuccessOutput = document.querySelector(".usernameSuccessOutput");

// const loginUsernameField = document.querySelector("#loginUsernameField")
// const loginfeedBackArea = document.querySelector(".loginfeedBackArea");
// const loginUsernameSuccessOutput = document.querySelector(".loginUsernameSuccessOutput");

const emailField = document.querySelector("#useremailField");
const emailFeedBackArea = document.querySelector(".emailFeedBackArea");
const emailSuccessOutput = document.querySelector(".emailSuccessOutput");

// const passwordField = document.querySelector("#passwordField");
// const confirmPasswordField = document.querySelector("#confirmPasswordField");
// const showPasswordToggle = document.querySelector(".showPasswordToggle");
// const passwordStrengthNotice = document.querySelector('#password_strength');

const submitBtn = document.querySelector("#submit-btn");

// Password Visibility Toggle
// const handleToggleInput = (e) => {
//   if (showPasswordToggle.textContent === "SHOW") {
//     showPasswordToggle.textContent = "HIDE";
//     passwordField.setAttribute("type", "text");
//     confirmPasswordField.setAttribute("type", "text");
//   } else {
//     showPasswordToggle.textContent = "SHOW";
//     passwordField.setAttribute("type", "password");
//     confirmPasswordField.setAttribute("type", "password");
//   }
// };

// Password Visibility Toggle Trigger
// showPasswordToggle.addEventListener("click", handleToggleInput);

// SignUp Email Ajax Validation
emailField.addEventListener("focusout", (e) => {
  const emailVal = e.target.value;

  emailSuccessOutput.style.display = "block";

  emailSuccessOutput.innerHTML = '<i class="fa fa-spinner fa-spin"></i>  '+`Checking  ${emailVal}`;

  emailField.classList.remove("is-invalid");
  emailFeedBackArea.style.display = "none";

  if (emailVal.length > 0) {
    fetch("/Auth/validate-email", {
      body: JSON.stringify({ email: emailVal }),
      method: "POST",
    })
      .then((res) => res.json())
      .then((data) => {
        emailSuccessOutput.style.display = "none";
        console.log("data", data);
        if (data.email_error) {
          submitBtn.disabled = true;
          emailField.classList.add("is-invalid");
          emailFeedBackArea.style.display = "block";
          emailFeedBackArea.innerHTML = `<p>${data.email_error}</p>`;
        } else {
          submitBtn.removeAttribute("disabled");
        }
      });
  }
});

// SignUp Username Ajax Validation
usernameField.addEventListener("focusout", (e) => {
  const usernameVal = e.target.value;

  usernameSuccessOutput.style.display = "block";

  usernameSuccessOutput.innerHTML = '<i class="fa fa-spinner fa-spin"></i>  '+`Checking  ${usernameVal}`;

  usernameField.classList.remove("is-invalid");
  feedBackArea.style.display = "none";

  if (usernameVal.length > 0) {
    fetch("/Auth/validate-username", {
      body: JSON.stringify({ username: usernameVal }),
      method: "POST",
    })
      .then((res) => res.json())
      .then((data) => {
        usernameSuccessOutput.style.display = "none";
        console.log("data", data);
        if (data.username_error) {
          usernameField.classList.add("is-invalid");
          feedBackArea.style.display = "block";
          feedBackArea.innerHTML = `<p>${data.username_error}</p>`;
          submitBtn.disabled = true;
        } else {
          submitBtn.removeAttribute("disabled");
        }
      });
  }
});

// // Password Strength Test
// function scorePassword(pass) {
//     var score = 0;
//     if (!pass)
//         return score;

//     // award every unique letter until 5 repetitions
//     var letters = new Object();
//     for (var i=0; i<pass.length; i++) {
//         letters[pass[i]] = (letters[pass[i]] || 0) + 1;
//         score += 5.0 / letters[pass[i]];
//     }

//     // bonus points for mixing it up
//     var variations = {
//         digits: /\d/.test(pass),
//         lower: /[a-z]/.test(pass),
//         upper: /[A-Z]/.test(pass),
//         nonWords: /\W/.test(pass),
//     }

//     variationCount = 0;
//     for (var check in variations) {
//         variationCount += (variations[check] == true) ? 1 : 0;
//     }
//     score += (variationCount - 1) * 10;

//     return parseInt(score);
// }

// function checkPassStrength(pass) {
//     var score = scorePassword(pass);
//     if (score > 80)
//         return "strong";
//     if (score > 60)
//         return "good";
//     if (score >= 30)
//         return "weak";

//     return "";
// }

// // Password Strength Display In Page
// passwordField.addEventListener("keyup", (e) => {
//   const pass_event_value = e.target.value;
//   console.log(pass_event_value)
//   pass_true_strength = checkPassStrength(pass_event_value)

//   passwordStrengthNotice.style.display = "block";
//   if (pass_true_strength == "weak") {
//     passwordStrengthNotice.classList.remove("text-success");
//     passwordStrengthNotice.classList.remove("text-yellow");
//     passwordStrengthNotice.classList.add("text-danger");
//     passwordStrengthNotice.textContent = checkPassStrength(pass_event_value)
//   } else if (pass_true_strength == "good") {
//       passwordStrengthNotice.classList.remove("text-success");
//       passwordStrengthNotice.classList.remove("text-danger");
//       passwordStrengthNotice.classList.add("text-yellow");
//       passwordStrengthNotice.textContent = checkPassStrength(pass_event_value)
//   } else if (pass_true_strength == "strong") {
//       passwordStrengthNotice.classList.remove("text-danger");
//       passwordStrengthNotice.classList.remove("text-yellow");
//       passwordStrengthNotice.classList.add("text-success");
//       passwordStrengthNotice.textContent = checkPassStrength(pass_event_value)
//   } else {
//      passwordStrengthNotice.style.display = "none";
//   }

