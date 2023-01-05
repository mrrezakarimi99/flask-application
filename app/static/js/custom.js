/*
    Make Modal For login
*/
const loginModal = document.getElementById('loginModal');
const registerModal = document.getElementById('registerModal');
const forgetPassword = document.getElementById('forgetPassword');

function actionModal(action , modal) {
    if (action === 'open') {
        switch (modal) {
            case 'login':
                openModal(loginModal);
                break;
            case 'register':
                openModal(registerModal);
                break;
            case 'forgetPassword':
                openModal(forgetPassword);
                break;
            default:
                break;
        }
    } else {
        switch (modal) {
            case 'login':
                closeModal(loginModal);
                break;
            case 'register':
                closeModal(registerModal);
                break;
            case 'forgetPassword':
                closeModal(forgetPassword);
                break;
            default:
                break;
        }
    }
}

function closeModal(model) {
    loginModal.style.display = "none";
    registerModal.style.display = "none";
    forgetPassword.style.display = "none";
    model.style.display = "none";
}

function openModal(model) {
    loginModal.style.display = "none";
    registerModal.style.display = "none";
    forgetPassword.style.display = "none";
    model.style.display = "block";
    globalCloseLoginModal(event , model);
}

/*
    End Make Modal For login
*/

/*
    Login Form
*/
let params = getUrlParams();
if (params['login'] === 'true') {
    actionModal('open' , 'login');
}

function validateLoginForm() {
    const email = document.getElementById('email-register').value;
    const username = document.getElementById('username-register').value;
    const password = document.getElementById('password-register').value;
    const passwordConfirmation = document.getElementById('confirm-password-register').value;
    const error = document.getElementById('error-register');

    if (email === '' || password === '' || username === '' || passwordConfirmation === '') {
        error.innerHTML = 'Please Fill All Fields';
        return false;
    } else {
        if (email.indexOf('@') === -1) {
            error.innerHTML = 'Please Enter Valid Email';
            return false;
        }
        if (password !== passwordConfirmation) {
            error.innerHTML = '\n Password Not Match';
            return false;
        }
        error.innerHTML = '';
        return true;
    }
}

function registerUser(e){
    if(validateLoginForm()){
        document.getElementById('register').submit();
    }else{
        return false;
    }
}
/*
    End Login Form
 */

/*
    Make Global Function For Close Modal
*/
function globalCloseLoginModal(event , model) {
    window.onclick = function(event) {
        if (event.target === model) {
            model.style.display = "none";
        }
    }
}

function getUrlParams() {
    let params = {};
    window.location.search.replace(/[?&]+([^=&]+)=([^&]*)/gi, function(str, key, value) {
        params[key] = value;
    });
    return params;
}

