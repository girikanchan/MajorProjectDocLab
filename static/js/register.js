const form = document.querySelector("form");
const nextBtn = form.querySelector(".nextBtn");
const backBtn = form.querySelector(".backBtn");
const allInput = form.querySelectorAll(".first input");

nextBtn.addEventListener("click", () => {
    allInput.forEach(input => {
        if (input.value !== "") {
            form.classList.add('secActive');
        } else {
            form.classList.remove('secActive');
        }
    });
});

backBtn.addEventListener("click", () => {
    form.classList.remove('secActive');
});


document.getElementById("password").addEventListener("keyup", function () {
    var password = document.getElementById("password").value;
    var confirmPassword = document.getElementById("confirmPassword").value;
    if (password != confirmPassword) {
        document.getElementById("message").innerHTML = "Passwords do not match.";
    } else {
        document.getElementById("message").innerHTML = "";
    }
});


document.getElementById("register-form").addEventListener('submit', function(event) {
    event.preventDefault();

    const name = document.getElementById("name").value;
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;
    const confirmPassword = document.getElementById("password2").value;
    const contact = document.getElementById("contno").value;
    const address = document.getElementById("address").value;
    const city = document.getElementById("district").value;
    const state = document.getElementById("state").value;
    const pincode = document.getElementById("pincode").value;
    const nation = document.getElementById("nation").value;
    const nationality = document.getElementById("nationality").value;
    const date_of_birth = document.getElementById("date_of_birth").value;
    const id_type = document.getElementById("id_type").value;
    const id_no = document.getElementById("id_number").value;
    const id_issue = document.getElementById("id_issue").value;
    const gender = document.getElementById("gender").value;
    const occupation = document.getElementById("occupation").value;
    const issue_date = document.getElementById("issue_date").value;
    const issue_state = document.getElementById("issue_state").value;
    const add_type = document.getElementById("add_type").value;

    fetch('http://localhost:8000/api/user/register', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ name, email, password, confirmPassword, contact, nation, state, date_of_birth, add_type, address, city, nationality, pincode, gender, occupation, issue_date, issue_state, id_type, id_no, id_issue }),
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
        window.location.href = "http://localhost:8000/login";
    })
    .catch((error) => {
        console.error('Error:', error);
    });
});


function redirectToLogin() {
    // You can add additional client-side validation here if needed

    // Redirect to the login page
    window.location.href = "{% url 'login' %}";

    // Prevent the form from submitting immediately
    return false;
}