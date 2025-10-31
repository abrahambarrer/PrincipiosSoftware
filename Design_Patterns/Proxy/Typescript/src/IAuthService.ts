export interface IAuthService {
    login(correo: string, contrasenia: string): Promise<boolean>;
    getProtectedData(): Promise<string>;
}