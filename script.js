document.addEventListener('DOMContentLoaded', function () {
    const darkModeToggle = document.getElementById('dark-mode-toggle');
    if (darkModeToggle) {
        darkModeToggle.addEventListener('click', function () {
            document.body.classList.toggle('dark-mode');
            console.log('Modo Oscuro activado'); // Esto te ayudará a verificar si el botón funciona
        });
    } else {
        console.error('Botón de Modo Oscuro no encontrado'); // Esto avisará si el botón no se encuentra
    }

    const loginForm = document.getElementById('loginForm');
    if (loginForm) {
        loginForm.addEventListener('submit', function(event) {
            event.preventDefault();
            const username = document.getElementById('username').value;
            const password = document.getElementById('password').value;
            const errorMessage = document.getElementById('error-message');
            // Validar credenciales
            if (username === "draberenice" && password === "2003") {
                // Redireccionar al menú principal
                window.location.href = "main.html";
            } else {
                // Mostrar mensaje de error
                errorMessage.textContent = "Usuario o contraseña incorrectos.";
            }
        });
    } else {
        console.error('Formulario de Inicio de Sesión no encontrado'); // Esto avisará si el formulario no se encuentra
    }
});
