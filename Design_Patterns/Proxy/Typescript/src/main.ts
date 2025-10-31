const emailInput = document.getElementById("username") as HTMLInputElement;
const passwordInput = document.getElementById("password") as HTMLInputElement;
const loginButton = document.getElementById("sumbit-btn") as HTMLButtonElement;

cosnt authProxy = new AuthProxy(new RealAuthService(), false);

loginButton.addEventListener("click", async () => {
    const correo = emailInput.value;
    const contraseña = passwordInput.value;
    try {
        const success = await AuthProxy.login(correo, contraseña);

        if (success) {
            alert("Usuario autorizado");
        }
        else {
            alert("Credenciales invalidas");
        }

    } catch (error: any) {
        throw new Error(error.message);
    }
})